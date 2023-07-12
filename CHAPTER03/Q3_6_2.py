import random

nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
num4 = "".join(random.sample(nums, k=4))
while True:
    val = input("4桁の数字を入力して")
    if val == num4:
        break
    ans = ""
    for i in range(4):
        if num4[i] == val[i]:
            ans += num4[i]
        else:
            ans += "X"
    print(ans)
