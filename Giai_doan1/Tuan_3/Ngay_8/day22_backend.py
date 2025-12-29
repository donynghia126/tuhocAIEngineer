import os
import json

class Student:
    def __init__(self,student_id,name,score):
        self.student_id = student_id
        self.name = name
        self.score = score
    def to_dict(self):
        return {"ID":self.student_id,"Name":self.name,"Score":self.score}
    def __str__(self):
        return (f"ID: {self.student_id}, Name: {self.name}, Score: {self.score}.")


class StudentManager:
    def __init__(self, filename = "data.json"):
        self.students = []
        self.filename = filename

    
    
    def add_student(self,student):
        for s in self.students:
            if s.student_id == student.student_id:
                print(f"ID {student.student_id} đã có trong danh sách") 
                return
        
        self.students.append(student)
        print(f"Đã thêm sinh viên ID: {student.student_id}")

    def remove_student(self,student_id):
        initial_count = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]

        if len(self.students) < initial_count:
            print("Đã xoá thành công!!")
        else:
            print(f"Không tìm thấy ID {student_id}")
    def show_all(self):
        if not self.students:
            print("Danh sách rỗng")
            return
        
        print("--- Danh sách sinh viên ---")
        for s in self.students:
            print(s)
        print("-"*20)
    
    def save_to_json(self):
        try:
            data_to_save = [s.to_dict() for s in self.students]
            with open(self.filename, "w", encoding="utf-8") as f:
                json.dump(data_to_save, f,ensure_ascii=False,indent=4)
            print("Đã lưu file Json")
        except Exception as e:
            print(f"Có lỗi xảy ra khi lưu file: {e}")





