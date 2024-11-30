import math
def gaz(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return gaz(n, divisor + 1)
n = int(input("Введите натуральное число n > 1: "))
if gaz(n):
    print("YES")
else:
    print("NO")