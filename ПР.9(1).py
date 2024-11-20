def main():
    n = int(input("Введите количество строк (n): "))
    m = int(input("Введите количество столбцов (m): "))
    matrix = []
    print("Введите элементы матрицы построчно:")
    for i in range(n):
        row = list(map(float, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)
    max_sum = float('-inf')
    min_sum = float('inf')
    max_row = []
    min_row = []
    for row in matrix:
        row_sum = sum(row)
        if row_sum > max_sum:
            max_sum = row_sum
            max_row = row
        if row_sum < min_sum:
            min_sum = row_sum
            min_row = row
    print(f"Строка с наибольшей суммой ({max_sum}): {max_row}")
    print(f"Строка с наименьшей суммой ({min_sum}): {min_row}")
if __name__ == "__main__":
    main()