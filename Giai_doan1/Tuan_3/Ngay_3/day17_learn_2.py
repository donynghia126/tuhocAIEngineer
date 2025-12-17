#NOTE TÍNH ĐA HÌNH _ POLYMORPHISH

# class Cow:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         return self.name + "Says mooooooooo"
    
# class Cat:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         return self.name + "Says Meowwwwwwww"
    

# my_cow = Cow("Bò")
# my_cat = Cat("Mèo")

# print(my_cow.speak())
# print(my_cat.speak())

# class Animal:
#     def speak(self):
#         return "some sound"
    
# class Dog(Animal): # overriding method
#     def speak(self):
#         return "Woof!!!!"
    
# my_ani = Animal()
# my_dog = Dog()

# print(my_ani.speak())
# print(my_dog.speak())

#NOTE TÍNH CHẤT TRỪU TƯỢNG - ABSTRACTION

from abc import ABC, abstractmethod

# lớp trừu tượng
class Animal(ABC):
    # phương thức trừu tượng
    @abstractmethod
    def speak(self):
        pass
    

    # Không phải là phương thruwsc trừu tượng
    def not_abstract_method(self):
        print("Không cần ghi đè lại")

# ani = Animal() #Lỗi không thể tạo từ lớp trừu tượng


# Class con kế thua từ lớp trừu tượng
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
my_dog = Dog()
print(my_dog.speak())
my_dog.not_abstract_method()