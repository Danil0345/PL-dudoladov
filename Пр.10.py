def read_matrix_from_file(filename):
    """
    Читает матрицу из файла.
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            matrix = [list(map(float, line.split())) for line in lines]
        return matrix
    except Exception as e:
        print(f"Ошибка при чтении файла {filename}: {e}")
        return None


def write_results_to_file(filename, max_row, max_sum, min_row, min_sum):
    """
    Записывает результаты в файл.
    """
    try:
        with open(filename, 'w') as file:
            file.write(f"Строка с наибольшей суммой ({max_sum}): {max_row}\n")
            file.write(f"Строка с наименьшей суммой ({min_sum}): {min_row}\n")
    except Exception as e:
        print(f"Ошибка при записи в файл {filename}: {e}")
def main():
    input_filename = "ДудоладовДД_У244_vvod.txt"
    output_filename = "ДудоладовДД_У244_vivod.txt"
    matrix = read_matrix_from_file(input_filename)
    if matrix is None:
        print("Ошибка: данные не были загружены.")
        return
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
    write_results_to_file(output_filename, max_row, max_sum, min_row, min_sum)
    print(f"Результаты записаны в файл: {output_filename}")
if __name__ == "__main__":
    main()
