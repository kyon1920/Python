# 异常处理及程序调试
# Bug：原意为“臭虫”或“虫子”，现指系统或程序中的缺陷或错误

# 异常概述
# 什么是异常：异常就意味着出现错误并且中断程序的正常执行
# print （"拼搏到感动自己") 前面的括号为中文状态下输入的，会出现无效的语法错误
# 还有一种情况，就是程序可以正常运行，由于使用者操作不当或者输入的数据不符合要求也会出现异常
# 例如：除数为0的异常、NameError尝试访问一个未声明的变量、IndexError索引超出范围、IndentationError缩进错误、TypeError型错误
# ValueError传值错误、KeyError请求不存在的字典关键字、IOError IO错误、ImportError找不到要导入的模块、MemoryError内存不足出错......

# 异常处理语句
# 异常相关语句：try...except语句、try...except...else语句、try...except...finally语句、使用raise语句抛出异常
# try...except语句：可以捕获异常并进行相应的处理，得到处理结果
# 语法：
# try:
#     block1
# except [ExceptionName(指定异常名字，如果指明了就处理该异常，未指明就都处理) [as alias(给异常起别名)]]:
#     block2
# 实例：模拟幼儿园分苹果
def division():
    '''分苹果'''
    print("="*15,"分苹果了","="*15)
    apple = int(input("请输入苹果的个数："))    # 输入苹果个数
    children = int(input("请输入来了几个小朋友："))    # 输入小朋友人数
    result = apple//children
    remain = apple - result*children
    if remain > 0:
        print(apple,"个苹果，平均分给",children,"个小朋友，每人分",result,"个，剩下",remain,"个")
    else:
        print(apple,"个苹果，平均分给",children,"个小朋友，每人分",result,"个")
if __name__ == '__main__':
    try:
        division()
    except (ZeroDivisionError,ValueError) as e:
        print("输入错误：", e)

# try...except...else语句：可以捕获异常并进行相应的处理，得到处理结果
# 语法：
# try:
#     block1
# except [ExceptionName(指定异常名字，如果指明了就处理该异常，未指明就都处理) [as alias(给异常起别名)]]:
#     block2
# else:
#     block3
# 以分苹果为例：
def division():
    '''分苹果'''
    print("="*15,"分苹果了","="*15)
    apple = int(input("请输入苹果的个数："))    # 输入苹果个数
    children = int(input("请输入来了几个小朋友："))    # 输入小朋友人数
    result = apple//children
    remain = apple - result*children
    if remain > 0:
        print(apple,"个苹果，平均分给",children,"个小朋友，每人分",result,"个，剩下",remain,"个")
    else:
        print(apple,"个苹果，平均分给",children,"个小朋友，每人分",result,"个")
if __name__ == '__main__':
    try:
        division()
    except (ZeroDivisionError, ValueError) as e:
        print("输入错误：", e)
    else:
        print("分苹果顺利完成！")

# try...except...finally语句：可以捕获异常并进行相应的处理，得到处理结果
# 语法：
# try:
#     block1
# except [ExceptionName(指定异常名字，如果指明了就处理该异常，未指明就都处理) [as alias(给异常起别名)]]:
#     block2
# finally:    (无论是否出现异常，都会执行这个代码块)
#     block3
# 以分苹果为例：
def division():
    '''分苹果'''
    print("="*15,"分苹果了","="*15)
    apple = int(input("请输入苹果的个数："))    # 输入苹果个数
    children = int(input("请输入来了几个小朋友："))    # 输入小朋友人数
    result = apple//children
    remain = apple - result*children
    if remain > 0:
        print(apple,"个苹果，平均分给",children,"个小朋友，每人分",result,"个，剩下",remain,"个")
    else:
        print(apple,"个苹果，平均分给",children,"个小朋友，每人分",result,"个")
if __name__ == '__main__':
    try:
        division()
    except (ZeroDivisionError, ValueError) as e:
        print("输入错误：", e)
    else:
        print("分苹果顺利完成！") 
    finally:
        print("进行了一次分苹果操作。")

# 使用raise语句抛出异常：我们预测到某语句可能会出现异常，而我们又不想在这个时候处理异常的话就使用raise语句来抛出
# 语法：raise [ExceptionName若不写还是会出现异常[(reason描述信息)]]
# 还是以小朋友分苹果为例：
def division():
    '''功能：分苹果'''
    print("="*15,"分苹果了","="*15)
    apple = int(input("请输入苹果的个数："))    # 输入苹果个数
    children = int(input("请输入来了几个小朋友："))    # 输入小朋友人数
    if apple < children:
        raise ValueError("苹果太少了，不够分")    # 该语句执行后 后面的语句将不会执行
    result = apple//children
    remain = apple - result*children
    if remain > 0:
        print(apple,"个苹果，平均分给",children,"个小朋友，每人分",result,"个，剩下",remain,"个")
    else:
        print(apple,"个苹果，平均分给",children,"个小朋友，每人分",result,"个")
if __name__ == '__main__':
    try:
        division()
    except (ZeroDivisionError, ValueError) as e:
        print("输入错误：", e)
    else:
        print("分苹果顺利完成！") 
    finally:
        print("进行了一次分苹果操作。")

# 程序调试：
# 使用自带IDLE进行程序调试：
# 打开IDLE→点击上方有个Debug菜单→弹出对话框→由IDLE打开文件→在文件中设置断点(鼠标右键菜单中Set breakpoint)
# →执行程序(会在Debug窗口中显示执行信息)→Debug窗口应用见下方图片→根据Debug窗口进行相应调试→找出问题，进行修改

# 使用assert(断言)语句调试程序：
# 语法：assert expression(为真什么都不做，为假是抛出AssertionError异常) [,reason]
# 还是以小朋友分苹果为例：
def division():
    '''功能：分苹果'''
    print("="*15,"分苹果了","="*15)
    apple = int(input("请输入苹果的个数："))    # 输入苹果个数
    children = int(input("请输入来了几个小朋友："))    # 输入小朋友人数
    assert apple > children, "苹果不够分"    # 应用断言调试
    result = apple//children
    remain = apple - result*children
    if remain > 0:
        print(apple,"个苹果，平均分给",children,"个小朋友，每人分",result,"个，剩下",remain,"个")
    else:
        print(apple,"个苹果，平均分给",children,"个小朋友，每人分",result,"个")
if __name__ == '__main__':
    try:
        division()
    except AssertionError as e:    # 处理断言异常
        print("输入有误：", e)
# 断言不能用在检查用户输入，只能用在检测某些内容是否始终为真，如果不能保证，说明程序当中存在Bug，我们需要对这种情况进行处理，因为assert语句只对调试阶段有效
# Python -O 文件名.py 命令 来关闭断言语句
