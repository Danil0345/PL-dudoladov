array = []
n = int(input("Введите количество элементов массива: "))
for i in range(n):
    num = int(input(f"Введите элемент {i + 1}: "))
    array.append(num)
odd_numbers = [num for num in array if num % 2 != 0]
if odd_numbers:
    odd_numbers.sort(reverse=True)
    print("Массив из нечетных чисел в порядке убывания:", odd_numbers)
else:
    print("Нечетных чисел нет")