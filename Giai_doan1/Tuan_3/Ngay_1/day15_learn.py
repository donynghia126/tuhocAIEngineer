#NOTE: Class trong python

class Person: 
    #Class attribute - Đặc trưng toàn bộ class Person.count
    count = 0

    # hàm khởi tạo - constructor
    def __init__(self , name , age):
        self.name = name #seft.name chính là instance attribuyte - gắn liền với TỪNG đối tượng
        self.age = age
        Person.count +=1

    # định nghĩa method - phương thức
    def in_ra(self):
        print(f"Name: {self.name}. Age {self.age}.")

# Tạo các đối tượng object
per_1 = Person("Dony",20)
per_2 = Person("Kamisato",20)


# print(Person.count)

print(per_1.name)
per_2.in_ra()
