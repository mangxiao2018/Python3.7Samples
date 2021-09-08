# codeing=utf-8

"""
@description:循环知识点练习
@author:zhangyanqing@
@date:2020-11-1
@version:python-3.7
"""

# 不用break的处理办法
stop = True

while stop:
    a = int(input('请输入一个数字:'))
    if a == 1:
        stop = False
    else:
        pass

# 使用break的处理办法
stop = True

while stop:
    a = int(input('请输入一个数字:'))
    if a == 1:
        break
    else:
        pass

data_template = [1,2,3,4,5,6,7,23,4245,213,8,9,10]
for i in data_template:
    print(i)
    print("n~b~")
print("for loop end.")

# 注意range(a,b)相当于 [a,b)左闭右开
for i in range(1,10):
    print(i)

# 嵌套循环
# 经典案例：乘法口诀
for n in range(1,10):
    for m in range(1,n + 1):
        print(f'{n} * {m} = {n * m}',end=' ')
    print()