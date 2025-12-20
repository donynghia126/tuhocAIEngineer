"""1"""
def fibonacci_gen():
    a = 0
    b = 1
    while True:
        yield a
        a,b = b,a + b

fibo = fibonacci_gen()
        

i = 0
while i <= 5:
    print(next(fibo))
    i += 1

"""2"""


def batch_loader(data, batch_size):
    for i in range(0,len(data),batch_size):
        yield data[i:i+batch_size]

my_data = ["Ảnh 1", "Ảnh 2", "Ảnh 3", "Ảnh 4", "Ảnh 5", "Ảnh 6", "Ảnh 7"]
loader = batch_loader(my_data, batch_size=3)

for batch in loader:
    print(f"Đang train với batch: {batch}")