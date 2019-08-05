# 运算符/操作符
# 主要有 算术运算符、赋值运算符、比较运算符/关系运算符、逻辑运算符、位运算符

# 算术运算符：用来进行四则运算 + - * / %(求余)
# %(求余) 它的符号是和除数的符号一致的
a = 36
b = 5
print("36/5 = ",36/5)    # 除法
print("36*5 = ",36*5)    # 乘法
print("36%5 = ",36%5)    # 求余
print("36%-5 = ",36%(-5))
print("-36%-5 = ",(-36)%(-5))
# 运用/来进行除法运算得到浮点数、运用//来进行除法运算得到整数
# 示例：求平均成绩
python = 95
english = 92
c = 89
sub = python - english
print("python与english的分差：",sub)
avg = (python+english+c)/3
print("三门课程的平均成绩：",avg)

# 赋值运算符 = += -= *= /= %= (后面5个运算符的意思是先将表达式进行相应计算后执行赋值操作)
# age += 1 等价于 age + 1 = age
age = 18
print("age的值：", age)
age += 1
print ("执行+=1后的结果：", age)
age *= 2
print ("执行+=1后再执行*=2的结果：", age)

# 比较运算符：==、!=、>、<、>=、<=  结果有真(True)、假(False)
# 实例：
python = 95
english = 92
c = 89
print ("python:", python ," english:", english ," c:", c)
print ("python > english:", python > english)
print ("python < english:", python < english)
print ("python >= english:", python >= english)
print ("python <= english:", python <= english)
print ("python == c:", python == english)
print ("python != c:", python != english)
# 当判断一个变量是否介于两个值之间时，可以采用“值1<值2<值3”的形式
n = 20
print ("n:", n)
print ("10 < n < 50:",10 < n < 50)

# 逻辑运算符：与and(一假则假)、或or(一真则真)、非!(假变真、真变假)
# 实例：手机店打折活动
print ("\n******手机店打折活动进行中******")
strWeek = input("请输入星期(如：星期一)：")    # 输入星期
intTime = int(input("请输入小时(0-23)："))    # 输入时间
if (strWeek == "星期二" and (intTime >= 10 and intTime <= 11) or strWeek == "星期五" and (intTime >= 14 and intTime <= 15)):
    print("恭喜你，获得折扣参与资格，快快选购吧~")
else:
    print("对不起，您来晚一步，期待下次活动！")

# 位运算符：把数字看作二进制数来进行计算的 采用补码有符号位表示
# 位与&(有0即0)、位或|(有1即1)、位取反~(0变1、1变0)、位异或^(全0或全1才为0)、位左移<<、位右移>>
# 实例：密码转换问题
pwd = input("请输入密码：")
print ("原密码：", pwd)
key = input("请输入密钥：")
passwd = int(pwd) ^ int(key)
print ("加密后：", passwd)
print ("解密后：", passwd ^ int(key))
# 左移位运算<<：向左移动指定的位数，左边溢出位被丢弃，右边的空位用0补充，相当于*2的n次幂
# 右移位运算>>：向右移动指定的位数，右边溢出位被丢弃，最高为1空位添1，为0空位添0，相当于/2的n次幂
# 步骤：先转换为二进制数，按照上面规则进行移位
number = 32
print ("左移一位：", number>>1)
print ("右移一位：", number<<1)

# 运算符优先级
# Python运算规则：优先级高的运算先执行，优先级低的运算后执行，同一优先级的操作按照从左向右顺序执行
# 可以用()改变优先级次序
