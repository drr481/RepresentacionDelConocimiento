import networkx as nx
import algoritmo as alg
import matplotlib.pyplot as plt

# Crear un grafo dirigido
G = nx.DiGraph()

# Añadir nodos
vertices = [1, 2, 3, 4, 5, 6]
G.add_nodes_from(vertices)

# Añadir aristas (edges)
aristas = [(1, 3), (2, 3), (3, 4), (3, 5), (5, 6), (4, 6)]
G.add_edges_from(aristas)

# Dibujar el grafo
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
plt.show()

alg.eliminar_hojas_todo(G, [1,5,2])

# Dibujar el grafo
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=15)
plt.show()
