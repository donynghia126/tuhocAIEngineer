"""
🟢 Bài 1: Từ điển Anh - Việt (Phiên bản "Không Crash")
Mục tiêu: Áp dụng .get() để xử lý lỗi.

Đề bài: Cho sẵn một từ điển:

Python

data = {
    "hello": "xin chào",
    "love": "yêu",
    "computer": "máy tính",
    "code": "mã lệnh"
}
Yêu cầu:

Cho người dùng nhập 1 câu tiếng Anh bất kỳ (ví dụ: "I love computer code").

Tách câu đó thành các từ riêng biệt (dùng .split()).

Dịch từng từ sang tiếng Việt.

Nếu từ đó có trong data: In nghĩa tiếng Việt.

Nếu không có: Giữ nguyên từ tiếng Anh.

Ghép lại thành câu hoàn chỉnh và in ra.

Ví dụ:

Input: "hello computer"

Output: "xin chào máy tính"
"""

data = {
    "hello": "xin chào",
    "love": "yêu",
    "computer": "máy tính",
    "code": "mã lệnh"
}


while True:
    input_tu = input("Nhập từ cần dịch (Gõ 'Thoát' thể thoát): ")
    tu_can_dich = input_tu.split()
    tu_da_dich = []
    if input_tu.lower() == "thoát":
        print("Đã thoát chương trình!")
        break
    for tu in tu_can_dich:
        nghia = data.get(tu.lower(),tu)
        tu_da_dich.append(nghia)
    print(f"Nghĩa là : {' '.join(tu_da_dich)}")

"""
🔴 Bài 2: Đếm tần suất từ (Word Frequency Counter) - 🔥 Bài tủ Data Science
Mục tiêu: Đây là bài toán cơ bản nhất của NLP (Xử lý ngôn ngữ tự nhiên). Bạn cần đếm xem mỗi từ xuất hiện bao nhiêu lần để biết văn bản nói về chủ đề gì.

Đề bài: Cho một đoạn văn bản dài:

Python

paragraph = "apple banana apple orange banana apple mango"
Yêu cầu:

Viết chương trình đếm số lần xuất hiện của từng loại quả.

Lưu kết quả vào một Dictionary dạng: {'apple': 3, 'banana': 2, 'orange': 1, ...}.

In ra loại quả nào xuất hiện nhiều nhất.

Gợi ý thuật toán:

Tách chuỗi thành list: words = paragraph.split().

Tạo một dict rỗng: counts = {}.

Duyệt qua từng từ trong list words:

Nếu từ đó đã có trong counts: Tăng giá trị lên 1 (counts[word] += 1).

Nếu từ đó chưa có: Gán giá trị bằng 1 (counts[word] = 1).
"""

paragraph = "apple banana apple orange banana apple mango mango mango mango"

paragraph_list = paragraph.split()
counts = {}
for word in paragraph_list:
    # if word in counts:
    #     counts[word] +=1
    # else:
    #     counts[word] = 1
    counts[word] = counts.get(word,0) + 1

print(f"Danh sách Dic: {counts}")

qua_nhieu_nhat = ""
so_lan = 0
for qua,so in counts.items():
    if counts[qua] > so_lan:
        qua_nhieu_nhat = qua
        so_lan = so

print(f"Quả xuất hiện nhiều nhất là {qua_nhieu_nhat} với {so_lan} lần")


#Nhanh hơn cho data
from collections import Counter

# Tự động đếm và trả về Dictionary
counts2 = Counter(paragraph_list) 

print(counts2) 
# Kết quả y hệt: Counter({'apple': 3, 'banana': 2, ...})
# Tìm key có value lớn nhất
qua_nhieu_nhat2 = max(counts, key=counts.get) 

print(f"Quả nhiều nhất là: {qua_nhieu_nhat2}")