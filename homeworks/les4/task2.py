"""
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена».
"""

import cProfile

def test_simple(func):
    lst = [None, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for i, el in enumerate(lst):
        print(func(i))
        assert el == func(i)


def sieve_prime(n):
    size = 100
    sieve = [i for i in range(size)]
    sieve[1] = 0
    prime_n = 0
    while n != prime_n:
        for i in range(2, size):
            if sieve[i] != 0:
                prime_n += 1
            if prime_n == n:
                return sieve[i]
            j = i * 2
            while j < size:
                sieve[j] = 0
                j += i
        sieve.extend([i for i in range(size, size * 2)])
        size *= 2
        prime_n = 0

def sieve_optimized(n):
    size = 1000000
    sieve = [i for i in range(size)]
    sieve[1] = 0
    prime_n = 0
    while n != prime_n:
        for i in range(2, size):
            if sieve[i] != 0:
                prime_n += 1
            if prime_n == n:
                return sieve[i]
            if i*i < size:
                j = i * i
                while j < size:
                    sieve[j] = 0
                    j += i
        sieve.extend([i for i in range(size, size * 2)])
        size *= 2
        prime_n = 0

def prime(n):
    if n == 0:
        return None
    number = 1
    prime_n = 0
    while n != prime_n:
        number += 1
        is_prime = True
        for d in range(2, int(number ** 0.5)+1):
            if number % d == 0:
                is_prime = False
            d += 1
        if is_prime == True:
            prime_n += 1
    return number



#test_simple(prime)
#print(sieve_optimized(100))


# def sieve_prime(n):
# Скорость в том числе зависит от начального размера решета (size),
# Лучшие результаты получаются если изначальный размер решета включает в себя искомое число
# при минимальной величине size

# "import task2" "task2.sieve_prime(20)"
# 1000 loops, best of 5: 20.4 usec per loop

# "task2.sieve_prime(100)"
# 1000 loops, best of 5: 455 usec per loop

# "task2.sieve_prime(200)"
# 1000 loops, best of 5: 1.05 msec per loop

# "task2.sieve_prime(500)"
# 1000 loops, best of 5: 5.09 msec per loop


# вложенные вызовы характеризуют количество перестроений решета
# cProfile.run('sieve_prime(100)')
# 1    0.000    0.000    0.001    0.001 <string>:1(<module>)
# 1    0.001    0.001    0.001    0.001 task2.py:19(sieve_prime)
# 3    0.000    0.000    0.000    0.000 task2.py:34(<listcomp>)
# 3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
# cProfile.run('sieve_prime(500)')
# 1    0.000    0.000    0.006    0.006 <string>:1(<module>)
# 1    0.005    0.005    0.006    0.006 task2.py:19(sieve_prime)
# 6    0.000    0.000    0.000    0.000 task2.py:34(<listcomp>)
# 6    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


# def sieve_optimized(n):
# В целом резульаты лучше, но зависимость от начального размера решета сохраняется

# "task2.sieve_optimized(20)
# 1000 loops, best of 5: 14.8 usec per loop

# "task2.sieve_optimized(100)"
# 1000 loops, best of 5: 285 usec per loop

# "task2.sieve_optimized(200)"
# 1000 loops, best of 5: 647 usec per loop

# "task2.sieve_optimized(500)"
# 1000 loops, best of 5: 3.05 msec per loop


# cProfile.run('sieve_optimized(100)')
# 3    0.000    0.000    0.000    0.000 task2.py:54(<listcomp>)
# 3    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}

# cProfile.run('sieve_optimized(500)')
# 1    0.000    0.000    0.004    0.004 <string>:1(<module>)
# 1    0.003    0.003    0.003    0.003 task2.py:38(sieve_optimized)
# 6    0.000    0.000    0.000    0.000 task2.py:54(<listcomp>)
# 1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
# 6    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}


# def prime(n):
# Алгоритм, реализующий перебор делителей, значительно медленнее решета
# "task2.prime(20)"
# 1000 loops, best of 5: 47.3 usec per loop
# "task2.prime(100)"
# 1000 loops, best of 5: 657 usec per loop
# "task2.prime(200)"
# 1000 loops, best of 5: 2.03 msec per loop
# "task2.prime(500)"
# 1000 loops, best of 5: 9.96 msec per loop

# cProfile.run('prime(500)')
# вложенных вызовов нет