import json


class InvalidAgeError(Exception):
    """Lỗi khi tuổi không hợp lệ (<0 hoặc >150)"""
    pass

class Student:
    def __init__(self, uid, name, age):
        self.uid = uid
        self.name = name
        self.age = age

    def to_dict(self):
        """chuyển object thành dict để lưu vào JSON"""
        return {"id": self.uid,"name": self.name,"age":self.age}

class StudentManager:
    def __init__(self, filename="students.json"):
        self.filename = filename
        self.students = self.load_data()

    def load_data(self):
        try: 
            with open(self.filename, "r", encoding= "utf-8") as f:
                data = json.load(f)
                #List Conprehension: Biến list dict thành list object Student
                return [Student(d["id"], d["name"],d["age"]) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            #Nếu file chưa có hoặc file lỗi, trả về list rỗng
            return []
        
    def save_data(self):
        # List Comprehensionn: biết list object thành list dict
        data = [s.to_dich() for s in self.students]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii= False, indent = 4)
    
    def add_student(self, name, age):
        # --- TĂNG LOGIC: KIỂM TRA DỮ LIỆU ---
        # Nếu dữ liệu sai logic, "ném" lỗi ra ngoài cho thằng main xử lý
        if age < 0 or age > 150:
            raise InvalidAgeError(f"Tuổi {age} không hợp lệ(từ 0-  150)")

        # Tạo ID tự động (Audo Increment)
        if self.students:
            new_id = self.students[-1].uid +1
        else:
            new_id = 1

        new_sv = Student(new_id,name,age)
        self.students.append(new_sv)

        # Lưu ngay vào file
        self.save_data()
        return new_sv

    def get_all(self):
        return self.students