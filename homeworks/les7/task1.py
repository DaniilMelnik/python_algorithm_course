"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
import random

size = 10
array = [random.randint(-100, 100) for i in range(size)]
print(array)


def bubble_sort(array):
    n = 1
    while n < len(array):
        swapped = False
        for j in range(len(array) - n):
            if array[j + 1] > array[j]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if not swapped:
            break
        n += 1


bubble_sort(array)
print(array)
