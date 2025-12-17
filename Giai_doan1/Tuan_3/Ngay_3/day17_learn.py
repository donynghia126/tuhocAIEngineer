# TÍNH CHẤT KẾ THỪA - INHERITANCE

class Person:
    def __init__(self,name):
        self.name = name

    def print_name(self):
        print(self.name)

class Student(Person):
    pass

my_stu = Student("Dony")
my_stu.print_name()