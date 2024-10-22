x = float(input("Введите пробег за первый день (км): "))
y = float(input("Введите пробег за все время (км): "))
day = 1
while x < y:
    x *= 1.1
    day += 1
print(day)