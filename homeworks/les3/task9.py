"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""
import random

dimension = 4
M = [[random.randint(-10, 10) for _ in range(0, dimension)] for _ in range(0, dimension)]
print("Исходная матрица: ")
for line in M:
    for el in line:
        print(f"{el:>4}", end ="")
    print()

min_list = M[0]
for col in range(0, len(M)):
    for line in M:
        if line[col] < min_list[col]:
            min_list[col] = line[col]
print(f"Минимальные элементы столбцов: \n{min_list}")

max_el = min_list[0]
for el in min_list:
    if el > max_el:
        max_el = el
print("максимальный элемент среди минимальных элементов стобцов: ", max_el)


