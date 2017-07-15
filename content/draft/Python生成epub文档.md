**开始之前**

本教程讲述如何创建 EPUB 格式的电子图书。EPUB 是一种基于 XML 的、对开发者友好的格式，正逐渐成为数字图书的事实标准。但 EPUB
不仅可用于图书，还包括：

  * 对文档打包以便离线阅读或者分发 
  * 打包博客文章或者其他 Web 内容 
  * 使用常见的开放源代码工具创建、搜索和整理 

###  解剖 EPUB 包

一个 EPUB 就是一个简单 ZIP 格式文件（使用 .epub 扩展名），其中包括按照预先定义的方式排列的文件。

简单 EPUB 档案的目录和文件结构


    mimetype
    META-INF/
       container.xml
    OEBPS/
      content.opf
      title.html    (可忽略)
      content.html  (可忽略) 
      stylesheet.css
      toc.ncx 
      images/       (可忽略)
         cover.png

mimetype 文件

这个文件非常简单，必须命名为 mimetype，文件内容如下：


    application/epub+zip

要注意，mimetype 文件不能包含新行或者回车。  
此外，mimetype 文件必须作为 ZIP 档案中的第一个文件，而且自身不能压缩。首先创建该文件并保存，并确保它在 EPUB 项目的根目录中。

META-INF/container.xml

EPUB 根目录下必须包含 META-INF 目录，而且其中要有一个文件 container.xml。EPUB
阅读系统首先查看该文件，它指向数字图书元数据的位置。


OEBPS/content.opf

指定了图书中所有 内容的位置，如文本和图像等其他媒体。它还给出了另一个元数据文件，内容的 Navigation Center eXtended (NCX)
表。该 OPF 文件是 EPUB 规范中最复杂的元数据。


        Hello World: My First EPUB
        svoid
        urn:uuid:12345


内容的 NCX 表

NCX 定义了数字图书的目录表。复杂的图书中，目录表通常采用层次结构，包括嵌套的内容、章和节。


        Hello World: My First EPUB
      
      
        
          
            Book cover
          
          
        
        
          
            Contents


添加最后的内容

现在知道了 EPUB 需要的所有元数据，可以加入真正的图书内容了。可以使用下载的内容，也可以自己写，只要文件名和元数据匹配即可。然后创建下列文件和文件夹：  
title.html：图书的标题页。创建该文件并在其中包含引用封面图片的 img 元素，src 的属性值为 images/cover.png。  
images：在 OEBPS 下创建该文件夹，然后复制给定的示例图片（或者创建自己的图片）并命名为 cover.png。  
content.html：图书的实际文字内容。  
stylesheet.css：将该文件放在和 XHTML 文件相同的 OEBPS 目录中。该文件可以包含任意 CSS 声明，比如设置字体或者文字颜色。

###  Python生成epub的简单实例

```
# encoding:utf-8
#!/usr/bin/python3
import zipfile
import os.path

'''
Script Name     : createEpubBook.py
Author          : svoid
Created         : 2015-03-28
Last Modified   : 
Version         : 1.0
Modifications   : 
Description     : 根据HTML生成epub文档
'''


def create_mimetype(epub):
    epub.writestr('mimetype','application/epub+zip',compress_type=zipfile.ZIP_STORED)

def create_container(epub):
    container_info = '''

    '''
    epub.writestr('META-INF/container.xml',container_info, compress_type=zipfile.ZIP_STORED)

def create_content(epub,path):
    content_info = '''

        Hello World: My First EPUB
        Svoid
        urn:uuid:12345

          %(manifest)s

          %(spine)s
    '''
    manifest = ''
    spine = ''
    for html in os.listdir(path):
        basename = os.path.basename(html)
        if basename.endswith('html'):
            manifest += '' % (basename, basename) 
            spine += '' % (basename)
    epub.writestr('OEBPS/content.opf',content_info % {
                                'manifest': manifest,
                                'spine': spine,},
                                compress_type=zipfile.ZIP_STORED)

def create_stylesheet(epub):
    css_info = '''
        body {
          font-family: sans-serif;     
        }
        h1,h2,h3,h4 {
          font-family: serif;     
          color: red;
        }
    '''
    epub.writestr('OEBPS/stylesheet.css',css_info,compress_type=zipfile.ZIP_STORED)

def create_archive(path):
    epub_name = '%s.epub' % os.path.basename(path)
    os.chdir(path)
    epub = zipfile.ZipFile(epub_name, 'w')
    create_mimetype(epub)     
    create_container(epub)
    create_content(epub,path)
    create_stylesheet(epub)
    for html in os.listdir('.'):
        basename = os.path.basename(html)
        if basename.endswith('html'):
            epub.write(html, 'OEBPS/'+basename, compress_type=zipfile.ZIP_DEFLATED)
    epub.close()

if __name__ == '__main__':
    path = 'D:\\persion\\epub\\test1'
    create_archive(path)
```

参考文档：  
<http://www.ibm.com/developerworks/cn/xml/tutorials/x-epubtut/index.html>  
<http://www.manuel-strehl.de/dev/simple_epub_ebooks_with_python.en.html>
