import networkx as nx
import matplotlib.pyplot as plt

# Створення зваженого графа
G = nx.Graph()

# Додавання вершин
nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
G.add_nodes_from(nodes)

# Додавання зважених ребер (дороги з вказаною довжиною)
edges = [
    ("A", "B", 4), ("A", "C", 2), ("B", "D", 5), ("C", "D", 1),
    ("C", "E", 6), ("D", "F", 3), ("E", "F", 2), ("E", "G", 5),
    ("F", "H", 4), ("G", "H", 3)
]
G.add_weighted_edges_from(edges)

# Функція для знаходження найкоротшого шляху за алгоритмом Дейкстри
def dijkstra_shortest_path(graph, start, goal):
    return nx.shortest_path(graph, source=start, target=goal, weight="weight")

# Виконання алгоритму Дейкстри
start_node, goal_node = "A", "H"
dijkstra_result = dijkstra_shortest_path(G, start_node, goal_node)
path_length = nx.shortest_path_length(G, source=start_node, target=goal_node, weight="weight")

# Виведення результатів
print(f"Найкоротший шлях за Дейкстрою від {start_node} до {goal_node}: {dijkstra_result}")
print(f"Загальна вага шляху: {path_length}")

# Візуалізація графа
plt.figure(figsize=(6, 6))
pos = nx.spring_layout(G)  # Розташування вершин
nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=1500, font_size=12)
edge_labels = {(u, v): w for u, v, w in edges}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Зважений транспортний граф")
plt.show()
