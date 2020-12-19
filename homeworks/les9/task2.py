"""
2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from collections import (
    Counter,
    deque,
)


class Haffman_node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def get_table(self):
        tb = {}

        def _show(tree, path=''):
            if tree.data is not None:
                tb[tree.data] = path
                return
            if tree.left is not None:
                _show(tree.left, path + '0')
            if tree.right is not None:
                _show(tree.right, path + '1')

        _show(self)
        return tb


def Haffman(text):
    frequency = Counter(text).most_common()
    deq = deque()
    for el in frequency:
        deq.appendleft(el)
    while len(deq) > 1:
        leaf_left = deq.popleft()
        leaf_right = deq.popleft()

        if not type(leaf_left[0]) is Haffman_node:
            leaf_left = (Haffman_node(leaf_left[0]), leaf_left[1])
        if not type(leaf_right[0]) is Haffman_node:
            leaf_right = (Haffman_node(leaf_right[0]), leaf_right[1])
        bound = Haffman_node(None, leaf_left[0], leaf_right[0])

        weight = leaf_left[1] + leaf_right[1]
        index = 0
        for idx, el in enumerate(deq):
            if el[1] >= weight:
                break
            else:
                index += 1

        deq.insert(index, (bound, weight))

    res = deq[0][0]
    tb = res.get_table()
    result_text = ' '.join(format(tb[i]) for i in text)
    return result_text, tb


if __name__ == '__main__':
    test_string = 'beep boop beer!'
    print('Исходная строка в двоичном виде: ', ' '.join(format(ord(i), 'b') for i in test_string), sep='\n')
    result_string, table = Haffman(test_string)
    print('Закодированная строка: ', result_string)
    print('Таблица кодов: ', table)
