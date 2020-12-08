"""
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
"""
char_num = int(input("Введите номер буквы латинского алфавита (0-25): "))
start_sym = ord('a')
symbol = chr(start_sym + char_num)
print(symbol)