"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random
import sys


def memory(x):
    sum_of_elements = 0
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for el in x.items():
                sum_of_elements += memory(el)
        elif not isinstance(x, str):
            for el in x:
                sum_of_elements += memory(el)
        elif isinstance(x, str):
            sum_of_elements = sys.getsizeof(x)
    sum_of_elements += sys.getsizeof(x)
    return sum_of_elements


def using_list():
    random_list = [random.randint(-10, 10) for _ in range(0, 20)]
    print(random_list)

    negative_massive = []
    for el in random_list:
        if el < 0:
            negative_massive.append(el)
    max_negative = max(negative_massive)
    index_max = random_list.index(max_negative)

    sum_of_memory = memory(negative_massive) + memory(index_max) + memory(max_negative)  # память потребляемая алгоритмом
    print(max_negative, index_max)

    print(sum_of_memory)  # результат (зависит от random_list)


def without_list():
    random_list = [random.randint(-10, 10) for _ in range(0, 20)]
    print(random_list)

    max_negative = 0
    index_max = 0
    for el in random_list:
        if el < 0:
            if el > max_negative or max_negative == 0:
                max_negative = el
                index_max = random_list.index(el)
    sum_of_memory = memory(index_max) + memory(max_negative)  # память потребляемая алгоритмом
    print(max_negative, index_max)

    print(sum_of_memory)  # результат 56 байт


def using_sort():
    random_list = [random.randint(-10, 10) for _ in range(0, 20)]
    print(random_list)
    max_negative = 0
    for el in sorted(random_list):
        if 0 > el > max_negative or max_negative == 0:
            max_negative = el
    sum_of_memory = memory(max_negative)
    print(max_negative, random_list.index(max_negative))
    print(sum_of_memory)  # результат 28 байт





if __name__ == '__main__':
    # using_list()
    # without_list()
    using_sort()