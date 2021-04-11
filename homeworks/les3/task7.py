"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба минимальны), так и различаться.
"""

import random

random_list = [random.randint(-10, 10) for _ in range(0, 10)]
print(random_list)

first_min = random_list[0]
second_min = None
for i, el in enumerate(random_list):
    if el < first_min:
        second_min = first_min
        first_min = el
        continue
    if el > first_min:
        if second_min is None or el < second_min:
            second_min = el
    if el == first_min and i != 0:
        second_min = first_min

print(f"Первое минимальное число: {first_min}, второе минимальное число: {second_min}")
