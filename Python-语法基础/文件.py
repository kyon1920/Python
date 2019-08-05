# 文件：基本文件操作、目录操作、高级文件操作

# 基本文件操作(File对象)：打开文件 → (写入内容、读取内容(可以不关闭，Python回收机制)) → 关闭文件

# 创建和打开文件：open()函数
# 语法：file = open(filename(打开或者要创建的文件名：r只读、w只写、a追加)[,mode(指定文件打开模式)[,buffering（）]])
# file = open('status.txt','r')    # 打开在程序目录下已存在的文件
file1 = open('status.txt','w')    # 创建文件
# 实例：蚂蚁庄园的新鲜事
print('\n',"="*10,"蚂蚁庄园动态","="*10)
file = open('message.txt','w')    # 自动创建文件
print("\n即将显示 ......\n")
# file = open('message.txt','r')    # 打开文件：默认以GBK打开
# file = open('message.txt','r',encoding = 'utf-8')    # 以utf-8格式打开文件
# print(file.read())    # 读取文件内容
# 以二进制形式打开文件：图片、音频......
file = open('1.png','rb')    # 以二进制形式打开文件
print(file)

# 关闭文件
# 语法：file.close()
print("关闭前：",file.closed)    # 判断文件有没有被关闭
file.close()
print("关闭后：",file.closed)

# 打开文件时使用with语句
# 语法：
# with expression(可以指定打开文件的open函数) as target(指定一个变量，保存结果):
#     with-body
with open('status.txt','r') as file:    # 打开文件
    pass
print("关闭了吗？",file.closed)

# 写入文件内容
# 语法：file.write(string要写入的内容)
list1 = ["Messi",'姆巴佩',"姚明","张怡宁"]
with open('status.txt','w') as file1:    # 打开文件
    file1.write("相信自己：")
    file1.writelines(list1)    # 不换行写入一个列表
    file1.writelines(line + "\n" for line in list1)    # 换行输出
    file1.close()    # 需要关闭或者运行下面的flush()方法才可正常写入
    # file1.flush()
file1 = open('status.txt','r')
print("已经写入：",file1.read())
file1.close()

# 读取文件：打开方式只能为 r 读取或 r+ 读写
# 语法：file.read([size(要读取的字符个数，默认为全部)])
# 语法：file.readline()    读取一行
# 语法：file.readlines()    读取全部行
file2 = open('status.txt','r+')
string = file2.readline()    # 读取一行
if string == "":
    exit
else:
    print(string, end = "\n")
file2.seek(8)    # 指针移动到第5个字符
string = file2.read(9)    # 读取9个字符
print(string)
file2.close()

# 目录操作：os/os.path模块实现
# os模块：它是Python内置的与(操作系统)功能和(文件系统)相关的模块。该模块中的语句的执行结果通常与操作系统有关
# os和os.path模块
import os
print(os.name)    # 获取操作系统的名字，nt表示Windows操作系统，posix表示Linux或者MacOS操作系统
print(str(os.linesep))    # 获取操作系统所用的换行符
print(str(os.sep))    # 获取操作系统中的分隔符

# 路径：通过它可以找到文件的字符串
# 相对路径：存在当前路径→确定文件路径
# os模块中getcwd()函数可获取当前文件的工作目录
import os
print(os.getcwd())
with open('demo/status.txt') as file:    # 通过相对路径打开文件或者r'demo\status.txt'或者'demo\\status.txt'
    print(file.read())
# 绝对路径：直接确定文件位置
# 通过os.path.abspath(path(相对路径))来获取一个文件的绝对路径
print(os.path.abspath(r'demo\status.txt'))
# 拼接路径
# 语法：os.path.join(path1[,path2[,......]])
print(os.path.join(r'H:\Python Program',r'demo\status.txt'))    # 拼接路径：相对路径拼接出来的就是相对路径
# 拼接时出现多个绝对路径的话，系统会以最后一个为准，而且不会检查该路径是否真实存在
print(os.path.join(r'H:\Python Program',r'C:\Python',r'demo\status.txt'))

# 判断目录/文件是否存在
# 语法：os.path.exists(path)    path不区分大小写
import os
print(os.path.exists(r'D:\demo'))    # 判断目录是否真实存在
print(os.path.exists(r'C:\Python'))    # 判断目录是否真实存在
print(os.path.exists(r'H:\Python Program\status.txt'))    # 判断文件是否存在

# 创建目录
# 语法：os.mkdir(path,mode = 0o777(可省略，通常不写))    不能直接创建多级目录
import os
if not os.path.exists(r'D:\demo'):
    os.mkdir("D:\\demo")    # 在D盘文件下创建demo
else:
    print("该目录已经存在")
# 创建多级目录
# 可以用上面的函数进行递归调用
import os
def mkdir(path):    # 创建一个递归函数用于创建目录
    if not os.path.isdir(path):    # 判断是否为路径
        mkdir(os.path.split(path)[0])
    else:
        return
    os.mkdir(path)    # 创建目录
mkdir(r"D:\demo\test\demo")
# 函数实现：os.mkdirs(name,mode = 0o777)    推荐
import os
os.mkdirs(r'D:\demo\mr\demo\Navigator97')

# 删除目录
# 语法：os.rmdir(path(相对路径或者绝对路径))    删除空目录
import os
if not os.path.exists(r'D:\demo\mr\demo\Navigator97'):
    os.rmdir(r'D:\demo\mr\demo\Navigator97')    # 删除目录
    print("目录删除成功")
else:
    print("目录不存在！")
# 删除不为空的目录：需要使用Python内置的shutil模块
# 语法：shutil.rmtree(path)
import shutil
shutil.retree(r'D:\demo')    # 删除不为空的目录

# 遍历目录
# 语法：os.walk(top[, topdown(确定遍历顺序，True自上而下遍历，False相反)][,onerror指定错误处理方式，默认为忽略][,followlinks(True指定在支持的系统上访问由符号链接(软链接)指向的目录)])
# 返回值：元组生成器对象(diepath字符串,dirnames列表,filenames列表)
import os
path = os.walk(r'H:\Python Program')
for p in path:
    print(p,'\n')
# 实例：遍历指定目录
import os
path = r'C:/Python'
print('【',path,"】目录下包含的文件和目录：")
for root,dirs,files in os.walk(path, topdown = True):     # 遍历指定目录
    for name in dirs:
        print(os.path.join(root,name))    # 输出遍历到的目录
    for name in files:
        print("\t",os.path.join(root,name))    # 输出遍历到的目录

# 高级文件操作
# 删除文件
# 语法：os.remove(path)
import os
if os.path.exists(r'E:\Python'):
    os.remove(r"E:\Python")
else:
    print("文件不存在！")
# 重命名文件和目录
# 语法：os.rename(src要重命名的目录或文件的路径,dst重命名后的目录或文件的路径)
import os
# 对文件进行重命名
src = r'E:\Python\text.txt'    # 原路径
dst = r'E:\Python\m.txt'    # 修改后
if os.path.exists(src):
    os.rename(src,dst)
else:
    print("文件不存在！")
# 对目录进行重命名
src = r'E:\Python\demo1'    # 原路径
dst = r'E:\Python\demo2'    # 修改后
if os.path.exists(src):
    os.rename(src,dst)    # 只能修改最后一级的目录名称
else:
    print("目录不存在！")

# 获取文件基本信息：右键(属性→详细信息)
# 语法：os.stat(path)
# 返回值为一些对象  下方图可见：st_ctime创建日期、st_mtime修改日期、st_size大小、st_mode文件保护模式、st_ino文件的索引号、st_atime文件的最后一次访问时间
# 实例：获取文件的基本信息
import os
def formatTime(longtime):
    '''格式化时间的函数'''
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(longtime))    # 格式化时间
def formatByte(number):
    '''格式化文件大小'''
    for (scale,label) in [(1024*1024*1024,'GB'),(1024*1024,'MB'),(1024,'KB')]:
        if number >= scale:    # 处理大于等于1KB
            return "%.2f %s" %(number*0.1/scale,label)
        elif number ==1:
            return "1 字节"
        else:    # 小于1KB
            byte = "%.2f" % (number or 0)
    return (byte[:-3] if byte.endswith(".00") else byte) + "字节"
fileinfo = os.stat(r'mr.png')    # 获取文件的基本信息
print("文件完整路径：",os.path.abspath("mr.png"))    # 获取文件的完整路径
print("索引号：",fileinfo.st_ino)    # 获取文件的索引号
print("设备名：",fileinfo.st_dev)    # 获取文件设备名
print("文件大小：",formatByte(fileinfo.st_size))    # 未格式化以字节显示
print("最后一次访问时间：",formatTime(fileinfo.st_atime))
print("最后一次修改时间：",formatTime(fileinfo.st_mtime))
print("最后一次状态变化时间：",formatTime(fileinfo.st_ctime))    # 获取文件创建时间
