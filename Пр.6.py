input_string = input("Введите строку: ")
replaced_string = input_string.replace('а', 'о')
replacement_count = input_string.count('а')
length_without_spaces = len(input_string.replace(" ", ""))
print("Строка после замены:", replaced_string)
print("Количество замен:", replacement_count)
print("Количество символов в строке без пробелов:", length_without_spaces)