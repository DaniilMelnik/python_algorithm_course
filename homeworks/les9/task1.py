"""
1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача
считается не решённой.
"""
import hashlib


def all_substrings(s: str) -> tuple:
    assert len(s) > 0, 'Строка не может быть пустой'

    result = 0
    subs = {}
    for len_sub in range(1, len(s)):
        for i in range(len(s) - len_sub + 1):
            hsub = hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest()
            if hsub not in subs.values():
                if s[i:i + len_sub] not in subs.keys():
                    subs[s[i:i + len_sub]] = hsub

                    result += 1

    return result, list(subs.keys())


if __name__ == '__main__':
    s = input('введите строку: ')
    res, keys = all_substrings(s)
    print(f'Количество подстрок в строке: "{s}"\nравно: {res}')
    print('Список подстрок: ', keys)
