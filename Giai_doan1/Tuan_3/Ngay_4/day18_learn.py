"""Gigher order function"""
#NOTE: Take one or more function as arguments - Nhận functions như tham số
def cal(nums):  #Hàm thông thường
    return sum(nums)

def higher_order_func_1(my_func, my_list): #My_func sẽ chính là tham số được truyền vào cho my_func
    my_sum = my_func(my_list)
    return my_sum

my_result = higher_order_func_1(cal,[3,4,5])

print(my_result)



#NOTE: Return a function as its result - trả về function (như kết quả trả về)

# Trả về hàm trong hàm
def cal_min(a,b):
    if a<b:
        return a
    else:
        return b
    
def cal_max(a,b):
    if a>b:
        return a
    else:
        return b

#đi tạo highter order function và trong này sẽ trả về hàm thông thường
def higher_order_func(cal_name):
    if cal_name == "min":
        return cal_min #Trả về tên của func đã định nghĩa ở trên cal_min
    elif cal_name == "max":
        return cal_max #trả về tên của func đã định nghĩa ở trên cal_max
    
#tính min
my_res = higher_order_func("min")
print(my_res(3,5))
#tính max
my_res = higher_order_func("max")
print(my_res(3,5))

"""Decorators - TH không có arguments (đối số)"""
#NOTE: dùng higher-order functtion thông thường
# Wrapper (hàm bao) và wrapped (hàm được bao)

# Dùng higher order function để thay đổi tính năng của wrapperd
def decoratoer_example(func):
    def wrapper():
        print("Before the functiion is called")
        func()
        print("After the functiion is called")
    return wrapper

@decoratoer_example # Chỉ sử dụng khi áp dụng decorator
def say_hello(): #hàm được bao
    print("hello")

"""
say_hello nó sẽ tương đương với decorator_example(sayhello)
say hello = decorator_example(sayhello)

say_hello() = wrapper()
"""

#NOTE Sử dụng higher order function nguyên bản
# my_func = decoratoer_example(say_hello)
# my_func()

#NOTE: sử dụng decorator
say_hello() #gọi trưc tiếp được hàm wrapped (hàm được bao)


"""Decorators - TH có arguments (đối số)"""

#NOTE: sử dụng higher-order function

# def decorator_function(func):
#     def wrapper(name,age):
#         print("Before the function is called")
#         func(name,age)
#     return wrapper

# #hàm được bao
# def say_hello1(name,age):
#     print(f"Hello {name}, you are {age} years old.")

# my_function = decorator_function(say_hello1)
# my_function("Dony",12)




#NOTE: áp dụng decorators - TH này có sử dụng arguments

def decorator_function(func):
    def wrapper(name,age):
        print("Before the function is called")
        func(name,age)
    return wrapper

#hàm được bao
@decorator_function
def say_hello1(name,age):
    print(f"Hello {name}, you are {age} years old.")

say_hello1("Dony",15)