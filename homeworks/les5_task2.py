"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк.
Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик.
"""
from itertools import zip_longest
from collections import OrderedDict
from collections import defaultdict

test_input = "A2 * C4F"

hex_keys = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}

first_hex, operation, second_hex = test_input.split(" ")
first_hex = list(first_hex)
second_hex = list(second_hex)

first_hex = list(map(lambda x: int(hex_keys.get(x, x)), first_hex))
second_hex = list(map(lambda x: int(hex_keys.get(x, x)), second_hex))

if operation == "*":
    temp_list = second_hex
    d = defaultdict(int)
    for iKey, i in enumerate(reversed(first_hex)):
        remainder = 0
        jkey = 0
        for j in reversed(second_hex):
            in_cell = d[jkey + iKey]
            d[jkey + iKey] = (in_cell + remainder + (i * j)) % 16
            remainder = (in_cell + (i * j)) // 16
            jkey += 1
        while remainder > 0:
            d[jkey + iKey] += remainder
            remainder //= 16
            jkey += 1
        iKey += 1
elif "+" == operation:
    d = OrderedDict()
    remainder = 0
    for key, el in enumerate(zip_longest(reversed(first_hex), reversed(second_hex), fillvalue=0)):
        tmp = sum(el)
        d[key] = (tmp + remainder) % 16
        remainder = tmp // 16
    while remainder > 0:
        d["last"] = remainder
        remainder //= 16

hex_keys = {val: key for key, val in hex_keys.items()}
result = list([hex_keys.get(val, val) for key, val in d.items()])
result.reverse()
print(result)

