import networkx as nx
import heapq
import matplotlib.pyplot as plt
G = nx.Graph()

stations = ["A", "B", "C", "D", "E", "F", "G", "H"]
G.add_nodes_from(stations)

edges = [
    ("A", "B", 4),
    ("A", "C", 3),
    ("B", "D", 2),
    ("C", "D", 4),
    ("C", "E", 7),
    ("D", "F", 5),
    ("E", "F", 1),
    ("F", "G", 2),
    ("G", "H", 3),
    ("E", "H", 6)
]
G.add_weighted_edges_from(edges)

# Алгоритм Дейкстри
def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    visited = set()
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Знаходження найкоротших шляхів з кожної вершини
shortest_paths = {}

for node in G.nodes:
    shortest_paths[node] = dijkstra(G, node)

# Виведення результатів
for source, targets in shortest_paths.items():
    print(f"Найкоротші відстані від {source}:")
    for target, distance in targets.items():
        print(f"  до {target}: {distance}")
    print()

# Візуалізація графа
pos = nx.spring_layout(G)  # Позиції для вершин
plt.figure(figsize=(8, 6))
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Граф з найкоротшими шляхами")
plt.show()
