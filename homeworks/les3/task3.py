"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
import random

random_list = [random.randint(-100, 100) for _ in range(0, 10)]
print(random_list)

max_index = 0
min_index = 0
for index, el in enumerate(random_list):
    if el > random_list[max_index]:
        max_index = index
    if el < random_list[min_index]:
        min_index = index
random_list[max_index], random_list[min_index] = random_list[min_index], random_list[max_index]
print(random_list)
