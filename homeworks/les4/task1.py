"""
Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
Количество элементов (n) вводится с клавиатуры.
Реализовать несколько версий алгоритма.
Проанализировать скорость и сложность алгоритмов
"""

import cProfile


def test_series(func):
    lst = [1, 0.5, 0.75, 0.625, 0.6875, 0.65625, 0.671875, 0.6640625, 0.66796875]
    for i, el in enumerate(lst):
        print(f'{func(i)} OK')
        assert el == func(i)



def sum_of_series(n):
    result = 0
    for el in range(0, n + 1):
        result += pow(-1, el) / (2 ** el)
    return result


def sum_of_series2(n):
    result = 1
    addition = 1
    for el in range(0, n):
        addition = -1 * (addition / 2)
        result += addition
    return result

def sum_of_series_rec(n):
    if n == 0:
        return 1
    if n == 1:
        return 0.5
    return sum_of_series_rec(n - 1) + (sum_of_series_rec(n - 2) - sum_of_series_rec(n - 1)) / 2

def sum_from_gp(n):
    n_1 = 1
    step = -0.5
    n_sum = n_1 * (1 - step ** n) / (1 - step)
    return n_sum


test_series(sum_from_gp)
# print(sum_from_gp(6))

# def sum_of_series(n):
# Изначальная версия функции

# "task1.sum_of_series(100)"
# 1000 loops, best of 5: 56.3 usec per loop

# "task1.sum_of_series(500)"
# 1000 loops, best of 5: 448 usec per loop

# "task1.sum_of_series(1000)"
# 1000 loops, best of 5: 1.06 msec per loop

# "task1.sum_of_series(2000)"
# 1000 loops, best of 5: 2.77 msec per loop

# cProfile.run('sum_of_series(2000)')
# 101    0.000    0.000    0.000    0.000 {built-in method builtins.pow} 100
# 501    0.000    0.000    0.000    0.000 {built-in method builtins.pow} 500
# 1001    0.000    0.000    0.000    0.000 {built-in method builtins.pow} 1000
# 2001    0.001    0.000    0.001    0.000 {built-in method builtins.pow} 2000



# def sum_of_series2(n):
# Модифицированная версия функции

# "task1.sum_of_series2(100)"
# 1000 loops, best of 5: 7.31 usec per loop

# "task1.sum_of_series2(500)"
# 1000 loops, best of 5: 36.2 usec per loop

# "task1.sum_of_series2(1000)"
# 1000 loops, best of 5: 76.3 usec per loop

# "task1.sum_of_series2(2000)"
# 1000 loops, best of 5: 156 usec per loop

# cProfile.run('sum_of_series2(2000)')
# вложенных вызовов нет



# def sum_of_series_rec(n):
# Алгоритм с использованием рекурсии

# "task1.sum_of_series_rec(5)"
# 1000 loops, best of 5: 5.99 usec per loop
# "task1.sum_of_series_rec(10)
# 100 loops, best of 5: 513 usec per loop
# "task1.sum_of_series_rec(15)
# 100 loops, best of 5: 41.8 msec per loop

#cProfile.run('sum_of_series_rec(15)')

# 61/1    0.000    0.000    0.000    0.000 task1.py:31(sum_of_series_rec) 5
# 5044/1    0.001    0.000    0.001    0.001 task1.py:31(sum_of_series_rec) 10
# 413710/1    0.113    0.000    0.113    0.113 task1.py:31(sum_of_series_rec)
# 33929305/1    8.114    0.000    8.114    8.114 task1.py:31(sum_of_series_rec) 20