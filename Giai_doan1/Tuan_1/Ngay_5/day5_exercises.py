"""
🟢 Bài 1: Refactor BMI (Từ Ngày 1 & 2)
Yêu cầu: Viết 2 hàm riêng biệt.

Hàm tinh_bmi(can_nang, chieu_cao): Trả về số BMI.

Hàm danh_gia_bmi(bmi): Trả về chuỗi đánh giá ("Gầy", "Béo"...).

Chương trình chính gọi 2 hàm này.

Code mẫu (Bạn điền tiếp vào ...):

Python

def tinh_bmi(can_nang, chieu_cao_cm):
    chieu_cao_m = chieu_cao_cm / 100
    return can_nang / (chieu_cao_m ** 2)

def danh_gia_bmi(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi < 25:
        return "Bình thường"
    # ... viết tiếp ...

# --- Chương trình chính ---
w = float(input("Nhập kg: "))
h = float(input("Nhập cm: "))

chi_so = tinh_bmi(w, h)
ket_luan = danh_gia_bmi(chi_so)

print(f"BMI của bạn là {chi_so:.2f}. Đánh giá: {ket_luan}")
"""

def tinh_bmi(chieu_cao, can_nang):
    bmi = can_nang / (chieu_cao/100)**2
    return bmi

def danh_gia_bmi(bmi):
    if bmi<18.5:
        return "Gầy"
    elif bmi < 23:
        return "Bình Thường"
    elif bmi < 25:
        return "Thừa Cân"
    elif bmi < 30:
        return "Béo Phì"
    elif bmi < 35:
        return "Béo Phì độ II"
    else:
        return "Béo Phì độ III"
    
chieu_cao = float(input("Nhập Chiều Cao(cm): "))
can_nang = float(input("Nhập Cân Nặng(kg): "))

bmi = tinh_bmi(chieu_cao,can_nang)
danh_gia = danh_gia_bmi(bmi)

print(f"BMI của bạn là {bmi:.2f} và được đánh giá là '{danh_gia}'")

"""
🟡 Bài 2: Refactor Giải phương trình bậc 2 (Từ Ngày 2)
Yêu cầu: Đóng gói logic vào hàm giai_phuong_trinh(a, b, c).

Hàm này không cần return giá trị tính toán để dùng tiếp, mà có thể print trực tiếp kết quả nghiệm bên trong hàm cũng được (đối với bài này). Hoặc xịn hơn là trả về một Tuple nghiệm.
"""
import math
def giai_phuong_trinh(a,b,c):
    delta = b**2 - (4 * a * c)
    if a == 0:
        if b == 0:
            print(f"Phương trình này vô số nghiệm")
            return
        else:
            x = -c /b
            print(f"Phương trình này chỉ có một nghiệm là {x}")
            return x
    if delta < 0 :
        print( f"Phương trình này vô nghiệm")
        return
    elif delta == 0:
        x = -b/(2*a)
        print(f"Phương trình này có nghiệm kép là {x}")
        return x
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phương trình này có 2 nghiệm là {x1},{x2}")
        return x1,x2

kq = giai_phuong_trinh(1,-5,6)

print(f"Tuple nghiệm của bạn là {kq} ")


"""
🔴 Bài 3: Refactor Đếm tần suất từ (Từ Ngày 5)
Yêu cầu: Viết hàm dem_tu(doan_van):

Input: Một đoạn văn (string).

Output: Một dictionary chứa số lượng từ.
"""




def dem_tu(doan_van):
    count  = {}
    for tu in doan_van:
        count[tu] = count.get(tu, 0) + 1
    return count
def so_tu_nhieu_nhat(so_tu):
    tu_nhieu_nhat = ""
    nhieu_lan = 0
    for tu,solan in so_tu.items():
        if nhieu_lan < solan:
            nhieu_lan = solan
            tu_nhieu_nhat = tu
    return tu_nhieu_nhat,nhieu_lan

while True:
    so_tu = input("Nhập đoạn văn bạn cần đếm số từ (không tính khoảng trắng): ")
    so_tu_list = so_tu.split()
    if so_tu.lower() == "exit":
        break
    dem_tu_xem_bao_nhieu = dem_tu(so_tu_list)
    tu_nhieu_nhat, so_lan_xuat_hien = so_tu_nhieu_nhat(dem_tu_xem_bao_nhieu)
    print(f"Dic số từ là: {dem_tu_xem_bao_nhieu}")
    print(f"Từ xuất hiện nhiều nhất là {tu_nhieu_nhat} với {so_lan_xuat_hien} lần")
    



    
