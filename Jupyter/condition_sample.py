# codeing=utf-8

"""
@description:条件知识点练习
@author:zhangyanqing@
@date:2020-11-1
@version:python-3.7
"""

a = 1
b = 2
c = 4
if a < b:
    print("a is less than b")
else:
    print("a is greater than b")


a = 1
b = 2
c = 3
if a > b:
    print("a is greater than b")
elif c > a:
    print("c is greater than a")
else:
    print("other")

a = 1
b = 2
c = 3
if a < b < c:
    print("a is less than b ,b is less than c")
else:
    print("other")

a = 1
b = 2
c = 3
if a < b > c:
    print("a is less than b ,b is less than c")
else:
    print("other")

