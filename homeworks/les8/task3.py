"""
3. Написать программу, которая обходит не взвешенный ориентированный граф без петель, в котором все вершины связаны,
по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
"""
import random

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
#TODO все вершины должны быть связаны
def generate_graph(n_vertex):
    graph = []
    for v in range(n_vertex):
        bounds = []
        for el in range(random.randint(1, n_vertex)):
            bound = v
            while bound == v:  # т.к граф без петель
                bound = random.randint(0, n_vertex - 1)
            bounds.append(bound)
        graph.append(bounds)
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

print(generate_graph(4))

print(depth_first_search(test_graph))

# def depth_first_search_iterative(graph):
#     length = len(graph)
#     is_visited = [False] * length
#     is_visited[0] = True
#
#     way = []
#     start = 0
#     way.append(start)
#     while len(way) > 0:
#         for i, vertex in graph[way[start]]:
#             if vertex and not is_visited[i]:
#                 is_visited[i] = True
#                 way.append(vertex)
#
#     return visited



