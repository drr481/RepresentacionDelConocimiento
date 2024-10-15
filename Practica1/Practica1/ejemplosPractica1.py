import networkx as nx
from Practica1 import algoritmo_separacion
import matplotlib.pyplot as plt

# Crea una lista de grafos con diferentes componentes conectadas
graphs = [nx.DiGraph() for _ in range(5)]

#1.Grafo sin componentes no conexos
graphs[0].add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'),

                           ('C', 'E'), ('D', 'F'), ('E', 'F')])

#2.Grafo que tiene 2 componentes no conexos
# Añadir el primer componente (A, B, C)
graphs[1].add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'A')])  
# Añadir el segundo componente (D, E, F)
graphs[1].add_edges_from([('D', 'E'), ('E', 'F'), ('F', 'D')])  

#3.Grafo que tiene todos los nodos unidos entre si (grafo completo con 6 nodos, no tiene nodos separables)
graphs[2].add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'F'),
                           ('B', 'C'), ('B', 'D'), ('B', 'E'), ('B', 'F'), 
                           ('C', 'D'), ('C', 'E'), ('C', 'F'), 
                           ('D', 'E'), ('D', 'F'), ('E', 'F')])

#4.Grafo cícliclo con 6 nodos
graphs[3].add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A')])


#5.Grafo vacío
#Sería el último grafo de la lista, graphs[4]


'''
Metodología para mostrar los grafos en uno de los cuadrantes resultantes de dividir la ventana
'''
# Crear una figura con 6 subplots (2 filas y 3 columnas)
fig, axes = plt.subplots(2, 3, figsize=(12, 8))

# Aplanar el array de ejes (axes) para fácil indexación
axes = axes.flatten()

    
# Dibujar cada grafo en su propio subplot
for i, G in enumerate(graphs):
    ax = axes[i]
    
    # Dibujar el grafo en el subplot correspondiente
    pos = nx.spring_layout(G)  # Posicionamiento del grafo
    nx.draw(G, pos, ax=ax, with_labels=True, node_color="skyblue", node_size=400, font_size=10, font_color="black", edge_color="gray", width=2)
    
    # Añadir título a cada grafo
    ax.set_title(f"Grafo {i+1}")

    if i == 4:
        ax.set_title("Grafo 5: vacío")

# El último subplot no debe mostrar nada
axes[-1].axis('off')  # Ocultar el último subplot

# Ahora dibujamos las líneas que dividen los cuadrantes en la figura principal
# Obtenemos el tamaño de la figura (ancho y alto)
fig_width, fig_height = fig.get_size_inches()

# Dibujar líneas divisorias
fig.subplots_adjust(wspace=0.3, hspace=0.3)  # Espacio entre subplots
plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

# Dibujar líneas verticales para dividir las columnas
fig.add_artist(plt.Line2D([0.33, 0.33], [0.05, 0.95], color='black', linewidth=5, transform=fig.transFigure))  # Línea 1/3
fig.add_artist(plt.Line2D([0.66, 0.66], [0.05, 0.95], color='black', linewidth=5, transform=fig.transFigure))  # Línea 2/3

# Dibujar línea horizontal para dividir las filas
fig.add_artist(plt.Line2D([0.05, 0.95], [0.5, 0.5], color='black', linewidth=5, transform=fig.transFigure))  # Línea 1/2

# Mostrar la figura con los grafos y las líneas divisorias
plt.show()



'''
Ejemplos de nodos que son separables en el grafo o no con
los distintos grafos que hay
'''

"1.Ejemplos para grafo 1: sin componentes no conexos"

#No Separables en el grafo
x_y = {'A', 'C'}
z = {'E'}
print("x_y:", x_y)
print("z:", z)
print(f"Resultados G{1}: {algoritmo_separacion(graphs[0], x_y, z)}\n")


#Separables en el grafo
x_y = {'D', 'E'}
z = {'C'}

#Cuando se llama a la función algoritmo_separacion, modifica el grafo y al volver a aplicar la función 
#se aplica sobre el grafo modificado, por lo que se debe volver a crear el grafo para usarlo de nuevo



graphs[0].add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'),

                           ('C', 'E'), ('D', 'F'), ('E', 'F')])
print("x_y:", x_y)
print("z:", z)
print(f"Resultados G{1}: {algoritmo_separacion(graphs[0], x_y, z)}\n")

"2.Ejemplos para grafo 2: tiene 2 componentes no conexos"

#No Separables en el grafo
x_y = {'A', 'C'}
z = {'B'}

print("x_y:", x_y)
print("z:", z)
print(f"Resultados G{2}: {algoritmo_separacion(graphs[1], x_y, z)}\n")
  

#Separables en el grafo
x_y = {'B', 'D'}
z = {'E'}


# Añadir el primer componente (A, B, C)

graphs[1].add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'A')])  # Grafo cíclico de 3 nodos

# Añadir el segundo componente (D, E, F)
graphs[1].add_edges_from([('D', 'E'), ('E', 'F'), ('F', 'D')])  # Otro grafo cíclico de 3 nodos

print("x_y:", x_y)
print("z:", z)
print(f"Resultados G{2}: {algoritmo_separacion(graphs[1], x_y, z)}\n")


"3.Ejemplos para grafo 3 (al ser un grafo completo, no hay nodos separables)"
# No Separables en el grafo
x_y = {'A', 'D'}
z = {'E'}

print("x_y:", x_y)
print("z:", z)
print(f"Resultados G{3}: {algoritmo_separacion(graphs[2], x_y, z)}\n")



#Grafo que tiene todos los nodos unidos entre si (grafo completo con 6 nodos)

x_y = {'A', 'C'}
z = {'D',  'E', 'F'}

graphs[2].add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('A', 'F'),
                           ('B', 'C'), ('B', 'D'), ('B', 'E'), ('B', 'F'), 
                           ('C', 'D'), ('C', 'E'), ('C', 'F'), 
                           ('D', 'E'), ('D', 'F'), ('E', 'F')])

print("x_y:", x_y)
print("z:", z)
print(f"Resultados G{3}: {algoritmo_separacion(graphs[2], x_y, z)}\n")

"4.Ejemplos para grafo 4"
# No Separables en el grafo
x_y = {'B', 'D'}
z = {'A', 'F'}

print("x_y:", x_y)
print("z:", z)
print(f"Resultados G{4}: {algoritmo_separacion(graphs[3], x_y, z)}\n")

# Separables en el grafo

x_y = {'B', 'D'}
z = {'A', 'C','E', 'F'}

graphs[3].add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E'), ('E', 'F'), ('F', 'A')])

print("x_y:", x_y)
print("z:", z)
print(f"Resultados G{4}: {algoritmo_separacion(graphs[3], x_y, z)}\n")


'''
Tratando errores
'''
#2 nodos o más  que no están en el grafo y un conjunto no vacío {Z} que tiene 1 nodo
#que está en el grafo
print("\n")
print("Prueba de errores 1")

x_y = {'D', 'K'}
z = {'E'}

print("x_y:", x_y)
print("z:", z)
resXYNoenG = [None] * 5 
for i in range(5):

    try:
        resXYNoenG[i] = algoritmo_separacion(graphs[i], x_y, z)  # Llama a la función y guarda el resultado en 'res[i]'
    except Exception as e:
        print(f"ErrorGrafo[{i + 1}]:", str(e))  # Muestra un mensaje si ocurre una excepción

# Crea un grafo con un conjunto con más de 2 nodos para x_y y 
#un conjunto no vacío {Z} que tiene 1 nodo
print("\n")

print("Prueba de errores 2")


x_y = {'D','E', 'F', 'G'}
z= {'C'}

print("x_y:", x_y)
print("z:", z)

resMas2NodosXY = [None] * 5

for i in range(5):

    try:
        resMas2NodosXY[i] = algoritmo_separacion(graphs[i], x_y, z)  # Llama a la función y guarda el resultado en 'res[i]'
    except Exception as e:
        print(f"ErrorGrafo[{i + 1}]:", str(e))  # Muestra un mensaje si ocurre una excepción


# Crea un grafo con un conjunto con 2 nodos para x_y y 
#un conjunto no vacío {Z} que tiene 1 nodo que no está en el grafo
print("\n")
print("Prueba de errores 3")


x_y = {'D','E'}
z = {'K'}
print("x_y:", x_y)
print("z:", z)

resZNoenG = [None] * 5
for i in range(5):

    try:
        resZNoenG[i] = algoritmo_separacion(graphs[i], x_y, z)  # Llama a la función y guarda el resultado en 'res[i]'
    except Exception as e:
        print(f"ErrorGrafo[{i + 1}]:", str(e))  # Muestra un mensaje si ocurre una excepción

