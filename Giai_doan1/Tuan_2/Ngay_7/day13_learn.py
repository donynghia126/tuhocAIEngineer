"""Xử lý ngoại lệ"""


my_dict = {"age":10,"name":"Dony"}
try:
    # reulult = 10 / 0
    my_value = my_dict["add"]
except ZeroDivisionError:
    print("Lỗi chia cho 0")
except KeyError:
    print("Lỗi keyerror")
print("bye bye")
print("-"*30)



try:
    num = int(input("Nhập vào 1 số: "))
    result = 100 / num
except ZeroDivisionError:
    print("Không thể chia cho 0")
    
except ValueError:
    print("Nhập sai rồi, hãy nhập số")

else:
    print("Nhập số OK, phép chia ok",result)

finally:
    print("hehe")