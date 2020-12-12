"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

import random

size = 10
array = [round(random.uniform(0, 50), 2) for i in range(size)]

print(array)


def merge_sort(array):
    if len(array) == 1:
        return array

    array1 = merge_sort(array[:len(array) // 2])
    array2 = merge_sort(array[len(array) // 2:])
    array.clear()
    i, j = 0, 0
    len_array1, len_array2 = len(array1), len(array2)

    while i < len_array1 and j < len_array2:
        if array1[i] < array2[j]:
            array.append(array1[i])
            i += 1
        else:
            array.append(array2[j])
            j += 1

    if i == len_array1:
        array.extend(array2[j:])
    if j == len_array2:
        array.extend(array1[i:])

    return array


merge_sort(array)
print(array)
