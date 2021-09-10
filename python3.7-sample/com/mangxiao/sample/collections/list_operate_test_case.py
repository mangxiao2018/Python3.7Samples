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