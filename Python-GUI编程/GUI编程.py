# GUI编程
# 什么是GUI：它的全称是 Graphical User Interface 图形用户界面，与之对应的是CMI 它的全称是command-line interface 命令行界面
# 安装wxPython：只需在cmd中输入一行命令pip install -U wxPython即可
# 在安装时出现超时是因为安装源是国外网站，只需要切换一下就好：pip install -i https://pypi.doubanio.com/simple/ --trusted-host pypi.doubanio.com wxpython
# 升级wxPython：python -m pip install --upgrade pip
# 官方文档地址：https://wxpython.org/pages/overview/
# wxPython官方网站：https://wxpython.org/

# 示例：在官方文档中的hello-world示例
# First things, first. Import the wxPython package.
import wx
# Next, create an application object.
app = wx.App()
# Then a frame.
frm = wx.Frame(None, title="Hello World")
# Show it.
frm.Show()
# Start the event loop.
app.MainLoop()

# 常用的GUI框架：wxPython pyQt Kivy Flexx Tkinter

# 创建应用程序
# 应用程序对象：管理主事件循环  通过app=wx.App()来创建一个应用程序对象，对于复杂的程序可以用子类来继承wx.App()类
# 顶级窗口对象：管理数据，控制并呈现给用户  调用 frame=wx.Frame()来创建一个顶级窗口对象
# 应用程序对象和顶级窗口对象的关系：如下图

# 创建wx.App的子类
# 实现步骤：定义子类(继承wx.App)→定义Onlnit()(创建Frame顶级窗口)初始化方法→创建实例→调用实例的MainLoop()方法
# 创建实例：
import wx    # 导入wxpython
class App(wx.App):    # 定义一个子类
    def OnInit(self):
        frame = wx.Frame(parent=None,title="Hello wxPython")    # 因为是顶级窗口，所以没有父窗口None
        frame.Show()    # 顶级窗口的Show方法
        return True
if __name__ == '__main__':    # 以主程序的形式运行
    app = App()    # 实例化该子类
    app.MainLoop()    # 调用主循环方法

# 使用wx.Frame框架(窗口)
# wx.Frame()语法：见下图
# 实例：
import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title='创建Frame',pos=(500,500),size=(300,300))    
if __name__ == '__main__':
    app1 = wx.App()
    frame1 = MyFrame(parent=None,id=-1)
    frame1.Show()
    app1.MainLoop()

# 直接使用wx.App类
import wx
app2 = wx.App()
frame2 = wx.Frame(None,title="Hello wxPython")
frame2.Show()
app2.MainLoop()

# 窗口中的常用控件：文本、按钮、输入框、单选框、多选框......
# 首先需要画一个画板，在画板中我们才能做相应的操做，如添加控件，画图象等
# wx.Panel(self)是一个画板
# 文本控件：StaticText文本类  wx.StaticText()
# 步骤：创建窗口→设置画板，使其铺满整个窗口→在画板窗口部分添加画板

# wx.StaticText()语法格式：见下图
# 实例：使用wx.StaticText输出Python之禅
# 使用font = wx.Font(...)和title.setFont(font)函数来设置字体
string = '''
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
class MyFrame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self,parent,title = "Python之禅", pos = (200,100), size = (600,600))
        panel = wx.Panel(self)
        font = wx.Font(16,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        title = wx.StaticText(panel,label='Python之禅——Tim Peters',pos = (100,20))
        title.SetFont(font)
        font1 = wx.Font(14,wx.DEFAULT,wx.FONTSTYLE_NORMAL,wx.NORMAL)
        title1 = wx.StaticText(panel,label=string,pos = (100,40))
        title1.SetFont(font1)
if __name__ == '__main__':
    app3 = wx.App()
    frame3 = MyFrame(parent = None, id = -1)
    frame3.Show()
    app.MainLoop()

# TextCtrl输入文本类
# 可以输入单行多行文本，还可以实现密码输入控件
# 语法格式如下图
# 实例：实现用户登录
import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title='用户登录',pos=(100,100),size=(400,300))
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel,label="请输入用户名和密码",pos=(140,20))
        self.label_user = wx.StaticText(panel,label = '用户名',pos=(50,50))
        self.text_user = wx.TextCtrl(panel,pos=(100,50),size=(235,25),style=wx.TE_LEFT)
        self.label_password = wx.StaticText(panel,label='密码',pos=(50,90))
        self.text_password = wx.TextCtrl(panel,pos=(100,90),size=(235,25),style=wx.TE_PASSWORD)
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
    
# Button按钮类
# 语法格式如下图
# 实例：在上面的代码中添加确定和取消按钮
import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title='用户登录',pos=(100,100),size=(400,300))
        panel = wx.Panel(self)
        self.title = wx.StaticText(panel,label="请输入用户名和密码",pos=(140,20))
        self.label_user = wx.StaticText(panel,label = '用户名',pos=(50,50))
        self.text_user = wx.TextCtrl(panel,pos=(100,50),size=(235,25),style=wx.TE_LEFT)
        self.label_password = wx.StaticText(panel,label='密码',pos=(50,90))
        self.text_password = wx.TextCtrl(panel,pos=(100,90),size=(235,25),style=wx.TE_PASSWORD)
        # 创建确定和取消按钮
        self.bt_confirm = wx.Button(panel,label='确定',pos=(105,130))
        self.bt_cancle = wx.Button(panel,label='取消',pos=(195,130))
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(parent=None,id=-1)
    frame.Show()
    app.MainLoop()

# Sizer布局：可以保持窗体的布局以适应窗体的改变，以上布局做不到
# 什么是BoxSizer：它是垂直列(VERTICAL)或者水平行(HORIZONTAL)布局

# 使用BoxSizer布局
# 创建BoxSizer：sizer = wx.BoxSizer(wx.VERTICAL(竖直方向)/HORIZONTAL(水平方向))
# 添加控件：sizer.Add()
# 面板中设置Sizer：panel.SetSizer(sizer)
# 实例：
import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="用户登录",pos=(100,100),size=(500,500))
        panel4 = wx.Panel(self)
        self.title = wx.StaticText(panel4,label="请输入用户名和密码")
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER,border=25)
        panel4.SetSizer(vsizer)
if __name__ == '__main__':
    app4 = wx.App()
    frame4 = MyFrame(parent=None,id=-1)
    frame4.Show()
    app4.MainLoop()
# 实例：使用BoxSizer设置登录界面布局
import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="用户登录",pos=(100,100),size=(400,300))
        panel5 = wx.Panel(self)
        # 创建按钮
        self.bt_confirm = wx.Button(panel5,label="确定")
        self.bt_cancel = wx.Button(panel5,label="取消")
        # 创建文本
        self.title = wx.StaticText(panel5,label="请输入用户名和密码")
        self.label_user = wx.StaticText(panel5,label="用户名：")
        self.text_user = wx.TextCtrl(panel5,style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel5,label="密　码：")
        self.text_pwd = wx.TextCtrl(panel5,style=wx.TE_PASSWORD)
        # 创建横行容器
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user,proportion=0,flag=wx.ALL,border=5)
        hsizer_user.Add(self.text_user,proportion=1,flag=wx.ALL,border=5)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd,proportion=0,flag=wx.ALL,border=5)
        hsizer_pwd.Add(self.text_pwd,proportion=1,flag=wx.ALL,border=5)

        hsizer_botton = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_botton.Add(self.bt_confirm,proportion=0,flag=wx.ALL,border=5)
        hsizer_botton.Add(self.bt_cancel,proportion=0,flag=wx.ALL,border=5)

        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER,border=15)
        vsizer_all.Add(hsizer_user,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)
        vsizer_all.Add(hsizer_pwd,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)
        vsizer_all.Add(hsizer_botton,proportion=0,flag=wx.ALIGN_CENTER|wx.TOP,border=15)
        panel5.SetSizer(vsizer_all)
        
if __name__ == '__main__':
    app5 = wx.App()
    frame5 = MyFrame(parent=None,id=-1)
    frame5.Show()
    app5.MainLoop()

# 事件处理
# 什么是事件：用户在GUI组件上进行的操作都可以叫做事件，比如：按下按钮、输入文字、关闭窗口
# 绑定事件
# 语法格式：例在确定按钮上绑定事件bt_confirm，Bind(wx.EVT_BUTTON,OnclickSubmit(函数，当事件发生时执行函数))，可以参考官方手册
# 实例：使用事件判断用户登录
import wx
class MyFrame(wx.Frame):
    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,title="用户登录",pos=(100,100),size=(400,300))
        panel5 = wx.Panel(self)
        # 创建按钮
        self.bt_confirm = wx.Button(panel5,label="确定")
        self.bt_confirm.Bind(wx.EVT_BUTTON,self.OnClickSubmit)
        self.bt_cancel = wx.Button(panel5,label="取消")
        self.bt_cancel.Bind(wx.EVT_BUTTON,self.OnClickCancel)
        # 创建文本
        self.title = wx.StaticText(panel5,label="请输入用户名和密码")
        self.label_user = wx.StaticText(panel5,label="用户名：")
        self.text_user = wx.TextCtrl(panel5,style=wx.TE_LEFT)
        self.label_pwd = wx.StaticText(panel5,label="密　码：")
        self.text_pwd = wx.TextCtrl(panel5,style=wx.TE_PASSWORD)
        # 创建横行容器
        hsizer_user = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_user.Add(self.label_user,proportion=0,flag=wx.ALL,border=5)
        hsizer_user.Add(self.text_user,proportion=1,flag=wx.ALL,border=5)
        hsizer_pwd = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_pwd.Add(self.label_pwd,proportion=0,flag=wx.ALL,border=5)
        hsizer_pwd.Add(self.text_pwd,proportion=1,flag=wx.ALL,border=5)

        hsizer_botton = wx.BoxSizer(wx.HORIZONTAL)
        hsizer_botton.Add(self.bt_confirm,proportion=0,flag=wx.ALL,border=5)
        hsizer_botton.Add(self.bt_cancel,proportion=0,flag=wx.ALL,border=5)

        # 创建纵向容器
        vsizer_all = wx.BoxSizer(wx.VERTICAL)
        vsizer_all.Add(self.title,proportion=0,flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER,border=15)
        vsizer_all.Add(hsizer_user,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)
        vsizer_all.Add(hsizer_pwd,proportion=0,flag=wx.EXPAND|wx.LEFT|wx.RIGHT,border=45)
        vsizer_all.Add(hsizer_botton,proportion=0,flag=wx.ALIGN_CENTER|wx.TOP,border=15)
        panel5.SetSizer(vsizer_all)

    def OnClickSubmit(self, event):
        message = ""
        username = self.text_user.GetValue()    # 获取text_user的值
        password = self.text_pwd.GetValue()    # 获取text_pwd的值
        if username == "" or password == "":
            message = "用户名或密码不能为空"
        elif username == "Navigator" and password == "zhangshao976":
            message = "登录成功"
        else:
            message = "用户名和密码不匹配"
        wx.MessageBox(message)    # 弹窗
    def OnClickCancel(self,event):
        self.text_user.SetValue("")
        self.text_pwd.SetValue("")
        
if __name__ == '__main__':
    app5 = wx.App()
    frame5 = MyFrame(parent=None,id=-1)
    frame5.Show()
    app5.MainLoop()
