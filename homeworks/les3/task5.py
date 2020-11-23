"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
Это два абсолютно разных значения.
"""

import random

random_list = [random.randint(-10, 10) for _ in range(0, 20)]
print(random_list)

max_negative = 0
index_max = 0
negative_massive = []
for el in random_list:
    if el < 0:
        negative_massive.append(el)
        if el > max_negative or max_negative == 0:
            max_negative = el
            index_max = random_list.index(el)

print(max_negative, index_max)
