"""
🟢 Bài 1: Máy tính an toàn (Safe Calculator)
Tình huống: Người dùng rất hay nhập linh tinh (nhập chữ vào chỗ nhập số, hoặc chia cho 0).

Yêu cầu: Viết hàm chia_hai_so(a, b):

Nhận vào 2 tham số.

Dùng try...except để thực hiện phép chia a / b.

Bắt buộc bắt các lỗi sau:

Nếu b = 0: Bắt lỗi ZeroDivisionError -> In ra và trả về: "Lỗi: Không thể chia cho 0".

Nếu a hoặc b là chữ: Bắt lỗi ValueError hoặc TypeError -> In ra và trả về: "Lỗi: Vui lòng nhập số".

Lỗi lạ khác: Bắt Exception -> Trả về: "Lỗi không xác định".

Đảm bảo chương trình luôn trả về kết quả (dù là số hay thông báo lỗi), không được dừng chương trình giữa chừng.
"""


def chia_hai_so(a,b):
    try:
        so_a = float(a)
        so_b = float(b)
        result = so_a/so_b
        return round(result,2)
    except ZeroDivisionError:
        return "Lỗi: không thể chia hết cho 0"
    except ValueError:
        return "Lỗi: Vui lòng nhập số"
    except:
        return "Lỗi không xác định"

    


"""
🔴 Bài 2: Truy xuất dữ liệu an toàn (Safe Data Retrieval) - Nâng cao
Tình huống: Trong AI, dữ liệu thường là các List hoặc Dictionary lồng nhau rất phức tạp. Nếu truy cập sai key hoặc index, chương trình train model chạy cả ngày sẽ bị tắt ngóm.

Yêu cầu: Viết hàm lay_gia_tri_an_toan(data, key_hoac_index):

Hàm này nhận vào một cục dữ liệu data (có thể là List hoặc Dictionary).

Cố gắng lấy giá trị ra:

Nếu data là List: Nó sẽ hiểu tham số thứ 2 là index.

Nếu data là Dict: Nó sẽ hiểu tham số thứ 2 là key.

Dùng try...except để xử lý:

IndexError: Nếu index vượt quá độ dài List.

KeyError: Nếu key không có trong Dict.

TypeError: Nếu data không phải là List hay Dict (ví dụ truyền vào một số nguyên).

Nếu có lỗi: In ra "Không tìm thấy dữ liệu" và trả về None.
"""


def lay_gia_tri_an_toan(data, key_hoac_index):
    try:
        ketqua = data[key_hoac_index]
        return ketqua
    except (IndexError,KeyError,TypeError):
        print("không tìm thấy dữ liệu")
        return None
    


#---------------------------------------------
print("--- TEST BÀI 1 ---")
print(chia_hai_so(10, 2))       # Mong muốn: 5.0
print(chia_hai_so(10, 0))       # Mong muốn: Lỗi chia 0
print(chia_hai_so("10", "ha"))  # Mong muốn: Lỗi nhập chữ

print("\n--- TEST BÀI 2 ---")
my_list = ["Táo", "Cam", "Xoài"]
my_dict = {"ten": "Dony", "job": "AI Engineer"}

print(lay_gia_tri_an_toan(my_list, 1))    # Mong muốn: Cam
print(lay_gia_tri_an_toan(my_list, 99))   # Mong muốn: Không tìm thấy (None)
print(lay_gia_tri_an_toan(my_dict, "ten")) # Mong muốn: Dony
print(lay_gia_tri_an_toan(my_dict, "luong")) # Mong muốn: Không tìm thấy (None)
print(lay_gia_tri_an_toan(12345, 0))      # Mong muốn: Lỗi kiểu dữ liệu (None)
    

    
    



