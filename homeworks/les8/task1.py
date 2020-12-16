"""
1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
Примечание. Решите задачу при помощи построения графа.
"""

n_friends = int(input("Введите количество друзей: "))

graph = [[1 if grip != man else 0 for grip in range(n_friends)] for man in range(n_friends)]
print(graph)

n_grips = 0
for el in graph:
    n_grips += sum(el)

print("Количество рукопожатий: ", n_grips)
