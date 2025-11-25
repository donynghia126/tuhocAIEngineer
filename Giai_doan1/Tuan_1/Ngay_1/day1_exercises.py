"""Bài 1: Tạo "Card Visit" điện tử
Mục tiêu: Làm quen với biến (variable) và cách in chuỗi (string formatting).

Đề bài: Viết một chương trình lưu trữ thông tin cá nhân của bạn vào các biến, sau đó in ra màn hình một đoạn giới thiệu ngắn gọn.

Yêu cầu:

Tạo biến ho_ten (kiểu chữ) để lưu tên bạn.

Tạo biến tuoi (kiểu số nguyên) để lưu tuổi.

Tạo biến chuyen_nganh (kiểu chữ) để lưu ngành học (ví dụ: IT).

Tạo biến truong (kiểu chữ) để lưu tên trường (Shimane IT College).

Dùng lệnh print để in ra một câu hoàn chỉnh ghép các thông tin trên.

💡 Hướng dẫn (Gợi ý):

Để ghép biến vào trong chuỗi in ra, cách chuyên nghiệp nhất hiện nay là dùng f-string.

Cú pháp: f"Xin chào {ten_bien}, hôm nay trời đẹp."
"""



ho_ten = "Dony"
tuoi = 20
chuyen_nganh = "IT"
truong = "shimade"

print(f"Xin chào tôi tên là {ho_ten}. Năm nay tôi {tuoi} tuổi. Tôi đang học tại {truong} và chuyên ngành {chuyen_nganh}")

"""
 Bài 2: Công cụ chuyển đổi nhiệt độ (C to F)Mục tiêu: Hiểu về nhập dữ liệu từ bàn phím (input) và ép kiểu số thực (float).Đề bài:Bạn bè quốc tế thường dùng độ F, còn Việt Nam/Nhật Bản dùng độ C. Hãy viết công cụ giúp bạn nhập vào độ C và máy tính tự quy đổi ra độ F.Yêu cầu:Hiển thị dòng chữ: "Nhập nhiệt độ C: ".Cho người dùng nhập số vào.Tính toán ra độ F.In kết quả ra màn hình theo format: ... độ C tương đương với ... độ F.🧮 Công thức:$$F = (C times 1.8) + 32$$💡 Hướng dẫn (Gợi ý):Hàm input() luôn luôn trả về dữ liệu dạng chữ (string), kể cả khi bạn gõ số.Để tính toán được, bạn phải ép nó sang dạng số thực. Dùng hàm float().Ví dụ: do_c = float(input("..."))
 """

do_C = float(input("Nhập độ C: "))

do_F = (do_C*1.8) + 32

print(f"{do_C} độ C tương đương với {do_F} độ F")

"""
Bài 3: Tính Tiền Yên Nhật sang VND (Thực tế cho bạn)
Mục tiêu: Làm quen với hằng số và toán tử nhân.

Đề bài: Bạn đi siêu thị ở Nhật và muốn biết món đồ này trị giá bao nhiêu tiền Việt Nam. Hãy viết tool tính nhanh.

Yêu cầu:

Khai báo một biến tỉ giá cố định (ví dụ: 1 Yên = 165 VND).

Cho người dùng nhập số tiền Yên (JPY) muốn đổi.

Tính ra số tiền VND.

In kết quả.

💡 Hướng dẫn (Gợi ý):

Tiền VND thường là số nguyên, bạn có thể dùng int() để ép kiểu kết quả cuối cùng cho đẹp (bỏ phần thập phân .0 thừa thãi).

Khi in số tiền lớn, có thể dùng dấu phẩy ngăn cách hàng nghìn cho dễ đọc. (Google thử từ khóa: "python f-string comma separator" xem sao nhé, cái này tự tìm hiểu sẽ nhớ dai hơn).
"""

ti_gia = 165

so_tien_yen = int(input("Nhập số tiền yên (JPY) muốn đổi: "))

so_tien_viet = so_tien_yen * ti_gia 

print(f"{so_tien_yen} Yên quy ra tiền Việt là {so_tien_viet:,} VND")

"""

Bài 4: Tính chỉ số BMI (Bài tập tư duy)Mục tiêu: Kết hợp tất cả kiến thức: Input, ép kiểu, toán tử mũ (**), và làm tròn số.Đề bài:Viết chương trình kiểm tra chỉ số khối cơ thể (BMI).Yêu cầu:Nhập cân nặng (tính bằng kg).Nhập chiều cao (tính bằng cm - lưu ý là cm nhé).Đổi chiều cao từ cm sang m.Tính BMI theo công thức.In kết quả BMI ra màn hình, làm tròn lấy 2 chữ số thập phân.🧮 Công thức:$$BMI = \frac{Cân nặng}{(Chiều cao đổi ra mét)^2}$$💡 Hướng dẫn (Gợi ý):Trong Python, phép lũy thừa (mũ 2) không dùng ^ mà dùng **. Ví dụ: $3^2$ viết là 3**2.Để làm tròn 2 chữ số thập phân trong f-string, dùng cú pháp :.2f. Ví dụ: f"Kết quả là {bien_so:.2f}".
"""

can_nang = float(input("Nhập Cân Nặng(kg): "))
chieu_cao_cm = float(input("Nhập Chiều Cao(cm): "))
chieu_cao_m = chieu_cao_cm/100

bmi = can_nang/chieu_cao_m**2

print(f"Kết quả BMI của bạn là: {bmi:.2f}")