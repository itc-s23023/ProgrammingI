"""
table = [f"{i} x {j} = {i*j}" for i in range(1, 10) for j in range(1, 10)]
for v in range(0, len(table), 9):
    print('\t'.join(table[v:v+9]))
"""

for i in range(1, 10):
    print("".join(f"{i * j:4}" for j in range(1, 10)))
