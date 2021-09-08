# codeing=utf-8

"""
@description:变量知识点练习
@author:zhangyanqing@
@date:2020-10-31
@version:python-3.7
"""

a_dic = {'Alic':100,'Tom':0,'ada':59}
b_dic = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
c_dic = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
print(a_dic['Alic'])

# 更新数据
c_dic['Age']=24
print(c_dic)

# len(dict) 计算字典元素个数，即键的总数
print(len(a_dic))

# str(dict) 输出字典，以可打印的字符串表示。
print(str(a_dic))

# type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。
print(type(a_dic))

# 字典拷贝,返回一个字典的浅复制
d_dic = {}
d_dic = a_dic.copy()
print(d_dic)

# dict.get(key, default=None)
# key -- 字典中要查找的键。
# default -- 如果指定的键不存在时，返回该默认值值。
print(a_dic.get('Alic'))

# key in dict
# key -- 要在字典中查找的键。
print('Alic' in a_dic)
print('Alic' in b_dic)

# dict.items()
# 返回可遍历的(键, 值) 元组数组
print(a_dic.items())

# dict.keys()
# 返回一个迭代器。
print(a_dic.keys())

# dict.values()
# 返回一个迭代器，可以使用 list() 来转换为列表
print(a_dic.values())

# dict.setdefault(key, default=None)
# key -- 查找的键值
# default -- 键不存在时，设置的默认键值
v_dic = {'aa':None,'bb':None,'cc':None}
v_dic.setdefault('aa',123)
v_dic.setdefault('bb',456)
v_dic.setdefault('dd',789)
print(v_dic)

# dict.update(dict2)
# 该方法没有任何返回值。把dict2里的数据追加到dict中
p_dic = {'Name': 'Runoob', 'Age': 7}
q_dic = {'Sex': 'female' }
p_dic.update(q_dic)
print(p_dic)
print(q_dic)

# pop(key[,default])
# key: 要删除的键值
# default: 如果没有 key，返回 default 值
p_dic.pop('Name')
print(p_dic)

# popitem()
# 返回一个键值对(key,value)形式，按照 LIFO（Last In First Out 后进先出法） 顺序规则，即最末尾的键值对。
o_dic = {'name': '张三', 'alexa': 10000, 'url': 'google.com'}
result =o_dic.popitem()
print(result)
print(o_dic)

# dict.fromkeys(seq[, value])
# seq -- 字典键值列表
# value -- 可选参数, 设置键序列（seq）对应的值，默认为 None
u_tuple = ('name','age','sex')
e_dic = dict.fromkeys(u_tuple)
print(e_dic)
f_dic = dict.fromkeys(u_tuple,10)
print(f_dic)

# 删除键'Name'
del c_dic['Name']

# 使用 del 删除手，再打印会抛异常，因为使用del删除是真删除
# KeyError: 'Name'
# print("c_dic:",c_dic)

# 清空字典
b_dic.clear()
print("b_dic:",b_dic)

# 删除字典
del a_dic
# 使用 del 删除手，再打印会抛异常，因为使用del删除是真删除
# 报 NameError: name 'a_dic' is not defined
# print("a_dic:",a_dic)