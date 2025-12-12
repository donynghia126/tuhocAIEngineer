import re

#NOTE: re.match - tìm kiếm ở đầu text - trả về Match object hoặc None
# my_str = "Hello, nice to meet you"
# match = re.match("Hello", my_str)
# print(match)
# print(match.span())
# print(match.group())



#NOTE: re.search - tìm kiếm bất kì vị trí nào text
# trả về Match object đầu tiền (có nhiều hơn cũng thế) hoặc None

# my_str = "Hello, nice to meet you meet"
# match = re.search("meet", my_str)
# print(match)
# print(match.span())
# print(match.group())

#NOTE: re.findall(): trả về list tất cả matches

# my_str = """Xin chào các bạn
#             Chúc các bạn buổi tối vui vẻ
#         """

# match = re.findall("bạn",my_str)
# print(match)

#NOTE: re.split(): Takes a string, splits it at the match points, returns a list

# my_str = "Xin chào các bạn, chào các bạn mình về đây"

# match = re.split("các",my_str, maxsplit=1)
# print(match)

#NOTE: re.sub() REplaces one or many matchs within a string
my_str = "tsuki ga kirei desu ne , tsuki ga kirei!!!, tsuki ga kirei!!!"

new_str = re.sub("tsuki ga kirei","Anata no koto ga suki",my_str)

print(new_str)
