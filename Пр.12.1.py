def sum_of_digits(N):
    total = 0
    while N > 0:
        digit = N % 10
        total += digit
        N //= 10
    return total
N = int(input("Введите натуральное число: "))
result = sum_of_digits(N)
print("Сумма цифр числа:", result)
