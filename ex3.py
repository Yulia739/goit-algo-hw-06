import networkx as nx
import matplotlib.pyplot as plt

# Функція для створення графа
def create_weighted_graph():
    graph = nx.Graph()
    nodes = ["A", "B", "C", "D", "E", "F", "G", "H"]
    graph.add_nodes_from(nodes)
    
    edges = [
        ("A", "B", 4), ("A", "C", 2), ("B", "D", 5), ("C", "D", 1),
        ("C", "E", 6), ("D", "F", 3), ("E", "F", 2), ("E", "G", 5),
        ("F", "H", 4), ("G", "H", 3)
    ]
    
    graph.add_weighted_edges_from(edges)
    
    return graph, edges

# Функція пошуку найкоротшого шляху
def dijkstra_shortest_path(graph, source, destination):
    shortest_path = nx.shortest_path(graph, source=source, target=destination, weight="weight")
    path_length = nx.shortest_path_length(graph, source=source, target=destination, weight="weight")
    return shortest_path, path_length

# Ініціалізація графа
transport_graph, edge_weights = create_weighted_graph()
start_node, goal_node = "A", "H"
shortest_route, total_distance = dijkstra_shortest_path(transport_graph, start_node, goal_node)

# Виведення результатів
print(f"Найкоротший маршрут від {start_node} до {goal_node}: {shortest_route}")
print(f"Загальна вага шляху: {total_distance}")

# Візуалізація графа
plt.figure(figsize=(7, 7))
layout = nx.spring_layout(transport_graph, seed=42)
nx.draw(transport_graph, layout, with_labels=True, node_color="skyblue", edge_color="black", node_size=1600, font_size=14)
labels = {(u, v): w for u, v, w in edge_weights}
nx.draw_networkx_edge_labels(transport_graph, layout, edge_labels=labels)
plt.title("Оптимізований граф маршрутів")
plt.show()
