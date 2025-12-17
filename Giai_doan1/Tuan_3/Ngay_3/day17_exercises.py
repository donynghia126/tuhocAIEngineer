class Student:
    def __init__(self,name):
        self.name = name
        self.__grades = []
    def add_grade(self,score):
        if 0 <= score <=10:
            self.__grades.append(score)
            print(f"Đã thêm điểm {score} vào khung điểm")
        else:
            print("Điểm không hợp lệ")
    def get_avarage(self):
        if not self.__grades: return 0
        return sum(self.__grades)/len(self.__grades)
    def introduce(self):
        print(f"Tôi là Sv {self.name}")

class AI_Student(Student):
    def __init__(self,name, specialization):
        super().__init__(name)
        self.specialization = specialization
    def introduce(self):
        print(f"Tôi là Sv {self.name}, chuyên ngành {self.specialization}")


stu_1 = Student("Dony")
stu_1.introduce()
stu_2 = AI_Student("Dony","IT")
stu_2.introduce()
stu_2.add_grade(1)
stu_2.add_grade(51)
stu_2.add_grade(-16)
stu_2.add_grade(10)
stu_2.add_grade(5)
print(stu_2._Student__grades)
print(stu_2.get_avarage())