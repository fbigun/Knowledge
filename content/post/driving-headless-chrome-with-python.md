---
title: "用python驱动Headless Chrome"
date: 2017-07-13T09:26:50+08:00
menu: "main"
Categories: ["Development","Docker"]
Tags: ["Development","Docker"]
Description: "介绍 Docker Dockerfile 的简单使用方法和示例"
---

# 用python驱动Headless Chrome

> 早在4月份，谷歌宣布将在Chrome 59中发布Headless Chrome。由于相关标志已经在Chrome Canary上市，所以Duo Labs团队认为测试出来很有趣，还提供了Chrome的简要介绍使用Selenium和Python。

![Headless Chrome](https://duo.com/assets/img/blogv2/headless-chrome.gif)

## 浏览器自动化

在我们深入了解任何代码之前，让我们来讨论一个Headless 浏览器是什么，为什么它是有用的。简而言之，Headless 浏览器是没有图形用户界面（GUI）的Web浏览器，通常通过编程控制或通过命令行界面进行控制。

Headless 浏览器的许多用例之一是自动化可用性测试或测试浏览器交互。如果您尝试检查页面在不同浏览器中的呈现方式，或者在用户启动某个工作流程之后确认页面元素存在，则使用Headless 浏览器可以提供大量帮助。除此之外，如果动态地呈现内容（比如说，通过Javascript），传统的面向web的任务，如网页抓取，可能很难做到。使用Headless 浏览器可以轻松访问此内容，因为内容与完整浏览器完全相同。

## Headless Chrome 和 Python

### 黑暗时代

在 Headless Chrome 发布之前，无论何时驱动 Chrome ，可能涉及多个窗口或标签页，您都必须担心CPU和/或内存使用情况。两者都与必须从所请求的URL显示具有渲染图形的浏览器相关联。

当使用 Headless 浏览器时，我们不用担心。因此，我们可以期望较低的内存开销和更快的执行我们编写的脚本。

### 使用 Headless

#### 安装

在开始之前，我们需要安装[Chrome Canary](https://www.google.com/chrome/browser/canary.html)并下载最新的[ChromeDriver](http://npm.taobao.org/mirrors/chromedriver/)（目前为5.​​29）。

接下来，让我们制作一个包含我们所有文件的文件夹：

```
$ mkdir going_headless
```

现在我们可以将ChromeDriver移动到我们刚刚创建的目录中：

```
$ mv Downloads/chromedriver going_headless/
```

由于我们使用Selenium与Python，所以建立一个Python虚拟环境是一个好主意。我使用virtualenv，所以如果你使用另一个虚拟环境管理器，命令可能会有所不同。

```
$ cd going_Headless && virtualenv -p python3 env
$ source env/bin/activate
```

接下来我们需要做的是安装Selenium。如果您不熟悉Selenium，它是一套工具，允许开发人员以编程方式驱动Web浏览器。它具有Java，C＃，Ruby，Javascript（Node）和Python的语言绑定。要为Python安装Selenium软件包，我们可以运行以下操作：

```
$ pip install selenium
```

#### 例

现在我们已经把所有的东西都拿走了，让我们来看看有趣的部分。我们的目标是编写一个在duo.com上搜索我的名字“Olabode”的脚本，并检查我最近在Android安全性中写过的一篇文章。如果您遵循上述说明，您可以使用无锡版的Chrome Canary与Selenium：

```
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'

driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver'),   chrome_options=chrome_options)
driver.get("http://www.duo.com")

magnifying_glass = driver.find_element_by_id("js-open-icon")
if magnifying_glass.is_displayed():
    magnifying_glass.click()
else:
    menu_button = driver.find_element_by_css_selector(".menu-trigger.local")
    menu_button.click()

search_field = driver.find_element_by_id("site-search")
search_field.clear()
search_field.send_keys("Olabode")
search_field.send_keys(Keys.RETURN)
assert "Looking Back at Android Security in 2016" in driver.page_source
driver.close()
```

#### 示例说明

我们来分解脚本中发生了什么。 我们从导入所需的模块开始。 键在键盘中提供键，如RETURN，F1，ALT等。

```
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
```

接下来，我们创建一个ChromeOptions对象，该对象将允许我们设置我们要使用的Chrome二进制文件的位置，并通过Headless 参数。 如果你省略Headless 参数，您将看到浏览器窗口弹出并搜索我的名字。

另外，如果您没有将二进制位置设置为系统上的Chrome Canary的位置，则将使用安装的当前版本的Google Chrome。 我在Mac上写了这个教程，但是你可以在这里找到这个文件在其他平台上的位置。 您只需在相应的文件路径中替换Chrome Chrome浏览器。

```
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'
driver = webdriver.Chrome(executable_path=os.path.abspath(“chromedriver"),   chrome_options=chrome_options)
```

将使用driver.get函数导航到指定的URL。

```
driver.get("https://www.duo.com")
```

duo.com网站是响应式的，所以我们必须处理不同的条件。 因此，我们检查是否显示预期的搜索按钮。 如果不是，我们点击菜单按钮输入我们的搜索字词。

```
magnifying_glass = driver.find_element_by_id("js-open-icon")
if magnifying_glass.is_displayed():
    magnifying_glass.click()
else:
    menu_button = driver.find_element_by_css_selector(".menu-trigger.local")
    menu_button.click()
```

现在我们清除搜索字段，搜索我的名字，并将RETURN键发送到驱动器。

```
search_field = driver.find_element_by_id("site-search")
search_field.clear()
search_field.send_keys("Olabode")
search_field.send_keys(Keys.RETURN)
```

我们检查以确保我最近发布的一篇文章中的博客文章标题是页面的来源。

```
assert "Looking Back at Android Security in 2016" in driver.page_source
```

最后，我们关闭浏览器。

```
driver.close()
```

### 基准

#### 走向Headless

所以，很酷，我们现在可以使用Selenium和Python来控制Chrome，而不必看到浏览器窗口，但是我们对我们之前讨论的性能优势更感兴趣。 使用上述相同的脚本，我们分析了完成任务，高峰内存使用率和CPU百分比所花费的时间。 我们用psutil调查CPU和内存使用情况，并使用timeit测量任务完成的时间。

|                        | Headless (60.0.3102.0) | Headed (60.0.3102.0) |
| :--------------------: | :--------------------: | :------------------: |
|      Median Time       |      5.29 seconds      |     5.51 seconds     |
|   Median Memory Use    |        25.3 MiB        |      25.47 MiB       |
| Average CPU Percentage |         1.92%          |        2.02%         |

对于我们的小脚本，完成任务所需的时间（4.3％），内存使用率（.5％）和CPU百分比（5.2％）之间的差异很小。 虽然我们的例子中的收益非常小，但这些收益在具有数十个测试的测试套件中将被证明是有益的。

## 手动与Adhoc

在上面的脚本中，我们在创建WebDriver对象时启动ChromeDriver服务器进程，并在调用quit（）时终止。 对于一次性脚本，这不是问题，但是这可能会浪费大量测试套件的时间，为每个测试创建一个ChromeDriver实例。 幸运的是，我们可以自己手动启动和停止服务器，只需要对上面的脚本进行一些更改。

### 示例代码段

```
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

service = webdriver.chrome.service.Service(os.path.abspath(“chromedriver"))
service.start()

chrome_options = Options()
chrome_options.add_argument("--headless")

# path to the binary of Chrome Canary that we installed earlier
chrome_options.binary_location = '/Applications/Google Chrome   Canary.app/Contents/MacOS/Google Chrome Canary'

driver = webdriver.Remote(service.service_url,   desired_capabilities=chrome_options.to_capabilities())
```

### 片段解释

虽然只有三行代码发生了变化，但是我们来谈谈它们中的内容。 为了手动控制ChromeDriver服务器，我们必须使用ChromeDriverService。 我们通过创建一个具有ChromeDriver路径的服务对象，然后我们可以启动该服务。

```
service = webdriver.chrome.service.Service(os.path.abspath(“chromedriver"))
service.start()
```

最后我们要做的是创建一个可以连接到远程服务器的WebDriver。 为了使用Chrome Canary和Headless 部分，我们必须传递所有选项的字典，因为远程WebDriver对象不接受Option对象。

```
driver = webdriver.Remote(service.service_url,   desired_capabilities=chrome_options.to_capabilities())
```

### 收益

通过添加手动启动服务，我们看到预期的速度提高。 Headless 和浏览器完成脚本任务的中间时间下降了11％（4.72秒），分别为4％（5.29秒）。

|                         | Headed Browser | Headless Browser |
| :---------------------: | :------------: | :--------------: |
| Median Time(% decrease) |       4%       |       11%        |
|  Median Time (Seconds)  |  5.29 seconds  |   4.72 seconds   |

## 总结

Headless Chrome的发布一直在等待着。 随着PhantomJS的创始人作为维护者的消息宣布，我们坚信Headless Chrome是Headless 浏览器的未来。

虽然我们在本演练中介绍了Selenium，但值得一提的是，如果您进行任何类型的分析或需要创建您访问的页面的PDF，那么[Chrome DevTools API](https://chromedevtools.github.io/devtools-protocol/)可以是一个有用的资源。 我们希望这可以帮助您开始使用Headless 版Chrome，无论您是进行任何类型的质量检测测试，还是自动执行所有日常的网络相关任务。

注意：--disable-gpu命令是暂时需要，最后会消失。

## Resources

[Github Repo](https://github.com/duo-labs/tutorials/tree/master/going_headless)

### Chrome Links

- [Chrome Mirr](https://api.shuax.com/tools/getchrome)
- [Chrome Driver mirr](http://npm.taobao.org/mirrors/chromedriver/)
- [Chrome Canary](https://www.google.com/chrome/browser/canary.html)
- [Chrome Driver](https://sites.google.com/a/chromium.org/chromedriver/downloads)
- [Chrome DevTools API](https://chromedevtools.github.io/devtools-protocol/)

### Selenium Links

- [Selenium HQ](http://www.seleniumhq.org/)
- [Selenium Python Package](http://selenium-python.readthedocs.io/)
