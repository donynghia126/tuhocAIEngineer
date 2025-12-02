"""
🟢 Bài 1: Chuẩn hóa tên người dùng (Bắt buộc)
Đề bài: Người dùng nhập tên rất ẩu: name = " nGuyen vAN aNh " Yêu cầu:

Xóa hết khoảng trắng thừa ở đầu, đuôi và ở giữa các từ.

Viết hoa chữ cái đầu của từng từ (Title Case).

Kết quả mong muốn: "Nguyen Van Anh".

Gợi ý "Combo hủy diệt":

split() để tách thành list các từ sạch sẽ.

Dùng List Comprehension để title() từng từ.

join() lại thành chuỗi.
"""

name = " nGuyen vAN aNh "

chuan_hoa = " ".join(word.title() for word in name.split() )

print(chuan_hoa)

"""
🟡 Bài 2: Làm sạch dữ liệu rác (Data Cleaning)
Đề bài: Bạn crawl dữ liệu giá sản phẩm từ web về, nhưng nó bị dính ký tự lạ: prices = ["100.000đ", "20.500 VND", " 50000 ", "1.200.000 đ"]

Yêu cầu: Viết hàm clean_price(price_str) để:

Xóa bỏ chữ "đ", "VND", khoảng trắng.

Xóa bỏ dấu chấm . ngăn cách hàng nghìn.

Chuyển thành số nguyên (int).

Ví dụ: clean_price("1.200.000 đ") -> trả về số 1200000.
"""

prices = ["100.000đ", "20.500 VND", " 50000 ", "1.200.000 đ"]

def clean_price(price_str):
    clean_pr = int(price_str.replace("đ","").replace("VND","").replace(".","").replace(" ",""))
    return clean_pr

clean_data = [clean_price(price) for price in prices]
print(f"Cách 1: {clean_data}")

#cách 2

import re
def clean_price_pro(price_str):
    clean_str = int(re.sub(r'\D', "", price_str))
    return clean_str
clean_data_pro = [clean_price_pro(price) for price in prices]
print(f"Cách 2: {clean_data_pro}")

"""
🔴 Bài 3: Phân tích Log Server (Giả lập thực tế)
Đề bài: Server ghi lại log lỗi như sau: log = "ERROR:2025-12-02:Disconnection detected:User 123"

Yêu cầu: Hãy dùng split để tách chuỗi trên và in ra một Dictionary thông tin:

Python

{
    "type": "ERROR",
    "date": "2025-12-02",
    "message": "Disconnection detected", # Lưu ý phần này có thể chứa dấu :
    "user_id": "User 123"
}
Gợi ý: split có tham số maxsplit. Hãy thử log.split(":", 2) xem điều gì xảy ra?
"""

log = "ERROR:2025-12-02:Disconnection detected:User 123"

parts = log.split(":",2)
message , user_id = parts[2].split(":",1)

log_data = {
            "type":parts[0],
            "data":parts[1],
            "message":message,
            "user_id": user_id
        }


print(log_data)