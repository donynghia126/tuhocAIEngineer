
"""
🟢 Bài 1: Chẵn hay Lẻ?
Mục tiêu: Biết dùng toán tử chia lấy dư (%).

Đề bài: Nhập một số nguyên từ bàn phím. Kiểm tra xem số đó là số CHẴN hay số LẺ.

Gợi ý:

Số chẵn là số chia hết cho 2 (số dư bằng 0).

Phép chia lấy dư trong Python là %. Ví dụ: 5 % 2 ra 1.

Logic: if so_nhap_vao % 2 == 0:
""" 

int_input = int(input("Nhập một số Nguyên để biết chẵn hay lẻ: "))
if int_input % 2 == 0:
    print(f"Số {int_input} là số chẳn")
else: 
    print(f"Số {int_input} là số lẻ")


"""
Bài 2: BMI V2.0 (Nâng cấp bài hôm qua)
Mục tiêu: Áp dụng if-elif-else.

Đề bài: Lấy lại code bài BMI hôm qua. Sau khi tính ra số BMI, hãy in ra kết luận sức khỏe:

BMI < 18.5: "Gầy"

18.5 <= BMI < 24.9: "Bình thường"

25 <= BMI < 29.9: "Thừa cân"

BMI >= 30: "Béo phì"
"""

can_nang = float(input("Nhập Cân Nặng(kg): "))
chieu_cao_cm = float(input("Nhập Chiều Cao(cm): "))
chieu_cao_m = chieu_cao_cm/100

bmi = can_nang/(chieu_cao_m**2)

if bmi < 18.5:
    print("Gầy")
elif  18.5 <= bmi < 25:
    print("Bình thường")
elif 25 <= bmi < 30:
    print("Thừa cân")
else: 
    print("Béo phì")

"""
🔴 Bài 3: Kiểm tra Năm Nhuận (Leap Year) - Bài test logic
Mục tiêu: Kết hợp điều kiện phức tạp (and, or).

Đề bài: Nhập vào một số năm (ví dụ: 2024). Kiểm tra xem đó có phải năm nhuận không.

Quy tắc năm nhuận:

Năm chia hết cho 400 -> LÀ năm nhuận.

HOẶC (Năm chia hết cho 4 VÀ KHÔNG chia hết cho 100) -> LÀ năm nhuận.

Còn lại -> KHÔNG phải năm nhuận.

Ví dụ:

2000: Nhuận (chia hết cho 400).

2024: Nhuận (chia hết cho 4, ko chia hết cho 100).

2100: Không nhuận (chia hết cho 4, nhưng cũng chia hết cho 100 và ko chia hết cho 400).
"""

year = int(input("Nhập số năm: "))

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0 :
    print(f"Năm {year} là năm nhuận")
else:
    print(f"Năm {year} không phải là năm nhuận")

"""
Bài 4 (Thử thách): Trò chơi Kéo - Búa - Bao
Mục tiêu: Làm game đầu tay! Sử dụng thư viện random.

Đề bài: Viết chương trình chơi oẳn tù tì với máy tính.

Máy tính tự chọn ngẫu nhiên 1 trong 3: "Kéo", "Búa", "Bao".

Bạn nhập lựa chọn của bạn.

So sánh và in kết quả: "Hòa", "Bạn thắng", hay "Máy thắng".
"""

import random

print("Kéo Búa Bao")
print("1. Kéo | 2. Búa | 3. Bao")

may_chon = random.randint(1,3)
nguoi_chon = int(input("Bạn chọn gì (Nhập số từ 1 đến 3)? "))
if may_chon == 1:
    may = "kéo"
elif may_chon == 2:
    may = "Búa"
else:
    may = "Bao"

if nguoi_chon == 1:
    nguoi = "kéo"
elif nguoi_chon == 2:
    nguoi = "Búa"
else:
    nguoi = "Bao"

print(f"Bạn chọn {nguoi}, Máy chọn {may}")

if nguoi_chon == may_chon:
    print("Hoà")
elif nguoi_chon == 1 :
    if may_chon == 2:
        print("Bạn Thua.")
    else:
        print("Bạn thắng")
elif nguoi_chon == 2:
    if may_chon == 3:
        print("Bạn Thua.")
    else:
        print("Bạn thắng")
elif nguoi_chon == 3:
    if may_chon == 1:
        print("Bạn Thua.")
    else:
        print("Bạn thắng")