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

# Візуалізація графа
plt.figure(figsize=(6, 6))
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray", node_size=1500, font_size=12)
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз характеристик графа
print(f"Кількість вершин: {G.number_of_nodes()}")
print(f"Кількість ребер: {G.number_of_edges()}")
print("Ступінь кожної вершини:")
for node, degree in G.degree():
    print(f"Вершина {node}: {degree}")
