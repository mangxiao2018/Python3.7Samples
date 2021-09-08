# codeing=utf-8

"""
@description:运算符知识点练习
@author:zhangyanqing@
@date:2020-10-31
@version:python-3.7
"""

a = 1
b = 2
c = 3
print("a + b :", a + b)
# / 除法，不是整除
print("a / b :",a / b)
print("c - a :",c - a)
print("b * c :",b * c)
# ** 幂次方
print("b**2 :",b**2)
# 按位异或运算符：当两对应的二进位相异时，结果为1
print("b^2 :",b^2)
# % 取模 - 返回除法的余数
print("c % b :",c % b)
# // 取整除 - 向下取接近商的整数
print("c // b :", c // b)


i1,i2=10,3
f1,f2=3.2,1.5
c1,c2=3+4.1j,5.2+6.3j
print(i1+i2) #输出“13”
print(c1-c2) #输出“(-2.2-2.2j) ”
print(f1*f2) #输出“4.800000000000001”
print(i1/i2) #输出“3.3333333333333335”
print(i1//i2) #输出“3”
print(i1%i2) #输出“1”
print(-f1) #输出“-3.2”
print(+f2) #输出“1.5”
print(i1**i2) #输出“1000”
