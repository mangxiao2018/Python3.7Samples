#类的定义
#在一个类中，除了可以包含前面所说的属性，还可以包含各种方法。
#属性对应一个类可以用来保存哪些数据，而方法对应一个类可以支持哪些操作（即数据处理）。
## 类的定义形式多样
# 我们既可以直接创建新的类，也可以基于一个或多个已有的类创建新的类；
# 我们既可以创建一个空的类，然后再动态添加属性和方法，也可以在创建类的同时设置属性和方法。
## 类的定义
# 类中的属性对应前面所学习的变量，而类中的方法
# 对应前面所学习的函数。通过类，可以把数据和操
# 作封装在一起，从而使得程序结构更加清晰，这也
# 就是所谓的类的封装性。
# 类体的各语句需要采用缩进方式以表示它们是类中的语句

# 对类属性的访问，既可以直接通过类名访问，也可以通过该类的对象访问，访问方式为：类名或对象名.属性名
class Student: # 定义一个名字为Student的类
    name = 'Unknown'  # 定义Student类中有一个name属性
    __id = '未知'  # 定义Student类中有一个__id私有属性
    pass       # 一个空语句，起到占位作用，表示Student类中没有任何属性和方法

    def SetName(self, newname): #定义类的普通方法SetName
        self.name=newname #将self对应实例对象中的name属性值赋为newname

    def PrintName(self): #定义类的普通方法PrintName
        print('姓名：%s'%self.name) #输出self对应实例对象中的name属性值

    def SetInfo(self,newname,newid): #定义SetInfo方法
        self.name=newname #将self对应实例对象的name属性赋为newname
        self.__id=newid #将self对应实例对象的__id属性赋为newid

    def PrintInfo(self): #定义PrintInfo函数
        print('姓名：%s，身份证号：%s'%(self.name,self.__id))

    # 构造方法是Python类中的内置方法之一，
    # 它的方法名为__init__，在创建一个类对象时会自动执行，负责完成新创建对象的初始化工作。
    def __init__(self):
        print('构造方法被调用！')
        self.name = '未知'  # 将self对应对象的name属性赋值为“未知”
    """
    提示：类对象销毁有如下三种情况：
    （1）局部变量的作用域结束。
    （2）使用del删除对象。
    （3）程序结束时，程序中的所有对象都将被销毁
    """
    def __del__(self): #定义析构方法
        print('姓名为%s的对象被销毁！'%self.name)

# 私有属性，是指在类内可以直接访问、而在类外无法直接访问的属性。
# Python中规定，在定义类时，如果一个类属性名是以__（两个下划线）开头，则该类属性为私有属性

# 析构方法是类的另一个内置方法，它的方法名为__del__，在销毁一个类对象时会自动执行，负责完成待销毁对象的资源清理工作，如关闭文件等。


def funcx(name):
    stux=Student(name) #创建Student类对象stu

if __name__ == '__main__':
    stu = Student() # 创建Student类的对象，并将创建的对象赋给变量st
    print(stu) # 输出stu
    print('第4行输出：', Student.name)
    stu1 = Student()  # 创建Student类对象stu1
    stu2 = Student()  # 创建Student类对象stu2
    print('第7行输出：stu1 %s,stu2 %s' % (stu1.name, stu2.name))
    Student.name = '未知'  # 将Student的类属性name赋为"未知"
    print('第9行输出：', Student.name)
    print('第10行输出：stu1 %s,stu2 %s' % (stu1.name, stu2.name))
    stu1.SetName('李晓明')  # 通过stu1对象调用SetName方法
    stu2.SetName('马红')  # 通过stu1对象调用SetName方法
    stu1.PrintName()  # 通过stu1对象调用PrintName方法
    stu2.PrintName()  # 通过stu2对象调用PrintName方法

    stu.PrintInfo()  # 通过stu对象调用PrintInfo方法
    # print('身份证号：%s'%stu.__id) #取消前面的注释，则程序会报错

    # 实际上，Python中并不存在无法访问的私有属性。
    # 如果我们在类中定义了一个私有属性，则在类外访问该私有属性时需要在私有属性名前加上“_类名”。
    print('身份证号：% s' % stu._Student__id)

    stu3 = stu2
    del stu2  # 使用del删除stu2对象
    funcx('张刚')  # 调用func函数
    del stu3  # 使用del删除stu3对象
    stu4 = Student('刘建')  # 创建Student类对象stu4