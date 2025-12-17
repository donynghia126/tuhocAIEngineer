# TÍNH CHẤT KẾ THỪA - INHERITANCE

class Person:
    def __init__(self,name):
        self.name = name

    def print_name(self):
        print(self.name)

#Class con - class kế thừa
class Student(Person):
    #Tâis sử dụng lại hàm khởi tạo của class cha
    def __init__(self, name, age):
        # super().__init__(name) #Cách 1
        Person.__init__(self,name)
        self.age = age
        

my_stu = Student("Dony",10)
my_stu.print_name()
print(my_stu.age)