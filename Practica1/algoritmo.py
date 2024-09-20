import networkx as nx

def eliminar_hojas_todo(G, exp):
    lista = []
    for i in G.nodes():
        if i not in exp:
            elimina_hojas_recursivo(G, i, lista, exp)

def elimina_hojas_recursivo(G, nodo, lista, exp):
    lista.append(nodo)
    for hijo in G.successors(nodo):
        if hijo not in lista:
            elimina_hojas_recursivo(G, hijo, lista, exp)
    
    if len(G.successors(nodo)) == 0 and nodo not in exp:
        G.remove_node(nodo)