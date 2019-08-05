# 数据类型

# 数字类型：整型、浮点型、复数
# 整数 - 十进制、八进制、二进制、十六进制
a = 11111111111111111111111111111111111111111111111
b = 22222222222222222222222222222222222222222222222
print(a + b)
# 浮点数应用-前面的计算BMI程序
height = 1.70
weight = 55
print("您的身高" + str(height))    # 输出身高
print("您的体重" + str(weight))    # 输出体重
BMI = weight/(height*height)    # 输出BMI指数 
print("您的BMI指数为" + str(round(BMI,2)))    # round()的作用是保留两位小数
if BMI < 18.5:
    print("您的体重过轻 ~@_@~")
elif BMI >= 18.5 and BMI < 24.9:
    print("正常范围，注意保持 -_- ")
else:
    print("肥胖 ~@_@~")
# 复数
a = 3.14 + 12.5j
b = 3.14 + 12.5j
print (a + b)


# 变量=名字=标签
# 不需要先声明变量命，只需要直接赋值就可以了
python = "人生苦短，我用Python"    # 定义一个字符类型的变量
print (python)
age = 18    # 定义整型变量
print (age)
# 通过type()来获取变量类型
print (type(python))
print (type(age))
# 允许多个变量同时获取一个值
no = number = 1024
print(no,number)
# 测试内存地址  id()函数可以获取内存地址
print (id(no), id(number))    # 可以知道两个变量同用了一块地址的值
# 变量名定义规则：必须是一个有效的标识符、选择有意义的单词、不能使用python中的保留字
# 续：慎用大写字母O和小写字母l
# 定义一个常量：不是真正意义上的常量，只是在命名上面为大写字母加下划线组成的标识为常量

# 字符串类型
# 用' '、" "、''' '''来存放字符串，其中''' '''可以不放在一行上
title = '我喜欢的名言'
mont1 = "花开花落，又是一季"
mont2 = '''生活或许并不是你想象中的那么好，单也不会是你想象中的那么差，人的坚强和脆弱都超乎了自己的想象，有时候因为一句话就泪流满面，有时候你回头，发现以及走过了最艰难的时刻。'''
print (title)
print (mont1)
print (mont2)
# 在单引号里面需要输出单引号，需要加上\，“\”在这里为转义字符
# 在输出的字符串前面加上r可以原样输出，包括转义字符
print (r'123\'456')

# 数据类型转换：变量由赋给的值决定的
# 转换函数 int() float() str() hex() oct() bin()
money = 56.75 + 72.91 + 88.50 + 68.51    # 累加总计金额
money_str = str(money)    # 转换为字符串
print ("商品总金额：" + money_str)
money_int = int(money)    # 转换为整型
print("商品总金额(去掉小数点后的金额)：" + str(money_int))
money_bin = bin(money_int)
print("转换为二进制后的金额为：" + str(money_bin))

# 布尔类型 - 表示 真 或者 假 值
# 注意： True != true  False != false  True、False为Python中的布尔值
# 布尔值可以转换为数字1 、 0
# False、None、0、0.0、虚数0、空序列(空字符串、空元组、空列表、空字典)
# 续：对象中的__bool__方法或者__len__方法返回0，其它对象返回的为真值
