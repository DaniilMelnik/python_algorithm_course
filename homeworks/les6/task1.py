"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""
import sys


def show_size(x, level=0):
    print('\t' * level,
          f'type = {x.__class__}, size = {sys.getsizeof(x)}, object = {x}, id = {id(x)}, reference = {sys.getrefcount(x)}',
          sep="")
    sum_of_elements = 0
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for el in x.items():
                sum_of_elements += show_size(el, level + 1)
        elif not isinstance(x, str):
            for el in x:
                sum_of_elements += show_size(el, level + 1)
    sum_of_elements += sys.getsizeof(x)
    print('\t' * level, f'итого, {sum_of_elements}', sep="")
    return sum_of_elements


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


print("version: ", sys.version, "platform: ", sys.platform)

# Решение при помощи вложенных циклов
def using_for():
    sum_of_memory = 0  # переменная для подсчета суммы
    for n in range(2, 10):
        sum_of_memory_m = 0  # переменная для суммы во внутреннем цикле
        n_divisible = 0
        for m in range(2, 100):
            if m % n == 0:
                n_divisible += 1
            sum_of_memory_m += memory(m)  # сумма памяти занимаемой целыми числами в range(2, 100)
        sum_of_memory += memory(n)  # сумма памяти занимаемой целыми числами в range(2, 10)
        if n == 9:  # учет временных переменных в последнем цикле
            sum_of_memory += memory(n_divisible) + sum_of_memory_m

        print(f"{n_divisible} чисел от 2 до 99 кратно числу {n}")
    print(sum_of_memory)  # 2996 байт
# функции range генерируют списки целых чисел от 2 до 100 и от 2 до 10 в циклах.
# В данном случае подсчитано количество памяти занимаемой сгенерированными целыми числами, и счетчика делителей.
# Конечно, поскольку range является особым итерируемым объектом расход памяти в нём скорее всего оптимизирован,
# но на основе информации из урока, проверить это затруднительно.

# решение с использованием цикла while
def using_while():
    i = 2
    while i < 10:
        n_divisible = 0
        j = 2
        while j < 400:
            if j % i == 0:
                n_divisible += 1
            j += 1
        i += 1
        print(f"{n_divisible} чисел от 2 до 99 кратно числу {i}")
    print(sys.getsizeof(i))
# В данном случае используются всего 3 переменные int расход памяти составляет 84 байта. Поскольку целые числа
# от -5 от 255 сохрняются в памяти при запуске интерпретатора, их id отличаются, но память для них выделять не нужно



if __name__ == '__main__':
    using_while()