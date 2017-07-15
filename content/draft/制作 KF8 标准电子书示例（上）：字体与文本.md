关于如何制作 Kindle 电子书，可以参考《[遵循亚马逊标准！Kindle
电子书专业制作教程](https://kindlefere.com/post/132.html)》这篇文章，文中介绍了制作 Kindle
电子书的必要步骤，但对如何格式化电子书内容着墨不多，所以本文将会把这部分内容展开，结合示例详细说明。限于篇幅本文分为上下两篇，分别为“字体与文本”和“[图片与背景](https://kindlefere.com/post/389.html)”。

> 目录

>

> 一、字体样式  
> 1、用 Font 标签设置字体  
> 2、用 CSS 样式设置字体  
> 二、文本样式  
> 三、文本对齐  
> 四、文本阴影  
> 五、首字下沉  
> 六、显示区域  
> 七、添加边框  
> 八、背景颜色  
> 九、边框风格  
> 十、数据表格

## 一、字体样式

KF8 标准的 Kindle
电子书支持多种为文本添加样式的方式。不过一般情况下，不建议为文本内容指定字体样式（如字体、字号、颜色等），因为用户更喜欢根据自己的阅读偏好控制显示字体或本文的显示。

为文本设置字体样式有两种方法，一种是使用 HTML 中的 **font** 标签，另一种是使用 CSS 样式。

### 1、用 Font 标签设置字体

你可以为电子书内容设置字体（Font Face），一旦为内容指定了字体，用户在 Kindle
字体设置里选择的字体将会被你所指定的字体所取代。除了可以添加系统自带字体（如英文字体 Bookerly、Baskerville、Helvetica
等，中文字体“宋体”、“黑体”等），还可以使用[自定义字体](https://kindlefere.com/post/324.html)。

**示例截图：**

![text-style_1](https://kindlefere.b0.upaiyun.com/uploads/2016/05/text-
style_1.png)

**示例代码：**
    
    
    <p>
    	<font face="Georgia">Georgia, </font>
    	<font face="Caecilia">Caecilia, </font>
    	<font face="Trebuchet">Trebuchet, </font>
    	<font face="Verdana">Verdana, </font>
    	<font face="Arial">Arial, </font>
    	<font face="Times New Roman">Times New Roman, </font>
    	<font face="Courier">Courier, </font>
    	<font face="Lucida">Lucida</font><br>
    	<font color="red" size="1">Red size 1 text. </font>
    	<font color="blue" size="2">Blue size 2 text. </font>
    	<font color="green" size="4">Green size 4 text. </font>
    	<font color="purple" size="6">Purple size 6 text. </font>
    </p>

**实现说明：**

使用 HTML 的 `font` 标签及其属性 `face` 设置字体，使用属性 `color` 和 `size` 设置字体颜色和字号。

    
    
    <font face="Georgia" color="green" size=4 >

除了使用 HTML 标签外，也可以使用 CSS 样式属性 `font-family` 实现同样的效果。

    
    
    font-family: arial;
    color: red;
    font-size: 129%;

注意，对于当前只有黑白屏幕的 Kindle 设备来说，把字体设置为彩色并没有什么作用，但是对于可以阅读 mobi 格式的平板设备，以及未来会出现的彩色
E-Ink 设备就有用了。

### 2、用 CSS 样式设置字体

除 font 标签外，还可以使用 CSS 样式实现包括风格、字号、异体（小型大写字母）在内的字体设置。

**示例截图：**

![text-style_2](https://kindlefere.b0.upaiyun.com/uploads/2016/05/text-
style_2.png)

**示例代码：**
    
    
    <p>
    	<span style="font-style: normal; font-weight: normal; font-variant: normal;">Normal text.</span><br>
    	<span style="font-style: italic; font-weight: lighter; font-variant: normal;">Italic lighter text.</span><br>
    	<span style="font-style: italic; font-weight: bold; font-variant: normal;">Italic bold text.</span><br>
    	<span style="font-style: oblique; font-weight: bolder; font-variant: small-caps;">Oblique bold small-caps text.</span><br>
    </p>

**实现说明：**

样例中实现的字体效果是通过 `font-style`（字体风格）、`font-weight`（字体粗细）和 `font-variant`（小型大写字）这三个
CSS 属性实现的。其中 `font-variant` 属性对中文没什么意义。

    
    
    <span style="font-style: italic; font-weight: lighter; font-variant: normal">

注意，为说明更直观，这里的 CSS
代码使用的是“内联样式”，你可以使用[“外部样式表”或“内部样式表”](http://w3school.com.cn/html/html_css.asp)。

## 二、文本样式

除了字体样式可以设置，还可以使用文本样式格式化文本内容，比如字间距和文本对齐。

**示例截图：**

![text-style_3](https://kindlefere.b0.upaiyun.com/uploads/2016/05/text-
style_3.png)

**示例代码：**
    
    
    <p>
    	<span style="word-spacing: 1em; text-transform: uppercase;">Uppercase text with Word spacing 1em.</span><br>
    	<span style="letter-spacing: .2em; word-spacing: 2em; text-decoration: underline;">Underlined text with letter spacing 0.2em, word spacing 2em.</span><br>
    	<span style="text-decoration: line-through; text-transform: capitalize;">Capitalized line through text.</span>
    </p>

**实现说明：**

如示例所示，设置文本样式，可以使用 CSS 样式属性 `word-spacing`（字间距）、`text-
transform`（字母大小写）、`letter-spacing`（字母间距）以及 `text-decoration`（文本修饰）实现。

    
    
    <span style="letter-spacing: .2em; word-spacing: 2em; text-decoration:underline;">

## 三、文本对齐

使用 CSS 样式可以使文本内容按照你所想要效果对齐，如居中、左对齐或右对齐。

**示例截图：**

![text-style_4](https://kindlefere.b0.upaiyun.com/uploads/2016/05/text-
style_4.png)

**示例代码：**
    
    
    <div>
    	<p style="text-align: center;">Center aligned text.<br> Lorem ipsum sed ut nibh nibh. Vestibulum facilisis nulla id leo ullamcorper molestie. Donec sit amet mauris ut arcu vulputate faucibus. Sed eleifend fringilla mauris, eget fermentum nibh consequat eget.</p><br>
    	<p style="text-align: left;">Left aligned text.<br> Lorem ipsum etiam euismod tortor ac massa hendrerit et rhoncus magna lobortis. Nulla et faucibus nibh. Aliquam sed arcu eget nisl vulputate fermentum. Cras sed arcu sed turpis placerat vehicula.</p><br>
    	<p style="text-align: right;">Right aligned text.<br> Lorem ipsum curabitur nulla mauris, porta non elementum at, imperdiet a velit. Suspendisse in orci adipiscing lectus tempor molestie ac a nibh. Ut malesuada sapien luctus risus laoreet non lobortis erat porta. Mauris ante purus, tincidunt a condimentum sit amet, sagittis auctor turpis.</p>
    </div>

**实现说明：**

调整文本对齐方式可以使用 `text-align` 属性，三个值分别为
center（居中对齐）、left（左对齐）、right（右对齐）。设置文本首行缩进可以使用 `text-indent` 属性。

    
    
    text-align: right;
    text-indent: 0em;

比如中文中常用的首行缩进两个字符，就可以使用 `text-indent: 2em;` 这行 CSS 代码实现。

## 四、文本阴影

为使内容显得更具风格，还可以为文本设置阴影。

**示例截图：**

![text-style_5](https://kindlefere.b0.upaiyun.com/uploads/2016/05/text-
style_5.png)

**示例代码：**
    
    
    <div>
    	<p style="text-shadow: 5px 5px #379027; font-size: 500%; font-weight: bolder;"> Shadowed text.</p>
    </div>

**实现说明：**

设置文本阴影可以使用 `text-shadow` 这一 CSS 属性。需要注意的是，示例中 `text-shadow`
有三个属性，从左至右依次为：阴影的水平位移大小、阴影的垂直位移大小以及阴影的颜色。

    
    
    text-shadow: 5px 5px #379027;

## 五、首字下沉

首字下沉可以用来使得文本的第一个字母或单词的样式与众不同。

**示例截图：**

![text-style_6](https://kindlefere.b0.upaiyun.com/uploads/2016/05/text-
style_6.png)

**示例代码：**
    
    
    <div>
    	<p><span class="dropcaps1">L</span>orem ipsum sed ut nibh nibh. Vestibulum facilisis nulla id leo ullamcorper molestie. Donec sit amet mauris ut arcu vulputate faucibus. Sed eleifend fringilla mauris, eget fermentum nibh consequat eget.
    	Etiam euismod tortor ac massa hendrerit et rhoncus magna lobortis. Nulla et faucibus nibh. Aliquam sed arcu eget nisl vulputate fermentum. Cras sed arcu sed turpis placerat vehicula.</p>
    	<p><span class="dropcaps2">Lorem</span> ipsum curabitur nulla mauris, porta non elementum at, imperdiet a velit. Suspendisse in orci adipiscing lectus tempor molestie ac a nibh. Ut malesuada sapien luctus risus laoreet non lobortis erat porta. Mauris ante purus, tincidunt a condimentum sit amet, sagittis auctor turpis.
    	Etiam euismod tortor ac massa hendrerit et rhoncus magna lobortis. Nulla et faucibus nibh. Aliquam sed arcu eget nisl vulputate fermentum. Cras sed arcu sed turpis placerat vehicula.</p>
    </div>

▲ 首字下沉示例 HTML 代码

    
    
    span.dropcaps1{
    	float: left;
    	font-size: 4em;
    	font-weight: bold;
    	color: #C11B17;
    	margin-top: -.2em;
    	margin-bottom: -.2em;
    	margin-right: .1em;
    	padding-right: .1em;
    	text-shadow:5px -3px #151B54;
    }
    
    span.dropcaps2{
    	float: left;
    	font-size: 4em;
    	font-weight: bold;
    	color: #7D2252;
    	margin-top: -.2em;
    	margin-bottom: -.2em;
    	margin-right: .1em;
    	padding-right: .1em;
    }

▲ 首字下沉示例 CSS 代码

**实现说明：**

设置首字下沉可以使用 `float`、`font` 和 `margin` 属性。示例中实现首字下沉的 CSS 代码如下所示。

    
    
    span.dropcaps{
    	float: left;
    	font-size: 4em;
    	font-weight: bold;
    	color: #6A287E;
    	margin-top: -.2em;
    	margin-bottom: -.2em;
    	margin-right: .1em;
    	padding-right: .1em;
    }

## 六、显示区域

如果有需要，还可以通过宽度和高度来设置文本内容的显示区域。

**示例截图：**

![text-style_7](https://kindlefere.b0.upaiyun.com/uploads/2016/05/text-
style_7.png)

**示例代码：**
    
    
    <div>
    	<p style="width:50%;">Lorem ipsum duis ultrices eleifend rhoncus. Quisque vulputate nisl ultricies nisi posuere at lacinia quam suscipit. Curabitur risus nunc, laoreet at interdum eget, rutrum non neque. Donec et turpis libero. Nunc commodo, nisl laoreet fringilla iaculis, magna dui tincidunt orci, a aliquet velit leo vitae orci. Phasellus varius orci fermentum mi aliquam vitae convallis odio aliquet. Nam commodo lobortis sem, vel ultricies erat suscipit eget.</p>
    </div>

**实现说明：**

设置文本内容的显示区域可以使用 `width` 和 `height` 这两个 CSS 属性。

    
    
    width: 50%;
    height: 50%;

设置区域时，有些单词可能会溢出设置宽度的边界，可以使用 `word-wrap` 这个属性避免这一问题。

    
    
    word-wrap: break-word;

## 七、添加边框

如果有需要，可以使用边框装饰文本内容。

**示例截图：**

![text-style_8](https://kindlefere.b0.upaiyun.com/uploads/2016/05/text-
style_8.png)

**示例代码：**
    
    
    <div>
    	<p style="width: 50%; padding: 1em; border-left-style: solid; border-top-style: solid; border-right-style: groove; border-bottom-style: groove; border-color: green; border-width: 0.4em;">Lorem ipsum sed ut nibh nibh. Vestibulum facilisis nulla id leo ullamcorper molestie. Donec sit amet mauris ut arcu vulputate faucibus. Sed eleifend fringilla mauris, eget fermentum nibh consequat eget. Etiam euismod tortor ac massa hendrerit et rhoncus magna lobortis. Nulla et faucibus nibh. Aliquam sed arcu eget nisl vulputate fermentum. Cras sed arcu sed turpis placerat vehicula.</p>
    </div>

**实现说明：**

为内容设置边框可以使用 `border` 这一 CSS 属性，不同的边框风格、尺寸和颜色可以实现不同的边框样式。`border` 的 CSS
代码可以如示例中那样分开写，以便更精确的控制每一条边，也可以把所有边框属性在一个声明之中，可以根据实际情况选用。各种属性用法可查看 CSS 参考手册中的
[Border 用法](http://www.w3school.com.cn/cssref/pr_border.asp)。

    
    
    border: 0.3em solid red;

注意，为使内容更具可读性，可以使用` padding` 属性在内容和边框之间产生一些空间。

## 八、背景颜色

有时候为了着重强调，为文本内容设置背景色可使其显得更具吸引力。

**示例截图：**

![text-style_9](https://kindlefere.b0.upaiyun.com/uploads/2016/05/text-
style_9.png)

**示例代码：**
    
    
    <div>
    	<p style="background: #3dbdbd;">Lorem ipsum aliquam interdum, libero id elementum rutrum, metus urna adipiscing elit, quis ultricies urna turpis sit amet lorem. Mauris ante diam, commodo in suscipit eget, fermentum eget quam. Integer blandit dui mauris. Aenean tempor enim ut erat facilisis eget aliquet erat egestas. Aliquam tincidunt facilisis nisl, id venenatis nulla imperdiet dignissim. Curabitur enim urna, lobortis sed eleifend in, sodales ac purus. Pellentesque vel ullamcorper dui. Phasellus auctor eleifend suscipit.</p>
    </div>

**实现说明：**

设置内容的背景颜色可以使用 `background` 这一 CSS 属性实现。

    
    
    background: red;

关于背景样式的更多内容，请查看《制作 KF8 标准电子书示例（下）：图片与背景》这篇文章。

## 九、边框风格

用 CSS 属性为文本内容添加边框后，还可以设置不同的边框风格以区分不同内容，如笔记、标注、标签等。比如圆角边框，就可以很明显得在视觉上区分不同类型的内容。

**示例截图：**

![text-style_10](https://kindlefere.b0.upaiyun.com/uploads/2016/05/text-
style_10.png)

**示例代码：**
    
    
    <div>
    	<p style="border: 0.2em green solid; border-radius: 2em; padding: 1%;">Lorem ipsum nulla mollis, lacus vitae cursus fermentum, tellus quam ornare nisl, in congue mi dolor sit amet purus. Mauris tempor orci ut neque sollicitudin gravida.</p><br>
    	<p style="border: 0.2em green solid; border-radius: 1em; padding: 1%;">Lorem ipsum proin at fermentum justo. Duis sodales diam eget erat pellentesque auctor. Duis molestie consequat accumsan. Vestibulum consectetur ligula adipiscing nisl rhoncus vel bibendum tellus feugiat. Mauris sit amet metus sem. Sed eros risus, facilisis faucibus commodo sed, cursus sed nisi. Morbi nibh mi, tincidunt semper tempor at, feugiat non erat. Aliquam euismod lorem a diam viverra rhoncus. Curabitur ultricies erat quis leo semper in luctus nunc vehicula. Nam tempor, nibh et consectetur facilisis, nunc felis consectetur erat, eget fermentum urna turpis sed arcu. Ut tincidunt sodales massa sed tempus. Mauris at neque arcu. Curabitur mauris nisi, semper in feugiat ac, aliquet nec leo. Aliquam ultrices consectetur magna vel lobortis. Integer vehicula lectus nec ipsum bibendum rhoncus. Fusce varius malesuada tellus at pulvinar.</p>
    </div>

**实现说明：**

设置圆角边框可以使用 `border-radius` 这一 CSS 属性。

    
    
    border-radius: 1em;

## 十、数据表格

可以添加带有丰富样式的表格。

**示例截图：**

![text-style_11](https://kindlefere.b0.upaiyun.com/uploads/2016/05/text-
style_11.png)

**示例代码：**
    
    
    <div>
    	<img class="mobicontent" src="images/table.png" width="250" height="370">
    	<table class="defaultcontent" border="3" style="display: block; width:12em" cellspacing="5" cellpadding="10">
    		<caption>Table</caption>
    		<tr>
    			<td> 1, 1 content</td>
    			<td> 1, 2 content </td>
    		</tr>
    		<tr>
    			<td> 2, 1 content </td>
    			<td> 2, 2 content </td>
    		</tr>
    	</table>
    </div>

**实现说明：**

表格在 mobi 格式中看起来不是很美观。对于 mobi 格式，可以将 CSS 媒体查询和隐藏属性 `display: none;`
结合使用，用有着同样内容的图片替代表格。

以上便是制作 Kindle 电子书时对文本内容的常用设置，当然有些用法并不拘泥示例中的代码，如果想知道 KF8 标准电子书都支持哪些 HTML 和
CSS，可以参考《[KF8 格式电子书支持的 HTML 标签和 CSS
属性](https://kindlefere.com/post/143.html)》这篇文章或者前往[亚马逊官网](http://www.amazon.com/gp/feature.html?docId=1000729901)获悉。下篇我们将会详细介绍
Kindle 电子书中的图片和背景的用法。

