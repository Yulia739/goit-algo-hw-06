import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (вулиці, райони)
nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
G.add_nodes_from(nodes)

# Додавання ребер (дороги між районами)
edges = [
    ("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"),
    ("D", "F"), ("E", "F"), ("E", "G"), ("F", "H"), ("G", "H")
]
G.add_edges_from(edges)

# Функція для DFS
def dfs_path(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs_path(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None

# Функція для BFS
def bfs_path(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in path:
                if neighbor == goal:
                    return path + [neighbor]
                queue.append((neighbor, path + [neighbor]))
    return None

# Виконання алгоритмів
start_node, goal_node = "A", "H"
dfs_result = dfs_path(G, start_node, goal_node)
bfs_result = bfs_path(G, start_node, goal_node)

# Виведення результатів
print(f"DFS шлях від {start_node} до {goal_node}: {dfs_result}")
print(f"BFS шлях від {start_node} до {goal_node}: {bfs_result}")

# Візуалізація графа
plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=1500, font_size=12)
plt.title("Транспортна мережа міста")
plt.show()
