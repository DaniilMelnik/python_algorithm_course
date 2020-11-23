"""
Определить, какое число в массиве встречается чаще всего.
"""
from collections import defaultdict
import random

random_list = [random.randint(0, 10) for _ in range(0, 50)]
print(random_list)
temp_dict = defaultdict(int)
for el in random_list:
    temp_dict[el] += 1
max_key = 0
max_val = 0
for key, val in temp_dict.items():
    if val > max_val:
        max_key = key
        max_val = val
print(f"{max_key} встречается чаще всего: {max_val} раз")




