# 基本输入和输出
# 输入：在键盘上输入、输出：在屏幕上输出

# 输入
# variable = input("提示输入提示")
tip = input("请输入文字：")    # 如果需要的其它数据类型，则需要强制数据类型转换
print (tip)
print (type(tip))

# 输出
# print (输出内容) 基本输出函数，输出内容可以是数字、字符串、表达式
a = 10
b = 6
print ("数字：" , 6)    # “,”将输出放在一行，不过系统会自动加上一个空格
print ("表达式a*b:", a*b)
print ("字符串：", "快乐学习，快乐成长！")
# 将输出结果写到一个文件中
fp = open (r'H:\Python Program\mot.txt', 'a+')
print("I love you three thousand times.", file = fp)    # 输出到文件中
fp.close()    #关闭文件
