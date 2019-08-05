# 模块：什么是模块？、自定义模块、以主程序的形式执行、Python中的包、引用其它模块

# 什么是模块？ 模块就是Python程序，把能够实现某一特定功能的代码放在一个文件中作为一个模块，从而方便其它程序和脚本导入并使用
# 使用模块的好处：可以避免函数名和变量名冲突、更容易查找代码、提高代码的可重用性、有选择的使用

# 使用import语句导入模块
# 语法：import modulename [as alias]  as 指定别名
# 实例:
# import BMI as bmi    # 导入模块    在和本文件相同的文件夹下有一个BMI.py文件
# bmi.fun_bmi()    # 调用模块中的函数

# 使用from...import语句导入模块
# 语法：form modelname import member(变量、函数、类，导入模块中的全部定义用*)
# 实例：
# from BMI import fun_bmi    # 导入模块中的fun_bmi函数
# print(dir())    # 显示导入的模块的所有定义
# fun_bmi()
# 导入两个同名的模块或者模块中有同名函数、变量、类名时，只能用import来进行导入，还可以起别名

# 模块搜索目录：要导入的模块文件不在相同目录中时用到的
# import sys
# print(sys.path)    # 系统会在列出的目录下去查找模块，找不到就会报错
# 三种解决方法：临时添加、添加.pth文件(推荐)、在PYTHONPATH环境变量中添加

# 临时添加：只在执行时有效，关闭就无效了
# import sys
# sys.path.append('临时目录')    # \需要转义、也可以只用一个/

# 添加.pth文件：在Python安装目录下Python36→Lib→site-packages文件夹中添加.pth文件
# 文件名无要求，文件内容如下：
# # .pth是我创建的路径文件
# E:/Python Program/trmp
# 保存文件→改名为后缀为.pth的文件就行：然后直接import可用

# 添加环境变量
# 开始菜单下的计算机→单击鼠标右键选择属性菜单项→高级系统设置→环境变量→新建系统变量→设定变量名：PYTHONPATH、变量值为：文件所在路径→确定

# Python中的包
# 包 == 包含__init__.py文件的文件夹
# 作用：模块可以避免函数名和变量名重名引发的冲突、包可以避免模块名重名引发的冲突，它还可以将功能相近的模块组织到一个目录下(起到规范代码的作用)

# 了解Python程序中的包结构：下方有图片详解
# 在开发过程中，通常会创建多个包来存放不同类的文件
# 创建包
# 进入相应目录→新建文件夹→在该文件夹中创建Python文件(__init__.py和其它模块)
# 使用包：体现使用import语句来从包当中加载模块
# 三种加载模式

# import + 完整包名 + 模块名    指定加载的模块
# 实例：在同Python文件目录下有一个包setting，包中文件__init__.py和size.py(包含两个变量width、height)
# import setting.size    # 导入模块size
# print("width:",setting.size.width)   # 输出宽度
# print("height:",setting.size.height)    # 输出高度

# from + 完整包名 + import + 模板名    使用时不再需要加包名
# from setting import size    # 导入模块size
# print("width:",size.width)   # 输出宽度
# print("height:",size.height)    # 输出高度

# from + 完整包名 +.模块名 + import + 定义名    可以直接用定义名进行操作 *导入所有模块
# from setting .size import width,height    # 导入模块size
# print("width:",width)   # 输出宽度
# print("height:",height)    # 输出高度

# 以主程序的形式执行
# 语法：if __name__ == '__main__':
# 理解：通俗的理解__name__ == '__main__'：假如你叫小明.py，在朋友眼中，你是小明(__name__ == '小明')；在你自己眼中，你是你自己(__name__ == '__main__')。
# if __name__ == '__main__'的意思是：当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。

# 导入和使用标准模块(标准库)  import 语句进行导入
# 使用生成随机数的模块
import random
number = random.randint(0,10)    # 生成一个0-10的随机整数
print(number)
# 实例：生成4位由字母和数字组成的验证码
import random    # 导入随机数模块
if __name__ == '__main__':
    checkcode = ""    # 保存验证码的变量
    for i in range(4):
        index = random.randrange(0,4)    # 生成一个0~3的一个数
        if index != i and index + 1 != i:
            checkcode += chr(random.randint(97,122))    # 生成a-z中的一个小写字母
        elif index + 1 == i:
            checkcode += chr(random.randint(65,90))    # 生成A-Z中的一个大写字母
        else:
            checkcode += str(random.randint(0,9))    # 生成0~9中的一个数字
    print("验证码:",checkcode)
# 在Python中标准模块大约有200多个，例如re(正则表达式)、math(数学模块)、sys、json、time、thinter......
# 可以通过Python中的帮助文档来查看各标准模块的功能及用法
# 帮助文档所在位置：Python安装目录→Python36→Doc→python364.chm 双击打开，节点The Python Standard Li/brary即为标准库帮助文档说明

# 第三方模块(第三方库)的下载和安装
# https://pypi.org
# 语法：在cmd中使用 pip <command>(常用的参数值为install、uninstall、list) [modulename]
# pip list 可以查看电脑中目前安装了那些第三方库
# 推荐模块导入顺序：先导入标准模块、再导入第三方模块、最后导入自定义模块
