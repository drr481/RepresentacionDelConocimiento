import networkx as nx
import matplotlib.pyplot as plt

def algoritmo_separacion(g, x_y, z):
   
    # Verificar que {X, Y} tenga exactamente 2 nodos y que estén en el grafo
    if len(x_y) != 2:
        raise ValueError("El conjunto {X, Y} debe contener exactamente 2 nodos.")
    for nodo in x_y:
        if nodo not in g:
            raise ValueError(f"El nodo {nodo} de X,Y no existe en el grafo.")
    # Verificar que todos los nodos de Z existan en el grafo
    for nodo in z:
        if nodo not in g:
            raise ValueError(f"El nodo {nodo} de Z no existe en el grafo.")
    
    xy_union_z = x_y.union(z)
    
    # Paso 1:Eliminar nodos hoja (sin hijos) que no estén en {X, Y} ∪ Z
    explorados = []
    for nodo in list(g.nodes):
        if nodo not in explorados:
            elimina_hojas_recursivo(g, nodo, x_y, z, explorados)
    # Paso 2: Unir padres con hijos en común e ignorar la dirección de las aristas
    nuevas_aristas = set()

    # Recorrer los nodos para encontrar padres con hijos en común
    for nodo in g.nodes:
        hijos = list(g.successors(nodo))  # Encontrar los hijos de cada nodo
        for hijo in hijos:
            padres = list(g.predecessors(hijo))  # Encontrar los padres de cada hijo
            if len(padres) > 1:  # Si hay más de un padre, conectar los padres
                for i in range(len(padres)):
                    for j in range(i + 1, len(padres)):
                        nuevas_aristas.add((padres[i], padres[j]))  # Agregar arista entre los padres

    # Añadir las nuevas aristas entre los padres
    g.add_edges_from(nuevas_aristas)

    # Convertir el grafo dirigido en no dirigido
    g2 = nx.Graph()

    g2.add_nodes_from(g.nodes)
    
    for u, v in g.edges:
        g2.add_edge(u, v)


    # Paso 3: Ver si hay caminos entre X e Y en el grafo modificado sin pasar por Z
    g2.remove_nodes_from(z)  # Eliminar los nodos de Z

    X = x_y.pop()
    Y = x_y.pop()
    nodos_visitados = set()
    return not busqueda_camino(g2,X,Y,nodos_visitados)

def elimina_hojas_recursivo(g,nodo,x_y,z,explorados):
    explorados.append(nodo)
    for i in list(g.neighbors(nodo)):
        if i not in explorados:
            elimina_hojas_recursivo(g, i, x_y, z, explorados)
            
    if nodo not in x_y and nodo not in z and len(list(g.successors(nodo))) == 0 :
        g.remove_node(nodo)
    return None 
        
    

# Función auxiliar para buscar un camino entre dos nodos en un grafo

def busqueda_camino(g,x,y,nodos_visitados):
    nodos_visitados.add(x)
    for nodo in g.neighbors(x):
        if nodo not in nodos_visitados:
            if nodo == y:
                return True
            else:
                return busqueda_camino(g,nodo,y,nodos_visitados)
    return False
# Ejemplo de uso
G = nx.DiGraph()

# Añadir nodos y aristas del ejemplo en la imagen
G.add_edges_from([('A', 'C'), ('B', 'C'), ('C', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')])

# Definir los conjuntos {X, Y} y Z
x_y = {'A','E'}  # Conjunto {X, Y}, debe tener 2 nodos
z = {'B'}         # Conjunto Z, puede tener 0 o más nodos

# Llamar a la función del algoritmo de separación
resultado = algoritmo_separacion(G, x_y, z)
print(resultado)
