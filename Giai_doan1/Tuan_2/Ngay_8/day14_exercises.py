import re
"""
🟢 Bài 1: "Thám tử" dữ liệu (Data Extraction)
Tình huống: Bạn cào dữ liệu từ một trang web tuyển dụng, nhưng thông tin liên hệ nằm lẫn lộn trong văn bản mô tả.

Đề bài: Cho đoạn văn bản:

Python

text = """
# Chào các bạn, liên hệ admin qua email: support@gmail.com hoặc admin.hr@company.vn.
# Số điện thoại nóng: 0987654321 hoặc gọi 0123456789.
# Địa chỉ fake: 9999 (không phải sđt).
"""
Yêu cầu:

Dùng re.findall trích xuất danh sách tất cả Email.

Gợi ý Pattern: [\w\.-]+@[\w\.-]+ (Dịch: Chữ/số/chấm/gạch ngang + @ + Chữ/số/chấm/gạch ngang).

Dùng re.findall trích xuất danh sách Số điện thoại VN.

Quy tắc SĐT: Bắt đầu bằng số 0 và theo sau là 9 chữ số nữa (Tổng 10 số).

Gợi ý Pattern: 0\d{9}.
"""

text = """
Chào các bạn, liên hệ admin qua email: support@gmail.com hoặc admin.hr@company.vn.
Số điện thoại nóng: 0987654321 hoặc gọi 0123456789.
Địa chỉ fake: 9999 (không phải sđt).
"""

loc_email = r"[\w\.-]+@[\w\.-]+"

email = re.findall(loc_email,text)

print(email)

loc_phone = r"0\d{9}"

phone = re.findall(loc_phone,text)

print(phone)


"""
🔴 Bài 2: Kiểm tra mật khẩu (Password Validator)
Tình huống: Khi làm web, bạn cần bắt người dùng đặt mật khẩu mạnh.

Yêu cầu: Viết hàm check_password(password) trả về True nếu mạnh, False nếu yếu. Quy tắc "Mạnh":

Dài ít nhất 8 ký tự.

Có ít nhất 1 số (\d).

Có ít nhất 1 chữ in hoa (Dùng pattern [A-Z]).

Gợi ý: Thay vì viết 1 regex siêu phức tạp, hãy dùng re.search để kiểm tra từng điều kiện nhỏ:

Python

if len(password) < 8: return False
if not re.search(r"\d", password): return False # Nếu không tìm thấy số -> False
# ... kiểm tra tiếp chữ hoa ...
return True
Test Case:

Python

print(check_password("123456"))         # False (Ngắn)
print(check_password("abcdefgh"))       # False (Thiếu số, thiếu hoa)
print(check_password("Abcdefgh"))       # False (Thiếu số)
print(check_password("Abcdef12"))       # True
"""

def check_password(password) : 
    if len(password) < 8 : return False
    if not re.search(r"\d",password ): return False
    if not re.search(r"[A-Z]",password): return False
    return True

print(check_password("123456"))         # False (Ngắn)
print(check_password("abcdefgh"))       # False (Thiếu số, thiếu hoa)
print(check_password("Abcdefgh"))       # False (Thiếu số)
print(check_password("Abcdef12"))       # True