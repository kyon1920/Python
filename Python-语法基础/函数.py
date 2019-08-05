# 函数：可以完成某项工作的代码块
# 内置函数：print()、
# 自定义函数：函数的创建和调用、参数传递、返回值、变量的作用域、匿名函数
# 创建/定义 函数
# 语法：def functionname([parameterlist]):
#          ['''comments''']    为函数设定帮组信息，在调用时显示
#          [functionbody]    函数体
def filterchar(string):
    '''功能：过滤危险字符(如黑客)，并且将过滤后的结果输出
        string：要过滤的字符串
        没有返回值
    '''
    import re
    pattern = r'(黑客)|(抓包)|(Trojan)'    # 模式字符串
    sub = re.sub(pattern, "@_@", string)    # 进行模式匹配
    print(sub)
def empth():
    pass
# 调用函数
# 语法：functionname([parametersvalue])
about = "我是一名程序员，喜欢看一下黑客方面的书，想研究一下Trojan"
filterchar(about)
about1 = "我是一名黑客，擅长研究Trojan"
filterchar(about1)
# 实例：输出每日一贴
def function_tips():
    '''每天输出一条励志文字'''
    import datetime    # 导入日期时间类
    #    定义一个列表
    mot = ["今天星期一：\n坚持成功属于那些从不说“不可能”的人",
           "今天星期二：\n求知若饥，谦逊若愚",
           "今天星期三：\n不要等到明日，明天太遥远，今天就行动",
           "今天星期四：\n命运给予我们的不是失望之酒，而是希望之杯",
           "今天星期五：\n做对的事情比把事情做对重要",
           "今天星期六：\n含泪播种的人一定能笑着收获",
           "今天星期日：\n坚持下去不是因为我很坚强，而是因为我别无选择"]
    day = datetime.datetime.now().weekday()    # 获取当前星期
    print(mot[day])    # 输出每日一贴
function_tips()    # 调用函数
# 参数传递：了解形式参数和实际参数、位置参数、关键字参数、为参数设置默认值、可变参数
# 了解形式参数和实际参数：在函数名称后面小括号里面的是形式参数、调用时用的参数就是实际参数
# 值传递：当实际参数为不可变(immutable)参数的时候：int、str、float、(数值型number)、元组(tuple)
# 引用传递：当实际参数为可变(mutable)参数的时候：字典(dictionary)、列表型(list)
def demo(obj):
    '''进行参数相加'''
    print("原值：",obj)
    obj += obj
print("="*10,"值传递","="*10)
list1 = ["qi meng", "len yi yi", "xiang ling", "dai lan"]    # 可变对象
mot = "唯有在被追赶的时候，你才能真正的奔跑"    # 不可变对象
print("函数调用前：",mot)
print("函数调用前：",list1)
demo(mot)    # 调用函数
demo(list1)
print("函数调用后：",mot)
print("函数调用后：",list1)
# 实例：BMI
def fun_bmi(person,height,weight):
    '''功能：根据身高和体重计算BMI指数
        person:姓名
        height:身高  单位：米
        weight:体重  单位：千克
    '''
    print(person + "的身高：" + str(height) + "米\t体重：" + str(weight) + "千克")
    bmi = weight/(height*height)
    print("您的BMI指数为："+str(bmi))
    if bmi < 18.5:
        print("您的体重过轻~@_@~")
    elif bmi < 24.9:
        print("正常范围，注意保持 (-_-)")
    elif bmi < 29.9:
        print("您的体重过重 ~@_@~")
    else:
        print("肥胖 ~@_@~")
# 调用函数
fun_bmi("路人甲",1.83,60)    # 计算路人甲的BMI指数
print()
fun_bmi("路人乙",1.60,50)    # 计算路人乙的BMI指数
# 位置参数：必须按照定义时的个数和顺序进行参数传递，也称必备参数(例如上面的fun_bmi()函数)
# 关键字参数：使用形式参数的名字来确定输入的参数值
# 语法形式：
# def functionname(p1,p2,p3)
# 以下调用结果是一样的
# functionname(p1=value1,p2=value2,p3=value3)
# functionname(p3=value3,p2=value2,p1=value1)
# 演示：以上面的BMI函数为例：
print()
fun_bmi(height=1.69, weight=56, person="路人丙")
# 为参数设置默认值    这个形式参数必须指向一个不可变对象
# def functionname(...,[parameter1=defaultvalue1]):
#     functionbody
def fun_bmi1(person,height,weight = 55):
    '''功能：根据身高和体重计算BMI指数
        person:姓名
        height:身高  单位：米
        weight:体重  单位：千克
    '''
    print(person + "的身高：" + str(height) + "米\t体重：" + str(weight) + "千克")
    bmi = weight/(height*height)
    print("您的BMI指数为："+str(bmi))
    if bmi < 18.5:
        print("您的体重过轻~@_@~")
    elif bmi < 24.9:
        print("正常范围，注意保持 (-_-)")
    elif bmi < 29.9:
        print("您的体重过重 ~@_@~")
    else:
        print("肥胖 ~@_@~")
# 调用函数
print()
fun_bmi1("路人甲",1.72)    # 计算路人甲的BMI指数
print(fun_bmi1.__defaults__)    # 显示函数的默认值
# 体现必须指向一个不可变对象
def demo(obj=None):
     if obj == None:
         obj=[]
     print("obj的值：",obj)
     obj.append(1)
demo()
demo()
# 可变参数：个数不固定的参数 0-n个参数
# 形式 *parameter 接收任意多个不同形式的参数，并且把它们放到一个元组当中
# 形式 **parameter 接收任意多个类似关键字参数一样显式赋值的实际参数，并将其放到一个字典中
def coffee(*coffeename):    # 输出咖啡名称的函数
    print("\n我喜欢的咖啡有")
    for item in coffeename:
        print(item)    # 输出咖啡名称
coffee("蓝山")
coffee("蓝山","卡布奇洛","阿根廷")
list1 = ["蓝山","卡布奇洛","阿根廷"]
coffee(*list1)
# 实例：BMI计算
def fun_bmi1(*person):    # 可变参数
    '''功能：根据可变参数获取姓名、身高和体重并计算BMI指数
    '''
    for list_person in person:
        for item in list_person:
            person = item[0]
            height = item[1]
            weight = item[2]
            print(person + "的身高：" + str(height) + "米\t体重：" + str(weight) + "千克")
            bmi = weight/(height*height)
            print("您的BMI指数为："+str(bmi))
            if bmi < 18.5:
                print("您的体重过轻~@_@~")
            elif bmi < 24.9:
                print("正常范围，注意保持 (-_-)")
            elif bmi < 29.9:
                print("您的体重过重 ~@_@~")
            else:
                print("肥胖 ~@_@~")
print()
list_w = [["绮梦",1.70,65],["冷伊一",1.78,50],["梓轩",1.72,66]]
list_m = [["零语",1.80,75],["黛兰",1.75,70]]
fun_bmi1(list_w,list_m)    # 计算BMI指数
# **parameter
def sign(**sign):
    print()
    for key,value in sign.items():    # 遍历字典
        print(key,"的星座：",value)
sign(绮梦="水瓶座",冷伊一="射手座")
sign(香菱="双鱼座",黛兰="双子座",琦琦="巨蟹座")
dict1 = {"香菱":"双鱼座","黛兰":"双子座","琦琦":"巨蟹座"}
sign(**dict1)
# 返回值：调用函数后得到的一个结果
# return [value]
# 实例：实现顾客折扣结账
def fun_checkout(money):
    '''功能：计算商品合计金额并进行折扣处理
        money：保存商品金额的列表
        返回值：商品的合计金额和折扣后的金额
    '''
    money_old = sum(money)    # 计算合计金额
    money_new = money_old
    if 500 <= money_old < 1000:    # 享受9折优惠
        money_new = '{:.2f}'.format(money_old * 0.9)
    elif 1000 <= money_old <= 2000:
        money_new = '{:.2f}'.format(money_old * 0.8)
    elif 2000 <= money_old <= 3000:
        money_new = '{:.2f}'.format(money_old * 0.7)
    elif money_old >= 3000:
        money_new = '{:.2f}'.format(money_old * 0.6)
    return money_old, money_new    # 返回总金额和折扣后的金额
print("\n开始结算......")
list_money = []
while True:
    inmoney = (float)(input("请输入商品金额(输入0表示输入完毕：)"))
    if int(inmoney) == 0:
        break    # 退出循环
    else:
        list_money.append(inmoney)
money = fun_checkout(list_money)    # 调用函数
print("合计金额：",money[0], "应付金额：", money[1])
# 变量的作用域：它是指程序代码能够访问该变量的区域，如果超出该区域，再访问时就会出现错误
# 局部变量：只在某一作用域里面有效、全局变量：在所有作用域里都有效，不能在函数体内改变全局变量的值
# global 关键字  在函数体内修改全局变量的值或者是说在函数体内定义一个全局变量
# 实例：
pinetree = "我是一棵松树"    # 全局变量
def fun_chirstmastree():
    '''功能：松树的一个梦
        无返回值
    '''
    pinetree = "挂上彩灯，礼物......我变成一棵圣诞树  @^.^@ \n"    # 定义一个局部变量
    print(pinetree) 
# 函数体外
print("\n下雪了......\n")
print("="*15,"开始做梦……","="*15)
fun_chirstmastree()    # 调用函数
print("="*15,"梦醒了……","="*15)
pinetree = "我身上落满雪花，"+pinetree+"-_-"    # 为全局变量赋值
print(pinetree)
# 匿名函数：相当于群众演员，用一次就不用了，也不用起名  lambda表达式
# 基本语法：result = lambda [arg1 [,arg2,……,argn]]:expression(不能出现for、while语句)
# 实例：计算圆的面积
import math
r = 10    # 半径
result = lambda r:math.pi*r*r
print(result(r))
# 实例：书籍信息排序
bookinfo = [("不一样的卡梅拉",22.50,120),("零基础学Android",65.10,89.80),("摆渡人",23.40,36.00),("福尔摩斯探案全集",22.50,128)]
print("爬取到的商品信息：\n",bookinfo,"\n")
bookinfo.sort(key = lambda x:(x[1], x[1]/x[2]))    # 指定排序规则
print("排序后的商品信息：\n",bookinfo,"\n")
