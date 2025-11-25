"""
🟢 Bài 1: Phân tích điểm số (Master về List)
Mục tiêu: Tìm max, min, sắp xếp List.

Đề bài: Cho một danh sách điểm thi của lớp học: diem_so = [8.5, 4.0, 9.0, 6.5, 4.0, 10.0, 7.5]

In ra điểm cao nhất và thấp nhất (Dùng hàm max(), min() hoặc tự viết vòng lặp tìm).

Tính điểm trung bình của cả lớp.

Sắp xếp danh sách điểm theo thứ tự từ cao xuống thấp (Giảm dần).

In danh sách sau khi sắp xếp.

Gợi ý:

Sắp xếp giảm dần: diem_so.sort(reverse=True)
"""
diem_so = [8.5, 4.0, 9.0, 6.5, 4.0, 10.0, 7.5]

#Cách 1
diem_cao_nhat = max(diem_so)
diem_thap_nhat = min(diem_so)

print(f"Điểm cao nhất là: {diem_cao_nhat}")
print(f"Điểm thấp nhất là: {diem_thap_nhat}")


diem_trung_binh = sum(diem_so) / len(diem_so)
print(f"Điểm trung bình là {round(diem_trung_binh,2)}")

diem_so.sort(reverse=True)
print(f"Điểm số sắp xếp từ cao xuống thấp là {diem_so}")

#Cách 2
scores = [8.5, 4.0, 9.0, 6.5, 4.0, 10.0, 7.5]


maxScore = 0
minScore = scores[0]
sumScore = 0

for score in scores:
    sumScore = sumScore+score
    if score > maxScore:
        maxScore = score
    if score < minScore:
        minScore = score
print(f"Điểm cao nhất cách 2 là: {maxScore}")
print(f"Điểm thấp nhất cách 2 là: {minScore}")
print(f"Điểm trung bình là {round(sumScore/len(scores),2)}")

"""
🟡 Bài 2: Làm sạch dữ liệu (Master về Set)
Mục tiêu: Xóa phần tử trùng lặp.

Đề bài: Bạn thu thập được danh sách khách hàng đăng ký, nhưng hệ thống bị lỗi nên tên bị trùng lặp: names = ["An", "Binh", "Cuong", "An", "Dung", "Binh"]

Hãy tạo ra một danh sách mới chỉ chứa các tên duy nhất (không trùng).

Sắp xếp danh sách tên đó theo bảng chữ cái A-Z.

In ra số lượng khách hàng thực tế.

Gợi ý:

Cách nhanh nhất để khử trùng list: Ép kiểu sang Set -> set(names).

Sau đó ép ngược lại thành List để sắp xếp -> list(...).
"""

names = ["An", "Binh", "Cuong", "An", "Dung", "Binh"]
names = list(set(names))
names.sort()
print(f"Số lượng khách: {len(names)}")
print(names)

"""
Bài 3: Từ điển thuật ngữ AI (Master về Dictionary)
Mục tiêu: Thao tác thêm, sửa, xóa trong Dictionary.

Đề bài: Tạo một từ điển (dictionary) chứa các thuật ngữ:

Python

tu_dien = {
    "AI": "Tri tue nhan tao",
    "ML": "Hoc may",
    "DL": "Hoc sau"
}
Người dùng nhập vào một từ viết tắt (Ví dụ: "AI").

Nếu từ đó có trong từ điển -> In ra nghĩa tiếng Việt.

Nếu không có -> Hỏi người dùng nghĩa là gì và lưu từ mới đó vào từ điển.

In ra toàn bộ từ điển cập nhật cuối cùng.

Gợi ý:

Kiểm tra Key có trong Dict không: if key in tu_dien:

Thêm mới: tu_dien["key_moi"] = "gia_tri_moi"
"""

tu_dien = {
    "AI": "Tri tue nhan tao",
    "ML": "Hoc may",
    "DL": "Hoc sau"
}
print(f"Danh sách từ hiện có: {list(tu_dien.keys())}")

while True:
    tu_khoa = input("Nhập từ bạn muốn tra (gõ 'exit' để thoát'): ").upper()
    if tu_khoa == "EXIT":
        print("Tạm Biệt.")
        break
    if tu_khoa in tu_dien:
        print(f"Từ {tu_khoa} là {tu_dien[tu_khoa]}.")
        print("Bạn còn muốn tra từ nào nữa không ? Nếu không vui lòng gõ 'exit' để thoát.")
    if tu_khoa not in tu_dien:
        print("Xin lỗi vì từ này chưa có trong từ điển. Vui lòng bạn thêm vào giúp tui nhé. ")
        nghia_moi = input(f"từ {tu_khoa} nghĩa là: ")
        tu_dien[tu_khoa] = nghia_moi
        print("💾 Đã lưu từ mới thành công!")
        print(f"Danh sách từ hiện có: {list(tu_dien.keys())}")
    
print(f"Danh sách từ hiện có: {list(tu_dien.keys())}")