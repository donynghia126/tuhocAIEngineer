ma_tran_5x5 = [
    [0,0,1,0,0],
    [0,0,1,0,0],
    [1,1,1,1,1],
    [0,0,1,0,0],
    [0,0,1,0,0]
]

# ⬜,⬛
for x in ma_tran_5x5:
    for pixel in x:
        if pixel == 1:
            print("⬛", end = " ")
        else:
            print("⬜", end = " ")
    print()

print("-"*20)

ma_tran_5x5_2 = [
    [1,0,0,0,1],
    [0,1,0,1,0],
    [0,0,1,0,0],
    [0,1,0,1,0],
    [1,0,0,0,1]
]
for x in ma_tran_5x5_2:
    for pixel in x:
        if pixel == 1:
            print("⬛", end = " ")
        else:
            print("⬜", end = " ")
    print()

print("-"*20)
        
       
matrix_2x3 = [
    [1,2,3],
    [4,5,6]
]

sum_matrix = 0
for i in matrix_2x3:
    for j in i:
        sum_matrix += j

print(f"kết quả ma trận là {sum_matrix}")