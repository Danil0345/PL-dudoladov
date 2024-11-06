array = []
n = int(input("Введите количество элементов массива: "))
for i in range(n):
    num = int(input(f"Введите элемент {i + 1}: "))
    array.append(num)
max = array[0]
max_index = 0
for i in range(len(array)):
    if array[i] > max:
        max = array[i]
        max_index = i
print("Максимальный элемент:", max)
print("Порядковый номер (индекс):", max_index+1)