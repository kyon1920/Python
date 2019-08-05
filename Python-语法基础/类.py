# 面向对象和类：面向对象概述、类的定义和使用、属性(property)、继承
# 面向对象程序设计(Object Oriented Programming、OOP)

# 面向对象概述：核心概念：对象、类   三个特征：封装、继承、多态
# 对象：万物皆对象：由 属性(静态的) 和 方法(动态的) 组成
# 类：一组具有相似事物的统称
# 类和对象的关系与联系：对象是现实生活中存在的、而类是一种抽象，类可以衍生出对象
# 封装：把类的内部实现和使用分离开来，保留少数的接口供用户使用
# 继承：子类通过继承可以获得父类的属性和方法，并且可以重写或添加属性和方法，继承可以实现代码的重用
# 多态：多种形态，同种名字实现不同功能

# 类：定义类、创建类的实例、创建__init__()方法、创建类的成员并访问、访问限制
# 定义类：class关键字
# 语法：class ClassName:    ([惯例]驼峰式命名法：首字母大写、多字母首字母大写)
#           '''类的帮助信息'''
#           statement
class Geese:
    '''大雁类'''
    pass
    # 属性
    # 方法
# 创建类的实例：ClassName(parameterlist)
wildGeese = Geese()    # 创建大雁类的一个实例
print(wildGeese)
print(type(wildGeese))
# 创建__init__()方法 = 构造方法：创建类的实例的时候自动执行，在Python中只能有一个构造方法
class Geese:
    '''大雁类'''
    def __init__(s, name):
        print("我是一只小小雁,我叫：", name)
wildGeese = Geese("Navi")    # 创建实例

# 创建类的成员并访问：实例方法、数据成员
# 语法：def functionName(self, parameterlist):
#          block
# 调用：instanceName.functionName(parametervalue)
# 实例：创建大雁类并定义飞行方法、创建数据成员(类属性、实例属性)并访问：
# 类属性：在类中，并且方法体外所有实例之间共享
class Geese:
    '''大雁类'''
    neck = "脖子较长"    # 类属性(脖子)
    wing = "振翅频率高"    # 类属性(翅膀)
    leg = "腿位于身体的中心支点，行走自如"    # 类属性(腿)
    def __init__(self, name):
        print("我是一只小小雁,我叫：", name)
        # 输出类属性
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)
    def flying(self,state='正在休息'):    # 飞行方法
        print("飞行状态：",state)
wildGeese = Geese("Navi")
wildGeese.flying("在天空翱翔")    # 调用实例方法
wildGeese.flying()
# 实例
class Geese:
    '''大雁类'''
    neck = "脖子较长"    # 类属性(脖子)
    wing = "振翅频率高"    # 类属性(翅膀)
    leg = "腿位于身体的中心支点，行走自如"    # 类属性(腿)
    number = 0
    def __init__(self, name):
        print("我是一只小小雁,我叫：", name)
        # 输出类属性
        print(Geese.neck)
        print(Geese.wing)
        print(Geese.leg)
        Geese.number += 1
    def flying(self,state='正在休息'):    # 飞行方法
        print("飞行状态：",state)
wildGeese = Geese("Navi")
list1 = []
for i in range(4):
    list1.append(Geese("Navi"))    # 创建大雁类的实例
print("一共有%d只大雁！"%Geese.number)    # 输出大雁的只数
Geese.beak = "喙的基部较高，长度和头部几乎相等"    # 添加一个类属性
print(wildGeese.beak)
print(list1[2].beak)
# 实例属性：在类中，并且方法体内，只作用于当前实例，只能通过实例访问，不能通过类名进行访问
class Geese:
    '''大雁类'''
    def __init__(self, name):
        self.neck = "脖子较长"    # 实例属性(脖子)
        self.wing = "振翅频率高"    # 实例属性(翅膀)
        self.leg = "腿位于身体的中心支点，行走自如"    # 实例属性(腿)
        print("我是一只小小雁,我叫：", name, "下面是我的实例属性：")
        # 输出实例属性
        print(self.neck)    # 访问实例属性
        print(self.wing)
        print(self.leg)
geese = Geese("Navi")
print(geese.leg)    # 通过实例访问
geese.leg = "通过腿我可以行走"
print(geese.leg)    # 修改实例属性
geese.eat = "我喜欢吃虫子"    # 添加一个实例属性
print(geese.eat)

# 访问限制
# _foo(保护protected类型，只允许类本身和子类进行访问，实例名也可以访问)、__foo(私有类型的成员，只有类本身才能访问)、__foo__(系统定义的名字，特殊的方法)
class Swan:
    '''天鹅类'''
    _neck_swan = '天鹅的脖子很长'    # 保护类型的属性
    __leg_swan = "天鹅的腿也很长"
    def __init__(self):
        print("__init__():",Swan._neck_swan)    # 访问保护类型的属性
        print("__init__():",self.__leg_swan)    # 访问私有类型的属性
swan = Swan()
print("直接访问：",swan._neck_swan)    # 通过实例名访问受保护类型属性
# print("直接访问：",swan.__leg_swan)    # 通过实例名访问私有类型的属性    会出错
# 私有类型的可以通过 实例名._类名私有成员名 来进行访问，例如：
print("直接访问：",swan._Swan__leg_swan)    # 在类外访问私有成员

# 属性 property(也叫做装饰器)  != 类属性和实例属性：它是一种特殊的属性，访问计算后所得的值
# 创建用于计算的属性：@property 可以把一个方法转换为一个可用于计算的属性
# 语法：@property
#      def methodname(self):
#          block(return语句返回计算结果)
class Rect:
    def __init__(self,width,height):    # 构造方法
        self.width = width
        self.height = height
    @property
    def area(self):
        return self.width * self.height    # 计算矩形面积
rect = Rect(800,600)    # 创建类的实例
print("面积为：",rect.area)    # 加上装饰器后方法后面的()就可以去掉，相当于属性
# rect.area = 100    # 不能对property属性进行重新赋值    该语句错误
# 为属性添加安全保护机制：可以实现相当于私有类外读取却不能修改的功能
class TVShow:    # 电视节目类
    def __init__(self,show):
        self.__show = show
    @property
    def show(self):
        return self.__show    # 返回私有属性
tvshow = TVShow("正在播放《战狼2》")
print("默认：",tvshow.show)    # 获取私有属性值，但不能修改
# 通过装饰器为属性设定拦截器：允许对属性进行修改，但有一定的限制
class TVShow:    # 电视节目类
    list_film = ["《战狼2》","《红海行动》","《西游记之女儿国》","《熊出没之变形记》"]
    def __init__(self,show):
        self.__show = show
    @property
    def show(self):
        return self.__show    # 返回私有属性
    @show.setter
    def show(self,value):
        if value in TVShow.list_film:    # 判断值是否在列表中
            self.__show = "您选择了" + value + "，稍后将为您播放"    # 修改返回的值
        else:
            self.__show = "您点播的电影不存在！"
tvshow = TVShow("《战狼2》")
print("正在播放：",tvshow.show)    # 获取私有属性值，但不能修改
print("您可以从",TVShow.list_film,"中选择点播的电影")
tvshow.show = "《红海行动》"
print(tvshow.show)    # 获取属性值
tvshow.show = "《捉妖计2》"
print(tvshow.show)    # 获取属性值

# 继承：继承的基本语法、方法重写、在派生类当中调用基类的__init__()方法
# 继承的基本语法：class ClassName(baseclasslist):  '''类的帮助信息'''  statement
# 方法重写
# 再派生类中调用基类的__init__()方法：super().__init__()
# 实例：创建水果类，再创建它的子类
class Fruit:    # 水果 基类
    color = "绿色"    # 类属性
    def __init__(self,shape = "circle"):
        Fruit.shape = shape
    def harvest(self,color):
        print("水果是",color,"的")
        print("水果的形状是",Fruit.shape,"的")
        print("水果已经收获...")
        print("水果原来是",Fruit.color,"的")
class Apple(Fruit):
    color = "红色"
    def __init__(self):
        super().__init__()    # 调用基类的构造方法
        print("我是苹果")
    def harvest(self,color):    # 方法重写
        print("苹果是",color,"的")
        print("水果的形状是",Fruit.shape,"的")
        print("苹果已经收获...")
        print("苹果原来是",Fruit.color,"的")
class Orange(Fruit):
    color = "橙色"
    def __init__(self):
        super().__init__()    # 调用基类的构造方法
        print("我是橘子")
    def harvest(self,color):    # 方法重写
        print("橘子是",color,"的")
        print("水果的形状是",Fruit.shape,"的")
        print("橘子已经收获...")
        print("橘子原来是",Fruit.color,"的")
apple = Apple()    # 实例苹果的实例
apple.harvest(apple.color)    # 调用基类的harvest()方法
orange = Orange()    # 实例橘子的实例
orange.harvest(orange.color)    # 调用基类的harvest()方法
# 在派生类中定义了构造方法实例化对象是会执行派生类当中的构造方法，不会执行基类的构造方法，而如果在派生类中未定义构造方法，实例化对象时会执行基类的构造方法
