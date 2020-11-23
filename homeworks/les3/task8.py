"""
Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""
M = []
for line in range(0, 4):
    row = []
    row_sum = 0
    for el in range(0, 4):
        user_val = int(input(f"введите элемент {el} строки {line} матрицы: "))
        row.append(user_val)
        row_sum += user_val
    row.append(row_sum)
    M.append(row)

for line in M:
    for el in line:
        print(f"{el:>4}", end ="")
    print()
