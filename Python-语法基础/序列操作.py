# 结构：常用的数据存储方式：一种数据结构
# 在Python中主要有 列表、元组、字典、集合、字符串

# 序列
# 序列：序列是一块用于存放多个值的连续的内存空间，并且按一定顺序排列，可以通过索引取值
# 序列的相关功能：索引、切片、序列相加、乘法、检查某个元素是否是序列的成员、计算序列的长度、最大值和最小值
# 索引：就是一种编号 (从0开始)

# 切片：截取部分元素
# sname[start : end : step]
laliga = ["Messi","苏牙","格子","特里","皮克","内马尔","武磊"]
print(laliga[0:5:2])

# 序列相加：只能是同类型的序列相加
laliga1 = ["Messi", "Ciro", "Gelieziman"]
laliga2 = ["皮克", "凳子", "Xavi"]
laliga = laliga1 + laliga2
print(laliga)

# 序列的乘法
# 序列 * 序列 = 原来重复N次的结果
phone = ["HuaWei", "Mate 10", "Vivo X20"]
print(phone * 3)
number = [1,2,3]
print(number * 3)
print("*"*10)
# 初始化长度列表
emptylist = [None]*5
print(emptylist)

# 检查某个元素是否是序列的成员 in
# value in sequence
lilaga = ["Messi", "Ciro", "Ronarldo"]
print("Messi" in lilaga)    # 判断Messi在没在列表中
print("科比" in lilaga)
print("科比" not in lilaga)    # 判断科比是否不在列表中

# 计算序列的长度、最大值、最小值
# len()    获取序列的长度
number = [15,30,60,80]
print("列表的长度：", len(number))    # 输出列表的长度
# max()/min()    返回序列的最大值/最小值
print("列表的最大值：", max(number))    # 输出列表的最大值
print("列表的最小值：", min(number))    # 输出列表的最小值
# 附加：list()转换为列表、str()转换为字符串、sum()列表求和、sort()永久排序、sorted()临时排序、reversed()序列反转、enumerate()把序列组合成一个索引序列

# 列表
# 可变序列 -> 列表 -> [元素1,元素2,......元素n]
# 八项操作：创建和删除、访问元素、遍历、添加修改和删除元素、对列表进行统计计算、排序、列表推导式、二维列表的使用
# 创建和删除：使用赋值运算符直接创建列表、创建空列表、创建数值列表
# listname = [元素1,元素2,.....,元素n]
number = [2,4,6,8,10]    # 创建保存整数的列表
verse = ["春眠不觉醒","Python不得了"]
python = ['优雅', "明确", '''简单''']
untitle = ["python", 28, "人生苦短，我用Python", ["爬虫", "云计算", "Web开发"]]
emptylist = []    # 创建空列表
# 实例：跳跳加分系统
step = list(range(2,21,2))    # 生成每步计分列表
print(step)
# 删除列表：del listname
del step
del emptylist
# 不允许重复删除，不然会出现错误
# 删除语句很少用，Python自带的垃圾回收机制会自动销毁不用的列表，所以即使我们不手动删除。Python也会自动将其回收。
# 访问列表元素：直接使用print()函数输出、通过索引值获取指定位置的元素、切片
print(python)    # 输出python列表
python1 = python[1]     # 获取python列表中的第二个元素
print(python1)
print(python[:2])    # 切片
# 实例：每日一贴
import datetime    # 导入日期时间类
mot = ["今天星期一：\n坚持下去不是因为我很坚强，而是因为我别无选择。",
       "今天星期二：\n含泪播种的人一定能笑着收获。",
       "今天星期三：\n做对的事情比把事情做对重要。",
       "今天星期四：\n命令给予我们的不是失望之酒，而是希望之杯。",
       "今天星期五：\n不要等到明天，明天太遥远，今天就行动。",
       "今天星期六：\n求知若饥，谦逊若愚。",
       "今天星期日：\n成功将属于那些从不说“不可能”的人",
       ]
day = datetime.datetime.now().weekday()    # 获取当前的星期
print(mot[day])    # 输出每日一贴
# 遍历列表：把列表当中的所有元素都访问一遍
# 直接使用for循环实现
# for item in listname:
#    输出元素
print("2018年NBA常规赛西部排名：")
team = ["火箭","勇士","开拓者","雷霆","爵士"]    # 定义一个列表
for item in team:
    print(item)
# 需要元素的索引值enumerate()
for index, item in enumerate(team):
    print("第",index+1,"名：", item)
print("2017-2018赛季NBA西部联盟排名\n")
for index, item in enumerate(team):
    if index%2 == 0:
        print(item + "\t\t",end = " ")
    else:
        print(item + "\n")
# 添加、修改和删除列表元素
python = ["1","2"]
python1 = ["5","6"]
print("\n",len(python))
python.append("3")    # 末尾添加元素
python.append("3")    # 指定位置添加元素
python.insert(0,"4")    # insert方法效率没有append高
python.extend(python1)    # 向列表中添加新列表
print(len(python))
print(python)
python[1] = "10"    # 修改元素
del python[1]    # 根据索引进行删除
print("删除后：",python)
if "3" in python:
    python.remove("3")    # 根据值进行删除 
print("删除后：",python)
# 对列表进行统计计算：count()、index()获取元素首次出现时的下标、sum()统计各元素的和
number = [1,2,3,4,5,6,7,8]
num = number.count(1)    # 统计1出现的次数
print(num)
num = number.index(5)    # 获取5第一次出现的位置下标
print(num)
total = sum(number,1000)    # 累加
print(total)
# 对列表进行排序：sort(key=None,reverse=False)永久排序、sorted(listname,key=None,reverse=True)临时排序
number = [5,6,4,2,8,3,9,1,5,2,0]
print(number)
print(sorted(number,key = None,reverse = True))    # 输出排序后的列表
print(number)
number.sort()    # 永久排序 字符串列表key = str.lower(不区分大小写进行排序)
print(number)
# 列表推导式：列表推导式可以快速生成一个列表，或者根据某个列表生成满足指定需求的列表
import random   # 导入生成随机数模块
list1 = []
for i in range(10):
    list1.append(random.randint(10,100))    # 向列表当中添加随机数
print(list1)
# 修改
# list = [Expression for var in range]
list2 = [random.randint(10, 100) for i in range(10)]    # 此写法就是列表推导式
print(list2)
# 列表推导式：根据列表生成指定需求的列表
# newlist = [Expression for var in list]
price = [1000,500,800,888,666]
sale = [int(x*0.5) for x in price]
print("原价：",price)
print("打折后：",sale)
# 从列表中选择符合条件的元素组成新的列表
# newlist = [Expression for var in list if condition]
sale = [int(x*0.5) for x in price if x >= 800]
print(sale)
# 二维列表的使用：由行和列 list[行下标][列下标]
# 定义二维列表
room = [[1101,1102,1103,1104],
        [2101,2102,2103,2104],
        [3101,3102,3103,3104],
    ]
print(room)
room = []
# for循环自动生成
for x in range(1,4):    # 楼层
    room.append([])    # 添加一个空列表
    for y in range(101,105):    # 每一层的房间数
        room[x-1].append(x*1000+y)
print(room)
# 通过列表推导式生成
room = [[x*1000+y for y in range(101,105)] for x in range(1,4)]
print(room)
# 进行逆序排列    listname.reverse()

# 元组：没有权限内容不可变
# 元组的创建和删除、访问元组元素、修改元组元素、元组推导式、元组与列表的区别
# 元组的创建和删除：使用赋值运算符直接创建元组、创建空元组、创建数值元组
# tuplename = (元素1,元素2,...,元素n)
number = (1,2,3,4,5,6,7,8,9)
print(number)
ukguzheng = ("渔舟唱晚",'高山流水','''出水莲''',"汉宫秋月")
print(ukguzheng)
untitle = ("Python",28,("人生苦短，我用Python"),["爬虫","WEB开发"])
print(untitle)
verse = ("一片冰心在玉壶")    # 注：它不是一个元组，它是一个字符串
print(type(verse))
verse = ("一片冰心在玉壶",)    # 加上一个逗号就是一个元组
print(type(verse))
# 创建空元组
emptytuple = ()
print(emptytuple)
# 创建数值元组
tuple1 = tuple(range(2,21,2))
print(tuple1)
# 删除元组    删除不存在的元组会出现错误    同列表会自动删除
# del tuplename
del tuple1
# 访问元组元素：直接利用print()函数输出、索引、切片
print(untitle)
print(untitle[3])
print(untitle[1:4])
# 修改元组元素
coffee = ('蓝山','卡布奇洛','曼特零','摩卡','麝香猫','哥伦比亚')
coffee = ('蓝山','卡布奇洛','曼特零','摩卡','拿铁','哥伦比亚')    # 修改
print(coffee)
newcoffee = ('麝香猫',)    # 注意这里有逗号，如果没有则不能连接成功
allcoffee = newcoffee + coffee
print(allcoffee)
# 元组推导式：可以快速生成一个元组，或者根据某个元组生成满足指定需求的元组
import random    # 导入随机数模块
randomnumber = (random.randint(10, 100) for i in range(10))
print(randomnumber)    # 得到生成器对象
# 输出生成器元素
# for i in randomnumber:
#    print(i, end='')
print(randomnumber.__next__())    # 输出第一个元素
print(randomnumber.__next__())    # 输出第二个元素
print(randomnumber.__next__())    # 输出第三个元素
print(tuple(randomnumber))    # 输出元组元素

# 元组和列表的区别：
# 元组:不可变序列、支持切片操作(只能访问元组元素)、元组访问速度快、可以作为字典键
# 列表：可变序列、支持切片操作(可以访问、修改列表元素)、列表访问速度满、不能作为字典键

# 字典：字典的创建和删除、通过键值对访问字典、遍历字典、添加修改和删除字典元素、字典推导式
# 字典的创建和删除
# dictionary = {'key1':'value1','key2':'value2'......,'keyn':'valuen'}
word = {'che':'车','chen':'尘','cheng':'城','chi':'吃'}
print(word)
# 将两个列表转换为字典
key = ['che','chen','cheng','chi']    # 音节列表
value = ['车','尘','城','吃']    # 汉字列表
zip1 = zip(key,value)    # 转换为zip对象
print(zip1)
word = dict(zip1)    # 转黄为字典
print(word)
# 定义一个空字典
word = {}
word = dict()
# 通过dict()来创建字典
dictionary = dict(绮梦='水瓶座',冷伊一='射手座',香菱='双鱼座',黛蓝='双子座')
print(dictionary)
# 创建只有key值得字典
dictionary = dict.fromkeys(key)
print(dictionary)
# 删除字典
# del dictionaryname
# dictionaryname.clear()    # 清空字典中的元素
# 通过键值对访问字典
# dictname[key]、dictname.get(key,[default])
dictionary = dict(绮梦='水瓶座',冷伊一='射手座',香菱='双鱼座',黛蓝='双子座')
print(dictionary["冷伊一"] if "冷伊一" in dictionary else "我的字典里不存在此人！")
print(dictionary.get("冷伊一"))
print(dictionary.get("冷伊"))
print(dictionary.get("冷伊","查无此人"))
# 遍历字典
sign = {'绮梦':'水瓶座','冷伊一':'射手座','香菱':'双鱼座','黛蓝':'双子座'}
print(sign.items())    # 通过items()方法得到字典
for key,value in sign.items():    # 通过for循环来输出每一个元素的键值对
    print(key, "的星座是", value)
for key in sign.keys():    # 通过for循环输出每一个元素的key值
    print(key)
for value in sign.values():    # 通过for循环输出每一个元素的value值
    print(value)
# 添加、修改、删除字典元素
# dictionary[key] = value
sign = {'绮梦':'水瓶座','冷伊一':'射手座','香菱':'双鱼座','黛蓝':'双子座'}
sign['碧琪'] = "巨蟹座"    # 添加时key不能重复，如果key存在的话执行修改操作
print(sign)
if '碧琪' in sign:
    del sign['碧琪']    # 删除key为碧琪的元素
print(sign)
# 字典推导式  和列表类似
# {键表达式:值表达式 for循环}
import random
randomdict = {i:random.randint(10,100) for i in range(1,5)}
print(randomdict)

# 集合：set 可变集合、frozenset 不可变集合
# 集合概念：用来保存不重复的元素，最好的应用是去重
# 集合的操作：集合的创建、集合的添加和删除、集合的交并差集运算
set1 = {'水瓶座','射手座','双鱼座','双子座','摩羯座'}    # 定义一个集合
print("set1:",set1)
set2 = {'水瓶座','射手座','双鱼座','双子座','摩羯座','水瓶座'}
print("set2:",set2)
# 无法通过索引来获取元素，因为它的元素是随机的，且不出现重复
# 定义空集合    定义字典时用 dictionary = {}
set3 = set()
print(type(set3))
# set()函数可以把列表转换为集合
# setname.add(element)    向集合中添加元素语法
mr = set(["零基础学习Java","零基础学习C","零基础学习C++","零基础学习PHP"])
mr.add("零基础学习Python")
print(mr)
mr.add("零基础学习Python")
print(mr)
# setname.remove() 删除指定元素    setname.pop() 删除一个随机元素    clear() 清空集合
if "零基础学习C" in mr:
    mr.remove("零基础学习C")
print(mr)
mr.pop()
print(mr)
mr.clear()    # 清空集合元素
print(mr)
del mr    # 删除集合
# 集合的交叉并、对称差集
# 实例：学生选课情况统计
python = set(["绮梦","冷伊一","香菱","梓轩"])
c = set(["冷伊一","零语","梓轩","圣博"])
print("选择Python的学生名单:",python)
print("选择C的学生名单：",c)
print("并集运算：",python | c)
print("交集运算：",python & c)
print("差集运算：",python - c)

# 字符串编码转换
# str    Unicode字符   bytes 二进制数据    不能同时使用，必须转换
# 使用encode()进行编码  把一个字符串转换成二进制编码
# 语法：str.encode([encoding="utf-8"/"GBK"][,errors="strict(遇到非法字符就抛出异常)/ignore(忽略非法字符)/replace(用?替换非法字符)/xmlcharrefreplace(使用xml的字符引用)"])
str1 = "野渡无人舟自横"
byte1 = str1.encode("GBK")    # 采用GDK编码进行转换
byte2 = str1.encode("utf-8")    # 采用utf-8编码进行转换
print("原字符串：",str1)
print("转换后的字符串：",byte1)
print("转换后的字符串：",byte2)
# 使用decode()进行解码
# 语法：str.decode([encoding="utf-8"][,errors="strict"])    同上
str1 = byte1.decode("GBK")
print("解码后的字符串：",str1)
str2 = byte2.decode("utf-8")
print("解码后的字符串：",str2)
# 字符串的常用操作：拼接字符串、计算字符串的长度、截取字符串、分割合并字符串、检索字符串、字母的大小写转换、去除字符串中的空格和特殊字符、格式化字符串
# ''、""必须写在一行上，''' '''可以写在多行上
# 拼接字符串 +
hi = "Hi!"    # 问候语
account = "How are you!"
hi8 = hi + account
print(hi8)
# 计算字符串的长度 len(string)函数  字符的个数(不管中字英文)
str1 = "人生苦短，我用Python!"
print(len(str1))
print(len(str1.encode("utf-8")))    # 计算utf-8编码下字符串长度
print(len(str1.encode("GBK")))    # 计算GBK编码下字符串长度
# 截取字符串  字符串属于序列 可以通过切片的方法
# 切片 string[start:end:step]
str1 = "人生苦短，我用Python!"
print(str1[0:5:2])
try:
    print(str1[52])
except IndexError:
    print("索引不存在！")
# 实例：从身份证号码中截取年份、月份、日
p1 = "你知道我的生日吗？"
print("程序员甲说:",p1)
p2 = "输入你的身份证号码。"
print("程序员乙说：",p2)
idcard = "123456199006277890"
print("程序员甲说：",idcard)
birthday = idcard[6:10] + "年" + idcard[10:12] + "月" + idcard[12:14] + "日"
print("程序员乙说：你是" + birthday + "出生的，所以你的生日是" + birthday[5:])
# 分割split()、合并字符串
# 分割语法：listname = str.split(sep(指定分割符：空格、换行符\n、制表符\t), maxsplit(分割次数，-1为默认值，表示没有限制))
str1 = "你  有 多 自信，\n世界 就有 多 相信你"
print(str1.split())
print(str1.split(" "))
print(str1.split(" ",2))
print(str1.split("\n",5))
# 合并字符串：把字符串进行连接
# newstr = string(合并时的分隔符).join(iterable(可迭代对象))
list1 = ["扎克伯格","俞敏洪","勤奋的天使"]
str1 = "@".join(list1)
str1 = "@" + str1
print(str1)
# 检索字符串：字符串查找
# count()计数、find()查找字符串、index()索引值、startwith()是否以指定字符串开头、endswith()是否以指定字符串结尾
# str.count(sub[,start[,end]])    检索字符串中包括多少个sub字符串的个数
print(str1.count('@'))
# str.find(sub[,start[,end]])、rfind()    检索是否存在字符串，显示首次出现的位置
print(str1.find('@'),str1.find('#'))
# str.index(sub[,start[,end]])、rindex()    与find()类似，未检索成功会抛出异常
print(str1.index('@'))
# str.startswith(prefix[,start[,end]])、str.endswith(prefix[,start[,end]])
# 字母的大小写转换
st = "aBcDEfg"
print(st.lower())    # 把大写字母转换成小写字母
print(st.upper())    # 把小写字母转换成大写字母
print(st)
print(st.title())    # 每个单词开头变为大写，其余都为小写
# 去掉字符串当中的空格和特殊字符(\t \r \n)
# str.strip([chars]) 去掉左边和右边的空格或者特殊字符、lstrip()去掉左边的空格或者特殊字符、rstrip()
st1 = "   https://Navogator97.github.io   "
print(st1.strip())
print(st1.lstrip())
print(st1.rstrip())
# 格式化字符串：使用%操作符、使用字符串对象的format()方法(推荐)
# 语法：'%[-]左对齐[+]右对齐[0][m][.n] 格式化字符'%exp(元组 不能是列表)
template = '编号：%09d\t公司名称：%s \t 官网：http://www.%s.com'    # 定义模板
item = (7,"百度","baidu")     # 要转换的内容
print(template%item)
item1 = (8, "Navigator", "Navigator97")
print(template%item1)
# 使用字符串的format()方法实现
# 语法：str.format(args)
# 模板str的语法格式：{[index][:[fill]align][sign][#][width][.precision][type]}
template = '编号：{:0>9s}\t公司名称：{:s} \t官网：https://www.{:s}.com'    # 模板
context1 = template.format("7","百度","baidu")
print(context1)
# 实例：
import math    # 导入数学模块
print("以货币形式显示：￥{:,.2f}元".format(1251+3950))    # 以货币形式显示
print("{0:.1f}用科学计数法显示：{0:E}".format(120000.1))    # 以科学记数法表示
print("PI取五位小数：{:.5f}".format(math.pi))    # 输出PI小数点后5位
print("{0:d}的十六进制是：{0:#x}".format(100))    # 十六进制显示
print("天才是由{:.0%}的灵感，加上{:.0%}的汗水".format(0.01,0.99))
