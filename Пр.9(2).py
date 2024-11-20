def transform_matrix(matrix):
    n = len(matrix)
    transformed_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] < 0:
                transformed_matrix[i][j] = 0
            else:
                transformed_matrix[i][j] = 1
    return transformed_matrix
def print_lower_triangle(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i >= j:
                print(matrix[i][j], end=' ')
            else:
                print(' ', end=' ')
        print()
def main():
    n = int(input("Введите размер матрицы N: "))
    print("Введите элементы матрицы построчно:")
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Строка {i + 1}: ").split()))
        matrix.append(row)
    transformed_matrix = transform_matrix(matrix)
    print("Нижняя треугольная матрица:")
    print_lower_triangle(transformed_matrix)
if __name__ == "__main__":
    main()