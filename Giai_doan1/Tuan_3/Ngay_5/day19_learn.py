# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)

# my_nums = square_numbers([1,2,3,4,5])
# my_nums = (x*x for x in [1,2,3,4,5])

# print(list(my_nums))

# for num in my_nums:

#   print(num)


# nums = [1,2,3]


# i_nums = nums.__iter__()
# # print(i_nums)
# # print(dir(i_nums))

# while True:
#     try:
#         item = next(i_nums)
#         print(item)
#     except StopIteration:
#         break

# # for num in nums:
# #     print(num)

class MyRange:
    def __init__(self, start, end):
        self.value = start
        self.end = end
    
    def __iter__(self):
        return self
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value +=1
        return current
    

def my_range(start):
    current = start
    while True:
        yield current
        current +=1
        if current >20: break

# nums= MyRange(1,10)
nums= my_range(1)

print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))

for num in nums:
    print(num)



