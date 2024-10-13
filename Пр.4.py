N = int(input("Введите количество чисел: "))
total = 0
for i in range(N):
    num = int(input("Введите число: "))
    total += num
print("Сумма чисел:", total)