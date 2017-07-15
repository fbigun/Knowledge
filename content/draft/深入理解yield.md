本篇博客转载了[点击打开链接](http://www.pythontab.com/html/2015/pythonhexinbiancheng_0415/946.html)，又加上了自己的一点理解

#  深入理解yield


yield的英文单词意思是生产，刚接触Python的时候感到非常困惑，一直没弄明白yield的用法。

只是粗略的知道yield可以用来为一个函数返回值塞数据，比如下面的例子：

```
def addlist(alist):

    for i in alist:

        yield i + 1
```
  
取出alist的每一项，然后把i + 1塞进去。然后通过调用取出每一项：

```
alist = [ 1, 2, 3, 4]

for x in addlist(alist):

    print x,
```

这的确是yield应用的一个例子

1\. 包含yield的函数

假如你看到某个函数包含了yield，这意味着这个函数已经是一个Generator，它的执行会和其他普通的函数有很多不同。比如下面的简单的函数：

```
def h():

    print 'To be brave'

    yield 5

h()
```

可以看到，调用h()之后，print 语句并没有执行！这就是yield，那么，如何让print
语句执行呢？这就是后面要讨论的问题，通过后面的讨论和学习，就会明白yield的工作原理了。

2\. yield是一个表达式

Python2.5以前，yield是一个语句，但现在2.5中，yield是一个表达式(Expression)，比如：

m = yield 5

表达式(yield 5)的返回值将赋值给m，所以，认为 m = 5 是错误的。那么如何获取(yield
5)的返回值呢？需要用到后面要介绍的send(msg)方法。

3\. 透过next()语句看原理

现在，我们来揭晓yield的工作原理。我们知道，我们上面的h()被调用后并没有执行，因为它有yield表达式，因此，我们通过next()语句让它执行。next()语句将恢复Generator执行，并直到下一个yield表达式处。比如：

```
def h():

    print 'Wen Chuan'

    yield 5

    print 'Fighting!'

c = h()

c.next()
```

c.next()调用后，h()开始执行，直到遇到yield 5，因此输出结果：

Wen Chuan

当我们再次调用c.next()时，会继续执行，直到找到下一个yield表达式。由于后面没有yield了，因此会拋出异常：

```
Wen Chuan

Fighting!

Traceback (most recent call last):

  File "/home/evergreen/Codes/yidld.py", line 11, in <module>

    c.next()

StopIteration
```

4\. send(msg) 与 next()

了解了next()如何让包含yield的函数执行后，我们再来看另外一个非常重要的函数send(msg)。其实next()和send()在一定意义上作用是相似的，区别是send()可以传递yield表达式的值进去，而next()不能传递特定的值，只能传递None进去。因此，我们可以看做

c.next() 和 c.send(None) 作用是一样的。

来看这个例子：

```
def h():

    print 'Wen Chuan'

    m = yield 5  # Fighting!

    print m

    d = yield 12

    print 'We are together!'

c = h()

c.next()  #相当于c.send(None)

c.send('Fighting!')  #(yield 5)表达式被赋予了'Fighting!'
```

输出的结果为：

Wen Chuan Fighting!

需要提醒的是，第一次调用时，请使用next()语句或是send(None)，不能使用send发送一个非None的值，否则会出错的，因为没有yield语句来接收这个值。

5\. send(msg) 与 next()的返回值

send(msg) 和 next()是有返回值的，它们的返回值很特殊，返回的是下一个yield表达式的参数。比如yield 5，则返回 5
。到这里，是不是明白了一些什么东西？本文第一个例子中，通过for i in alist 遍历
Generator，其实是每次都调用了alist.Next()，而每次alist.Next()的返回值正是yield的参数，即我们开始认为被压进去的东东。我们再延续上面的例子：

```
def h():

    print 'Wen Chuan'

    m = yield 5  # Fighting!

    print m

    d = yield 12

    print 'We are together!'

c = h()

m = c.next()  #m 获取了yield 5 的参数值 5

d = c.send('Fighting!')  #d 获取了yield 12 的参数值12

print 'We will never forget the date', m, '.', d
```

输出结果：

```
Wen Chuan Fighting!

We will never forget the date 5 . 12
```

6\. throw() 与 close()中断 Generator

中断Generator是一个非常灵活的技巧，可以通过throw抛出一个GeneratorExit异常来终止Generator。Close()方法作用是一样的，其实内部它是调用了throw(GeneratorExit)的。我们看：

```
def close(self):

    try:

        self.throw(GeneratorExit)

    except (GeneratorExit, StopIteration):

        pass

    else:

        raise RuntimeError("generator ignored GeneratorExit")

# Other exceptions are not caught  
```

因此，当我们调用了close()方法后，再调用next()或是send(msg)的话会抛出一个异常：

```
Traceback (most recent call last):

  File "/home/evergreen/Codes/yidld.py", line 14, in <module>

    d = c.send('Fighting!')  #d 获取了yield 12 的参数值12

StopIteration
```

调用next()函数返回的是yield后面的值，yield表达式的值不是yield后面跟着的东西，而是通过send()函数传入进去的值，传入的值赋值给当前yield表达式的值，详细见下面代码

```
def f():
    print('start')
    a = yield 1
    print(a)
    print('middle....')
    b = yield 2 #2这个值只是迭代值，调用next时候返回的值
    print(b) #传入的参数是给当前yield的，也就是yield 2，因为当前函数走到了yield 2，所以传入的参数没有给yield 1
    print('next')
    c = yield 3
    print(c)


a = f()
next(a)
next(a)
a.send('msg')
```

结果是：

```
start
None
middle....
msg
next
[Finished in 0.2s]
```
