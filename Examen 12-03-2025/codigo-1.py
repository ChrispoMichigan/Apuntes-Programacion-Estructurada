import random

c = 0
for x in range(1, 101):
    num = random.randint(1, 100)
    if num % 2 == 0:
        c += 1

print(f"Hay {c} números pares")
