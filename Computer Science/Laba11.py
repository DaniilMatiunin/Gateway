import networkx as nx
import pylab
import matplotlib.pyplot as plt
import heapq
'''Напишите функцию реализуущую алгоритм Дейкстры.'''

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_vertex = heapq.heappop(queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Рассматриваем этот новый путь только в том случае, если он лучше любого пути, который мы нашли до сих пор
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

'''Сгенерируйте случайный взвешенный граф. И определите на нём маршрут минимальной длины с помощью алгоритма Дейкстры.'''
graph = {
    'A': {'B': 10, 'C': 32},
    'B': {'A': 10, 'C': 25},
    'C': {'A': 32, 'B': 25}
}
print(dijkstra(graph,'A'))

'''Проиллюстрируйте работу одного из алгоритмов (поиска в ширину или глубину, Дейкстры) с помощью визуализации 
действий с графом на каждой 
итерации с помощью библиотек networkx и matplotlib, аналогично примеру 1.'''
import networkx as nx
import pylab
import matplotlib.pyplot as plt
pos = {0: {1, 2},
       1: {3, 4},
       2: {1, 4},
       3: {4},
       4: {1, 3, 5},
       5: {0, 2}}
def bfs(graph, s, out=0):
    parents = {v: None for v in graph}
    level = {v: None for v in graph}
    level[s] = 0
    queue = [s]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if level[w] is None:
                queue.append(w)
                parents[w] = v
                level[w] = level[v] + 1
        pos = nx.spring_layout(graph)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500)
        nx.draw_networkx_nodes(G, pos, nodelist=[v], node_color='red', node_size=500)
        nx.draw_networkx_edges(G, pos)
        plt.show()
        if out: print(level[w], level, queue)
    return level, parents

N = len(pos)
G = nx.DiGraph()
a = [(i, j) for i in range(N) for j in pos[i]] # генерация списка рёбер
G.add_nodes_from(range(N))
G.add_edges_from(a)
bfs(pos, 0, 1)
'''Используйте какой-нибудь интересный алгоритм из'''
import networkx as nx

#efficiency
'''В Коэффициент E / I Кракхардта (или, по-разному, индекс E-I) - это показатель социальной сети, который измеряет о
тносительную плотность внутренних связей внутри социальной группы
 по сравнению с количеством связей, которые эта группа имеет с внешним миром'''
'''Отношение E / I связано с концепцией проводимости, которая измеряет вероятность того, что
 случайное блуждание на подграфе выйдет из этого подграфа.'''
#Эффективность пары узлов является мультипликативной величиной, обратной кратчайшему расстоянию между узлами
G = nx.Graph([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3)])
nx.efficiency(G, 2, 3)
print(nx.efficiency(G, 2, 3))