
# pass
# print('hello world')
# # 1、IDLE交互窗口运行代码
# # 2、cmd中，输入；python
# '''
# 多行注释
# 单行注释
# '''
# # 下划线
# name_of_teacher = '乔峰'
# # 驼峰
# NameOfTeacher = '玉竹'

# name = '埃拉斯基'
# print(name)
# print("name")

# a = True
# print(a)

# a = input('please input content')
# b = input('please input content')
# print(a+b)
# print(type(a+b))
# a = bool(a)
# 类型转换函数int 、str、float、bool
# print(a)
# print(type(a))


# --------条件语句---------
# --------第一种-----------
# money = 500
# if money > 700:
#     print(123)
#     print(456)
# # python利用缩进符来判断条件语句的执行范围
# print(789)
# # 不加缩进的与条件判断无关

# ---------第二种------------
# money = input('please input your money')
# money = int(money)
#
# if money >500:
#     print('surf on internet')
# else:
#     print('go home')

# ---------第三种------------
# money = int(input('please input your money:'))
# if money > 1000:
#     if money > 1500:
#         print('foot massage')
#     else:
#         print('surf on internet')
# else:
#     print('go home')

# ----------第四种------------
# money = int(input('please input your money'))
#
# if money > 1000:
#     print(0)
# elif money > 500:
#     print(1)
# elif money > 200:
#     print(2)
# else:
#     print(3)

# else和elif不能单独使用


# ----------循环语句---------
# ---------while循环---------
# while True:     #死循环

# 用程序数数，从1~100
# i =1
# while True:
#     print(i)
#     i = i + 1

# i = 0
# while i <= 100:
#     print(i)
#     i += 1  # i += 1 与 i = i + 1  的效果一样

# 例题：从1+...+100 = ?
# i = 1
# count = 0
# while i <= 100:
#     count = i + count    #累加
#     i = i + 1
# print(count)

# 例题：1-2+3-4+.....-100 = ?
# i = 1
# count = 0
# while i <= 100:
#     if (i%2) == 0:         #==表示判断两个是否一致
#         count = count - i
#         i = i + 1
#     else:
#         count = count + i
#         i =i + 1
# print(count)
#

# break与continue的应用
# while True:
#     content = input("Enter content you want（enter q to break）: ")
#     if content == 'q':
#         break               #循环结束
#     print('seng to the beneath:',content)
# break：让循环立即停止
# continue：停止当前本次循环，持续下次循环

# i = 1
# while i <= 10:
#     if i == 4:
#         i += 1  # 如果不加这句，i会因为一直等于4，而中止循环
#         continue    # 停止当前本次循环，继续执行下次循环
#     print(i)
#     i += 1


# --------for循环-------

# s = 'hello,I am selia'
#
# for c in s:
#     print('result for this circulation:',c)

# for i in range(10):
#     print(i)

# for i in range(1,11):
#     print(i)

# i = 1
# while i <= 10:
#     print(i)
#     i += 2

# for i in range(1,11,2):
#     print(i)

# a = 10
# if a > 100:
#     pass
