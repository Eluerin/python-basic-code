# --------------int、float、bool
# float：浮点数
# print(10/3)
# 小数：数据范围是无限的，
# 整数：在某个特定的区间内可以被表示的清楚
# 1~100000000

# 0~1
# 计算机是一个二进制的产品:0,1
# 计算机表示一个小数,会有误差

# bool:取值范围只有:True,False
# 基础数据类型的转换
# a = 10   # 数字转换bool,非0都是True,0是false
# b = bool(a)
# print(type(b))
# print(b)
# 可以用于循环

# while 1:        #死循环
#     print('pay me money')


# s = ''          # 在python中,所有非空字符串都是True,空字符串是False
# print(bool(s))

# 综上,在python中,表示空的都是False,非空的都是True
# lst = [0]
# print(bool(lst))

# ----------实例:利用bool判断来实现死循环的终结
# while 1:
#     content = input("Enter something: ")
#     if content:
#         print('content sent to jungle:', content)
#     else:
#         break
# -----------------------------------------


# -------------字符串
# 输出：我叫XXX,今年XXX岁，我喜欢做XXXX
# name = input("Enter your name: ")
# address = input("Enter your address: ")
# age = int(input("Enter your age: "))            # 注意一定要改变数据类型
# hobby = input("Enter your hobby: ")

# # # %s：表示字符串占位(万能占位)
# # # %d：表示数字占位（int）
# # # %f；表示小数占位（float）

# # 以下为三种字符串格式化的方法，推荐第三种
# s0 = 'I am %s' % name       # 只有一项，不用加括号
# s = 'I am %s, I live in %s, I am %d years old, I love %s' % (name, address, age, hobby)
# s1 = 'I am {}, I live in {}, I am {} years old, I love {}'.format(name, address, age, hobby)
# s2 = f'I am {name}, I live in {address}, I am {age} years old, I love {hobby}'   # f-string
# print(s2)
# # 字符串格式化↑

# -------------索引和切片
# 索引：按照位置提取元素
# s = 'I am Joy'
# # 可以采用索引的方式提取某一个字符（文字）
# print(s[2])     # 索引都是从0开始数
# print(s[0])
# print(s[-1])    # 表示倒数（第一）

# 切片：从一个字符串中提取一部分内容
# s = 'I am Joy, what your name?'
# print(s[1:9])  # , s[11:20])   # 空格占一个位置
# # 语法：s[start:end] 从start到end进行切片，但是取不到end [start,end）
# # 但是字符串的切片仍然是从0开始数的,(1:9,只会返回第2到第9,8个字符)
# print(s[:9])  # 如果start从开头进行切片，可以省略开头
# print(s[9:])  # 从start一直截取到末尾
# print(s[:])   # 表示开头到结尾
# print(s[-4:-1])     # 目前还是只能从左往右截取,截取不到末尾
# print(s[-1:-3])     # 截取不到结果

# 可以给切片添加步长,来控制切片的方向
# s = 'ILOVEYOU'
# print(s[::-1])
# 语法:s[start:end:step] 从start切到end,每step个单位出来一个元素
# s = 'abcdefghijklmnopqrstuvw'
# print(s[3:8:2])     # 输出:dfh
# print(s[-1:-10:-3])     # 输出:wtq

# --------------字符串的操作（不对原字符串造成影响）
# ----大小写转换
# s = 'python class'
# s1 = s.capitalize()         # 只会对整个字符串的第一个字母进行大写处理
# print(s1)

# s = 'I have a dream'
# s1 = s.title()                # 对每个单词的首字母都进行大写处理，即标题格式
# print(s1)

# s = 'I HAVE A DREAM'
# s1 = s.lower()                  # 对每个字母都进行小写处理
# print(s1)

# s = 'I have a dream'
# s1 = s.upper()                  # 对每个字母都进行大写处理
# print(s1)

# 如何忽略大小写进行判断(如验证码)
# verify_code = 'xDai'
# user_input = input(f'Enter the verify code ({verify_code}): ')
# if user_input.upper() == verify_code.upper():
#     print('verify code right')
# else:
#     print('verify code wrong')
#     user_input = input(f'Enter the verify code ({verify_code}): ')
# lower由于无法处理某些国家的字母,所以广泛应用upper

# 以下为代码改进版
# verify_code = 'xDai'
# user_input = input(f'Enter the verify code ({verify_code}): ')
# while 1:
#     if user_input.upper() == verify_code.upper():
#         print('verify code right')
#         break
#     else:
#         print('verify code wrong')
#         user_input = input(f'Enter the verify code ({verify_code}): ')
# 总结:input函数本来就有再次输入的意味在里面,但要实现输入错误一直显示互动,还得需要循环结构


# -----------替换和切割----------
# strip() 去掉字符串左右两侧的空白符（空格、\t、\n）
# s = '                   hello, I am joy      '
# s = s.strip()             # 可以合并
# print(s.strip())

# 案例
# username = input('please enter your username: ')
# password = input('please enter your password: ')
# if username.strip() == 'admin':                   # 说明了.strip()等函数的自由性，可以在定义变量时使用，也可以在判断时使用
#     if password.strip() == '123456':
#         print('login pass')
#     else:
#         print('login fail, password is wrong')
# else:
#     print('login fail, username is wrong')
# 防止输入多一个空格

# replace(old,new) 字符串替换
# I am   happy   today
# s = 'I am   happy   today'
# s1 = s.replace(' ','')
# print(s1)

# split(用什么切割) 字符串切割,用什么切割，就会损失掉谁
# a = 'python_java_c_c#_javascript'
# lst = a.split('_')   # 切割之后的结果会放在列表当中
# print(lst)
# lst = a.split('_java_')
# print(lst)

# -------------查找和判断-----------
# 查找
# s = 'hello, I am zhourunfa'
# ret = s.find('zhourunfa')     # 返回字符串的位置
# ret = s.find('zhourunfa12312')  # 返回是-1，没有该字符串出现
# ret = s.index('zhourunfa')
# ret = s.index('zhourunfa12312')   # 返回直接报错，没有该字符串出现
# print(ret)

# print('zhourunfa123132' in s)   # in可以做条件上的判断
# print('zhourunfa' not in s)     # not in 判断是否不存在

# 判断
# name = input('enter your name:')
# # 判断你是不是姓张
# if name.startswith('zhang'):        # .startswith(''):判断开头（几个字符），endswith:判断结尾
#     print('your lastname is zhang')
# else:
#     print('your lastname is not zhang')

# money = input("Enter your money: ")
# if money.isdigit():             # is.digit():判断字符串是否由整数组成
#     money = int(money)
#     print("Your money is", money)
# else:
#     print('sorry, your money is invalid')


# ------------补充和总结------
# s = 'skeffef'
# len(s)
# print(len(s))       #length() 长度

# join()                # '连接符'.join() 连接
# lst = ('zhaobenshan','wangdana','heitudaye','madashuai')
# # 用’_‘把列表中的对象连起来
# print(type(lst))
# s = '_'.join(lst)
# print(s)

'''
1、f’{变量}‘：格式化一个字符串
2、索引和切片：
    索引:从0开始，[]
    切片：s[satrt:end:step]，取不到end
3、相关操作：
    字符串操作对原字符串是不发生改变的
    3.1、upper（） 在需要忽略大小写的时候
    3.2、strip() 可以去掉字符串左右两端的空白符（空格、\t、\n）
    3.3、replace() 字符串替换
    3.4、split() 切割字符串
    3.5、join() 拼接一个列表中的内容成为新字符串
    3.6、startswith（） 判断字符串是否以xxx开头
    3.7、len() 字符串长度（内置函数）
4、字符串的循环和遍历
for c in s:
    print(c)
关于 in：
    4.1、判断xxx是否在xxxxx中出现了
    4.2、for循环
'''


# --------------列表-----------
# 能装东西的东西（用[]表示，列表中的元素通过，隔开）
# a = ['zhangsan','李四','zhangshaogang ',[1,2,3,True,]]
# 特性：
# 1、列表像字符串一样也有索引和切片
# 2、索引超过范围会报错
# 3、可以用for循环进行遍历
# 4、用len可以拿到列表的长度
# lst = ['lion','elephant','griffe','panda']

# print(lst[1])
# print(lst[1:4])               # 列表的切片：也是用0开始
# print(lst[::-1])
# print(lst[232])    #list index out of range
# for item in lst:
    # print(item)

# 列表的增删改查
# lst = []
# print(lst)
# 向列表中增加元素
# 1、.append()  追加
# lst.append('zhaobenshan')
# lst.append('zhaoshaogang')
# lst.append('zhangwuj')

# .insert()   插入
# lst.insert(0,'zhangwuj')

# .extend()   合并两个列表,批量添加
# lst.extend(['afd','crgh','ghth'])
# print(lst)

# acg = ['a','c','g']
# lst.extend(acg)
# print(lst)

# 删除(只能一个一个删除) .pop(index)、.remove('')
# lst = ['ghth', 'apple', 'pineapple', 'mango', 'ice cream', 'egg']
# ret = lst.pop(3)      # 给出被删除的索引,返回被删除的元素
# print(lst)
# print(ret)
# lst.remove('ghth',)      # 删除某个元素(*)
# print(lst)

# 修改
# lst[4] = 'kai'          # 直接用索引进行修改操作
# print(lst)

# 查询
# print(lst[4])           # 直接用索引进行查询操作

# 案例
# 把所有姓张的人修改成姓王
# lst = ['zhangwuji', 'zhangsanfeng', 'zhangshaogang', 'zhaobenshan', 'machao', 'zhaomin', 'yangguo', 'zhangjunbao']

# len(lst)列表的长度 ->  直接拿到列表索引的for循环
# i = 0
# for item in lst:
#     if item.startswith('zhang'):
#         lst[i] = item.replace('zhang','wang')         # 用item进行赋值
#     i += 1
#     if i > len(lst) - 1:           # for循环在遍历完会自动结束循环，加结束循环条件属于以防万一
#         break
# print(lst)

# 改进代码
# for i in range(len(lst)):
#     if lst[i].startswith('zhang'):
#         lst[i] = lst[i].replace('zhang', 'wang')
# print(lst)


# -------补充操作
# 排序
# lst = [1,2,3, 'mahuteng', 'wusong']   # 列表会按照存放元素的顺序保存
# lst.sort()      # 对列表进行升序排序(不支持对str和int之间的排序)
# lst.sort(reverse = True)    # reverse: 翻转
# print(lst)
# 排序不会同时对str和int进行操作

# 嵌套(查询)
# lst = ['abs', 'def', 'end', ['cola', 'breath', 'hamburger', 123]]
# 如何取出嵌套的元素（如breath）
# print(lst[3][1])    # 第一个[]：外层列表中的第四个元素，第二个[]：内层列表的第二个元素。以此类推。

# 将cola改成pizza，并将hamburger大写
# lst[3][0] = lst[3][0].replace('cola', 'pizza')      # 赋值的原因是，字符串操作不会改变原字符串，需要赋值
# lst[3][2] = lst[3][2].upper()
# # print(lst[3][0].replace('cola', 'pizza'))         # python“多线程”操作的例子
# print(lst)

# 列表的循环删除（**）
# lst = ['zhangwuji', 'zhangsanfeng', 'zhangshaogang', 'zhaobenshan', 'machao', 'zhaomin', 'yangguo', 'zhangjunbao']
# # 由于删除列表元素，导致索引错位，以至于遗漏本该删除的元素
# temp = []  # 准备一个临时表，负责存储要删除的内容
# for item in lst:
#     if item.startswith('zhang'):
#         temp.append(item)       # 把要删除的内容记录下来
#         # lst.remove(item)      #有bug(但不会报错)
#
# for item in temp:               # 去原列表中进行删除操作
#     lst.remove(item)
# print(lst)
# 安全稳妥的循环删除方式：
#   将要删除的内容保存在一个新列表中,循环新列表,删除原列表

# 思考,不借助空列表,能实现循环删除吗?
# lst = ['zhangwuji', 'zhangsanfeng', 'zhangshaogang', 'zhaobenshan', 'machao', 'zhaomin', 'yangguo', 'zhangjunbao']
# i = 0
# while i < len(lst):
#     if lst[i].startswith('zhang'):
#         lst.remove(lst[i])      #有bug(但不会报错)
#     else:
#         i += 1
# print(lst)
# 总结,可以用while循环来控制索引增减



# ------------tuple -----------
# t = ('zhangwuji', 'jiwuyue','zhaowuji')
# t1 = ['zhangwuji', 'jiwuyue','zhaowuji']
# print(t)
# print(t1[0:3])
# t[0] = 'jiwuxin'        # 'tuple object does not support item assignment
# print(t)

# 固定某些数据,不允许外界修改
# tuple如果只有一个元素(*),需要在元素末尾添加一个逗号
# t = ('hha')         #默认的优先级是str
# t = ('hha',)
# print(t)
# print(type(t))

# 关于元组的不可变(?),
# t = (1,2,3,['asd','ptsd'])      # 元组里面嵌套列表,列表里的内容可以改变
# t[3].append('apple')
# print(t)


# -----------set集合,set集合是无序的------------
# s = {}
# print(type(s))          # 空集合是 dict字典

# s = {1,'sjk',2,3}
# print(type(s))            # 当{}中有内容,才会返回类型set集合
# print(s)

# s = {1,2,3,'ptsd',(),[]}       # unhashable type 'lsit'
# print(s)
# unhashable:
# python中的set集合进行数据存储的时候,需要对数据进行hash计算,根据计算的hash值进行存储数据
#   set集合要求存储的数据必须是可以进行hash计算的
#  可以hash的数据类型:不可变的数据类型,
#  include: int,str,bool,tuple,
# 不包括: list,dict,set

# 向set中增添数据
# s = set()  # 创建空集合
# t = tuple()  # 空元组
# l = list()   # 空列表
# s1 = str()   # 空字符串
#
# print(s,t,l,s1)

# s.add('range')
# s.add('world')
# s.add('length')
# print(s)

# s.pop()    # 由于集合无需,测试时无法验证时最后一个
# s.remove('world')
# print(s)

# set的修改,需要先删除,再新增
# set的查询只能通过for循环
# for item in s:
#     print(item)

# set的交集、并集、差集
# s1 = {'刘能','赵四','谢广坤'}
# s2 = {'刘主任','赵老登','谢顶'}
# print(s1 & s2)      # 交集
# print(s1.intersection(s2))
#
# print(s1 | (s2))  # 并集
# print(s1.union(s2))
#
# print(s1 - s2)  # 差集
# print(s1.difference(s2))

# set作用：可以去除重复
# s1 = ['joy','kunl','caiyl','houpq','joy','caiyl']
# print(s1)
# print(set(s1))
# print(list(set(s1)))        # 去除重复之后的数据是无序的


# -------------dict字典--------------
# dic = {'fruit': 'apple', 'vegetable': 'tomato'}
# val = dic['vegetable']      # 用起来只是把索引换成了key
# print(val)
# print(dic['vegetable'])

# 字典的key必须是hashable的数据类型
# 字典的value可以是任何数据类型
# dic = {[]:123}
# print(dic)

# dic = {'app':['ios', 'android', 'homos']}
# print(dic['app'])

# 字典的增删改查
# dic = dict()            # 空字典
# dic['jay'] = '周杰伦'
# dic[1] = 1234
# print(dic)

# dic['jay'] = '扁嘴伦'      # 此时,字典中已经有了jay,此时执行的就是修改操作了
# print(dic)

# dic.setdefault('tom','jerry')   # 设置默认值,如果以前有了tom,setdefault就会失去作用.
# print(dic)
# dic.setdefault('tom','garfield')   # 设置默认值,如果以前有了tom,setdefault就会失去作用.
# print(dic)

# 删除
# dic.pop('jay')
# print(dic)

# del dic['jay']
# print(dic)

# 查询
# print(dic['tom'])
# print(dic['jay323'])    # 如果key不存在,程序会报错;当确定key值时可以使用
# print(dic.get('jay'))
# print(dic.get('jay'))   # 如果key不存在,会返回none

# None:空类型
# a = None
# print(a)        # 空值,不能进行任何操作(区别于‘none’)
# print(type(a))

# s = ''          # 空字符串

# 例:
# dic = {
#     'zhaosi':'歪嘴',
#     'liuneng':'结巴',
#     'guangkun':'作妖',
#     'dajiao':'寡妇'
# }
# name = input('please enter name:')
# val = dic.get(name)
# if val is None:
#     print('our village do not have this person')
# else:
#     print(val)

# 字典的循环遍历 :可以用for循环,直接拿到key
# for key in dic:
#     print(key,dic[key])

# 2、希望把所有的key\value保存在一个列表中
# print(list(dic.keys()))
# print(list(dic.values()))

# 3、直接拿到字典中的key和value
# print(list(dic.items()))            # .items()函数：返回元组
# for item in dic.items():
#     # print(item)
#     # print(type(item))
#     key = item[0]
#     value = item[1]
#     print(key, value)

#改进
# a, b = (1,[2,3.4])
# 元组、列表都可执行的操作，该操作称为解构（解包）
# 将元组、列表中的元素分别赋值给不同的对象(但变量数量和元素数量必须要对应)
# print(a)
# print(b)
#
# a,b = 1,2
# print(a)
# print(b)
#
# a,b = [1,2]
# print(a)
# print(b)
# 所以，通过元组的解包，实现“直接拿到字典中的key和value”
# for item in dic.items():
#     key,value = item
#     print(key,value)

# 甚至直接通过.items（）函数直接取值
# for key,value in dic.items():
#     print(key,value)

# 字典的嵌套：
# wangfeng = {
#     'name':'wangfeng',
#     'age':18,
#     'hobby':'song',
#     'wife':{
#         'name':'zhangziyi',
#         'hobby':'dance',
#         'assistant':{
#             'name':'dazhangwei',
#             'age':34,
#             'hobby':'art'
#         }
#     },
#     'children':[
#         {'name':'wangyuan','age':0},
#         {'name':'wangxi','age':2}
#     ]
# }

# # 汪峰妻子的助手的爱好
# print(wangfeng['wife']['assistant']['hobby'])
# # 汪峰孩子1的名字
# print(wangfeng['children'][0]['name'])
# # 给汪峰的孩子2加一岁
# wangfeng['children'][1]['age'] = wangfeng['children'][1]['age'] + 1
# print(wangfeng['children'][1]['age'])

# 补充：字典的循环删除(构建临时列表)
# temp = []
# for key in dic:
#     if key.startswith('zhao'):
#         temp.append(key)
# for item in temp:   # 循环列表temp，删除字典中的内容
#     dic.pop(item)
# print(dic)


# -------字符集和编码-----------
# print(2**16)

# -------bytes---------
# s = '周杰伦'
# bs1 = s.encode('gbk')  # b'xxxx'bytes类型
# bs2 = s.encode('utf-8')
# print(bs1)
# print(bs2)

# 如何将gbk的字节转化为utf-8的字节
# bs = b'\xd6\xdc\xbd\xdc\xc2\xd7'
# 先变成文字符号（字符串）
# s = bs.decode('gbk')    # 解码
# bs2 = s.encode('utf-8')     #重新编码
# print(bs2)

# 1、str.encode('编码')  进行编码
# 2、str/decode('编码')  进行解码
# 3、程序员创建文件多用utf-8
# 4、编码类型不同也是乱码的原因

#英文可以被ascll码所识别
# s = '你好abc呵呵哒'
# print(s.encode('utf-8'))

# s = 'abcdefg'
# print(s.encode('gbk'))


