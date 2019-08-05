# 网络编程

# 什么是网络？
# 各个孤立的工作站或主机相连在一起，从而达到资源共享和通信的目的

# 局域网：在某一个区域内，由多台计算机互联而成的计算机组
# 使用局域网可以实现文件共享、软件共享、打印机共享以及发送电子邮件和传值等
# 优点：规模小、容易搭建、传输数据快
# 缺点：规模太小

# 广域网：能够连接世界的局域网，例如 因特网、万维网www
# 国家与国家之间的网络通信需要搭建海底电缆

# 局域网和广域网就是我们现在使用的网络

# 网络协议：一种联网的同一标准(互联网协议簇 Internet Protocol Suite)
# 有TCP协议、IP协议、UDP协议、FTP协议、HTTP协议、DNS协议......

# TCP/IP
# TCP/IP协议扮演着非常重要的角色，通常我们用TCP/IP协议代表互联网协议簇
# TCP/IP != (TCP and IP)    而是一组协议的简称

# TCP/IP四层结构
# 应用层
# 传输层：主要包括TCP、UDP协议
# 网络层：主要包括IP协议
# 链路层

# IP协议

# IP地址：互联网协议地址，设备的标识
# IP地址的形式：实际上是32位的整数，按8位进行分组分为4组
# 例如：IP Adress: 127.16.254.1

# 我们要访问一个网站，首先得知道它的IP地址
# 例如：我们来获取百度的IP地址
# 在命令行cmd输入：ping www.baidu.com
# 出现的类似以上地址形式的一串数字就是百度的IP地址
# 可以通过IP地址来访问百度，在网页最上方地址栏输入即可
# 在我们访问网页的时候并没有用它的IP地址，而是用的域名
# IP地址和域名是通过DNS服务器实现的映射

# MAC地址，也就是网卡地址
# 每个计算机在出厂之前都会分配一个网卡地址
# 由48个二进制位组成，通常12个16进制位来表示
# 例如：MAC Address:00-B0-D0-86-BB-F7
# 查看计算机的MAC地址方式
# 在cmd窗口中输入：ipconfig/all 找到物理地址即为MAC地址
# IP地址可更改，MAC地址不可更改
# IP地址和MAC地址之间也存在一种映射关系

# IP的作用
# IP协议处在网络层，它负责把数据从一台计算机通过网络发送给另一台计算机
# 从发送端到路由器，再由路由器到另一个路由器，几经周折，最后到接收端

# TCP协议
# TCP协议处于四层结构中的传输层，处于IP协议之上
# 主要负责在两台计算机之间建立可靠连接，保证数据包按顺序到达
# 为了建立可靠连接，TCP会通过三次握手的方式实现
# 三次握手目的：检测双方是否具备发送和接收功能
# 通过了三次握手就可以进行发送数据了

# 端口号：每一个端口号对应着相应的服务
# 例如:80端口-HTTP服务、21端口-FTP、8080端口-Tomcat、3306端口-MySQL
# 其实我们计算机内大多数与网络相关的应用都有对应的端口号
# 一个应用可以占用多个端口号
# 系统会使用0-1024端口号，所有我们使用的时候只能用1024以上的端口号

# UDP简介
# UDP协议和TCP协议同处于传输层，作用也为传输数据
# UDP协议是面向无连接的协议
# 使用UDP协议时，不需要建立链接，
# 只需要知道对方的IP地址和端口号就可以直接发送数据包

# TCP和UDP的区别
# TCP协议在发送数据之前需要进行三次握手，而UDP没有，可直接发送
# TCP协议可以反馈数据是否到达   可靠
# 而UDP协议无任何反馈   不可靠
# TCP协议需要建立连接请求，连接成功后发数据  效率低
# 而UDP协议不需要创建请求，直接发数据   效率高

# 由于UDP的特性，它经常应用于聊天室、视频直播等应用程序中

# TCP编程
# 由于TCP具有安全可靠的特性，所有TCP应用更为广泛
# 在创建TCP连接时，主动发起请求的叫做客户端，被动响应的是服务器

# 创建TCP服务器
# 步骤：
# 创建Socket()→绑定IP和端口号Bind()→监听数据Listen()→
# 接收数据Accept()→当有客户端发送请求的时候Receive()、Send()
# →关闭Close()
# 实例：使用服务器向浏览器发送"Hello world"
import socket

host = '127.0.0.1'    # IP号
port = 8080    # 端口号

web = socket.socket()    # 创建socket()
web.bind((host,port))    # 绑定IP和端口号
web.listen(5)    # 监听
print('服务器等待客户端连接')
while True:
    conn,addr = web.accept()
    # conn是一个新的socket对象，addr是连接客户端的IP地址
    data = conn.recv(1024)    # 获取客户端请求的数据
    print(data)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\nHello World')
    conn.close()
# 运行结果：服务器等待客户端连接
# 因为没有客户端，就当网页为客户端了
# 在网页地址栏输入：127.0.0.1:8080就会在网页上显示Hello world
# 这样程序运行完美结束，成功

# 创建TCP客户端
# 步骤：创建Socket()→调用Connect()方法连接服务器→
# 使用Send()发送信息、Receive()接收服务→Close()关闭Socket
# 实例：创建一个客户端接收上面的服务器
import socket

host = '127.0.0.1'
port = 8080

client = socket.socket()
client.connect((host,port))    # 连接到服务器
send_data = input('请输入要发送的数据：')
client.send(send_data.encode())    # 发送前需要进行编码
recv_data = client.recv(1024).decode()    # 接收的解码
print('接收到的数据是%s' % recv_data)
client.close()

# 执行TCP服务器和客户端
# 实例：制作简易的聊天窗口
# 服务器端
import socket

host = socket.gethostname()
port = 12345
# 参数socke.AF_INET表示IPV4 socket_SOCK_STREAM表示TCP服务
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
sock,addr = s.accept()
print('连接已经建立')
info = sock.recv(1024).decode()
while info != 'byebye':
    if info:
        print('接收到的内容：%s' % info)
    send_data = input('输入发送的内容：')
    sock.send(send_data.encode())
    if send_data == 'byebye':
        break
    info = sock.recv(1024).decode()
sock.close()
s.close()
# 客户端
import socket

host = socket.gethostname()
port = 12345

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print('已经连接')
info = ''
while info != 'byebye':
	send_data = input('输入发送内容：')
	s.send(send_data.encode())
	if send_data == 'byebye':
		break
	info = s.recv(1024).decode()
	print('接收到的内容：%s' % info)
s.close()

# UDP编程
# UDP是面向消息的协议，不需要建立连接，不可靠，效率高

# UDP应用场景
# 语音广播
# 视频
# 聊天软件
# TFTP(简单文件传送)
# SNMP(简单网络管理协议)
# RIP(路由信息协议，如报告股票市场、航空信息)
# DNS(域名解释)

# 实例：将摄氏温度转换为华式温度
# 创建UDP服务器
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('127.0.0.1',8888))
print('绑定UDP到8888端口')
data,addr = s.recvfrom(1024)
data = float(data)*1.8+32
send_data = '转化后的温度(单位：华氏度)：' + str(data)
print('Recieved from %s %s' % addr)
s.sendto(send_data.encode(),addr)
s.close()
# 创建UDP客户端
# 流程
# 创建客户端套接字→发送/接收数据→关闭套接字
import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = input('请输入要转化的温度(单位：摄氏度)：')
s.sendto(data.encode(),('127.0.0.1',8888))
print('转化后的华氏度是%s' % s.recv(1024).decode())
s.close()

# 执行UDP服务器和客户端
# UDP服务器需要绑定端口号，客户端不需要，直接向服务器发送数据
