# python多线程相关概念及解释

[doc]

# 简介

多线程是为了抢占资源而设计的。同样作用的有多进程，不过因为线程的创建和切换代价远比进程低，一般是选择线程来执行多任务。因为线程会共享进程内的资源，为了处理多个线程处理相同的资源，又多出了锁的概念。  
而本身线程的创建其实也是有代价的，为了避免反复的创建和销毁，又有了线程池的概念。

# 线程的基本使用

## 直接调用threading.Thread类

```
#coding=utf-8
import threading
from time import sleep,ctime

def aLongTimeWorkWithIO():
    sleep(5)
    print("aLongTimeWorkWithIO  work  in thread:%s,%s" % (threading.current_thread().name, ctime()))

if __name__ == '__main__':
    print("start thread:", threading.current_thread().name, ctime())
    t = threading.Thread(target=aLongTimeWorkWithIO, args=())
    t.start()
    print("end thread:", threading.current_thread().name, ctime() )
```

输入结果：

> start thread: MainThread Mon Feb 6 22:50:04 2017  
>  end thread: MainThread Mon Feb 6 22:50:04 2017  
>  aLongTimeWorkWithIO work in thread:Thread-1,Mon Feb 6 22:50:09 2017

最基本的代码执行是按顺序，一条一条执行下去的。只有一条路。  
线程花费的CPU时间是占满主线程的。

而多线程的引入其实就是增加了代码执行路径。进程花费的CPU时间是在主线程和新线程之间交叉进行的。

## 继承threading.Thread类

```
#coding=utf-8
import threading
from time import sleep,ctime
class MyThread(threading.Thread):
    def run(self):
        sleep(5)
        print("aLongTimeWorkWithIO  work  in thread:%s,%s" % (threading.current_thread().name, ctime()))

if __name__ == '__main__':
    print("start thread:", threading.current_thread().name, ctime())
    t = MyThread()
    t.start()
    print("end thread:", threading.current_thread().name, ctime() )
```

重载下run方法即可。

# 线程交互

## 线程合并join

join(timeout)方法将会等待直到线程结束。这将阻塞正在调用的线程，直到被调用join()方法的线程结束。  
如果线程是独立变化的挺好。譬如需要下载10张图片。因为这10张图片没有依赖关系。所以可以同时启动10个线程去下载就好了。  
但有时候，线程之间是有依赖关系的，如父线程必须得等子线程完成 拿到子线程的运行结果才可以继续作业。

```
import threading
import time

def target():
    print('the curent threading  %s is running' % threading.current_thread().name)
    time.sleep(1)
    print('the curent threading  %s is ended' % threading.current_thread().name)

print('the curent threading  %s is running' % threading.current_thread().name)
t = threading.Thread(target=target)

#t.setDaemon(True) #1
t.start()
#t.join() #2
print('the curent threading  %s is ended' % threading.current_thread().name)
```

代码输出：

> the curent threading MainThread is running
> the curent threading Thread-1 is running
> the curent threading MainThread is ended
> the curent threading Thread-1 is ended

你可能会觉得奇怪。为啥主线程退出，子线程还会运行。这其实是python的主线程干的好事，他会在即将退出时检查所有的非daemon且alive的线程,一个一个调用join方法。

所以要使主线程退出，子线程也退出，只需要把子线程设置为daemon，如上面代码中的#1，打开注释就可。  
而join就是等待该线程执行完成。如上面的#2所示。同时打开#1和#2和都不打开的输出内容差不多，只是顺序不同。

> the curent threading MainThread is running  
> the curent threading Thread-1 is running  
> the curent threading Thread-1 is ended  
> the curent threading MainThread is ended

## 条件变量

条件变量也是处理线程间协作的一种机制，详情见下文。

## Event对象

线程可以读取共享的内存，通过内存做一些数据处理。这就是线程通信的一种，python还提供了更加高级的线程通信接口。Event对象可以用来进行线程通信，调用event对象的wait方法，线程则会阻塞等待，直到别的线程set之后，才会被唤醒。

```
#coding: utf-8
import  threading
import  time


class MyThread(threading.Thread):
    def __init__(self, event):
        super(MyThread, self).__init__()
        self.event = event

    def run(self):
        print("thread {} is ready ".format(self.name))
        self.event.wait()
        print("thread {} run".format(self.name))

signal = threading.Event()

def main():
    start = time.time()
    for i in range(3):
        t = MyThread(signal)
        t.start()
    time.sleep(3)
    print( "after {}s".format(time.time() - start))
    signal.set()


if __name__ == '__main__':
    main()
```


输出结果：

> thread Thread-1 is ready  
>  thread Thread-2 is ready  
>  thread Thread-3 is ready  
>  after 3.00528883934021s  
>  thread Thread-1 run  
>  thread Thread-3 run  
>  thread Thread-2 run

## 屏障barrier

屏障(barrier)是用户协调多个线程并行工作的同步机制。屏障允许每个线程等待，直到所有的合作线程都到达某一点，然后从该点继续执行。  
屏障允许任意数量的线程等待，直到所有的线程完成处理工作，而线程不需要退出。所有线程达到屏障后可以接着工作。

感觉在分治法中有用。分成的子任务都完成了才能合并。所以都需要等待其它子任务。

下面的代码t1和t2都在wait,直到t5也wait,达到了Barrier的值3,才继续运行。


```
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
from threading import Barrier, Lock
from time import time,sleep
from datetime import datetime

def test_with_barrier(synchronizer, serializer):
    name = threading.current_thread().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("thread %s -----> %s" % (name, datetime.fromtimestamp(now)))

def test_without_barrier():
    name = threading.current_thread().name
    now = time()
    print("thread %s -----> %s" % (name, datetime.fromtimestamp(now)))

def worker(dictionary, key, item):
    dictionary[key] = item
    print(key, item)

if __name__ == '__main__':
    synchronizer = Barrier(3)
    serializer = Lock()
    threads = []
    t1 = threading.Thread(target=test_with_barrier,args=(synchronizer, serializer))
    t2 = threading.Thread(target=test_with_barrier,args=(synchronizer, serializer))
    t3 =  threading.Thread(target=test_without_barrier)
    t4 = threading.Thread(target=test_without_barrier)

    t5 = threading.Thread(target=test_with_barrier,args=(synchronizer, serializer))
    threads.append(t1)
    threads.append(t2)
    threads.append(t3)
    threads.append(t4)

    for t in threads:
        t.start()


    sleep(5)
    t5.start()
```


输出结果：

> thread Thread-3 -----&gt; 2017-02-07 11:59:46.336922  
>  thread Thread-4 -----&gt; 2017-02-07 11:59:46.339094  
>  thread Thread-5 -----&gt; 2017-02-07 11:59:51.341117  
>  thread Thread-1 -----&gt; 2017-02-07 11:59:51.341264  
>  thread Thread-2 -----&gt; 2017-02-07 11:59:51.341474

# 避免共享资源冲突

## 锁的使用

### 互斥锁

多个线程可能会用到同一个资源，如果在使用这个资源的时候，不是原子操作。则很可能会产生不可预知的错误。例如线程A使用全局变量i,先读取值(i=1),然后再设置i(i=i+1)。线程B同样是先读取值(i=1),然后再设置i(i=i+1)。  
因为[先读取值(i=1),然后再设置i(i=i+1)]并不是一个原子操作，这里面有时间窗口，那么就会有可能引起错误。如在线程A获取到i=1时，这个时候CPU切换到了线程B。  
线程B执行的任务是把i设置为2。CPU切换为线程A,线程设置值为2。这里就有问题了，其实最初设计的时候期望值是3(期望线程A和B都能增加1)

为了模拟获取值和设置值之间的时间窗口。特意搞了个sleep。代码如下：

```
#coding: utf-8
import  threading
import  time

counter = 0
counter_lock = threading.Lock()
class  MyThread(threading.Thread):#使用类定义thread，继承threading.Thread
    def  __init__(self,name):
        threading.Thread.__init__(self)
        self.name = "Thread-" + str(name)

    def run(self):  #run函数必须实现
        global counter,counter_lock #多线程是共享资源的，使用全局变量
       # if counter_lock.acquire(): #当需要独占counter资源时，必须先锁定，这个锁可以是任意的一个锁，可以使用上边定义的3个锁中的任意一个
        tmp = counter
        time.sleep(1)
        counter = tmp+1
        print("I am %s, set counter:%s"  % (self.name,counter))
       #     counter_lock.release() #使用完counter资源必须要将这个锁打开，让其他线程使用


if  __name__ ==  "__main__":
    for i in range(1,11):
        my_thread = MyThread(i)
        my_thread.start()
```

输出结果：

> I am Thread-1, set counter:1  
>  I am Thread-8, set counter:1  
>  I am Thread-4, set counter:1  
>  I am Thread-6, set counter:1  
>  I am Thread-7, set counter:1  
>  I am Thread-2, set counter:1  
>  I am Thread-9, set counter:1  
>  I am Thread-5, set counter:1  
>  I am Thread-3, set counter:1  
>  I am Thread-10, set counter:1

锁的引入就是为了解决这个问题，它把非原子操作变成了原子操作。  
在线程没有获取到锁的时候只能等待，使用完共享资源再释放锁，以供其它线程使用。  
这里有2个注意点：  
1\. 是锁的使用必须是一致的。也就是对同样的共享资源，必须使用相同的锁机制。只要有一处没有使用，锁就没意义了。  
2\.
需要避免死锁。获取锁的顺序是和释放锁的顺序相反的。获取锁A,获取锁B,释放锁B,释放锁A。并且其它地方也必须按同样的顺序获取和释放锁。不这样的话很容易造成死锁。

下面的代码就是锁的简单使用，解决了上面代码中的问题。


```
#coding: utf-8
import  threading
import  time

counter = 0
counter_lock = threading.Lock()
class  MyThread(threading.Thread):#使用类定义thread，继承threading.Thread
    def  __init__(self,name):
        threading.Thread.__init__(self)
        self.name = "Thread-" + str(name)

    def run(self):  #run函数必须实现
        global counter,counter_lock #多线程是共享资源的，使用全局变量
        if counter_lock.acquire(): #当需要独占counter资源时，必须先锁定，这个锁可以是任意的一个锁，可以使用上边定义的3个锁中的任意一个
            tmp = counter
            time.sleep(1)
            counter = tmp+1
            print("I am %s, set counter:%s"  % (self.name,counter))
            counter_lock.release() #使用完counter资源必须要将这个锁打开，让其他线程使用


if  __name__ ==  "__main__":
    for i in range(1,11):
        my_thread = MyThread(i)
        my_thread.start()
```

输出结果如下：

> I am Thread-1, set counter:1  
>  I am Thread-2, set counter:2  
>  I am Thread-3, set counter:3  
>  I am Thread-4, set counter:4  
>  I am Thread-5, set counter:5  
>  I am Thread-6, set counter:6  
>  I am Thread-7, set counter:7  
>  I am Thread-8, set counter:8  
>  I am Thread-9, set counter:9  
>  I am Thread-10, set counter:10

需要说明的是，锁解决了共享资源冲突问题，同时他又影响了线程的并发度。降低了效率。  
合理的线程设计很重要，最好是没有共享资源的使用，如全局变量，共同文件等。

### 可重入锁

为了支持在同一线程中多次请求同一资源，python提供了可重入锁（RLock）。RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。直到一个线程所有的acquire都被release，其他的线程才能获得资源。


```
#coding: utf-8
import  threading
import  time


mutex = threading.RLock()

class MyThread(threading.Thread):

    def run(self):
        if mutex.acquire(1):
            print("thread {} get mutex".format(self.name))
            time.sleep(1)
            mutex.acquire()
            mutex.release()
            mutex.release()



def main():
    print("Start main threading")
    for i in range(2):
        MyThread().start()

    print("End Main threading")


if __name__ == '__main__':
    main()
```

输出结果：

> Start main threading  
>  thread Thread-1 get mutex  
>  End Main threading  
>  thread Thread-2 get mutex

## 条件变量

### 有了锁，为什么还要有条件变量

条件变量(cond)是在多线程程序中用来实现"等待--》唤醒"逻辑常用的方法。条件变量利用线程间共享的全局变量进行同步的一种机制，主要包括两个动作：一个线程等待"条件变量的条件成立"而挂起；另一个线程使“条件成立”。为了防止竞争，条件变量的使用总是和一个互斥锁结合在一起。线程在改变条件状态前必须首先锁住互斥量，函数pthread_cond_wait把自己放到等待条件的线程列表上，然后对互斥锁解锁(这两个操作是原子操作)。在函数返回时，互斥量再次被锁住。

**锁的引入已经解决了线程的同步问题，为什么还要用到条件变量呢？**  
首先，举个例子：在应用程序中有连个线程thread1，thread2，thread3和thread4，有一个int类型的全局变量iCount。iCount初始化为0，thread1和thread2的功能是对iCount的加1，thread3的功能是对iCount的值减1，而thread4的功能是当iCount的值大于等于100时，打印提示信息并重置iCount=0。  
如果使用互斥量，线程代码大概应是下面的样子：


```
       thread1/2：
       while (1)
       {
             pthread_mutex_lock(&mutex);
             iCount++;
             pthread_mutex_unlock(&mutex);
       }
       thread4:
       while(1)
       {
             pthead_mutex_lock(&mutex);
             if (100 <= iCount)
             {
                   printf("iCount >= 100\r\n");
                   iCount = 0;
                   pthread_mutex_unlock(&mutex);
             }
             else
             {
                   pthread_mutex_unlock(&mutex);
             }
       }
```

在上面代码中由于thread4并不知道什么时候iCount会大于等于100，所以就会一直在循环判断，但是每次判断都要加锁、解锁(即使本次并没有修改iCount)。这就带来了问题一，CPU浪费严重。所以在代码中添加了sleep(),这样让每次判断都休眠一定时间。但这由带来的第二个问题，如果sleep()的时间比较长，导致thread4处理不够及时，等iCount到了很大的值时才重置。对于上面的两个问题，可以使用条件变量来解决。  
首先看一下使用条件变量后，线程代码大概的样子：


```
      thread1/2:
       while(1)
       {
               pthread_mutex_lock(&mutex);
               iCount++;
               pthread_mutex_unlock(&mutex);
               if (iCount >= 100)
               {
                      pthread_cond_signal(&cond);
               }
       }         
       thread4:
       while (1)
       {
              pthread_mutex_lock(&mutex);
              while(iCount < 100)
              {
                     pthread_cond_wait(&cond, &mutex);
              }
              printf("iCount >= 100\r\n");
              iCount = 0;
              pthread_mutex_unlock(&mutex);
       }
```

从上面的代码可以看出thread4中，当iCount &lt;
100时，会调用pthread_cond_wait。而pthread_cond_wait在上面应经讲到它会释放mutex，然后等待条件变为真返回。当返回时会再次锁住mutex。因为pthread_cond_wait会等待，从而不用一直的轮询，减少CPU的浪费。在thread1和thread2中的函数pthread_cond_signal会唤醒等待cond的线程（即thread4），这样当iCount一到大于等于100就会去唤醒thread4。从而不致出现iCount很大了，thread4才去处理。  
需要注意的一点是在thread4中使用的while (iCount &lt; 100),而不是if (iCount &lt;
100)。这是因为在pthread_cond_singal()和pthread_cond_wait()返回之间有时间差，假如在时间差内，thread3又将iCount减到了100以下了，那么thread4就需要在等待条件为真了。

### python中的例子

Pythonk中的条件变量是Condition对象。它除了具有acquire和release方法之外，还提供了wait和notify方法。线程首先acquire一个条件变量锁。如果条件不足，则该线程wait，如果满足就执行线程，甚至可以notify其他线程。其他处于wait状态的线程接到通知后会重新判断条件。

条件变量可以看成不同的线程先后acquire获得锁，如果不满足条件，可以理解为被扔到一个（Lock或RLock）的waiting池。直达其他线程notify之后再重新判断条件。该模式常用于生成者-
消费者模式：


```
#coding: utf-8
import  threading
import  time
import random

queue = []

con = threading.Condition()

class Producer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if len(queue) > 10:
                    print("{} Producer waiting".format(threading.current_thread().name))
                    con.wait()
                else:
                    elem = random.randrange(100)
                    queue.append(elem)
                    print("{}, Producer a elem {}, Now size is {}".format( threading.current_thread().name,elem, len(queue)))
                    time.sleep(random.random())
                    con.notify()
                con.release()


class Consumer(threading.Thread):
    def run(self):
        while True:
            if con.acquire():
                if len(queue) < 0:
                    print("{} Consumer waiting".format(threading.current_thread().name))
                    con.wait()
                else:
                    elem = queue.pop()
                    print("{}, Consumer a elem {}. Now size is {}".format(threading.current_thread().name, elem, len(queue)))
                    time.sleep(random.random())
                    con.notify()
                con.release()

def main():
    for i in range(3):
        Producer().start()

    for i in range(2):
        Consumer().start()


if __name__ == '__main__':
    main()
```


输出结果如下：

> Thread-1, Producer a elem 74, Now size is 1  
>  Thread-1, Producer a elem 16, Now size is 2  
>  Thread-1, Producer a elem 26, Now size is 3  
>  Thread-1, Producer a elem 97, Now size is 4  
>  Thread-1, Producer a elem 62, Now size is 5  
>  Thread-1, Producer a elem 76, Now size is 6  
>  Thread-1, Producer a elem 38, Now size is 7  
>  Thread-1, Producer a elem 59, Now size is 8  
>  Thread-1, Producer a elem 72, Now size is 9  
>  Thread-1, Producer a elem 87, Now size is 10  
>  Thread-1, Producer a elem 83, Now size is 11  
>  Thread-1 Producer waiting  
>  Thread-5, Consumer a elem 83. Now size is 10  
>  Thread-5, Consumer a elem 87. Now size is 9  
>  Thread-3, Producer a elem 19, Now size is 10  
>  Thread-3, Producer a elem 15, Now size is 11  
>  Thread-2 Producer waiting  
>  Thread-1 Producer waiting  
>  Thread-4, Consumer a elem 15. Now size is 10  
>  Thread-4, Consumer a elem 19. Now size is 9  
>  Thread-4, Consumer a elem 72. Now size is 8  
>  Thread-4, Consumer a elem 59. Now size is 7  
>  Thread-4, Consumer a elem 38. Now size is 6  
>  Thread-4, Consumer a elem 76. Now size is 5  
>  Thread-4, Consumer a elem 62. Now size is 4  
>  Thread-4, Consumer a elem 97. Now size is 3  
>  Thread-4, Consumer a elem 26. Now size is 2  
>  Thread-4, Consumer a elem 16. Now size is 1  
>  Thread-4, Consumer a elem 74. Now size is 0

## 信号量Semaphore

信号量是一个计数器，用于为多个线程提供对共享数据对象的访问。  
为了获得共享资源，线程需要执行下列操作。

  1. 测试控制该资源的信号量。
  2. 若此信号量的值为正，则线程可以使用该资源。在这种情况下，线程会将信号量减1,表示它使用了一个资源单位。
  3. 否则，若此信号量的值为0，则线程进入休眠状态，直至信号量值大于0.进程被唤醒后，它返回到步骤1.

当线程不再使用由一个信号量控制的共享资源时，该信号量值增1。如果有线程正在休眠等待此信号量，则唤醒它们。

scan2.py


```
# coding=UTF-8
import optparse
import socket
import threading
screenLock = threading.Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print('[+]%d/tcp open' % tgtPort)
        print('[+]' + str(results))
    except:
        screenLock.acquire()
        print('[-]%d/tcp close' % tgtPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIp = socket.gethostbyname(tgtHost)
    except Exception as e:
        print("[-] Cannot resolve '%s' " % tgtHost)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIp)
        print('\n[+] Scan Results for:%s' % tgtName[0])
    except:
        print('\n[+] Scan Results for:%s' % tgtIp)
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port' + str(tgtPort))
        t = threading.Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('usage%prog -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest = 'tgtPort', type='int', help='specify target port')
    options, args = parser.parse_args()
    if options.tgtHost is None or options.tgtPort is None:
        print(parser.usage)
        exit(0)
    else:
        tgtHost = options.tgtHost
        tgtPort = options.tgtPort
    args.append(tgtPort)
    portScan(tgtHost, args)

if __name__ == '__main__':
    main()
```


输出示例：

> hacker git:(master) ✗ python scan2.py -H
[www.baidu.com](http://www.baidu.com) -p 22  
>  [+] Scan Results for:103.235.46.39  
>  Scanning port22  
>  [-]22/tcp close

在这里Semaphore用来控制同一个线程在屏幕上的输出是连续的，不至于线程的输出相互交叉，从而导致不可读。

类似的还有`BoundedSemaphore`。  
示例代码：


```
# coding=UTF-8
from pexpect import pxssh
import optparse
import time
import threading

maxConnections = 5
connection_lock = threading.BoundedSemaphore(value=maxConnections)
Found = False
Fails = 0

def connect(host, user, password, release):
    global Found, Fails
    try:
        s = pxssh.pxssh()
        s.login(host, user, password)
        print('[+] Password Found: ' + password)
        Found = True
    except Exception as e:
        if 'read_nonblocking' in str(e):
            Fails += 1
            time.sleep(5)
            connect(host, user, password, False)
        elif 'synchronize with original prompt' in str(e):
            time.sleep(1)
            connect(host, user, password, False)
    finally:
        if release:
            connection_lock.release()

def main():
    parser = optparse.OptionParser('usage%prog '+'-H <target host> -u <user> -f <password list>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-f', dest='passwdFile', type='string', help='specify password file')
    parser.add_option('-u', dest='user', type='string', help='specify the user')
    (options, args) = parser.parse_args()
    host = options.tgtHost
    passwdFile = options.passwdFile
    user = options.user
    if host == None or passwdFile == None or user == None:
        print(parser.usage)
        exit(0 )
    fn = open(passwdFile, 'r')
    for line in fn.readlines():
        if Found:
            print("[*] Exiting: Password Found")
            exit(0)
        if Fails > 5:
            print("[!] Exiting: Too Many Socket Timeouts")
            exit(0)
        connection_lock.acquire()
        password = line.strip('\r').strip('\n')
        print("[-] Testing: " + str(password))
        t = threading.Thread(target=connect, args=(host, user, password, True))
        t.start()

if __name__ == '__main__':
    main()
```

在这个例子中BoundedSemaphore起到了限制最大并发线程数的作用。

## 队列

生产消费者模型主要是对队列进程操作，贴心的Python为我们实现了一个队列结构，队列内部实现了锁的相关设置。可以用队列重写生产消费者模型。

queue内部实现了相关的锁，如果queue的为空，则get元素的时候会被阻塞，知道队列里面被其他线程写入数据。同理，当写入数据的时候，如果元素个数大于队列的长度，也会被阻塞。也就是在
put 或 get的时候都会获得Lock。

实现和上面类似功能的代码如下：


```
#coding: utf-8
import  threading
import  time
import random

import queue

queue = queue.Queue(10)

class Producer(threading.Thread):

    def run(self):
        while True:
            elem = random.randrange(100)
            queue.put(elem)
            print("Producer a elem {}, Now size is {}".format(elem, queue.qsize()))
            time.sleep(random.random())

class Consumer(threading.Thread):

    def run(self):
        while True:
            elem = queue.get()
            queue.task_done()
            print("Consumer a elem {}. Now size is {}".format(elem, queue.qsize()))
            time.sleep(random.random())

def main():

    for i in range(3):
        Producer().start()

    for i in range(2):
        Consumer().start()


if __name__ == '__main__':
    main()
```

输出结果：

> Producer a elem 97, Now size is 1  
>  Producer a elem 56, Now size is 2  
>  Producer a elem 27, Now size is 3  
>  Consumer a elem 97. Now size is 2  
>  Consumer a elem 56. Now size is 1  
>  Consumer a elem 27. Now size is 0  
>  Producer a elem 41, Now size is 1  
>  Producer a elem 75, Now size is 2  
>  Producer a elem 18, Now size is 3  
>  Consumer a elem 41. Now size is 2  
>  ...

## ThreadLocal

这个概念在Java中也有。类似于**伪私有类属性**，在类方法前加__，如__X,Python会自动扩展这样的名称，以包含类的名称，从而使它们变成真正的唯一。这样在当前线程中就是全局变量，但对于整个进程来说，又是局部变量。

使用示例如下：


```
import threading
local = threading.local()
def func(name):
    print('current thread:%s' % threading.currentThread().name)
    local.name = name
    print("%s in %s" % (local.name,threading.currentThread().name))
t1 = threading.Thread(target=func,args=('haibo',))
t2 = threading.Thread(target=func,args=('lina',))
t1.start()
t2.start()
t1.join()
t2.join()
```

输出结果：

> current thread:Thread-1  
>  haibo in Thread-1  
>  current thread:Thread-2  
>  lina in Thread-2

# 线程池的使用

## threadpool

threadpool需要安装。`pip install threadpool`

```python  
import threadpool  
from time import sleep

def work(name):  
    sleep(1)  
    print("%s doing job" % name)

arg_list = [(["go2live.cn"],None), (["blog.go2live.cn"],None)]
pool = threadpool.ThreadPool(5)
requests = threadpool.makeRequests(work, arg_list)
[pool.putRequest(req) for req in requests]
pool.wait()
```

输出结果：

> go2live.cn doing job  
>  blog.go2live.cn doing job

## multiprocessing.dummy.Pool

标准库。


```
from time import sleep

from multiprocessing.dummy import Pool as ThreadPool

def work(name):
    sleep(1)
    print("%s doing job" % name)

pool = ThreadPool()
results = pool.map(work,['go2live.cn','blog.go2live.cn'])
print(results)
pool.close()
pool.join()

print('main ended')
```

输出结果：

> go2live.cn doing job  
>  blog.go2live.cn doing job  
>  [None, None]  
>  main ended

# 其它线程工具

在debug中可以利用threading模块获取到当前执行的线程情况：

支持的函数：

  * activeCount():返回激活的线程对象的数量
  * currentThread():返回当前cpu执行的线程对象
  * get_ident() 返回当前线程
  * enumerate(): 返回当前激活的线程对象列表
  * main_thread() 返回主 Thread 对象
  * settrace(func) 为所有线程设置一个 trace 函数
  * setprofile(func) 为所有线程设置一个 profile 函数
  * stack_size([size]) 返回新创建线程栈大小；或为后续创建的线程设定栈大小为 size
  * TIMEOUT_MAX Lock.acquire(), RLock.acquire(), Condition.wait() 允许的最大值

threading 可用对象列表：

  * Thread 表示执行线程的对象
  * Lock 锁原语对象
  * RLock 可重入锁对象，使单一进程再次获得已持有的锁(递归锁)
  * Condition 条件变量对象，使得一个线程等待另一个线程满足特定条件，比如改变状态或某个值
  * Semaphore 为线程间共享的有限资源提供一个”计数器”，如果没有可用资源会被阻塞
  * Event 条件变量的通用版本，任意数量的线程等待某个事件的发生，在该事件发生后所有线程被激活
  * Timer 与 Thread 相识，不过它要在运行前等待一段时间
  * Barrier 创建一个"阻碍"，必须达到指定数量的线程后才可以继续。

## 延迟执行新线程Timer

class threading.Timer(interval, function, args=None, kwargs=None)  
过interval秒后再执行函数function，参数为后面的args和kwargs。

这东东在GUI编程中有用。把数据处理扔到新线程，从而不影响当前的用户交互。

示例代码：


```
#coding: utf-8
import  threading
import  time


def test():
    print("{} is running {}".format(threading.current_thread().name, time.ctime()))


def main():
    print("main thread start %s" % time.ctime())
    threading.Timer(3,test).start()
    print("main thread end %s" % time.ctime())


if __name__ == '__main__':
    main()
```

输出如下所示：

> main thread start Tue Feb 7 11:41:56 2017  
>  main thread end Tue Feb 7 11:41:56 2017  
>  Thread-1 is running Tue Feb 7 11:41:59 2017

# python的多线程缺陷

因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter
Lock，任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，解释器就自动释放GIL锁，让别的线程有机会执行。这个GIL全局锁实际上把所有线程的执行代码都给上了锁，所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，要真正利用多核，除非重写一个不带GIL的解释器。

所以，在Python中，可以使用多线程，但不要指望能有效利用多核。如果一定要通过多线程利用多核，那只能通过C扩展来实现，不过这样就失去了Python简单易用的特点。

不过，也不用过于担心，Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。多个Python进程有各自独立的GIL锁，互不影响。

# 总结

Python多线程在IO密集型任务中还是很有用处的，而对于计算密集型任务，应该使用Python多进程。

