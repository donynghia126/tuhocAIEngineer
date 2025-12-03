"""
🟢 Bước 1: Tạo dữ liệu giả (Fake Data)
Vì bạn chưa có file log nào, hãy chạy đoạn code này trước để tạo ra file server.log chứa dữ liệu hỗn độn.

Python

# Chạy cái này 1 lần để tạo file log giả
# noi_dung_log = """#INFO:2024-01-01:Server started
# ERROR:2024-01-01:Database connection failed
# INFO:2024-01-02:User login success
# WARNING:2024-01-02:High memory usage
# ERROR:2024-01-03:Timeout error request 404
# INFO:2024-01-03:Logout success
"""

with open("server.log", "w", encoding="utf-8") as f:
    f.write(noi_dung_log)

print("Đã tạo file server.log thành công!")
🟡 Bước 2: Bài tập Lọc Lỗi (Log Filter)
Đề bài:

Đọc file server.log vừa tạo ở trên.

Tìm những dòng có chứa chữ "ERROR".

Ghi những dòng lỗi đó sang một file mới tên là error_only.txt.

In ra màn hình thông báo: "Đã trích xuất xong X dòng lỗi".

Gợi ý thuật toán:

Mở file server.log chế độ đọc (r).

Mở file error_only.txt chế độ ghi (w).

Duyệt từng dòng (for line in f_read:).

Nếu "ERROR" nằm trong line -> Ghi dòng đó sang file kia.


"""

with (open("server.log","r",encoding="utf-8") as f_in, open("error_only.txt","w", encoding="utf-8") as f_out):
    count = 0
    for line in f_in:
        if "ERROR" in line:
            count+=1
            f_out.write(line)

print(f"Đã trích xuất xong {count} dòng lỗi")

"""🔴 Bước 3 (Nâng cao): Đọc file cấu hình
Đề bài: Giả sử bạn có file config.txt chứa nội dung:

Plaintext

username:admin
password:123456
port:8080
Hãy viết hàm read_config(file_path) đọc file này và trả về một Dictionary: {'username': 'admin', 'password': '123456', 'port': '8080'}.

(Gợi ý: Dùng split(":") và strip() để làm sạch \n xuống dòng)."""
def read_config(file_path):
    dic = {}
    with open(file_path,"r",encoding="utf-8") as f:
        for line in f:
            key,value = line.split(":",1)
            dic[key.strip()] = value.strip()

    return dic




print(read_config("config.txt"))


    

    
