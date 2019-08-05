# 流程控制语句
# 程序结构、选择语句、条件表达式、虚幻语句、跳转语句、pass空语句

# 程序结构：顺序结构、选择结构、循环结构
# 顺序结构：按照代码顺序执行
print ("第一次执行")
print ("第二次执行")
print ("第三次执行")
# 选择结构：按照条件表达式来执行，为真执行、假跳过
# 循环结构：在一定条件下循环执行语句块当中的代码

# 选择/条件语句
# 4种方式： 简单的if语句、if...else语句、if...elif...else语句、if语句的嵌套使用
# 在python种没有switch语句
# if 表达式:  成立条件：True、非空字符串、非0字
print ("选择/条件语句应用")
a = 10
if a < 10:
    print ("a < 10")
elif 10 <= a < 20:
    print ("10 <= a < 20")
elif 20 <= a < 50:
    print ("20 <= a < 50")
else:
    print ("a > 50")
# 条件表达式
# 结果1 if 表达式 else 结果2  在if之前为条件表达式为真的结果，在else之后为条件表达式为假的结果
a = 10
b = 20
r = a if a > b else b    #条件表达式实例
print (r)
# 使用条件表达式实现求绝对值的功能
a = -10
b = a if a > 0 else -a
print (b)

# 循环语句 while、for  Python中没有do...while循环
# while 条件表达式:循环体  循环判断条件表达式，为真执行、为假退出
none = True
number = 0
while none:
    number += 1;
    if number >=10:
        break;    # 退出循环条件
    else:
        print (number)
# for循环
# for 迭代变量 in 对象:循环体
# 实例：实现计算累加1到100的结果
print ("计算1+2+3+...+100的结果")
result = 0    # 保存结果的值
for number in range(101):    # range(start, end, step)函数
    result += number
print ("结果为：", result)
for i in range(1, 10, 2):    # 打印1-10之间的奇数
    print(i, end=' ')
# 循环嵌套
# 实例：寻找位置
for row in range(1,5):
    print("当前所造排：", row)
    if row == 2:
        for colunm in range(1,6):
            print("当前所在列：", colunm)
            if colunm == 3:
                print("找到了位置！")
# 实例：打印九九乘法表
print("打印九九乘法表：")
for i in range(1,10):
    for j in range(1,i+1):
        print(i, "*", j, " = ", i * j, "\t", end = ' ')
    print('\n')

# 跳转语句：break、continue
# break:完全跳出循环
for row in range(1,5):
    print("当前所造排：", row)
    if row == 2:
        for colunm in range(1,6):
            print("当前所在列：", colunm)
            if colunm == 3:
                print("找到了位置！")
                break
        break
# continue:跳出本次循环，进行下一次循环
total = 99    # 记录可拍桌子数
for number in range(1, 100):    # 从1循环到99
    if number % 7 == 0:    # 判断是否是7的倍数
        continue    # 继续下一次循环
    else:
        string = str(number)
        if string.endswith('7'):    # 是否以7结尾
            continue    # 继续下一次循环
    total -= 1    # 可拍桌子数1
print ("从1数到99共拍桌子", total, "次！")

# pass空语句：表示空语句，它不做任何事情，一般起到占位作用
for i in range(1, 10):
    if i%2 == 0:
        print(i, end = ' ')
    else:
        pass    # 占位，不做任何操作

# 综合实例：今有物不知其数，三三数之剩二，五五数之剩三、七七数之剩二，问几何？
print("\n今有物不知其数，三三数之剩二，五五数之剩三、七七数之剩二，问几何？\n")
none = True
number = 0
while(none):
    if number % 3 == 2 and number % 5 == 3 and 2 == number % 7:
        print("该数为：", number)
        break
    else:
        number += 1
