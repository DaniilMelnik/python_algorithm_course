"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
import random
from collections import deque

# тестовый граф из примера, для контроля
test_graph = [
    [1, 3, 4],
    [2, 5],
    [1, 6],
    [1, 5, 7],
    [2, 6],
    [6],
    [5],
    [6],
]


def generate_graph(n_vertex):
    graph = []

    for index, v in enumerate(range(n_vertex)):
        bounds = []
        length = random.randint(1, n_vertex - 1)
        while length > 0:
            bound = random.randint(0, n_vertex - 1)
            if bound == v or bound in bounds:  # граф без петель и связи не дублируются
                continue
            bounds.append(bound)
            length -= 1
        graph.append(bounds)

    # считаем ориентированный граф связным от точки 0 (как в примере), проверяем на связность
    is_visited = [False for _ in range(n_vertex)]
    is_visited[0] = True
    while not all(is_visited):
        deq = deque([0])
        while len(deq) > 0:
            current = deq.pop()
            for i, vertex in enumerate(graph[current]):
                if not is_visited[vertex]:
                    is_visited[vertex] = True
                    deq.appendleft(vertex)
        for index, vertex in enumerate(is_visited):  # если граф не связный, привязываем его к точке 0
            if not vertex:
                graph[0].append(index)
                break
    return graph


def depth_first_search(graph, visited=None, start=0):
    if len(graph[start]) == 0:
        return start
    if visited is None:
        visited = list()
        visited.append(start)

    for vertex in graph[start]:
        if vertex and vertex not in visited:
            visited.append(vertex)
            depth_first_search(graph, visited, vertex)

    return visited


if __name__ == '__main__':
    n = 6
    g = generate_graph(n)
    print("случайный граф: ", g, sep='\n')
    print(depth_first_search(g))
    print("тестовый граф: ", depth_first_search(test_graph), sep='\n')



