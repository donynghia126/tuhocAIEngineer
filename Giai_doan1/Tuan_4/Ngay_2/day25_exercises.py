
#Bài 1

def matrix_add(matrix_a,matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if rows_a != rows_b or cols_a != cols_b:
        print("Ma trận không cùng kích thước")
        return None
    
    matrix_sum = []

    for i,j in zip(matrix_a,matrix_b):
        row_sum = []
        for x,y in zip(i,j):
            row_sum.append(x+y)
        matrix_sum.append(row_sum)
    
    return matrix_sum

"""
    Cách 2:

    def matrix_add_pro(A, B):
    # Dịch: Lấy x+y với x, y là từng cặp số trong từng cặp hàng của A và B
    return [[x + y for x, y in zip(r_a, r_b)] for r_a, r_b in zip(A, B)]

    Cách 3:

    def matrix_add(matrix_a, matrix_b):
    # 1. Kiểm tra kích thước (Optional nhưng nên làm cho quen tư duy)
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if rows_a != rows_b or cols_a != cols_b:
        return "Lỗi: Hai ma trận không cùng kích thước!"

    # 2. Thực hiện phép cộng
    result = []
    for i in range(rows_a):
        row_result = [] # Tạo hàng mới cho kết quả
        for j in range(cols_a):
            # Cộng phần tử tương ứng: A[i][j] + B[i][j]
            sum_val = matrix_a[i][j] + matrix_b[i][j]
            row_result.append(sum_val)
        result.append(row_result) # Đưa hàng đã cộng xong vào kết quả
    
    return result
"""
# --- TEST THỬ ---
A = [
    [1, 2, 3],
    [4, 5, 6]
]

B = [
    [10, 20, 30],
    [40, 50, 60]
]

print("Tổng 2 ma trận:")
tong = matrix_add(A, B)
for row in tong:
    print(row)

# Bài 2:

def matrix_scalar_mul(matrix, k):
    return [[j*k for j in i] for i in matrix ]



# --- TEST THỬ ---
C = [
    [1, -2],
    [3, 0]
]

print("\nNhân ma trận với 3:")
tich = matrix_scalar_mul(C, 3)
for row in tich:
    print(row)