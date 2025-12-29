from day22_backend import Student, StudentManager

def main():
    manager = StudentManager()

    while True:
        print("\n--- Cục quản lý điểm sinh viên ---")
        print("1. Thêm sinh viên")
        print("2. Xoá sinh viên")
        print("3. Hiển thị danh sách")
        print("4. Lưu dữ liệu (json)")
        print("0. Thoát")

        choice = input("Nhập Lựa chọn: ")
        if choice == "1":
            student_id = input("Nhập ID học sinh: ").strip()
            student_name = input("Nhập Tên học sinh: ").strip().title()
            try:
                student_score = float(input("Nhập điểm học sinh: "))
                student = Student(student_id, student_name, student_score)
                manager.add_student(student)
            except ValueError:
                print("Vui lòng nhập điểm là số")
        elif choice == "2":
            student_remove_id = input("Nhập ID học sinh cần xoá: ").strip()
            manager.remove_student(student_remove_id)
        elif choice == "3":
            manager.show_all()
        elif choice == "4":
            manager.save_to_json()
        elif choice == "0":
            print("Tạm Biệt!!")
            break
        else:
            print("Vui lòng nhập đúng định dạng !!")

if __name__ == "__main__":
    main()