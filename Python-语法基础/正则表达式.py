# 正则表达式：是一种用来匹配字符串的强有力的武器，设计思想是用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，就认为它“匹配”，否则就不匹配
# 行定位符、元字符、限定符、字符类、排除字符、选择字符、转义字符、分组
# 行定位符：^表示开始："^Hi" "HiPython"可匹配 $表示结束："Bye$" "^Hi,GoodBye"可匹配
# 元字符：在正则表达式中具有特殊意义的专用字符，如上面的两个行字符都是元字符、.匹配除换行外的任意字符(一个.代表一个字符)、\w匹配字母数字下划线或汉字、\W匹配字母数字下划线或汉字以外的字符、\s匹配任意的空白符、\b匹配单词的开始或结束、\d匹配数字
# 限定符：限制匹配数量
# 字符类：定义一个字符结合，匹配这个集合当中字符：[]  [aeiou]匹配元音  [\u4e00-\u9fa5]匹配任意一个汉字
# 排除字符：和字符类相反：[^a-zA-Z]
# 选择字符：或：用来表示符合这个条件或符合另一个条件 | [a-z]|[0-9]
# 转义字符：\ 把一个特殊的字符转换为一个普通字符(上面提到的那些字符)
# 分组：() (\.[0-9]{1,3}){3} 对(\.[0-9]{1,3})进行了重复三次的匹配
# 正则表达式模块 re
# 三种操作：匹配字符串、替换字符串、分割字符串
# 1.匹配字符串    match()、search()、findall()
# 语法：re.match(pattern(模式字符串), string(要匹配的字符串), [flags](标志位))
import re
pattern = r'mr_\w'    # 模式字符串
string = 'MR_SHOP mr_shop'    # 要匹配的字符串
match = re.match(pattern, string, re.I)    # 匹配字符串
print(match)
print("起始位置：",match.start())
print("结束位置：",match.end())
print("匹配数据：",match.group())
# 实例：判断是不是中国移动手机号码
import re
pattern = r'(13[4-9]\d{8})|(15[01289]\d{8})$'    # 模式字符串
mobile = '13634888888'    # 要匹配的模式号码
re.match(pattern, mobile)
if match == 'None':
    print ("不是有效手机号码")
    print (moblie)
else:
    print("是有效手机号码")
# 语法：re.search(pattern, string, [flags])    同match()
import re
pattern = r'mr_\w'    # 模式字符串
string = 'MR_SHOP mr_shop'    # 要匹配的字符串
match = re.search(pattern, string, re.I)    # 匹配字符串
print(match)
print("起始位置：",match.start())
print("结束位置：",match.end())
print("匹配数据：",match.group())
# 实例：黑客匹配
import re
pattern = r'(黑客)|(抓包)|(监听)|(Ttojan)'    # 模式字符串
about = '我是一名程序员，我喜欢看黑客方面的图书，想研究一下Trojan。'
match = re.search(pattern,about)
if match == None:
    print(about, "@ 安全！")    # 没有匹配成功
else:
    print(about, "@ 出现危险字符！")    # 匹配成功
about = '我是一名程序员，我喜欢看计算机网络方面的图书，想研究一下网址开发。'
match = re.search(pattern,about)
if match == None:
    print(about, "@ 安全！")    # 没有匹配成功
else:
    print(about, "@ 出现危险字符！")    # 匹配成功
# 语法：re.findall(pattern, string, [flags])    标志位同上面，返回值不一样，为列表
import re
pattern = r'mr_\w'    # 模式字符串
string = 'MR_SHOP mr_shop'    # 要匹配的字符串
match = re.findall(pattern, string, re.I)    # 匹配字符串
print(match)
print("起始位置：",match[0])
# 替换字符串
# 语法：re.sub(pattern(模式字符串), repl(用来进行替换的字符串), string(要查找的被替换的原始字符串), count(进行模式匹配后进行替换的最大次数), flags(标志位：控制匹配方式))
import re
pattern = r'1[34578]\d{9}'
string = "中奖号码：84918981 联系电话：13611111111"
result = re.sub(pattern, "1XXXXXXXXXX",string,0)    # 替换字符串
print(result)
# 实例：替换危险符号
import re
pattern = r'(黑客)|(抓包)|(监听)|(Trojan)'    # 模式字符串
about = '我是一名程序员，我喜欢看黑客方面的图书，想研究一下Trojan。'
match = re.sub(pattern,"@_@",about)
print(match)    # 输出替换结果
# 使用正则表达式分割字符串
# 语法：re.split(pattern, string, [maxsplit](最大拆分次数), [flags])    以列表形式返回
import re
pattern = r'[?|&]'
url = "http://Navigator97.github.io?uaername = mr & pwd = Navigator97"
result = re.split(pattern, url)    # 分割字符串
print(result)
# 实例：@好友
import re
str1 = "@Navigator @扎克伯格 @俞敏洪 @勤奋的天使"
pattern = r'\s*@'
list1 = re.split(pattern, str1)    # 使用空格或者单独的@符号进行分割
print("您@的好友为：")
for item in list1:
    if item != "":
        print(item)
