def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def divide_fractions(A, B, C, D):
    numerator = A * D
    denominator = B * C
    common_divisor = gcd(numerator, denominator)
    numerator //= common_divisor
    denominator //= common_divisor
    return numerator, denominator
A = int(input("Введите числитель первой дроби A: "))
B = int(input("Введите знаменатель первой дроби B: "))
C = int(input("Введите числитель второй дроби C: "))
D = int(input("Введите знаменатель второй дроби D: "))
if B == 0 or D == 0:
    print("Знаменатель не может быть равен нулю.")
else:
    result_numerator, result_denominator = divide_fractions(A, B, C, D)
    print(f"Результат деления: {result_numerator}/{result_denominator}")