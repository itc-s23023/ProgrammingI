#for i in range(4):
#    base_circle = ["●", "●", "●", "●"]
#    base_circle[i] = '○'
#    result = base_circle
#    print(" ".join(result))



len_circle = int(input())
for i in range(len_circle):
    base_circle = list('●' * len_circle)
    base_circle[i] = '○'
    result = base_circle
    print(" ".join(result))
