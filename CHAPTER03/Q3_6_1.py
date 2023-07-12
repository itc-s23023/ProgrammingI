import random

s = str(random.randint(1000, 9999))

while True:
    user_input = input("4桁の数字を入力")

    if user_input == s:
        print("一致")
        break
    else:
        print("不一致")
