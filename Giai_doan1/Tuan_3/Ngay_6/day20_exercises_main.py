from day20_exercises_student import StudentManager,InvalidAgeError

manager = StudentManager()
while True:
    print("\n --- QUẢN LÝ SINH VIÊN (MODULAR) ---")
    print("1. Thêm sinh viên")
    print("2. Xem danh sách")
    print("3. Thoát")

    choice = input("Chọn chức năng: ")
    if choice == "1":
        try:
            # -- TẦNG GIAO DIỆNl NHẬP LIỆU ---
            name = input("Nhập tên: ").strip()
            if not name:
                raise ValueError("Tên không được để trống")
            
            age_input = input("Nhập tuổi: ")

            # Kiểm tra xem có phải số không (Validation cơ bản)
            if not age_input.isdigit():
                raise ValueError("Tuổi phải là một số nguyên!")
            
            age = int(age_input)

            # --- GỌI SANG BACKEND ---
            # Lúc này main không cần lo về việc < 0 hay > 150 nữa
            # Việc đó mânger lo. Nếu lỗi sẽ ném InvalidAgeError ra đây
            sv = manager.add_student(name, age)
            print(f"✅ Thêm thành công: {sv.name} (ID: {sv.uid})")
        except InvalidAgeError as e:
            # Bắt lỗi logic ( từ file student.py ném sang)
            print(f"❌ Lỗi Logic: {e}")

        except ValueError as e:
            # Bắt lỗi NHập liệu (do người dùng nhập bậy)
            print(f"❌ Lỗi Nhập Liệu: {e}")
        
        except Exception as e:
            #lưới đi an toàn cuối cùng
            print("❌ Lỗi Không xác định: {e}")
    elif choice == "2":
        lst = manager.get_all()
        if not lst:
            print("📭 Danh Sách Trống.")
        else:
            # In bảng đẹp dùng f-string alignment
            print(f"{"ID": <5}{"Tên":<20}{"Tuổi":<5}")
            print("-" * 30)
            for s in lst:
                print(f"{s.uid:<5}{s.name:<20}{s.age:<5}")
    elif choice =="3":
        print("Tạm Biệt!")
        break
    else:
        print("❌ Chọn sai rồi, nhập lại đi!")