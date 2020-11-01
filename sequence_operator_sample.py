# codeing=utf-8

"""
@description:序列运算符&运算符优先级知识点练习
@author:zhangyanqing@
@date:2020-11-1
@version:python-3.7
"""

x,y=[12,False],['abc',15,True]
z=x+y #x和y拼接后的结果赋给z
print(z) #输出“[12, False, 'abc', 15, True]”
s1,s2='我喜欢学习','Python'
s=s1+s2 #s1和s2拼接后的结果赋给s
print(s) #输出“我喜欢学习Python”
x_3=x*3 #将序列x的元素重复3次，生成一个新序列并赋给x_3
print(x_3) #输出“[12, False, 12, False, 12, False] ”
s_3=s*3 #将字符串s重复3次，生成一个新字符串并赋给s_3
print(s_3) #输出“我喜欢学习Python我喜欢学习Python我喜欢学习Python

# 在一个表达式中，通常会包含多个运算，这就涉及到了运算的顺序，其由两个因素确定：运算符的优先级和运算符的结合性。