> 目录

>

> 一、Kindle Previewer – 适用于初级用户  
> 二、KindleGen – 适用于高级用户  
> 1、适用于 Windows (XP, Vista, 7, 8) 的 KindleGen  
> 2、适用于 Mac OS 10.5 和 i386 以上版本的 KindleGen  
> 3、适用于 Linux 2.6 i386 的 KindleGen

亚马逊官方提供了两种电子书转换工具，一个是 Kindle Previewer，带 UI 易操作，适用于初级用户，还有一种是 KindleGen，无 UI
是命令行形式，适用于高级用户，其实 Kindle Previewer 也是调用 KindleGen 进行转换的。小伙伴们可以按照自己的需求选择使用。

和另一款电子书格式转换软件 Calibre 相比，亚马逊提供的转换工具有一个显著的优点，那就是不破坏原有的排版格式，比如一个排版精良的 azw3
格式电子书通过 Calibre 转换后通常会破坏掉原有的排版，如行距变小、内嵌字体丢失等，所以为避免这个问题可以这样做可以先通过 Calibre 将
azw3 转换成 epub 格式（因为这两款软件都不支持直接将 azw3 转换成 mobi），然后在通过这两款软件的任何一个将 epub 格式转换成
mobi，这样就可以保持原有排版风格了。

## 一、Kindle Previewer – 适用于初级用户

![Kindle
Previewer](https://kindlefere.b0.upaiyun.com/uploads/2014/07/Kindle_Previewer.jpg)

Kindle Previewer 是一个模拟 Kindle
设备和应用程序显示书籍内容的使用界面工具。是亚马逊官方开发的一款kindle系列产品模拟器，可以模拟出kindle系列产品的功能。当然也可以用来阅读.mobi等专有格式的电子书，还可以对部分电子书格式进行格式的转换。

### 1、Kindle Previewer 软件下载

<https://kindlefere.com/tools#Kindle_Previewer>

### 2、Kindle Previewer 使用步骤

  1. 下载 [Kindle Previewer](https://kindlefere.com/tools#Kindle_Previewer) 并安装；
  2. 安装完成后，打开 Kindle Previewer，单击“Open book”；
  3. 选择 EPUB/HTML/OPF 文档，按照向导指示转换电子书并进行预览；
  4. 转换成功的电子书扩展名为“.mobi”，位于与源 HTML/EPUB 相同的文件夹中带有“Compiled-”文件名的文件夹之下。

## 二、KindleGen – 适用于高级用户

![KindleGen](https://kindlefere.b0.upaiyun.com/uploads/2014/07/kindlegen.png)

KindleGen 是一个免费的命令行工具，也是亚马逊唯一官方支持的文件转换工具，可通过它把 HTML、XHTML 或 IDPF 2.0 格式（带有
XML.opf 描述文件的 HTML 内容文件）的源文件创建为 Kindle 电子图书。高级用户可以使用命令行工具将 EPUB/HTML 转换为
Kindle 电子书。 您可以在 Windows、Mac 和 Linux 平台上使用此界面。此工具可用于自动批量转换。

### 1、KindleGen 软件下载

<https://kindlefere.com/tools#KindleGen>

### 2、KindleGen 使用步骤：

**● 适用于 Windows (XP, Vista, 7, 8) 的 KindleGen**

  1. 下载 [KindleGen](https://kindlefere.com/tools#KindleGen) 并解压缩到 c:\KindleGen。
  2. 通过选择 Start menu（开始菜单）&gt; All Programs（所有程序）&gt; Accessories（附件）&gt; Command Prompt（命令提示符），打开一个命令提示符。
  3. 输入 c:\KindleGen\kindlegen。 系统将显示如何运行 KindleGen 的指导。
  4. 转换示例：要转换一个名为 book.html 的文件，请进入书所在的目录文件，例如 cd desktop，然后输入 c:\KindleGen\kindlegen book.html。 如果转换成功，一个名为 book.mobi 的新文件将显示在桌面。
  5. 请注意：我们建议您遵循这些步骤运行 KindleGen。 双击 KindleGen 图标不能打开此程序。运行上述命令时不带引号。 如果您将某个文件拖至 kindlegen 可执行文件，该工具将为您转换文件，但是您无法获得输出日志，因此，我们不推荐此操作。

**● 适用于 Mac OS 10.5 和 i386 以上版本的 KindleGen**

  1. 下载 [KindleGen](https://kindlefere.com/tools#KindleGen) 并解压缩。
  2. 在“应用程序”中找到并运行 Terminal（终端）。 
  3. 要查看如何运行 KindleGen 的指导，将解压后的 kindlegen 程序拖放到 Terminal（终端）窗口中并按 Enter（输入）即可查看指导。也可以通过在终端输入命令 cd ~/Downloads/KindleGen_Mac_i386_v2，然后输入命令 kindlegen，以查看指导。
  4. 转换示例：要转换名为 book.epub 的文件，先打开 Terminal（终端），然后将 kindlegen 程序拖放到 Terminal（终端）窗口，然后再把 book.epub 文件拖放到 Terminal（终端）窗口，最后按 Enter（回车）即可开始进行转换。如果转换成功，将会在源文件所在目录生成一个名为 book.mobi 的新文件。

**● 适用于 Linux 2.6 i386 的 KindleGen**

  1. 下载 [KindleGen](https://kindlefere.com/tools#KindleGen) 至一个文件夹，例如主目录中的 Kindlegen (~/KindleGen)。
  2. 解压文件的内容至 ‘~/KindleGen’。打开终端，使用命令“cd ~/KindleGen”移至包含下载文件的文件夹，然后使用命令“tar xvfz kindlegen_linux_2.6_i386_v2.tar.gz”解压内容。
  3. 打开终端应用程序，并输入 ~/KindleGen/kindlegen。 系统将显示如何运行 KindleGen 的指导。
  4. 转换示例：要转换一个名为 book.html 的文件，请进入书所在的目录文件，例如 cd desktop，然后输入 ~/KindleGen/kindlegen book.html。如果转换成功，一个名为 book.mobi 的新文件将显示在桌面。

### 3、KINDLEGEN命令说明

    
    
    *************************************************************
     Amazon kindlegen(MAC OSX) V2.9 build 1028-0897292 
     命令行电子书制作软件 
     Copyright Amazon.com and its Affiliates 2014 
    *************************************************************
    
    使用规则：
    kindlegen [文件名.opf/.htm/.html/.epub/.zip 或目录] [-c0 或 -c1 或 c2] [-verbose] [-western] [-o <文件名>]
    
    注释：
    zip formats are supported for XMDF and FB2 sources
    directory formats are supported for XMDF sources
    
    选项: 
    -c0：不压缩
    -c1：标准 DOC 压缩
    -c2：Kindle huffdic 压缩
    -o ：指定输出文件名。输出文件将被创建在与输入文件一样的目录中。 不应该包含目录路径。
    -verbose： 在电子书转换过程中提供更多信息 
    -western：强制创建 Windows-1252 电子书
    -releasenotes：显示发行说明
    -gif：转换为 GIF 格式的图像（书中没有 JPEG）
    -locale  ： 以选定语言显示消息 ( To display messages in selected language ) 
       en: 英语
       de: 德语
       fr: 法语
       it: 意大利语
       es: 西班牙语人
       zh: 中文
       ja: 日本
       pt: 葡萄牙
       ru: Russian
       nl: Dutch

除了以上所列出的参数之外，KindleGen 还有一个隐藏参数：`-dont_append_source`。该参数使得 kindlegen 在生成 mobi
时不再添加源文件到生成的 mobi 文件中，这样可以大大缩减 mobi 的体积，也就不再需要
[kindlestrip](https://kindlefere.com/post/240.html) 来帮助删除 mobi
文件的冗余成分了。具体命令如下所示：

    
    
    $ kindlegen -dont_append_source xxx.opf

### 4、关于 kindlegen 生成的 mobi 文件

使用 kindlegen 的默认设置生成的 mobi 文件主要包含四部分：

  * 一部分为 MOBI7(azw) 专属文件（html 主文件，内容相关的 opf 文档及目录相关的 ncx 文档）；
  * 一部分为 KF8(azw3) 专属文件（典型的 epub 文件树，包含 css 样式表）；
  * 一部分为 mobi7 和 KF8 格式共用的图片池，包含了所有 html/xhtml 文件链接的图片文件；
  * 最后一部分是转换前的源文件的打包存档（仅供调试之用，推送时不会看到），大小和转换前的 epub 文件相同，这部分对于阅读纯属冗余项，清除对阅读无丝毫影响，[kindlestrip](https://kindlefere.com/post/240.html) 的作用就是将 kindlegen 生成的 mobi 中这部分删除，以求更小的文件体积。

图片池部分有可选的附属部分 —— HD 图片池。当源文件中含大小超过 127KB 的图片时 kindlegen 会自动压缩图片至 127KB
以下（儿童电子书的图片大小为 255KB，这是亚马逊电子书标准所规定的图片体积上限），同时将原图保存在 HD 图片池中（但如果原图超过 2MB
的话还是会压缩至 2MB 以下，2MB 是亚马逊电子书标准中 HD 图片的大小上限）。

云端服务器会识别接收设备，将原始 mobi 文件切分后推送。kindle3 及之前的设备推送 MOBI7(azw) 文件；kindle4 之后的设备推送
KF8(azw3) 文件。MOBI7 格式较简陋，对设备性能要求较低，KF8 格式则更先进，基本支持了 epub
的各个特性，有独立的样式表使得排版更好。这两个文件共同之处在于都使用压缩后的普通图片池以适应电子墨水屏的阅读。而 HD 图片池将在推送至
kindlefire hdx
这样的高清屏设备时，再添加进推送的电子书文件中，以获得更佳的阅读效果。[KindleUnpack](https://kindlefere.com/post/187.html)
中的 HD image 选项正是用 HD 图片（若是有的话）替换压缩后的图片，生成的 epub
中的图片更高清。[via](http://kindleren.com/forum.php?mod=viewthread&tid=197123)

