"""
调用str函数对类对象进行处理时或者调用Python
内置函数format()和print()时自动执行，__str__方
法的返回值必须是字符串
"""
class Complex: #定义复数类Complex
    def __init__(self,real,image): #定义构造方法
        self.real=real #将self对应对象的real属性赋值为形参real的值
        self.image=image #将self对应对象的image属性赋值
    #为形参image的值
    def __str__(self): #定义内置方法__str__
        return str(self.real)+'+'+str(self.image)+'i'
"""
内置方法                   功能描述
__gt__(self, other) 进行self>other运算时自动执行
__lt__(self, other) 进行self<other运算时自动执行
__ge__(self, other) 进行self>=other运算时自动执行
__le__(self, other) 进行self<=other运算时自动执行
__eq__(self, other) 进行self==other运算时自动执行
__ne__(self, other) 进行self!=other运算时自动执行
"""
class Student: #定义Student类
    def __init__(self, name, age): #定义构造方法
        self.name=name #将self对应对象的name属性赋为形参
        #name的值
        self.age=age #将self对应对象的age属性赋为形参age的值
    def __le__(self, other): #定义内置方法__le__
        return self.age<=other.age

if __name__ == '__main__':
    c = Complex(3.2, 5.3)  # 定义Complex类对象c
    print(c) #输出“3.2+5.3i”

    stu1 = Student('李晓明', 19)  # 定义Student类对象stu1
    stu2 = Student('马红', 20)  # 定义Student类对象stu2
    print('马红的年龄小于等于李晓明的年龄：', stu2 <= stu1)