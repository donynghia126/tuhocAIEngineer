lois = [
    {
        "id":1,
        "tên lỗi":"IndexError",
        "Tại sao lỗi":"cái index đó vượt quá số lượng index mất rồi. có 3 phần tử nhưng index lại quá rồi",
        "Code sửa lại":"cho thêm cái if vào nếu lớn hơn hoặc bằng 3 thì print cái đó ra còn không thì thôi"
    },
    {
        "id":2,
        "tên lỗi":"KeyError",
        "Tại sao lỗi":"Địa chỉ đào đâu ra za",
        "Code sửa lại":"Thêm cái địa chỉ vào cái list đó hoặc sử dụng cái get('dia_chi', 'Ở Ngoài Đường')  vào"
    },
    {
        "id":3,
        "tên lỗi":"TypeError",
        "Tại sao lỗi":"thằng là int còn thằng kia là string thì sao + nhỉ",
        "Code sửa lại":"thêm cái int() vào cái thuong nhỉ"
    },
    {
        "id":4,
        "tên lỗi":"IndentationError",
        "Tại sao lỗi":"làm con mà đòi ngang hàng với cha. không chịu thụt đầu dòng vào",
        "Code sửa lại":"thêm 'tab' ở print('xin chào Dony')"
    },
    {
        "id":5,
        "tên lỗi":"NameError",
        "Tại sao lỗi":"ket_qua còn chưa có mà đã sử dụng rồi. ",
        "Code sửa lại":"cho cái ket_qua  lên trên nào"
    }
]


bao_cao = "BÁO CÁO LỖI !! \n"
bao_cao += "-"*10 + "\n\n"

for loi in lois:
    bao_cao += f"Lỗi số: {loi['id']}. \n"
    bao_cao += f"Tên lỗi: {loi['tên lỗi']}.\n"
    bao_cao += f"Tại sao lỗi: {loi['Tại sao lỗi']}\n"
    bao_cao += f"Code sửa như thế nào: {loi['Code sửa lại']}\n"
    bao_cao += "-"*10 + "\n\n"

ten_file = "baocao.txt"
with open(ten_file,'w', encoding="utf-8")as f:
    f.write(bao_cao)

print(f"Đã in lỗi ra file{ten_file}")
print(bao_cao)