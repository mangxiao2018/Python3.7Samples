#定义Person类
class Person:
    # 定义Person类
    def SetName(self, name): #定义SetName方法
        self.name=name #将self对应对象的name属性赋为形参name的值

class Student(Person): #以Person类作为父类定义子类Student
    def SetSno(self, sno): #定义SetSno方法
        self.sno=sno #将self对应对象的sno属性赋为形参sno的值

class Teacher(Person): #以Person类作为父类定义子类Teacher
    def SetTno(self, tno): #定义SetTno方法
        self.tno=tno #将self对应对象的tno属性赋为形参tno的值

class TA(Student,Teacher): #以Student类和Teacher类作为父类
    #定义子类TA
    def SetTeacher(self, teacher): #定义SetTeacher方法
        self.teacher=teacher #将self对象的teacher属性赋为形参teacher的值

if __name__=='__main__':
    stu=Student() #定义Student类对象stu
    stu.SetSno('1810100') #调用Student类中定义的SetSno方法
    stu.SetName('李晓明') #调用Student类从Person类继承过来的SetName方法
    print('学号：%s，姓名：%s'%(stu.sno,stu.name)) #输出学号和姓名
    t=Teacher() #定义Teacher类对象t
    t.SetTno('998012') #调用Teacher类中定义的SetTno方法
    t.SetName('马红') #调用Teacher类从Person类继承过来的SetName方法
    print('教工号：%s，姓名：%s'%(t.tno,t.name)) #输出教工号和姓名