"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

random_list = [random.randint(-10, 10) for _ in range(0, 10)]
print(random_list)

max_index = 0
min_index = 0
for index, el in enumerate(random_list):
    if el > random_list[max_index]:
        max_index = index
    if el < random_list[min_index]:
        min_index = index

result = 0
if max_index > min_index:
    for el in range(min_index + 1, max_index):
        result += random_list[el]
    print(f"суммируемые числа {random_list[min_index + 1:max_index]}")
else:
    for el in range(max_index + 1, min_index):
        result += random_list[el]
    print(f"суммируемые числа {random_list[max_index + 1:min_index]}")
print(result)