'''
1.给指定位置元素改值
'''
dogs = ['border collie', 'poodle', 'german shepherd']

dogs[0] = 'australian shepherd'
print(dogs)

'''
2.根据数值,获取对应的索引
'''
dogs = ['border collie', 'poodle', 'german shepherd']

print(dogs.index('poodle'))

'''
3.判断数据是否在列表中
'''
dogs = ['border collie', 'poodle', 'german shepherd']

print('australian cattle dog' in dogs)
print('poodle' in dogs)

'''
4.添加元素到列表
'''
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dogs.append('poodle')

for dog in dogs:
    print(dog.title() + "s are cool.")

'''
5.插入元素到列表
'''
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
dogs.insert(1, 'poodle')

print(dogs)

'''
6.合并两个列表
'''
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

'''
7.列表复制
'''
L = ['red']
L = L * 3
print(L)    # ['red', 'red', 'red']

'''
8.创建空列表
'''
# Create an empty list to hold our users.
usernames = []

# Add some users.
usernames.append('ben')
usernames.append('calvin')
usernames.append('allen')

# Greet all of our users.
for username in usernames:
    print("Welcome, " + username.title() + '!')

'''
9.列表顺序
'''
students = ['bern', 'allen', 'calvin']

# Put students in alphabetical order.
students.sort()

# Display the list in its current order.
print("Our students are currently in alphabetical order.")
for student in students:
    print(student.title())

#Put students in reverse alphabetical order.
students.sort(reverse=True)

# Display the list in its current order.
print("\nOur students are now in reverse alphabetical order.")
for student in students:
    print(student.title())

'''
10.sorted() vs. sort()
使用sort()对列表进行排序时，请记住你将无法恢复原始列表。 
如果要按排序顺序显示列表，但仍然保留原始顺序，则可以使用sorted()函数。 
sorted()函数也接受可选的reverse=True 参数
list.sort方法会“就地排序”列表，也就是说不会把原列表复制一份。
这也是这个方法的返回值是None的原因，提醒你本方法不会新建一个列表。
与list.sort相反的是内置函数sorted，它会新建一个列表作为返回值
'''
students = ['ben', 'allen', 'calvin']

# Display students in alphabetical order, but keep the original order.
print("Here is the list in alphabetical order:")
for student in sorted(students):
    print(student.title())

# Display students in reverse alphabetical order, but keep the original order.
print("\nHere is the list in reverse alphabetical order:")
for student in sorted(students, reverse=True):
    print(student.title())

print("\nHere is the list in its original order:")
# Show that the list is still in its original order.
for student in students:
    print(student.title())

'''
11.列表倒序
我们已经看到了一个列表的三个可能顺序：
1)创建列表的原始顺序
2)按字母顺序
3)反向字母顺序
我们可以使用另外一个顺序，这与列表的原始顺序相反。 
reverse() 函数给出这个顺序
注意，倒序操作是永久性的。当然，你可以跟着使用另一个reverse()调用并返回列表的原始顺序。
'''
students = ['ben', 'allen', 'calvin']
students.reverse()

print(students)

'''
12.排序数字列表
'''
numbers = [1, 3, 4, 2]

# sort() puts numbers in increasing order.
numbers.sort()
print(numbers)

# sort(reverse=True) puts numbers in decreasing order.
numbers.sort(reverse=True)
print(numbers)

numbers = [1, 3, 4, 2]

# sorted() preserves the original order of the list:
print(sorted(numbers))
print(numbers)

numbers = [1, 3, 4, 2]

# The reverse() function also works for numerical lists.
numbers.reverse()
print(numbers)
numbers.reverse()
print(numbers)

'''
13.得到列表长度
可以使用len()函数得到列表的长度
len() 函数返回一个整数
'''
usernames = ['ben', 'calvin', 'allen']
user_count = len(usernames)

print(user_count)


usernames = ['ben', 'calvin', 'allen']
user_count = len(usernames)

print("This will work: " + str(user_count))

'''
14.从列表删除元素
列表是一个动态结构。 可以定义一个空列表，然后在信息进入程序时将其填满。 为支持频繁的动态，需要一些方法在不再需要时从列表中删除元素。 可以通过其位置或值来从列表中删除项。

通过位置删除item
如果知道列表中项目的位置，则可以使用del命令删除该元素。 使用此方法，要给出输入命令del和列表名称，以及在方括号指定移除的元素的索引
'''
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
# Remove the first dog from the list.
del dogs[0]

print(dogs)

'''
15.通过值删除item
但请注意，仅删除具有此值的第一个元素。 如果有多个具有相同值的项，则列表中将保留其它具有此值的元素。
'''
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
# Remove australian cattle dog from the list.
dogs.remove('australian cattle dog')

print(dogs)

'''
16.删除所有元素
'''
letters = ['a','b','c']
letters.clear()

print(letters)

'''
17.从列表弹出元素
'''
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
last_dog = dogs.pop()

print(last_dog)
print(dogs)

# 实际上，你可以通过提供要弹出的元素的索引来从列表中弹出所需的任何元素。 所以我们可以通过弹出列表中的第一个元素来做一个先进先出的方法
dogs = ['border collie', 'australian cattle dog', 'labrador retriever']
first_dog = dogs.pop(0)

print(first_dog)
print(dogs)

'''
18.数字列表
'''
# Print out the first ten numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    print(number)

'''
19.range() 函数
如果想要使用大量数字, range() 函数可帮助我们生成长的数字列表。 以下是使用range 函数执行相同操作的两种方法。
range函数接收起始数字和结束数字。 你得到所有整数，但不包括结尾数字。 你还可以添加一个step值，告诉range函数在数字之间采取的步长有多大
'''
# Print the first ten numbers.
for number in range(1,11):
    print(number)

# Print the first ten odd numbers.
for number in range(1,21,2):
    print(number)

'''
20.定义列表数字范围
将这些数字存储在列表中，可以使用list()函数。 此函数接收一个范围，并将其转换为一个列表
'''
# Create a list of the first ten numbers.
numbers = list(range(1,11))
print(numbers)

'''
21.创建一个前一百万个数字的列表
表达式numbers[-10:]给我们一个列表的切片。 索引“-1”是列表中的最后一个元素，索引“-10”是列表末尾倒数第10个元素。 因此切片numbers [-10：]为我们提供了从该元素到列表末尾的所有内容
'''
# Store the first million numbers in a list.
numbers = list(range(1,1000001))

# Show the length of the list:
print("The list 'numbers' has " + str(len(numbers)) + " numbers in it.")

# Show the last ten numbers:
print("\nThe last ten numbers in the list are:")
for number in numbers[-10:]:
    print(number)

'''
22.min(), max(), 和 sum() 函数
可以对使用数字列表使用三种函数。 min()函数返回列表中的最小数字，max() 函数返回列表中的最大数字，sum()函数返回列表中所有数字的总和。
'''
ages = [23, 16, 14, 28, 19, 11, 38]

youngest = min(ages)
oldest = max(ages)
total_years = sum(ages)

print("Our youngest reader is " + str(youngest) + " years old.")
print("Our oldest reader is " + str(oldest) + " years old.")
print("Together, we have " + str(total_years) +
      " years worth of life experience.")