''''
1、基础切片
L[start:stop:step]
'''
#Example: Slice from index 2 to 7

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:7])    # ['c', 'd', 'e', 'f', 'g']

'''
2、带有负索引的切片
'''
L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[-7:-2])    # ['c', 'd', 'e', 'f', 'g']

'''
3、带有正负索引的切片
'''
# Slice from index 2 to -5

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:-5])    # ['c', 'd']

'''
4、指定切片step
'''
#Returns every 2nd item between position 2 to 7

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[2:7:2])    # ['c', 'e', 'g']

'''
5、负步长
'''
#Example: Returns every 2nd item between position 6 to 1

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[6:1:-2])    # ['g', 'e', 'c']

'''
6、在开始和结束处切片
而省略stop索引会将切片延伸到列表的末尾。
意思是L [start:]等效于L [start:len（L）]
'''
# Example: Slice the first three items from the list

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[:3])    # ['a', 'b', 'c']

#Example: Slice the last three items from the list

L = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(L[6:])    # ['g', 'h', 'i']

'''
7、反转列表
'''
#Example: Reverse a list with slicing operator

L = ['a', 'b', 'c', 'd', 'e']
print(L[::-1])

'''
8、修改多个列表元素值
'''
#Example: Modify multiple list items using slice

L = ['a', 'b', 'c', 'd', 'e']
L[1:4] = [1, 2, 3]
print(L)    # ['a', 1, 2, 3, 'e']

#Example: Replace multiple elements in place of a single element
L = ['a', 'b', 'c', 'd', 'e']
L[1:2] = [1, 2, 3]
print(L)    # ['a', 1, 2, 3, 'c', 'd', 'e']

'''
9、插入多个列表元素
'''
#Example: Insert multiple list items using slice

# Insert at the start
L = ['a', 'b', 'c']
L[:0] = [1, 2, 3]
print(L)    # [1, 2, 3, 'a', 'b', 'c']

# Insert at the end
L = ['a', 'b', 'c']
L[len(L):] = [1, 2, 3]
print(L)    # ['a', 'b', 'c', 1, 2, 3]

#Example: Insert multiple list items in the middle

# Insert in middle
L = ['a', 'b', 'c']
L[1:1] = [1, 2, 3]
print(L)    # ['a', 1, 2, 3, 'b', 'c']

'''
10.删除多个列表元素
'''
#Example: Delete multiple list items using slice

# assign empty list to slice
L = ['a', 'b', 'c', 'd', 'e']
L[1:5] = []
print(L)    # ['a']

# with del keyword
L = ['a', 'b', 'c', 'd', 'e']
del L[1:5]
print(L)    # ['a']

'''
11、克隆或复制列表
'''
#Example: Create a copy of a list using slice (shallow copy)

L1 = ['a', 'b', 'c', 'd', 'e']
L2 = L1[:]
print(L2)       # ['a', 'b', 'c', 'd', 'e']
print(L2 is L1) # False

