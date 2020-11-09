d=dict(sno='1810100', name='李晓明')
if d.get('sno')!=None: #如果get方法返回的不是None
    print('字典d中存在键为sno的元素')
else: #否则
    print('字典d中不存在键为sno的元素')
if 'name' in d: #如果字典d中有键为'name'的元素
    print('字典d中存在键为name的元素')
else:
    print('字典d中不存在键为name的元素')
if d.get('age')!=None: #如果get方法返回的不是None
    print('字典d中存在键为age的元素')
else: #否则
    print('字典d中不存在键为age的元素')