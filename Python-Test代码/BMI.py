# _*_ coding:utf-8 _*_ 
#coding=utf-8
'''
 @ 版权所有 重庆市XX科技有限公司◎版权所有
 @ 文件名：BMI.py
 @ 创建日期：2019/7/13
 @ 创建人：zhangshao
 @ 修改标识：2019/7/14
 @ 修改描述：增加根据BMI指数判断身材是否合理功能代码
 @ 修改日期：2019/7/14
'''
def fun_bmi():
    print('''根据身高、体重计算BMI指数''')
    # 输入身高和体重
    height=float(input("请输入您的身高:"))
    weight=float(input("请输入您的体重:"))

    bmi=weight/(height*height)    # BMI指数=体重/身高的平方

    print("您的BMI指数为："+str(bmi))

    if bmi<18.5:
        print("您的体重过轻 ~@_@~")
    elif bmi<24.9:
        print("正常范围，注意保持 (-_-)")
    elif bmi<29.9:
        print("您的体重过重 ~@_@~")
    else:
        print("肥胖 ~@_@~")
