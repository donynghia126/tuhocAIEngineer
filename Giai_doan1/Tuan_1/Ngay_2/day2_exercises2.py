"""
🔵 Bài 5: Giải phương trình bậc 2 ($ax^2 + bx + c = 0$)Mục tiêu: Kết hợp if-else phức tạp và thư viện toán học math.Kiến thức toán:Tính Delta: $\Delta = b^2 - 4ac$Nếu $\Delta < 0$: Vô nghiệm.Nếu $\Delta = 0$: Nghiệm kép $x = -b / (2a)$.Nếu $\Delta > 0$: Hai nghiệm phân biệt:$$x_1 = \frac{-b + \sqrt{\Delta}}{2a}, \quad x_2 = \frac{-b - \sqrt{\Delta}}{2a}$$Gợi ý Code:Để dùng căn bậc 2, cần import math.Căn bậc 2 của delta: math.sqrt(delta).
"""
import math
print('Nhập a,b,c trong phương trình bậc 2 (ax^2 + bx + c = 0)')

a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

if a == 0 and b !=0:
    x = -c/b
    print(f"Nghiệm của phương trình là: { x}")
elif a == 0 and b ==0:
    print("Phương trình vô nghiệm") 
elif a == 0 and b ==0 and c ==0:
    print("Phương trình có vô số nghiệm")
else:
    delta = b**2 - (4*a*c)
    print(f"delta bằng {delta}")

    if delta < 0:
        print("Phương Trình Vô nghiệm")
    elif delta == 0:
        x = -b/(2*a)
        print(f"Phương trình có nghiệm kép là {x}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Phương trình có 2 nghiệm là {x1:.1f} và {x2:.1f}")

"""
🟣 Bài 6: Game đoán số (Random Number Guessing) - Dự án nhỏ
Mục tiêu: Dùng vòng lặp while và break. Đây là logic cơ bản của mọi Game.

Kịch bản:

Máy tính bí mật chọn một số ngẫu nhiên từ 1 đến 100 (dùng random.randint(1, 100)).

Bạn nhập dự đoán của mình.

Máy gợi ý:

Nếu bạn đoán thấp hơn số bí mật -> Máy bảo: "Thấp quá, tăng lên đi!"

Nếu bạn đoán cao hơn -> Máy bảo: "Cao quá, giảm xuống!"

Nếu đoán đúng -> Máy bảo: "Chúc mừng! Bạn đoán đúng rồi." -> Dừng vòng lặp (break).

(Nâng cao): Đếm xem bạn mất bao nhiêu lượt mới đoán trúng.
"""

import random
print("Chào mừng đến với game đoán số từ (1 đến 100)")
so_ngau_nhien = random.randint(1,100)

so_luot_doan = 0

while True:
    
    so_luot_doan +=1
    try:
        so_du_doan = int(input("Nhập số bạn đoán (từ 1 đến 100): "))
    except ValueError:
        print("Đã bảo là nhập số mà lại nhập chữ!")
        continue # Quay lại đầu vòng lặp
    if 1 <= so_du_doan <= 100:
        if so_du_doan == so_ngau_nhien:
            print(f"Chúc mừng số bạn đoán đúng là số {so_ngau_nhien} với {so_luot_doan} lần đoán.")
            break
        elif so_du_doan < so_ngau_nhien:
            print(f"số của bạn thấp hơn số bí mật")
        elif so_du_doan > so_ngau_nhien:
            print(f"số của bạn cao hơn số bí mật")
    else:
        print("Vui lòng Nhập số từ 1 đến 100 và nhớ không phải là chữ hay có dấu phẩy gì nhoa")  



