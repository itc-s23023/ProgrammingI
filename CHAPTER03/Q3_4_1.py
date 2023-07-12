for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1_3_5_7_9


for i in range(10):
    if i % 2 == 0:
        print(i)  # 0
        break
    print(i)
