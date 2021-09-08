# codeing=utf-8

"""
@description:变量知识点练习
@author:zhangyanqing@
@date:2020-10-23
@version:python-3.7
"""

# Python语言常用的内置数据类型
# Number（数字）、String（字符串）、List（列表）、
# Tuple（元组）、Set（集合）、Dictionary（字典）
# Python中有3种不同的数字类型
# int（整型）、float（浮点型）、complex（复数类型）
# 整型数字包括正整数、0和负整数，不带小数点，无大小限制
# 不加任何前缀为十进制整数
# 加前缀0o为八进制整数
# 加前缀0x则为十六进制整数

# 十进制、8进制、16进制
a,b,c = 10,0o10,0x10
print(a)
print(b)
print(c)

# 使用bool函数可以将其他类型的数据转为Boolean类型，
# 当给bool函数传入下列参数时其将会返回False：
# 定义为假的常量，包括None或False任意值为0的数值，如0、0.0、0j等
# 空的序列或集合，如''（空字符串）、()（空元组）、[]（空列表）等

# 浮点型数字使用C语言中的double类型实现，可以用来表示实数
# 如3.14159、-10.5、3.25e3等
# 3.25e3是科学记数法的表示方式，其中e表示10，因此，3.25e3实际上表示的浮点数是3.25*103=3250.0
import sys
print(sys.float_info)

# 浮点型
# min和max是浮点数的最小值和最大值，dig是浮点
# 数所能精确表示的十进制数字的最大位数
# sys.float_info(max=1.7976931348623157e+308,max_exp=1024, max_10_exp=308,min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53,epsilon=2.220446049250313e-16, radix=2,rounds=1)

# 复数类型
# 复数由实部和虚部组成，每一部分都是一个浮点数，其书写方法如下
# a+bj或a+bJ
# 其中，a和b是两个数字，j或J是虚部的后缀，即a是实部、b是虚部

# 在生成复数时，也可以使用complex函数，其语法格式如下：
# complex([real[,imag]]
# 其中，real为实部值，imag为虚部值，返回值为real+imag*1j
print(complex(2,3))
# 如果省略虚部imag的值，则返回的复数为real+0j；如果实部real和虚部imag的值都省略，则返回的复数为0j
print(complex(2,))

c1,c2,c3,c4,c5=3+5.5j,3.25e3j,complex(5,-3.5), complex(5),complex()
print(c1)
print(c2)
print(c3)
print(c4)
print(c5)