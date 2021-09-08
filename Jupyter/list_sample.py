# codeing=utf-8

"""
@description:变量知识点练习
@author:zhangyanqing@
@date:2020-10-31
@version:python-3.7
"""

# List（列表）是Python中一种非常重要的数据类型。
# 列表中可以包含多个元素，且元素类型可以不相同。
# 每一元素可以是任一数据类型，包括列表（即列表嵌套）及后面要介绍的元组、集合、字典。
# 所有元素都写在一对方括号“[]”中，每两个元素之间用逗号分隔。
# 对于不包含任何元素的列表，即[]，称为空列表。

# 与字符串相同，利用下标“[]”可以从已有列表中取出其中部分元素形成一个新列表，其语法格式为：
# ls[beg:end] 其中，beg是要取出的部分元素在ls中的起始下标，end是要取出的部分元素在ls中的结束下标。
# 省略beg，则表示从ls中的第一个元素开始，等价于ls[0:end]；省略end，则表示要取出的部分元素从beg位置开始一直到最后一个元素（包括最后一个元素）；beg和end都省略则取出ls中的所有元素。

# 访问单个元素s[beg:end]返回的仍然是一个列表；而ls[idx]返回的是列表中的一个元素。
# 对于ls=[1, 2.5, 'test', 3+4j,True, [3,1.63], 5.3]，通过“ print(ls[2:3]) ” 和“print(ls[2])“输出的结果分别是 “ ['test'] “ 和“test“。
# ls[2:3]返回的是只有一个字符串元素'test'的列表，而ls[2]返回的则是ls中第3个元素的值（即字符串'test'）。

a_list = [1, 2, 3, 4, 2, 3, 5]
b_list = ['a', 'b', 'c', 'd']
c_list = ["a", "b", "c", "d"]
d_list = ['Google', 'Runoob', 1997, 2000]

print("--------------------------------------------------------------------------")
# 直接打印
for a in a_list:
    print(a)

print("--------------------------------------------------------------------------")
# 通过index打印
for i in range(len(b_list)):
    print(b_list[i])

print("--------------------------------------------------------------------------")

print(c_list[2])
print(d_list[:2])
print(a_list[2:5])

print("--------------------------------------------------------------------------")

# 更新列表
print("更新前d_list[1]：", d_list[1])
d_list[1] = 'Baidu'
print("更新后d_list[1]：", d_list[1])

print("--------------------------------------------------------------------------")

# 删除列表中元素
print("删除前d_list：", d_list)
del d_list[1]
print("删除后d_list：", d_list)

print("--------------------------------------------------------------------------")

# 多维列表
e_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(e_list)
# 行与列下标都是从0开始的
print(e_list[1][1])

print("--------------------------------------------------------------------------")

# len(list) 列表元素个数
print(len(e_list))
print(len(a_list))

# max(list) 返回列表元素最大值
print(max(a_list))

# min(list) 返回列表元素最小值
print(min(a_list))

# 将元组转换为列表
x_tuple = (1, 2, 3, 4)
l = list(x_tuple)
print(l)

print(" list.append--------------------------------------------------------------------------")

# list.append(obj) 在列表末尾添加新的对象
d_list.append(23)
print("d_list:", d_list)

print("list.count--------------------------------------------------------------------------")

# list.count(obj) 统计某个元素在列表中出现的次数
print("a_list`s 2 count:", a_list.count(2))

print("list.extend--------------------------------------------------------------------------")

# list.extend(seq) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
y_tuple = ('oa', 'wps', 'jd')
d_list.extend(y_tuple)
print("d_list:", d_list)

print("--------------------------------------------------------------------------")

# list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
print(d_list.index(1997))

print("list.insert--------------------------------------------------------------------------")

# list.insert(index, obj) 将对象插入列表
d_list.insert(2, 'abc')
print(d_list)

print("list.pop--------------------------------------------------------------------------")

# list.pop([index=-1]) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
d_list.pop(2)
print(d_list)

print("list.remove--------------------------------------------------------------------------")

# list.remove(obj) 移除列表中某个值的第一个匹配项
print("c_list:", c_list)
c_list.remove("b")
print("c_list:", c_list)

print("list.reverse--------------------------------------------------------------------------")

# list.reverse() 反向列表中元素
print("Before reverse sort:", b_list)
b_list.reverse()
print("After reverse sort:", b_list)

print(" list.sort--------------------------------------------------------------------------")

# list.sort( key=None, reverse=False) 对原列表进行排序
print("Before reverse sort:", a_list)
a_list.sort(reverse=True)
print("After reverse sort:", a_list)

print("list.clear()--------------------------------------------------------------------------")

# list.clear() 清空列表
b_list.clear()
print(b_list)

print("list.copy()--------------------------------------------------------------------------")

# list.copy() 复制列表
l2 = a_list.copy()
print(a_list)
print(l2)

print("--------------------------------------------------------------------------")