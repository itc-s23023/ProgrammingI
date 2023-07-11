import random
i = 0
while True:
    alphabet = random.choice('abcdefghijklmnopqrstuvwxyz')
    print(alphabet)
    i += 1
    if alphabet == 'h':
        print(str(i) + "回目です")
        break

