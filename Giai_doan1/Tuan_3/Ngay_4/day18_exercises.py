
"""1"""
def nhan_doi(x): 
    return x*2
def binh_phuong(x): 
    return x*x

def ap_dung(func, danh_sach):
    return [func(x) for x in danh_sach]

print(ap_dung(nhan_doi,[1,2,3]))
print(ap_dung(binh_phuong,[1,2,3]))

print("-" * 20)

"""2"""

def ham_goc():
    print("Tôi là hàm gốc")

def trang_tri(func):
    def wrapper():
        print("--Bắt đầu trang trí--")
        func()
        print("--Kết thúc trang trí--")
    return wrapper

ham_moi = trang_tri(ham_goc)
ham_moi()
print("-"*20)

"""3"""

import time

def timer(func):
    def wrapper(*args,**kwargs): #cân được mọi loại tham số
        t1 = time.time()
        result = func(*args,**kwargs)
        t2 = time.time()
        print(f"Hàm {func.__name__} chạy mất {t2-t1} giây")
        return result
    return wrapper

@timer
def train_model_fake(epochs):
    print(f"Đang train model với {epochs} epochs...")
    time.sleep(2)
    return "model Accuracy : 99%"

ket_qua = train_model_fake(10)
print("Kết quả nhận được:", ket_qua)
print("-"*20)

"""4"""

def debug(func):
    def wrapper(*args,**kwargs):
        print(f"[Debug] Đang gọi hàm {func.__name__}")
        print(f"[Debug] Tham số args = ({args} , kwargs = {kwargs})")
        result = func(*args,**kwargs)
        print(f"[Debug] kết quả: {result}")
        return result
    return wrapper

@debug
def add(a,b):
    return a + b

@debug
def loichao(ten, loichao = "hello"):
    return f"{loichao} {ten}"

add(25,62)
loichao("Dony","Xin chào")

