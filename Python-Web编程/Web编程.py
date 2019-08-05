# Web编程基础

# Web基础
# 客户端通过网址发起请求，服务器收到请求后进行响应
# 服务器将网页代码发送给客户端，客户端再以网页方式展示给客户
# 这种结构被称为：B/S结构

# 网络传输中的一种非常重要的协议
# HTTP协议：HyperText Transfer Protocol 超文本传输协议
# HTTP协议也属于TCP/IP协议族中的一元
# HTTP协议属于四层结构中的应用层，直接与用户打交道

# 各种协议与HTTP协议的关系
# 客户端要向服务器发起请求，首先得知道服务器的IP地址，但是IP地址太难记了，
# 所以通过域名进行访问，DNS服务器则将域名进行转化，客户端拿到IP地址以后，
# 在应用层生成针对目标Web服务器的HTTP请求报文，由传输层将报文分割并编号，
# 进入网络层，根据IP协议通过一系列的中转找到最终的服务器地址，在服务器端，
# 将接收到的一段一段数据再拼接成完整的信息，再交给应用层HTTP协议，处理
# Web服务器的请求并且了解客户端请求的页面资源，然后整理，将资源整理再以同
# 样的方式传回客户端

# Web服务器
# 大致分为4个步骤
# 1、建立请求
# 2、请求过程
# 3、应答过程
# 4、关闭连接

# HTTP协议的常用方法
# 请求时常用到的方法
# GET方法：请求指定的页面信息，并返回实体主体
# POST方法：向指定资源提交数据进行处理请求(例如提交表单或者上传文件)，数据
#     被包含再请求体中，POST请求可能导致新的资源的建立和/或已有资源的修改
# HEAD方法：类似于GET请求，只不过返回的响应中没有具体的内容，用于获取报头
# PUT方法：从客户端向服务器传送的数据取代指定的文档的内容
# DELETE方法：请求服务器删除指定的页面
# OPTIONS方法：允许客户端查看服务器的性能

# 服务器给客户端发送响应的时候会传递一个代码串
# 1**  信息，请求收到，继续处理
# 2**  成功，行为被成功地接受、理解和采纳
# 3**  重定向，为了完成请求，必须进一步执行的动作
# 4**  客户端错误，请求包含语法错误或者请求无法实现
# 5**  服务器错误，服务器不能实现一种明显无效的请求

# 前端基础
# 前端 FRONT END：它是与用户直接交互的部分，包括Web页面的结构，
#                 Web的外观视觉和表现以及Web层的交互实现
# 后端 BACK END：更多的与数据库进行交互，处理相应的业务逻辑，如何实现功能、
#               数据的存取、平台的稳定性和性能等等

# 后端语言主要包括C++、JAVA、Python、PHP、ASP、.NET......

# 前端简介
# HTML简介
# 全称：Hyper Text Markup Language  超文本标记语言
# 超文本的意思为不只是文本，还可以是图片、动画、视频等等
# HTML不是一门语言，它是一种标记标签，通常称为HTML标签
# 实例：创建一个HTML文件
<!DOCTYPE html>
<html>
<head>
	<title>这是一个HTML文件</title>
</head>
<body>
	<h1>蝶恋花</h1>
	<p>
	<br>&nbsp;&nbsp;&nbsp;&nbsp;
	槛菊愁烟兰泣露，罗幕轻寒，燕子双飞去。

        <br>&nbsp;&nbsp;&nbsp;&nbsp;
        明月不谙离恨苦，斜光到晓穿朱户。

        <br>&nbsp;&nbsp;&nbsp;&nbsp;
        昨夜西风凋碧树，独上高楼，望尽天涯路。

        <br>&nbsp;&nbsp;&nbsp;&nbsp;
        欲寄彩笺兼尺素，山长水阔知何处！
	</p>
</body>
</html>

# 通过浏览器打开这个文件，会发现这个网页颜值很低且简单
# 这时就需要通过CSS来美化这个页面
# CSS简介
# 全称：Cascading Style Sheets  层叠样式表
# 它也是一种标记语言，它用于为HTML文档定义布局，例如CSS涉及的字体、颜色等等
# 实例：使用CSS来美化前面的页面
<!DOCTYPE html>
<html>
<head>
	<title>这是一个HTML文件</title>
	<style type="text/css">
		main{
			height:150px;background: #309bd1
		}
		title{
			color: white;text-align: center;
		}
		content{
			margin:10px;
		}
	</style>
</head>
<body>
	<div class="main">
	<h1 class="title">蝶恋花</h1>
	    <p class="content">
	    <br>&nbsp;&nbsp;&nbsp;&nbsp;
	    槛菊愁烟兰泣露，罗幕轻寒，燕子双飞去。

            <br>&nbsp;&nbsp;&nbsp;&nbsp;
            明月不谙离恨苦，斜光到晓穿朱户。

            <br>&nbsp;&nbsp;&nbsp;&nbsp;
            昨夜西风凋碧树，独上高楼，望尽天涯路。

            <br>&nbsp;&nbsp;&nbsp;&nbsp;
            欲寄彩笺兼尺素，山长水阔知何处！
	    </p>
    </div>
	<div style="height:150px;background: #309bb1">
	<h2 style="color:white;text-align: center;">蝶恋花</h2>
	    <p style="margin:10px">
    	    <br>&nbsp;&nbsp;&nbsp;&nbsp;
	    槛菊愁烟兰泣露，罗幕轻寒，燕子双飞去。

            <br>&nbsp;&nbsp;&nbsp;&nbsp;
            明月不谙离恨苦，斜光到晓穿朱户。

            <br>&nbsp;&nbsp;&nbsp;&nbsp;
            昨夜西风凋碧树，独上高楼，望尽天涯路。

            <br>&nbsp;&nbsp;&nbsp;&nbsp;
            欲寄彩笺兼尺素，山长水阔知何处！
	    </p>
    </div>
</body>
</html>

# 引入外部文件方式
# style.css文件
main{
			height:150px;background: #309bd1
		}
		title{
			color: white;text-align: center;
		}
		content{
			margin:10px;
		}
# index.html文件
<!DOCTYPE html>
<html>
<head>
	<title>这是一个HTML文件</title>
	<link rel="stylesheet" type="text/css" href="./style.css">
</head>
<body>
	
	<div class="main">
	<h1 class="title">蝶恋花</h1>
	    <p class="content">
	    <br>&nbsp;&nbsp;&nbsp;&nbsp;
	    槛菊愁烟兰泣露，罗幕轻寒，燕子双飞去。

            <br>&nbsp;&nbsp;&nbsp;&nbsp;
            明月不谙离恨苦，斜光到晓穿朱户。

            <br>&nbsp;&nbsp;&nbsp;&nbsp;
            昨夜西风凋碧树，独上高楼，望尽天涯路。

            <br>&nbsp;&nbsp;&nbsp;&nbsp;
            欲寄彩笺兼尺素，山长水阔知何处！
	    </p>
</body>
</html>
# 以上以三种形式来引入了css文件
# 其中,标签内引入优先级最高,在head标签内使用style引入中,Web引入优先级最低

# 对于一个非前端人员来说，设计前端样式是头疼的
# Python + Bootstrap框架应该会是一种不错的选择
# 实例：使用Bootstrap实现一个页面
<!DOCTYPE html>
<html>
<head>
	<title>使用Bootstrap</title>
	<!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet"
href=
"https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
integrity=
"sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
crossorigin="anonymous">
</head>
<body>
	<div style="margin:20px">
	<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed"
      data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"
      aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">Brand</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id=
    "bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">Link
        <span class="sr-only">(current)</span></a></li>
        <li><a href="#">Link</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle"
          data-toggle="dropdown" role="button" aria-haspopup="true"
          aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">One more separated link</a></li>
          </ul>
        </li>
      </ul>
      <form class="navbar-form navbar-left">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search">
        </div>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">Link</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown"
          role="button" aria-haspopup="true" aria-expanded="false">Dropdown
          <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
<div class="jumbotron">
  <h1>Hello, world!</h1>
  <p>...</p>
  <p><a class="btn btn-primary btn-lg" href="#" role="button">
  Learn more</a></p>
</div>
<form>
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1"
    placeholder="Email">
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1"
    placeholder="Password">
  </div>
  <div class="form-group">
    <label for="exampleInputFile">File input</label>
    <input type="file" id="exampleInputFile">
    <p class="help-block">Example block-level help text here.</p>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox"> Check me out
    </label>
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
</form>
</div>
</body>
</html>
# 以上代码全部来自于Bootstrap官方文档

# JavaScript简介
# JavaScript != Java 无任何关系
# 它是一种脚本语言，不需要编译就可以在网页中运行
# 它可以实现网页特性，还可以响应用户请求，实现一些动态交互的功能
# 编写一段代码来实现动态效果
# 为按钮实现点击弹出时间
# 在上面的代码最后加上以下代码试一试
  <button id = "button" type="button" class="btn btn-success">
  (成功)Success</button>
</form>
</div>
<script type="text/javascript">
	document.getElementById("button").onclick=function(){
		alert("您点击了提交按钮");
	}
</script>
</body>
</html>

# 制作一个静态服务器
# 实现过程看下面截图

# CGI简介
# 前面实现了静态页面，而现在都是动态页面，CGI应运而生
# 全称：Common Gateway Interface  通用网关接口
# 它是一种运行在服务器端的程序
# 因为CGI在用户多的时候会开启多个进程，很容易使得系统崩溃
# 所以CGI的升级版FastCGI诞生
# 全称：Fast Common Gateway Interface
# 它使用进程线程池来处理一系列的请求
# 而且这些进程由Fast服务器自己管理，而不是由Web服务器管理，所以可以同时处理更多的请求
# FastCGI虽然解决了服务器同时处理多个页面的请求，但它也由缺陷
# 就是在编写一部程序的时候不方便
# 所以，WSGI就出现了
# Web Server Gateway Interface  Web服务器网关接口
# 它是Web服务器、Web应用程序或者框架之间的简单的通用接口
# 工作原理见下图

# 定义WSGI接口
# 语法：def application(environ,start_response):
#          start_response('200 OK',[('Content-Type','text/html')])
#          return[b'<h1>Hello,World!</h1>']
# 参数详解：environ 一个包含所有HTTP请求信息的字典对象
# start_response 一个发送HTTP响应的函数
# wsgiref模块是Python内置的WSGI服务器
# 实例：通过WSGI实现简单的Hello,World
from wsgiref.simple_server import make_server

def sayHi(environ,start_response):
    start_response('200 ok',[('Content-Type','text/html;charset=utf-8'),
                             ('Date','Thu,21 Jun 2019 20:05:10 GMT')])
    return [b'Hello World']

if __name__ == '__main__':
    ser = make_server('127.0.0.1',8000,sayHi)
    ser.serve_forever()

# 运行WSGI服务

# Web框架
# 为什么要使用Web框架？简化工作
# 什么是Web框架：实现一些基础功能的一堆代码，它就是通用的半成品
# 框架提供的常用功能：
# 管理路由
# 访问数据库
# 管理会话和Cookies
# 创建模板来显示HTML
# 促进代码的重用
# 如果Web框架不符合心意，可以自己编写框架，只要符合WSGI接口就OK
# Python中常用的Web框架
# Python中的Web框架有很多，因为只要符合WSGI接口每个人都可以编写Web框架
# 这也会带来麻烦，因为会使许多不懂Web框架开发的人员选择麻烦症
# 下面就是当前的主流的Web框架
# 1.Flask框架:它是一个轻量级的Web框架,基于Werkzeug实现的WSGI和Jinja2模板引擎
#             Flask的设计哲学是只保留核心，其它的通过扩展机制来增强它的功能
#             所以它的扩展机制非常丰富，几乎在Web开发的每一个环节都有其扩展
#             供我们选择，即便没有，开发者也可以轻松的实现一个   小而美
# 2.django框架:它提供了非常齐全的参照文档以及一站式的解决方案，包括缓存、RAM管
#              理后台、验证、表单处理等等，由于它具备这些功能，所以它使数据库
#              驱动的网站变得更加简单，但是也有弊端，代码耦合性更高了，不易替换
# 3.Bottle框架:它也是一个轻量级的Web框架，它只有一个文件，代码只使用了Python的
#              标准库，自带路由映射、模板、简单的数据库访问等Web框架组件，而不
#              需要额外其它第三方库，所以它才是真正的微框架 语法简单 部署方便
# 4.Tronado框架:现在是Facebook开源后的版本，因为它是非阻塞的服务器，所以它的速
#               度非常快，每秒钟可以处理数以千记的连接
# 在选择框架的时候需要依据自己的项目，如果项目比较小，就可以选择Flask、Bottle
# 如果项目需要一个通用的后台，可以使用django，因为它提供了一站式的解决方案，就
# 包括了管理后台

# Flask框架
# Flask依赖于两个库Werkzeug(WSGI toolkit WSGI工作集)和Jinja2(负责渲染模板)
# 在使用之前需要安装virtualenv、创建虚拟环境、激活虚拟环境
# 虚拟环境可以为每一个项目提供一个Python安装

# 安装虚拟环境：在命令行键入命令 pip install virtualenv
# 创建虚拟环境：从命令行进入工作目录 再创建目录mkdir Flask
# 使用命令virtualenv venv(虚拟环境名称) 
# 启动虚拟环境：从命令行键入activate 即在刚才目录下键入 venv\Scripts\activate
# 激活成功后会在命令行最前面显示 (venv)

# 安装Flask
# cmd命令行进入刚刚那个虚拟环境，键入命令：pip install Flask即可
# 安装完成后可利用pip list 查看是否安装成功
# 键入此命令后会在命令行显示已经安装好的包的包名和版本号
# 第一个Flask程序：输出Hello World
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World! 你好'

if __name__ == '__main__':
    app.run(debug=True)
# 在网页中输入：127.0.0.1:5000/可以看到return 语句返回的值

# 开启调试模式
# 第一种方式，就是上面的run()方法
# app.run(debug=True)这里就开启了调试模式，修改代码会自动在网页生成，不用重新运行
# 第二种方式
# 在app.run()上面加上一句：app.debug=True

# 路由
# 什么是路由？先看下面示例
from flask import Flask
app = Flask(__name__)

@app.route('/')    # 路由1
def hello():
    return 'Hello World! 你好'
@app.route('/index')    # 路由2
def index():
    return 'This is Index!'

if __name__ == '__main__':
    app.run(debug=True)
# 在运行这段程序后，在网址中输入127.0.0.1:5000/就会进入路由1，网页显示Hello World
# 在网址中输入127.0.0.1:5000/index就会进入路由2，网页显示This is Index!
# 大概能理解了，路由就是来标识某一IP和端口号对应的网页

# 变量规则
# <converter(变量名称):variable_name(变量名称)>
# 实例：根据参数输出相应信息
from flask import Flask
app = Flask(__name__)
@app.route('/user/<username>')    # 非限定类型
def show_user_profile(username):
    return "user:%s" % username
@app.route('/post/<int:postid>')    # 限定类型
def show_post(postid):
    return 'Post:%d' % postid

if __name__ == '__main__':
    app.run(debug=True)
# 构造URL
# 语法：url_for(endpoint(终点),**values(变量))
# 实例：获取URL信息
from flask import Flask,url_for
app = Flask(__name__)
@app.route('/post/<int:postid>')    # 限定类型
def show_post(postid):
    return 'Post:%d' % postid
@app.routr('/url/')
def get_url():
    return url_for('show_post',postid=2)

if __name__ == '__main__':
    app.run(debug=True)
# 结果为在网页上显示/post/postid=2，获取了上面路由的相关信息

# HTTP方法
# GET  浏览器告知服务器：只获取页面上的信息并发给我，这是最常用的方法
# HEAD  浏览器告诉服务器：欲获取信息，但是只关心消息头。应用应像处理GET请求一样来处理
# 它，但是不分发实际内容。在Falsk中完全不需人工干预，底层Werkzeug库已替我们处理好了
# POST  浏览器告诉服务器：想在URL上发布新消息，并且服务器必须确保数据已存储且存储一次
# 这是HTML表单通常发送数据到服务器的方法
# PUT  类似POST但是服务器可能触发了存储过程多次
# DELETE  删除给定位置的信息
# OPTIONS  给客户提供一个敏捷的途径弄清楚这个URL支持哪些HTTP方法
# 更多详解见下方截图部分

# 请求默认为GET请求
from flask import Flask,url_for
import request
app = Flask(__name__)
@app.routr('/login')
def login():
    if request.method == 'GET':
        return '这是GET方法'
if __name__ == '__main__':
    app.run(debug=True)
# 由上面程序运行结果可得默认请求
# 设置请求方式
from flask import Flask,url_for,request
app = Flask(__name__)
@app.routr('/login',methods=['POST','GET','PUT'])
def login():
    if request.method == 'GET':
        return '这是GET方法'
    elif request.method == 'POST':
        return '这是POST请求'
if __name__ == '__main__':
    app.run(debug=True)

# 静态文件
# 例如CSS、JS文件都是静态文件
# 为了同一管理，我们可以将这些文件放在同一个文件夹下，这就是一个静态文件
# 创建静态文件并在代码中获取这个文件
@app.routr('/login',methods=['POST','GET','PUT'])
def login():
    if request.method == 'GET':
        return '这是GET方法'
    elif request.method == 'POST':
        return '这是POST请求'

# 蓝图(蓝本)
# 什么是蓝图？是一种组织一组相关视图及其它代码的方式
# 为什么要使用蓝图？。蓝图可以重构项目的目录结构，如下图，是为了解决项目代码增加时的冗杂
# 使用蓝图的目的：分而治之
# 使用蓝图
# 创建蓝图 bp = Blueprint('admin'(蓝图名称),__name__,url_prefix='/admin')
# 注册蓝图 app.register_blueprint(bp)

# 模板：一个包含响应文本的文件
# 渲染模板：Jinja2
# 实例：
# Test.py文件
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def HTMLtest():
    return render_template('HTMLtest.html')
@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('user.html',name=username)

if __name__ == '__main__':
    app.run(debug=True)
# HTMLtest.html文件
<!DOCTYPE html>
<html>
<head>
	<title>使用Bootstrap</title>
	<!-- 最新版本的 Bootstrap 核心 CSS 文件 -->
<link rel="stylesheet" href=
"https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css"
integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u"
crossorigin="anonymous">
</head>
<body>
	<div style="margin:20px">
	<nav class="navbar navbar-default">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed"
      data-toggle="collapse" data-target="#bs-example-navbar-collapse-1"
      aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="#">Brand</a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
      <ul class="nav navbar-nav">
        <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
        <li><a href="#">Link</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
          aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">One more separated link</a></li>
          </ul>
        </li>
      </ul>
      <form class="navbar-form navbar-left">
        <div class="form-group">
          <input type="text" class="form-control" placeholder="Search">
        </div>
        <button type="submit" class="btn btn-default">Submit</button>
      </form>
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#">Link</a></li>
        <li class="dropdown">
          <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button"
          aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
          <ul class="dropdown-menu">
            <li><a href="#">Action</a></li>
            <li><a href="#">Another action</a></li>
            <li><a href="#">Something else here</a></li>
            <li role="separator" class="divider"></li>
            <li><a href="#">Separated link</a></li>
          </ul>
        </li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
<div class="jumbotron">
  <h1>Hello, world!</h1>
  <p>...</p>
  <p><a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a></p>
</div>
<form>
  <div class="form-group">
    <label for="exampleInputEmail1">Email address</label>
    <input type="email" class="form-control" id="exampleInputEmail1" placeholder="Email">
  </div>
  <div class="form-group">
    <label for="exampleInputPassword1">Password</label>
    <input type="password" class="form-control" id="exampleInputPassword1" placeholder="Password">
  </div>
  <div class="form-group">
    <label for="exampleInputFile">File input</label>
    <input type="file" id="exampleInputFile">
    <p class="help-block">Example block-level help text here.</p>
  </div>
  <div class="checkbox">
    <label>
      <input type="checkbox"> Check me out
    </label>
  </div>
  <button type="submit" class="btn btn-default">Submit</button>
  <button id = "button" type="button" class="btn btn-success">
  (成功)Success</button>
</form>
</div>
<script type="text/javascript">
	document.getElementById("button").onclick=function(){
		alert("您点击了提交按钮");
	}
</script>
</body>
</html>
# user.html文件
<!DOCTYPE html>
<html lang="en">
<head>
     <meta charset="utf-8">
     <tutle>Title</title>
</head>
<body>
    {{name}}
</body>
</html>

# 在Flask中使用Web表单
# 表单是允许用户与Web交互的基本元素
# CSRF保护和验证
# 全称：跨站请求伪造：通过第三方伪造表单数据以POST方式提交到应用服务器
# Python中Flask-WTF模块可以解决这一问题，使用它会生成令牌，并进行验证
# 令牌会在30分钟后会失效
# 安装Flask-WTF：在命令行键入：pip install flask-wtf
# 注意：需要将它安装到虚拟环境中
# 安装完成后检查：pip list
# Flask-WTF的配置
# app=Flask(__name__)
# app.config['SECRET_KEY']='Navigator97'
# 应用：
from flask import Flask,url_for
import request
app=Flask(__name__)
app.config['SECRET_KEY']='Navigator97'
app = Flask(__name__)
@app.routr('/login')
def login():
    if request.method == 'GET':
        return '这是GET方法'
if __name__ == '__main__':
    app.run(debug=True)
# 由上面程序运行结果可得默认请求
# 设置请求方式
from flask import Flask,url_for,request
app = Flask(__name__)
@app.routr('/login',methods=['POST','GET','PUT'])
def login():
    if request.method == 'GET':
        return '这是GET方法'
    elif request.method == 'POST':
        return '这是POST请求'
if __name__ == '__main__':
    app.run(debug=True)

# 表单类
# 在没有用表单类的时候，我们是这样创建表单的
from flask import Flask,url_for,request
app = Flask(__name__)
@app.routr('/login',methods=['POST','GET','PUT'])
def login():
    if request.method == 'GET':
        return '这是GET方法'
    elif request.method == 'POST':
        return '这是POST请求'
if __name__ == '__main__':
    app.run(debug=True)
# 然后需要创建html文档
<!DOCTYPE html>
<html lang="en">
<head>
     <meta charset="UTF-8">
     <tutle>Title</title>
</head>
<body>
    <form action="" method="post">
    <div>
        <label for="username">用户名</lable>
        <input type="text" required>    # required表示必须填写
    </div>
    <div>
        <label for="password">密码</lable>
        <input type="password" required>
    </div>
    <button type="submit">提交</button>
    </form>    
</body>
</html>

# 使用Flask-WTF实现表单验证
from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length    # 验证规则

class LoginForm(FlaskForm):
    name = StringField(label='用户名',validators=[DataRequired('用户名不能为空',
                                                            Length(min=4,max=16))])
    password = PasswordField(label='密码',validators=[DataRequired('密码不能为空')])
    submit = SubmitField(label='提交')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Navigator97'

@app.route('/')
def HTMLtest():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('HTMLtest.html')
@app.route('/user/<username>')
def show_user_profile(username):
    return render_template('user.html',name=username)

if __name__ == '__main__':
    app.run(debug=True)

# 实例：实现登录验证功能
# manage.py文件
from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired    # 验证规则

class LoginForm(FlaskForm):
    name = StringField(label='用户名',validators=[DataRequired('用户名不能为空')])
    password = PasswordField(label='密码',validators=[DataRequired('密码不能为空')])
    submit = SubmitField(label='提交')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Navigator97'

@app.route('/')
def HTMLtest():
    form = LoginForm()
    data={}
    if form.validate_on_submit():
        data['name'] = form.name.data
        data['password'] = form.password.data
    return render_template('index.html',form=form,data=data)

if __name__ == '__main__':
    app.run(debug=True)
# index.html文件
<!DOCTYPE html>
<html lang="en">
<head>
     <meta charset="UTF-8">
     <tutle>Title</title>
</head>
<body>
    <form action="" method="post">
    <div>
        {{ form.name.lable }}
        {{ form.name }}
    </div>
    {% for err in form.name.errors %}    # 找出并显示所有的错误信息
    <p style="color:red">
        {{ err }}
     {% endfor %}
    <div>
        {{ form.password.lable }}
        {{ form.paaword }}
    </div>
    {% for err in form.password.errors %}    # 找出并显示所有的错误信息
    <p style="color:red">
        {{ err }}
    {% endfor %}
    {{ form.csrf_token }}
    {{ form.submit }}
    </form>
{% if data % }
    您输入的用户名： {{ data['name'] }}
    您输入的密码： {{ data['password'] }}
{% endif %}
</body>
</html>
