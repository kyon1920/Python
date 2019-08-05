# 初识网络爬虫
# 内容：什么是爬虫？  网络爬虫的常用技巧、爬虫的常用框架、实战项目：快手爬票

# 什么是爬虫？
# 它并不是一只爬动的虫子，网络爬虫又被称为网络蜘蛛、网络机器人，他可以指定的规则(程序的算法)自动浏览网络并且获取网络中的信息
# 不仅仅只有Python可以编写网络爬虫，其实C/C++、JAVA、PHP都可以编写网络爬虫程序，但是Python编写的网络爬虫是最受开发人员喜爱的
# 利用Python编写网络爬虫程序的优点：快速开发、跨平台、解释性、多种网络爬虫框架

# 爬取百度首页代码示例
import urllib.request    # 导入网络请求模块
response = urllib.request.urlopen(r'http://www.baidu.com/')    # 实现网络请求
print(response.read().decode('utf-8'))

# 网络爬虫的常用技术
# 网络请求：确定我们要爬取的网络地址，对这个网络地址进行网络请求
# 最常用三个网络请求模块：Urllib(原生模块)、Urllib3、Requests
# Urllib模块：提供了多个子模块：常用的有request(定义了打开URL的方法和类)、error(主要包含异常类)、parse(用于URL的解析和引用)、robotparser(解析robors.txt文件)
# 什么是robots.txt文件？爬虫时访问的网站根目录中的文件，该文件会设置爬虫规则，告诉我们那个信息可以爬取，那些不能爬取，如无表示所有都能爬取
# 实现网络请求
import urllib.request
import urllib.parse    # 导入解析模块
# 创建参数
data = bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf-8')
# 发送post网络请求
response = urllib.request.urlopen("http://httpbin.org/post",data=data)
html = response.read()
print(html)

# 标准库的升级版：Urllib3
# 新增功能：如 线程安全、连接池、使用大部分编码上传文件、100%的测试覆盖率......
# 官网地址：https://urllib3.readthedocs.io/en/latest/
# 安装Urllib3：在命令行下输入 pip install urllib3
import urllib3    # 导入标准库升级模块
# 创建PoolManager对象，用于处理与线程的连接以及线程安全
http = urllib3.PoolManager()
# 发送网络请求
# response = http.request('GET','http://www.baidu.com')
response = http.request('POST','http://httpbin.org/post',fields={'word':'hello'})
print(response.data.decode())    # 打印请求信息

# 非标准模块：Requests模块
# 优点：比标准模块简单一些，操作更加人性化
# 功能特征：自动内容解码、分块请求、连接超时、自动解压、文件分块上传......
# 官方文档：http://www.python-requests.org/en/master/
# 安装：在命令行输入 pip install requests
# get()方法使用示例
import requests    # 导入网络请求模块
response = requests.get('http://www.baidu.com/')    # 发送网络请求
print('状态码：',response.status_code)    # 打印状态码
print('请求地址：',response.url)    # 打印请求地址
print('头部信息：',response.headers)    # 打印头部信息
print('cookie信息：',response.cookies)    # 打印cookies信息
print('文本源码：',response.text)    # 打印源码，以文本形式输出
print('字节流源码：',response.content)    # 打印字节流源码
# post()方法示例
import requests    # 导入网络请求模块
data = {'word':'hello'}    # 表单参数
response = requests.post('http://httpbin.org/post',data = data)    # 发送网络请求
print('状态码：',response.status_code)    # 打印状态码
print('字节流源码：',response.content)    # 打印字节流源码

# 请求headers处理：也就是头部处理
# 当进行网络请求的时候，会产生403错误信息，这个时候就需要进行headers处理了
# 错误原因是为了防止恶意采集数据，所以网页设置了反爬虫操作
# 请求头部的参数信息：
# Accept:text/html,application/xhtml+xm...plication/xml;q=0.9*/*;q=0.8  浏览器可接受的MME类型
# Accept-Encoding:gzip,deflate,br  浏览器能进行解码的编码方式
# Accept-Language:zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2  浏览器的语言种类
# Cache-Control:max-age=0  控制网页缓存
# Connection:keep-alive  是否可以持久得处理网络链接
# Cookie:BAIDUID=C3A70711039E0946211C95..._26350_20927;BD_UPN=13314352  将cookies返回到服务器
# Host:www.baidu.com  初始化URL中的主机和端口
# Upgrade-Insecure-Requests:1  通知服务器可以处理https协议
# User-Agent:Mozilla/5.0(Windows NT 6.1;W...)Gecko/20100101 Firefox/60.0  用于识别浏览器的类型
import requests
url = r'http://www.whatismyip.com/'    # 网络请求地址
response = requests.get(url)    # 发送网络请求
print(response.content.decode('utf-8'))
# 以上代码会出现403错误，并不能得到我们想要的数据
# 经过headers处理后：headers 在我们需要爬取的网页中，按F12找到Network选项，然后找到下面变量对应的值
import requests
url = r'http://www.whatismyip.com/'    # 网络请求地址
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}
response = requests.get(url,headers = headers)    # 发送网络请求
print(response.content.decode('utf-8'))

# 网络超时处理
# 出现情况：网络断开、网络不稳定、网络堵塞、网速过慢
# 爬虫超时示例
import requests
# 导入网络请求模块中的三个异常类
from requests.exceptions import ReadTimeout,HTTPError,RequestException
# 循环发送50次网络请求
for a in range(0,50):
	try:
	    response = requests.get('http://www.baidu.com/',timeout = 0.05)
	    print(response.status_code)    # 打印请求码
	except ReadTimeout:    # except Exception as e:
		# print("异常："+str(e))    # 打印异常
		print('timeout')
	except HTTPError:
		print('HTTPError')
	except RequestException:
		print('reqerror')

# 代理服务：使用代理IP
# 在爬取网页的过程中，会发现，不久前还可以爬取的网页，现在却爬不到了，有的会出现验证码的现象，这是因为计算机的IP被爬取的网站发现了
# 设置了代理IP后，网页就不再会发现你的IP，而不会出现上面的情况
# 可以使用代理IP的网站：www.xicidaili.com
import requests
# 设置代理IP
proxy = {'http':'106.75.8.141:808',
         'https':'113.124.85.154:9999'}    # 有可能失效，自行到上面网站进行更换，数据依次是'代理类型':'IP地址:端口'
response = requests.get('http://www.baidu.com/',proxies = proxy)
print(response.content.decode('utf-8'))

# 最后解析HTML，找到我们需要爬取的数据
# 在Python中可以解析HTML代码的模块有很多
# 常见模块：LXML模块(速度快、需要安装C语言库)、Requests-HTML模块(第三方)、HtmlParser模块(标准库模块，执行速度适中，但容错能力弱)
# 续：BeautifulSoup模块(比较强大，不仅支持Python标准库解析器，还支持第三方解析器，包含MXML解析器)
# 以BeautifulSoup来进行安装的三种方法
# 在Linux安装：apt-get install Python-bs4
# 在Windows安装：easy_install beautifulsoup4 或者 pip install beautifulsoup4
# 如果下载不是我们需要的版本：则通过访问https://www.crummy.com/software/BeautifulSoup4/bs4/download/下载想要的版本，然后通过命令 Python setup.py install进行安装
# 官方文档：https://www.crummy.com/software/BeautifulSoup/bs4/doc/index_zh.html
# 解析HTML示例：解析代码中的HTML代码、解析BaiduNews的HTML代码、解析本地代码
from bs4 import BeautifulSoup
html_doc = '''
<html><head><title>The Dormouse's story</title><head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link">Elsie</a>,
<a href="http://example.com/elsie" class="sister" id="link">Lacie</a> and
<a href="http://example.com/elsie" class="sister" id="link">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="stroy">...</p>
'''
soup = BeautifulSoup(html_doc,features='lxml')
print(soup)
print('HRML代码的title：',soup.title)
print('HRML代码的<body>部分：',soup.body)

# 获取百度的标题
import requests
response = requests.get('http://news.baidu.com/')
soup1 = BeautifulSoup(response.text,features='lxml')
print(soup1)
print('Baidu的title：',soup1.find('title').text)
print('Baidu代码的<body>部分：',soup1.body)

# 打印本地html文件代码
soup2 = BeautifulSoup(open(r'C:\桌面\html.html'),features='lxml')
print(soup2.prettify())

# 网络爬虫的常用框架
# Scrapy：急速而强大、易于扩展、便携式、可移植性强  官方网站：https://scrapy.org/
# Crawley Project：  官方网站：http://project.crawley-cloud.com/
# pyspider：分布式架构、支持多种数据库后端、强大的WebUI支持脚本编辑器，任务监视器，项目管理器以及结果查看器
# pyspider的官方网站：https://github.com/binux/pyspider/releases  开发文档：http://docs.pyspider.org/

# 实战：快手爬票
# 概述以及运行结果
# 通过12306官方网址获取车次及票况，需要我们进行输入的有出发点、目的地和日期，然后得到当天所有相关车次及有无票情况

# 搭建QT环境
# QT官方地址：https://www.qt.io/download
# 打开官方网站 或者 download.qt.io/archive/qt→建议下载5.6版本(在win10兼容性较好)、win7都行→下载
# 验证安装是否成功代码
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()

    sys.exit(app.exec_())

# 实现主窗体设计
# 主窗体、顶部图片、查询区域、选择车次类型、信息分类图片、信息表格区域
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PaPiao.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import  QPalette,QPixmap,QColor    # 导入QtGui模块

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 786)
        MainWindow.setMinimumSize(QtCore.QSize(960, 786))
        MainWindow.setMaximumSize(QtCore.QSize(960, 786))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label0 = QtWidgets.QLabel(self.centralwidget)
        self.label0.setGeometry(QtCore.QRect(0, 0, 960, 141))
        self.label0.setText("")
        self.label0.setObjectName("label0")

        label0_img = QPixmap('train.png')    # 导入顶部位图
        self.label0.setPixmap(label0_img)    # 设置调色版

        self.frame0 = QtWidgets.QFrame(self.centralwidget)
        self.frame0.setGeometry(QtCore.QRect(0, 140, 960, 80))
        self.frame0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame0.setObjectName("frame0")

        self.frame0.setAutoFillBackground(True)    # 开启自动填充背景
        palette0 = QPalette()    # 调色板类
        palette0.setBrush(QPalette.Background,QtGui.QBrush(QtGui.QPixmap('bj.jpg')))    # 设置背景图片 
        self.frame0.setPalette(palette0)    # 设置调色板

        self.chufadi0 = QtWidgets.QLabel(self.frame0)
        self.chufadi0.setGeometry(QtCore.QRect(30, 25, 54, 20))
        self.chufadi0.setObjectName("chufadi0")
        self.chufadi1 = QtWidgets.QTextEdit(self.frame0)
        self.chufadi1.setGeometry(QtCore.QRect(90, 20, 104, 31))
        self.chufadi1.setObjectName("chufadi1")
        self.label_2 = QtWidgets.QLabel(self.frame0)
        self.label_2.setGeometry(QtCore.QRect(265, 250, 72, 15))
        self.label_2.setObjectName("label_2")
        self.chufari0 = QtWidgets.QLabel(self.frame0)
        self.chufari0.setGeometry(QtCore.QRect(440, 25, 54, 20))
        self.chufari0.setObjectName("chufari0")
        self.chaxun = QtWidgets.QPushButton(self.frame0)
        self.chaxun.setGeometry(QtCore.QRect(680, 20, 93, 28))
        self.chaxun.setObjectName("chaxun")
        self.mudidi1 = QtWidgets.QTextEdit(self.frame0)
        self.mudidi1.setGeometry(QtCore.QRect(300, 20, 104, 31))
        self.mudidi1.setObjectName("mudidi1")
        self.mididi0 = QtWidgets.QLabel(self.frame0)
        self.mididi0.setGeometry(QtCore.QRect(240, 25, 54, 20))
        self.mididi0.setObjectName("mididi0")
        self.chufari1 = QtWidgets.QTextEdit(self.frame0)
        self.chufari1.setGeometry(QtCore.QRect(500, 20, 104, 31))
        self.chufari1.setObjectName("chufari1")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(0, 220, 960, 40))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.checkBox0 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox0.setGeometry(QtCore.QRect(110, 10, 91, 19))
        self.checkBox0.setObjectName("checkBox0")
        self.checileixing = QtWidgets.QLabel(self.frame1)
        self.checileixing.setGeometry(QtCore.QRect(30, 13, 72, 15))
        self.checileixing.setObjectName("checileixing")
        self.checkBox1 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox1.setGeometry(QtCore.QRect(260, 10, 91, 19))
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox2 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox2.setGeometry(QtCore.QRect(400, 10, 91, 19))
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox3 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox3.setGeometry(QtCore.QRect(550, 10, 91, 19))
        self.checkBox3.setObjectName("checkBox3")
        self.checkBox4 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox4.setGeometry(QtCore.QRect(690, 10, 91, 19))
        self.checkBox4.setObjectName("checkBox4")
        
        self.frame1.setAutoFillBackground(True)    # 开启自动填充背景
        palette1 = QPalette()    # 调色板类
        palette1.setBrush(QPalette.Background,QtGui.QBrush(QtGui.QPixmap('bj.jpg')))    # 设置背景图片 
        self.frame1.setPalette(palette1)    # 设置调色板

        self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(0, 330, 960, 455))
        self.text.setObjectName("text")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(0, 260, 960, 70))
        self.label1.setText("")
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        label1_img = QPixmap('train.png')    # 导入顶部位图
        self.label1.setPixmap(label0_img)    # 设置调色版

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "快手爬票"))
        self.chufadi0.setText(_translate("MainWindow", "出发地:"))
        self.label_2.setText(_translate("MainWindow", "目的地:"))
        self.chufari0.setText(_translate("MainWindow", "出发日:"))
        self.chaxun.setText(_translate("MainWindow", "查询"))
        self.mididi0.setText(_translate("MainWindow", "目的地:"))
        self.checkBox0.setText(_translate("MainWindow", "GC-高铁"))
        self.checileixing.setText(_translate("MainWindow", "车次类型:"))
        self.checkBox1.setText(_translate("MainWindow", "D-动车"))
        self.checkBox2.setText(_translate("MainWindow", "Z-直达"))
        self.checkBox3.setText(_translate("MainWindow", "T-特快"))
        self.checkBox4.setText(_translate("MainWindow", "K-快速"))

def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)    # 实例化Qapplication类，作为GUI主程序的入口
    MainWindow = QtWidgets.QMainWindow()    # 创建QMainWindow
    ui = Ui_MainWindow()    # 实例UI类
    ui.setupUi(MainWindow)    # 设置窗体UI
    MainWindow.show()    # 显示窗体
    sys.exit(app.exec_())    # 当窗口创建完成以后，需要结束主循环

if __name__ == '__main__':
    show_MainWindow()

# 分析请求参数
# 需要借助浏览器自带的网络监视器
# 以12306铁路售票官网为例，打开网络监视器会有4个参数，含义分别如下：
# leftTicketDTO.from_station:BJP    出发地：北京
# leftTicketDTO.to_station:SHH    目的地：上海
# leftTicketDTO.train_data:2019-07-24    出发日期
# purpose_codes:ADULT    成人票信息
# 在网络监视器中会发现这一些列的规律

# 下载站名文件
# 该文件可以获取城市所对应的英文缩写
# 站名文件地址：https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9058
# 通过代码将网站信息用读写信息方式下载文件
import requests
import re
import os

def getStation():
	url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9058'
	response = requests.get(url,verify=True)    # 发送网络请求并验证
	stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
	stations = dict(stations)    # 转换为字典形式
	stations = str(stations)    # 转换为字符串类型，否则无法写入文件
	write(stations)    # 调用写入方法，实现下载车站文件

def write(stations):
	file = open('stations.txt','w',encoding = 'utf-8_sig')    # 写入模式打开文件
	file.write(stations)    # 写入文件
	file.close()
def read():
	file = open('stations.txt','r',encoding = 'utf-8_sig')    # 以读模式打开文件
	data = file.readline()    # 以行形式读取文件
	file.close()
	return data
def isStations():
	isStations = os.path.exists('stations.txt')    # 判断车站文件是否存在
	return isStations

# 获取车票信息并将它显示在表格中
# 由网页监视器可以发现，在获取车票信息时我们看到的将是一大片的网页代码，其中夹杂着很多的乱码，其实这些乱码是12306的加密，是一种反爬技术
# 通过认真的观察之后，会发现，这些加密信息会有一定的规律
# 通过代码来破解信息
import requests

'''
    5-7 目的地 3 车次 6 出发地 8 出发时间 9 到达时间 10 历时 26 无座 29 硬座
    24 软座 28 硬卧 33 动卧 23 软卧 21 高级软卧 30 二等座 31 一等座 32 商务特等座
'''

response = requests.get('https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-07-25&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT')
result = response.json()
result = result['data']['result']
n = 0
for i in result:

	# print(i)
	list = i.split('|')    # 分割字符串
	for a in list:
		print(n, a)    # 打印信息编号
		n+=1
	n = 0
	# print(list)

# 最终实现
# get_stations.py
import requests
import re
import os

def getStation():
	url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9058'
	response = requests.get(url,verify=True)    # 发送网络请求并验证
	stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
	stations = dict(stations)    # 转换为字典形式
	stations = str(stations)    # 转换为字符串类型，否则无法写入文件
	write(stations)    # 调用写入方法，实现下载车站文件

def write(stations):
	file = open('stations.txt','w',encoding = 'utf-8_sig')    # 写入模式打开文件
	file.write(stations)    # 写入文件
	file.close()
def read():
	file = open('stations.txt','r',encoding = 'utf-8_sig')    # 以读模式打开文件
	data = file.readline()    # 以行形式读取文件
	file.close()
	return data
def isStations():
	isStations = os.path.exists('stations.txt')    # 判断车站文件是否存在
	return isStations
# query_request.py文件
from get_stations import *
data = []    # 用于保存整理好的车次信息
type_data = []    # 用于保存分类后车次信息
'''
5-7 目的地 3 车次 6 出发地 8 出发时间 9 到达时间 10 历时 26 无座 29 硬座
24 软座 28 硬卧 33 动卧 23 软卧 21 高级软卧 30 二等座 31 一等座 32 商务特等座
'''
def query(date,from_station, to_station):
    data.clear()    # 清空数据
    response = requests.get(r'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={0}&leftTicketDTO.from_station={1}&leftTicketDTO.to_station={2}&purpose_codes=ADULT'.format(date,from_station,to_station))    # 发送查询请求
    # 将json数据转换为字典类型，通过键值对取数据
    result = response.json()
    result = result['data']['result']
    # 判断车次是否存在
    if isStations() == True:
        stations = eval(read())    # 读取所有车站并转换为dic类型
        if len(result) != 0:    # 判断返回值是否为空
            for i in result:
                tmp_list = i.split('|')    # 分割数据段并添加到列表中
                from_station = list(stations.keys())[list(stations.values()).index(tmp_list[6])]
                to_station = list(stations.keys())[list(stations.values()).index(tmp_list[7])]
                seat = [tmp_list[3],from_station,to_station,tmp_list[8],tmp_list[9],tmp_list[10],tmp_list[32],tmp_list[31],tmp_list[30],tmp_list[21],tmp_list[23],tmp_list[33],tmp_list[28],tmp_list[24],tmp_list[29],tmp_list[26]]
                newSeat = []
    			# 循环将座位信息中的空 “” ，改为--
                for s in seat:
                    if s == "":
                        s = "--"
                    else:
                        s = s
                    newSeat.append(s)    # 保存新的座位信息
                data.append(newSeat)
    return data    # 返回整理好的车次信息
# 获取高铁信息方法
def g_vehicle():
	if len(data) != 0:
		for g in data:    # 循环所有火车数据
			i = g[0].startswith('G')    # 判断车次首字母是不是高铁
			if i:
				type_data.append(g)

# 移除高铁信息方法
def r_g_vehicle():
	if len(data) != 0:
		for g in data:
			i = g[0].startswith('G')
			if i:    # 移除高铁信息
			    type_data.remove(g)

# 获取动车信息方法
def d_vehicle():
	if len(data) != 0:
		for d in data:    # 循环所有火车数据
			i = d[0].startswith('D')    # 判断车次首字母是不是动车
			if i:
				type_data.append(d)

# 移除动车信息方法
def r_d_vehicle():
	if len(data) != 0:
		for d in data:
			i = d[0].startswith('D')
			if i:    # 移除动车信息
			    type_data.remove(d)

# 获取直达车信息方法
def z_vehicle():
	if len(data) != 0:
		for z in data:    # 循环所有火车数据
			i = z[0].startswith('Z')    # 判断车次首字母是不是直达车
			if i:
				type_data.append(z)

# 移除直达车信息方法
def r_z_vehicle():
	if len(data) != 0:
		for z in data:
			i = z[0].startswith('Z')
			if i:    # 移除直达车信息
			    type_data.remove(z)

# 获取特快车信息方法
def t_vehicle():
	if len(data) != 0:
		for t in data:    # 循环所有火车数据
			i = t[0].startswith('T')    # 判断车次首字母是不是特快车
			if i:
				type_data.append(t)

# 移除特快车信息方法
def r_t_vehicle():
	if len(data) != 0:
		for t in data:
			i = t[0].startswith('T')
			if i:    # 移除特快车信息
			    type_data.remove(t)

# 获取快速车信息方法
def k_vehicle():
	if len(data) != 0:
		for k in data:    # 循环所有火车数据
			i = k[0].startswith('K')    # 判断车次首字母是不是快速车
			if i:
				type_data.append(k)

# 移除快速车信息方法
def r_k_vehicle():
	if len(data) != 0:
		for k in data:
			i = k[0].startswith('K')
			if i:    # 移除快速车信息
			    type_data.remove(k)

# PaPiao.py文件
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PaPiao.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtGui import  QPalette,QPixmap,QColor    # 导入QtGui模块

from PyQt5.QtGui import *    # 导入QtGui
from PyQt5.QtCore import Qt    # 导入Qt类
from PyQt5.QtWidgets import *    # 导入QtWidgets下所有类及方法
from query_request import *    # 导入用于查询的文件
from get_stations import *    # 导入get_stations文件

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 786)
        MainWindow.setMinimumSize(QtCore.QSize(960, 786))
        MainWindow.setMaximumSize(QtCore.QSize(960, 786))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label0 = QtWidgets.QLabel(self.centralwidget)
        self.label0.setGeometry(QtCore.QRect(0, 0, 960, 141))
        self.label0.setText("")
        self.label0.setObjectName("label0")

        label0_img = QPixmap('train.png')    # 导入顶部位图
        self.label0.setPixmap(label0_img)    # 设置调色版

        self.frame0 = QtWidgets.QFrame(self.centralwidget)
        self.frame0.setGeometry(QtCore.QRect(0, 140, 960, 80))
        self.frame0.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame0.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame0.setObjectName("frame0")

        self.frame0.setAutoFillBackground(True)    # 开启自动填充背景
        palette0 = QPalette()    # 调色板类
        palette0.setBrush(QPalette.Background,QtGui.QBrush(QtGui.QPixmap('bj.jpg')))    # 设置背景图片 
        self.frame0.setPalette(palette0)    # 设置调色板

        self.chufadi0 = QtWidgets.QLabel(self.frame0)
        self.chufadi0.setGeometry(QtCore.QRect(30, 25, 54, 20))
        self.chufadi0.setObjectName("chufadi0")
        self.chufadi1 = QtWidgets.QTextEdit(self.frame0)
        self.chufadi1.setGeometry(QtCore.QRect(90, 20, 104, 31))
        self.chufadi1.setObjectName("chufadi1")
        self.label_2 = QtWidgets.QLabel(self.frame0)
        self.label_2.setGeometry(QtCore.QRect(265, 250, 72, 15))
        self.label_2.setObjectName("label_2")
        self.chufari0 = QtWidgets.QLabel(self.frame0)
        self.chufari0.setGeometry(QtCore.QRect(440, 25, 54, 20))
        self.chufari0.setObjectName("chufari0")
        self.chaxun = QtWidgets.QPushButton(self.frame0)
        self.chaxun.setGeometry(QtCore.QRect(680, 20, 93, 28))
        self.chaxun.setObjectName("chaxun")
        self.mudidi1 = QtWidgets.QTextEdit(self.frame0)
        self.mudidi1.setGeometry(QtCore.QRect(300, 20, 104, 31))
        self.mudidi1.setObjectName("mudidi1")
        self.mididi0 = QtWidgets.QLabel(self.frame0)
        self.mididi0.setGeometry(QtCore.QRect(240, 25, 54, 20))
        self.mididi0.setObjectName("mididi0")
        self.chufari1 = QtWidgets.QTextEdit(self.frame0)
        self.chufari1.setGeometry(QtCore.QRect(500, 20, 104, 31))
        self.chufari1.setObjectName("chufari1")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(0, 220, 960, 40))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.checkBox0 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox0.setGeometry(QtCore.QRect(110, 10, 91, 19))
        self.checkBox0.setObjectName("checkBox0")
        self.checileixing = QtWidgets.QLabel(self.frame1)
        self.checileixing.setGeometry(QtCore.QRect(30, 13, 72, 15))
        self.checileixing.setObjectName("checileixing")
        self.checkBox1 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox1.setGeometry(QtCore.QRect(260, 10, 91, 19))
        self.checkBox1.setObjectName("checkBox1")
        self.checkBox2 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox2.setGeometry(QtCore.QRect(400, 10, 91, 19))
        self.checkBox2.setObjectName("checkBox2")
        self.checkBox3 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox3.setGeometry(QtCore.QRect(550, 10, 91, 19))
        self.checkBox3.setObjectName("checkBox3")
        self.checkBox4 = QtWidgets.QCheckBox(self.frame1)
        self.checkBox4.setGeometry(QtCore.QRect(690, 10, 91, 19))
        self.checkBox4.setObjectName("checkBox4")
        
        self.frame1.setAutoFillBackground(True)    # 开启自动填充背景
        palette1 = QPalette()    # 调色板类
        palette1.setBrush(QPalette.Background,QtGui.QBrush(QtGui.QPixmap('bj.jpg')))    # 设置背景图片 
        self.frame1.setPalette(palette1)    # 设置调色板

        # self.text = QtWidgets.QTextEdit(self.centralwidget)
        self.text = QtWidgets.QTableView(self.centralwidget)
        self.text.setGeometry(QtCore.QRect(0, 330, 960, 457))
        self.text.setObjectName("text")
        
        self.model = QStandardItemModel()    # 创建存储数据模式
        # 根据空间自动改变宽度并且不可修改列宽度
        self.text.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 设置表头不可见
        self.text.horizontalHeader().setVisible(False)
        # 纵向表头不可见
        self.text.verticalHeader().setVisible(False)
        # 设置表格内容文字大小
        font = QtGui.QFont()
        font.setPointSize(10)
        self.text.setFont(font)
        # 设置表格内容不可编辑
        self.text.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # 垂直滚动条始终开启
        self.text.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(0, 260, 960, 70))
        self.label1.setText("")
        self.label1.setObjectName("label1")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        label1_img = QPixmap('bg1.png')    # 导入顶部位图
        self.label1.setPixmap(label1_img)    # 设置调色版

    # 查询按钮的单击事件
    def on_click(self):
        get_from = self.chufadi1.toPlainText()    # 获取出发地
        get_to = self.mudidi1.toPlainText()    # 获取目的地
        get_date = self.chufari1.toPlainText()    # 获取出发日期
        # 判断车站文件是否存在
        if isStations() == True:
            stations = eval(read())    # 读取所有车站并转换为dic类型
            # 判读所有参数是否为空，出发地、目的地、出发日期
            if get_from != "" and get_to != "" and get_date != "":
                # 判断输入的车站名称是否存在，以及时间格式是否正确
                if get_from in stations and get_to in stations and is_valid_data(get_date):
                    # 获取输入的日期是当前年初到现在一共过了多少天
                    inputYearDay = time.strptime(get_date,"%Y-%m-%d").tm_yday
                    # 获取系统当前日期是当前年初到现在一共过了多少天
                    yearToday = time.localtime(time.time()).tm_yday
                    # 计算时间差，也就是输入的日期减掉系统当前的日期
                    timeDifference = inputYearDay - yearToday
                    # 判断时间差为0时证明查询当前的查票
                    # 以及29天以后的车票，12306官方要求只能查询30天以内的车票
                    if timeDifference >=0 and timeDifference <= 28:
                        from_station = stations[get_from]    # 在所有车站文件中找到对应的参数、出发地
                        to_station = stations[get_to]    # 目的地
                        data = query(get_date,from_station,to_station)    # 发送查询请求，并获取返回信息
                        self.checkBox_default()
                        if len(data) != 0:    # 判断返回的值是否为空
                        # 如果不为空的数据就将车票信息显示在表格中
                            self.displayTable(len(data),16,data)
                        else:
                            self.messageDialog('警告','没有返回的网络数据！')
                    else:
                        self.messageDialog('警告','超出查询日期的范围内，不可查询过去的以及29天以后的车票信息！')
                else:
                    self.messageDialog('警告','输入的站名不存在，或日期格式不正确！')
            else:
                self.messageDialog('警告','请填写车站名称！')
        else:
            self.messageDialog('警告','未下载车站查询文件！')

    # 高铁复选框事件处理
    def change_G(self,state):
        # 选中将该信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取高铁信息
            g_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data),16,type_data)
        else:
            # 取消选择状态将移除数据
            r_g_vehicle()
            self.displayTable(len(type_data),16,type_data)

    # 动车复选框事件处理
    def change_D(self,state):
        # 选中将该信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取高铁信息
            d_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data),16,type_data)
        else:
            # 取消选择状态将移除数据
            r_d_vehicle()
            self.displayTable(len(type_data),16,type_data)

    # 直达车复选框事件处理
    def change_Z(self,state):
        # 选中将该信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取高铁信息
            z_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data),16,type_data)
        else:
            # 取消选择状态将移除数据
            r_z_vehicle()
            self.displayTable(len(type_data),16,type_data)

    # 特快车复选框事件处理
    def change_T(self,state):
        # 选中将该信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取高铁信息
            t_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data),16,type_data)
        else:
            # 取消选择状态将移除数据
            r_t_vehicle()
            self.displayTable(len(type_data),16,type_data)

    # 快速复选框事件处理
    def change_K(self,state):
        # 选中将该信息添加到最后要显示的数据当中
        if state == QtCore.Qt.Checked:
            # 获取高铁信息
            k_vehicle()
            # 通过表格显示该车型数据
            self.displayTable(len(type_data),16,type_data)
        else:
            # 取消选择状态将移除数据
            r_k_vehicle()
            self.displayTable(len(type_data),16,type_data)

    # 将所有车次分类复选框取消勾选
    def checkBox_default(self):
        self.checkBox0.setChecked(False)
        self.checkBox1.setChecked(False)
        self.checkBox2.setChecked(False)
        self.checkBox3.setChecked(False)
        self.checkBox4.setChecked(False)

    # 显示消息提示框，参数title为提示框标题文字，message为提示信息
    def messageDialog(self,title,message):
        msg_box = QMessageBox(QMessageBox.Warning, title, message)
        msg_box.exec_()

    # 用于显示车次信息的表格
    # train参数为共有多少趟列车，该参数作为表格的行
    # info参数为每趟列车的具体信息，例如有座、无座、卧铺等。该参数作为表格的列
    def displayTable(self, train, info, data):
        self.model.clear()
        for row in range(train):
            for column in range(info):
                # 添加表格内容
                item = QStandardItem(data[row][column])
                # 向表格中添加具体内容
                self.model.setItem(row,column,item)
        # 设置表格存储数据的模式
        self.text.setModel(self.model)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "快手爬票"))
        self.chufadi0.setText(_translate("MainWindow", "出发地:"))
        self.label_2.setText(_translate("MainWindow", "目的地:"))
        self.chufari0.setText(_translate("MainWindow", "出发日:"))
        self.chaxun.setText(_translate("MainWindow", "查询"))
        self.mididi0.setText(_translate("MainWindow", "目的地:"))
        self.checkBox0.setText(_translate("MainWindow", "GC-高铁"))
        self.checileixing.setText(_translate("MainWindow", "车次类型:"))
        self.checkBox1.setText(_translate("MainWindow", "D-动车"))
        self.checkBox2.setText(_translate("MainWindow", "Z-直达"))
        self.checkBox3.setText(_translate("MainWindow", "T-特快"))
        self.checkBox4.setText(_translate("MainWindow", "K-快速"))

        self.chufari1.setText(get_time())    # 出发日显示当天日期
        self.chaxun.clicked.connect(self.on_click)    # 查询按钮指定单击事件的方法
        self.checkBox0.stateChanged.connect(self.change_G)    # 高铁选择与取消事件
        self.checkBox1.stateChanged.connect(self.change_D)    # 动车选择与取消事件
        self.checkBox2.stateChanged.connect(self.change_Z)    # 直达车选择与取消事件
        self.checkBox3.stateChanged.connect(self.change_T)    # 特快车选择与取消事件
        self.checkBox4.stateChanged.connect(self.change_K)    # 快车选择与取消事件

import time
# 获取系统当前时间并转换请求数据所需要的格式
def get_time():
        # 获取当前时间戳
        now = int(time.time())
        # 转换为其它日期格式：如："%Y-%m-%d %H:%M:%S"
        timeStruct = time.localtime(now)
        strTime = time.strftime("%Y-%m-%d",timeStruct)
        return strTime
def is_valid_data(str):
    '''判断是否是一个有效日期字符串'''
    try:
        time.strptime(str,"%Y-%m-%d")
        return True
    except:
        return False


def show_MainWindow():
    app = QtWidgets.QApplication(sys.argv)    # 实例化Qapplication类，作为GUI主程序的入口
    MainWindow = QtWidgets.QMainWindow()    # 创建QMainWindow
    ui = Ui_MainWindow()    # 实例UI类
    ui.setupUi(MainWindow)    # 设置窗体UI
    MainWindow.show()    # 显示窗体
    sys.exit(app.exec_())    # 当窗口创建完成以后，需要结束主循环


if __name__ == '__main__':
    if isStations() == False:    # 判断是否存在车站文件
        getStation()    # 下载文件
        show_MainWindow()    # 显示主窗体
    else:
        show_MainWindow()
