# Python操作数据库
# 为什么要使用数据库，在使用数据库之前，我们是通过文件存储的方式来实现数据的存储的，对于数据量较小是可以的，但是大多数都是数据量很大的操作，这时文件操作就显得十分繁琐且复杂，在这样的情况下，我们就应该使用数据库了
# 数据库有很多种，分为关系型数据库和非关系型数据库，我们这里使用的是免费的且应用得十分广泛的MySQL关系型数据库，关于更多数据库知识这里不过多讲解

# 数据库编程接口
# 一种标准SIG：DB_API

# www.python.org/dev/peps/pep-0249/    有相关介绍和接口说明
# 连接对象  Connection Objects
# connect(dsn = "数据源名称：如MySQL",user用户名IP地址,password用户密码,host主机名,database数据库名称)函数    参数见下图
# 实例：见下图

# 游标对象  Cursor Objects
# 使用Connection对象调用Cursor()方法得到Cursor对象

# 使用Python操纵SQLite数据库(体积小，在Python集成有sqlite3模块)
# 验证：
import sqlite3
# 未出现错误提示则说明嵌有sqlite3

# 数据库基础知识
# 什么是数据库：简单来说就是一个存储数据的仓库
# 数据表：一个数据库可以包含多个数据表，它就是一系列二维数组的集合，用于存储和操作数据的逻辑结构，每张数据表都有行和列组成
# 数据表的列：每一列都由字段名和字段值组成
# 数据表的行：它是一种信息，每一行是一个记录
# 操作SQLite流程：连接数据库→执行SQL语句→关闭连接

# 用Python创建SQLite数据库文件
# 实例：创建SQLite数据库文件
# 流程：导入sqlite3模块→创建Connection对象→创建Cursor游标对象→执行SQL语句→关闭游标→关闭连接
# 实例：
import sqlite3    # 创建模块
conn = sqlite3.connect('Nav.db')    # 创建连接对象
cursor = conn.cursor()    # 创建游标对象
cursor.execute('create table user(id int(10) primary key, name varchar(20))')    # 执行SQL语句
cursor.close()    # 关闭游标
conn.close()    # 关闭连接

# 使用Python操纵数据库
# 下载安装MySQL:https://dev.mysql.com/downloads/windows/installer/5.7.html
# 开始安装MySQL：网上有教程！
# 下载Navicat for MySQL可视化工具进行数据库的相关操作，然后再用Python进行操控

# 使用Python内置操作MyQL模块PyMySQL，安装PyMySQL
# 打开命令行：键入命令 pip install PyMySQL  等待安装成功就好
import pymysql
# PyMySQL说明文档：https://pymysql.readthedocs.io/en/latest/
# PyMySQL同样遵循数据库标准
# Python连接MySQL数据库
import pymysql     # 导入PyMySQL模块
db = pymysql.connect(host = 'localhost',user = 'root',password = 'root',database = 'Nav')    # 调用connect()函数生产connection对象，参数详解见说明文档
cursor = db.cursor()    # 调用cursor()方法，创建Cursor()对象
cursor.execute('select version()')    # 执行SQL语句
data = cursor.fetchone()    # 得到输出结果
print(data)
cursor.close()    # 关闭游标
db.close()    # 关闭连接

# 创建数据表
# 实例：创建books图书表
import pymysql     # 导入PyMySQL模块
db = pymysql.connect(host = 'localhost',user = 'root',password = 'root',database = 'Nav')    # 调用connect()函数生产connection对象，参数详解见说明文档
cursor = db.cursor()    # 调用cursor()方法，创建Cursor()对象
cursor.execute('drop table if exists books')    # 如果存在books表就删除它
sql = """
CREATE TABLE books (
  id int(8) NOT NULL AUTO_INCREMENT,
  name varchar(50)·NOT·NULL,
  category varchar(50) NOT NULL,
  price decimal(10,2)·DEFAULT·NULL,
  publish_time·date·DEFAULT·NULL,
  PRIMARY·KEY·(id)
) ENGINE = MyISAM AUTO_INCREMENT = 1·DEFAULT·CHARSET=utf8;
"""
cursor.execute(sql)    # 执行SQL语句
data = cursor.fetchone()    # 得到输出结果
print(data)
cursor.close()    # 关闭游标
db.close()    # 关闭连接

# 操作MySQL数据
# 新增、删除、修改、查询：以新增为例，其余操作都差不多
# 实例：在books表中添加数据
import pymysql     # 导入PyMySQL模块
db = pymysql.connect(host = 'localhost',user = 'root',password = 'root',database = 'Nav',charset = 'utf8')    # 调用connect()函数生产connection对象，参数详解见说明文档
cursor = db.cursor()    # 调用cursor()方法，创建Cursor()对象
cursor.execute('drop table if exists books')    # 如果存在books表就删除它
sql = """
CREATE TABLE books (
  id int(8) NOT NULL AUTO_INCREMENT,
  name varchar(50)·NOT·NULL,
  category varchar(50) NOT NULL,
  price decimal(10,2) DEFAULT NULL,
  publish_time date DEFAULT NULL,
  PRIMARY KEY (id)
) ENGINE = MyISAM AUTO_INCREMENT = 1 DEFAULT CHARSET=utf8;
"""
cursor.execute(sql)    # 执行SQL语句
data = ('零基础学Python','Python','79.80','2018-11-11')
sql = "insert into books(name,category,price,publish_time) value(%s,%s,%s,%s)"
cursor.execute(sql,data)    # 插入一条语句
data = [('零基础学Python','Python','79.80','2018-11-11'),
        ('零基础学JAVA','Python','79.80','2019-11-14'),
        ('零基础学PHP','Python','79.80','2015-10-11'),
        ('C语言','Python','79.80','2016-08-25')]
try:
    cursor.executemany(sql,data)    # 插入多条语句
    data = cursor.fetchone()    # 得到输出结果
except:
    db.rollback()    # 如果插入失败执行回滚
print(data)
cursor.close()    # 关闭游标
db.close()    # 关闭连接
