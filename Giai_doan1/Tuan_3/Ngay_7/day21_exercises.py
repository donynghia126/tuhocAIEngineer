import json
import os

# ---CLASS 2: Đại diện cho từng sinh viên ---
class Student:
    def __init__(self, student_id,name,score):
        self.student_id = student_id
        self.name = name
        self.score = score
    def to_dict(self):
        return {"ID":self.student_id,"Name": self.name,"Score": self.score}
    def __str__(self):
        return f"[ID]: {self.student_id} - {self.name} - {self.score}"

# --- CLASS 2: Quản lý danh sách sinh viên ---
class StudentManager:
    def __init__(self, storage_file = "students.json"):
        self.students = []
        self.storage_file = storage_file

    def add_student(self,student):
        for s in self.students:
            if s.student_id == student.student_id:
                print(f"❌ Lỗi: ID {student.student_id} đã tồn tại!")
                return
        self.students.append(student)
        print(f"✅ Đã thêm sinh viên: {student.name}")
    
    def remove_student(self, student_id):
        initial_count = len(self.students)
        self.students = [s for s in self.students if s.student_id != student_id]

        if len(self.students) < initial_count:
            print(f"✅ Đã xoá sinh viên có ID {student_id}")
        else:
            print(f"⚠️ Không tìm thấy sinh viên ID {student_id}")
    
    def show_all(self):
        if not self.students:
            print("📭 Danh sách trống!")
            return
        print(f"\n--- DANH SÁCH SINH VIÊN ({len(self.students)}) ---")
        for s in self.students:
            print(s)
        print("-"*30)
    
    def save_data(self):
        try:
            data_to_save = [s.to_dict() for s in self.students]

            with open(self.storage_file,'w',encoding="utf-8") as f:
                json.dump(data_to_save, f, ensure_ascii=False,indent=4)
            print(f"💾 Đã lưu dữ liệu vào '{self.storage_file}' thành công!")
        except Exception as e:
            print(f"❌ Có lỗi khi lưu file: {e}")

 # --- PHẦN GIAO DIỆN (CLI) ---
# Tách biệt logic xử lý (Class) và giao diện người dùng (Main)

def main():
    manager = StudentManager("data_students.json")
    while True:
        print("\n=== HỆ THÔNG QUẢN LÝ SINH VIÊN ===")
        print("1. Thêm sinh viên")
        print("2. Xoá sinh viên")
        print("3. Hiển thị danh sách")
        print("4. Lưu dữ liệu (json)")
        print("0. Thoát")

        choice = input("👉 Nhập lựa chọn: ")

        if choice == "1":
            s_id = input("Nhập ID: " ).strip()
            name = input("Nhập Tên: ").strip().title()
            try:
                score = float(input("Nhập Điểm: "))
                new_student = Student(s_id,name,score)
                manager.add_student(new_student)
            except ValueError:
                print("❌ Điểm phải là số")
        elif choice == "2": 
            s_id = input("Nhập ID cần xoá: ").strip()
            manager.remove_student(s_id)
        elif choice == "3":
            manager.show_all()
        elif choice == "4":
            manager.save_data()
        elif choice == "0":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ")

if __name__ == "__main__":
    main()