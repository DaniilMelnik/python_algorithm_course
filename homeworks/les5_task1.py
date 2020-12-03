"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала для
каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести
наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import ChainMap

good_factory = {}
bad_factory = {}
all_factory = ChainMap(good_factory, bad_factory)
while True:
    user_input = input("Введите наименование предприятия и прибыль за год через пробел(q для выхода): ")
    if user_input == 'q':
        print("средняя прибыль: ", sum(all_factory.values()) / len(all_factory))
        print("good_factory: \n", good_factory.keys())
        print("bad_factory: \n", bad_factory.keys())
        break
    try:
        name, profit = user_input.split(" ")
        profit = int(profit)
    except:
        print("ошибка ввода")
        continue
    if profit > 0:
        good_factory[name] = profit
    else:
        bad_factory[name] = profit

