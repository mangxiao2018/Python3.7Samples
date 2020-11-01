# codeing=utf-8

"""
@description:身份运算符&成员运算符知识点练习
@author:zhangyanqing@
@date:2020-10-31
@version:python-3.7
"""

# 身份运算用于比较两个对象是否对应同样的存储单元。
"""
程序在运行时，输入数据和输出数据都是存放在内存中。内存中的一个存
储单元可以存储一个字节的数据，每个存储单元都有一个唯一的编号，称
为内存地址。根据数据类型不同，其所占用的内存大小也不同。一个数据
通常会占据内存中连续多个存储单元，起始存储单元的地址称为该数据的
内存首地址。利用id函数可以查看一个数据的内存首地址。
x is y等价于id(x)==id(y)，即判断x和y的内存首地址是否相同；x is not y等
价于id(x)!=id(y)，即判断x和y的内存首地址是否不相同。
"""

x,y=15,15
print(x is y) #输出“True”
print(x is not y) #输出“False”
print(x is 15) #输出“True”
x,y=[1,2,3],[1,2,3]
print(x is y) #输出“False”
print(x==y) #输出“True”
print(x is [1,2,3]) #输出“False”
x=y
print(x is y) #输出“True”

# 使用成员运算符判断一个数据是否是字典中的元素，实际上就是判断该数据是否是字典中某个元素的键。
x,y=15,['abc',15,True]
print(x in y) #输出“True”
x=20
print(x not in y) #输出“True ”
y=(20,'Python')
print(x in y) #输出“True ”
x,y='Py','Python'
print(x in y) #输出“True ”
x,y=20,{15,20,25}
print(x in y) #输出“True ”
x,y='one',{'one':1,'two':2,'three':3}
print(x in y) #输出“True ”
print(1 in y) #输出“False ”
