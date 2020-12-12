"""
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""

import random

m = 10
array = [random.randint(0, 10) for i in range(2 * m + 1)]
random.shuffle(array)
print(array)


def median(array, median_index=None):

    if median_index is None:
        median_index = len(array) // 2

    pivot = random.choice(array)
    left = [i for i in array if i < pivot]
    right = [i for i in array if i > pivot]
    equals = [i for i in array if i == pivot]

    if (len(left) + len(equals) - 1) >= median_index >= len(left):
        return pivot
    elif len(left) < median_index:
        return median(right, median_index - len(left) - len(equals))
    elif len(left) > median_index:
        return median(left, median_index)
    else:
        print('unexpected error')


def test_median(array):
    tmp = sorted(array)
    return tmp[len(array) // 2]


print('test_median: ', test_median(array))
print('my_median: ', median(array))
