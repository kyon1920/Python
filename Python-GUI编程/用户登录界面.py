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
