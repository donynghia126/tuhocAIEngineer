"""
🟢 Bài 1: Bình phương (Transformation)
Đề bài: Cho list: numbers = [1, 2, 3, 4, 5] Hãy tạo list mới squared_numbers chứa bình phương của các số đó ([1, 4, 9, 16, 25]) dùng List Comprehension.
"""
numbers = [1, 2, 3, 4, 5]

squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers)

"""
🟡 Bài 2: Lọc dữ liệu (Filtering) - Refactor bài Chẵn/Lẻ tuần trước
Đề bài: Cho list hỗn hợp: data = [10, 3, 5, 8, 20, 7, 30] Hãy tạo list high_scores chỉ chứa các điểm số lớn hơn 10 và là số chẵn.
"""

data = [10, 3, 5, 8, 20, 7, 30]
high_scores = [x for x in data if x > 10 and x %2 == 0]
print(high_scores)

"""
🔴 Bài 3: Chuẩn hóa tên (String Processing)
Đề bài: Bạn có danh sách tên nhập ẩu: names = [" hOa ", " bInH", "cUoNg "] Dùng List Comprehension để tạo list mới sạch đẹp: ["Hoa", "Binh", "Cuong"]. Gợi ý: Dùng .strip() để cắt khoảng trắng và .title() để viết hoa chữ cái đầu.
"""
names = [" hOa ", " bInH", "cUoNg "]
true_name = [x.strip().lower().title() for x in names ]
print(true_name)


"""
⚫ Bài 4: Sắp xếp thông minh (Lambda)
Đề bài: Cho danh sách sản phẩm (Tên, Giá):

Python

products = [("Laptop", 1500), ("Mouse", 20), ("Keyboard", 50), ("Monitor", 300)]
Hãy sắp xếp danh sách này theo Giá giảm dần (Đắt nhất đứng đầu). Gợi ý: products.sort(key=lambda ..., reverse=True)
"""
products = [("Laptop", 1500), ("Mouse", 20), ("Keyboard", 50), ("Monitor", 300)]

products.sort(key=lambda x:x[1], reverse= True)
print(products)


import sys

# Tạo list 1 triệu số
my_list = [x for x in range(1000000)]
print(f"List tốn: {sys.getsizeof(my_list)} bytes bộ nhớ")

# Tạo generator 1 triệu số
my_gen = (x for x in range(1000000))
print(f"Generator tốn: {sys.getsizeof(my_gen)} bytes bộ nhớ")

"""
💡 Góc mở rộng (Senior Knowledge)
Mình sẽ tặng bạn thêm một kiến thức nâng cao (liên quan đến List Comprehension) để bạn "ngâm cứu" thêm. Cái này cực quan trọng khi làm việc với Big Data.

Vấn đề:
Giả sử bạn có list chứa 1 tỷ số. Nếu dùng List Comprehension [x**2 for x in range(1_000_000_000)]:

Máy tính sẽ tạo ra 1 tỷ số đó ngay lập tức.

RAM sẽ bị đầy -> Tràn bộ nhớ (Memory Error) -> Máy treo.

Giải pháp: Generator Expression (...)
Thay vì dùng ngoặc vuông [], ta dùng ngoặc tròn ().

Python

# List Comprehension (Tạo hết ngay lập tức -> Tốn RAM)
list_x = [x**2 for x in range(5)]
print(list_x) # Output: [0, 1, 4, 9, 16]

# Generator Expression (Tạo từng cái một khi cần -> Tiết kiệm RAM)
gen_x = (x**2 for x in range(5))
print(gen_x) # Output: <generator object ...> (Nó chưa tính đâu!)

# Muốn lấy giá trị thì phải duyệt qua
for so in gen_x:
    print(so) # Lúc này nó mới tính từng số và in ra
Bài tập phụ (Optional): Bạn thử chạy đoạn code này xem sự khác biệt về bộ nhớ (chỉ cần chạy thử để cảm nhận thôi):

Python

import sys

# Tạo list 1 triệu số
my_list = [x for x in range(1000000)]
print(f"List tốn: {sys.getsizeof(my_list)} bytes bộ nhớ")

# Tạo generator 1 triệu số
my_gen = (x for x in range(1000000))
print(f"Generator tốn: {sys.getsizeof(my_gen)} bytes bộ nhớ")
Bạn sẽ thấy con số chênh lệch cực khủng khiếp!
"""