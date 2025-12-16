"""
Đề bài:

Tạo class Student.

Trong __init__, khai báo:

self.name: Public (để công khai).

self.__grades: Private (thêm 2 dấu gạch dưới) là một list rỗng.

Viết hàm Setter tên là add_grade(self, score):

Nhận vào điểm số.

Validation (Kiểm tra): Nếu điểm < 0 hoặc > 10 -> In ra "Điểm không hợp lệ!".

Nếu điểm hợp lệ -> Thêm vào list __grades.

Viết hàm Getter tên là get_average(self):

Tính và trả về điểm trung bình từ list __grades. (Trả về 0 nếu chưa có điểm).

Test (Quan trọng):

Tạo sinh viên.

Thử thêm điểm 8.0, 15.0 (lỗi), -2.0 (lỗi).

Thử in điểm trung bình.

Thử thách: Cố tình truy cập trực tiếp sv.__grades xem Python có báo lỗi không?

Mẫu code gợi ý:

Python

class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = []  # <-- Private variable

    def add_grade(self, score):
        if 0 <= score <= 10:
            self.__grades.append(score)
            print(f"Đã thêm điểm {score}")
        else:
            print(f"Lỗi: Điểm {score} không hợp lệ!")

    def get_average(self):
        # ... Viết logic tính trung bình ở đây ...
        pass

# --- Test ---
sv = Student("Dony")
sv.add_grade(9.5)
sv.add_grade(105) # Sẽ bị chặn

# print(sv.__grades) # <--- Dòng này sẽ gây lỗi AttributeError nếu bỏ comment
# """


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


sv = Student("Dony")
sv.add_grade(9.5)
sv.add_grade(10)
sv.add_grade(-2)
sv.add_grade(105)
print(sv.get_avarage())

print(sv._Student__grades)
# print(sv.__grades)