
def create_report():
    cases = [
        {
            "id": 1,
            "error_name": "IndexError",
            "reason": "Truy cập vào chỉ số (index) không tồn tại trong list (ví dụ list có 3 phần tử nhưng gọi index 5).",
            "fixed_code": "my_list = [1, 3, 4]\nif len(my_list) > 5:\n    print(my_list[5])\nelse:\n    print('Index out of range')"
        },
        {
            "id": 2,
            "error_name": "KeyError",
            "reason": "Truy cập vào key không tồn tại trong dictionary.",
            "fixed_code": "my_dict = {'Name': 'Dony', 'age': 20}\n# Dùng .get() để tránh lỗi nếu key không có\nprint(my_dict.get('address', 'Key not found'))"
        },
        {
            "id": 3,
            "error_name": "TypeError",
            "reason": "Thực hiện phép toán cộng giữa số (int) và chuỗi (str) mà không chuyển đổi kiểu dữ liệu.",
            "fixed_code": "num = 10\nprint(str(num) + ' anh em')  # Chuyển num sang string trước khi cộng"
        },
        {
            "id": 4,
            "error_name": "ZeroDivisionError",
            "reason": "Cố gắng chia một số cho 0, điều này không được phép trong toán học và lập trình.",
            "fixed_code": "try:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print('Không thể chia cho 0')"
        },
        {
            "id": 5,
            "error_name": "NameError",
            "reason": "Sử dụng một biến chưa được khai báo hoặc gán giá trị trước đó.",
            "fixed_code": "my_var = 'Hello'\nprint(my_var)"
        }
    ]

    report_content = "BÁO CÁO LỖI PYTHON (BUG HUNTING REPORT)\n"
    report_content += "=" * 40 + "\n\n"

    for case in cases:
        report_content += f"{case['id']}. Case {case['id']}:\n\n"
        report_content += f"Tên lỗi: {case['error_name']}\n\n"
        report_content += f"Tại sao lỗi: {case['reason']}\n\n"
        report_content += f"Code sửa lại:\n{case['fixed_code']}\n"
        report_content += "-" * 30 + "\n\n"

    # Ghi ra file
    file_name = "report_day12.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(report_content)
    
    print(f"Đã tạo báo cáo thành công tại: {file_name}")
    print(report_content)

if __name__ == "__main__":
    create_report()
