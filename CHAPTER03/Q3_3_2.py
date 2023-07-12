li = [1, 1, 2, 3, 5, 8, 13]
x = 0
for n in li:
    if n % 2 != 0:
        x += n
        print(x)  # 1_2_5_10_23
