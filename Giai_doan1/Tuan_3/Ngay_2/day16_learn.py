# Đóng gói

class Student:
    def __init__(self, name, age):
        self.age = age
        self.__name = name
    def print_name(self):
        print("Name: ", self.__name)

# Tạo đối tượng
my_stu = Student("Dony",10)
print("Trước khi thay đổi: ",my_stu._Student__name)
my_stu.print_name()
# my_stu.__name = "Ynod"
# print("Sau khi thay đổi: ", my_stu.__name)
