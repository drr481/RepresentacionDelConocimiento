import networkx as nx

def chowliu(factores):
    informacion_mutua = []
    variables = set()
    for i in range(len(factores)):
        variables.add(factores[i].dependencias)
    for i in range(len(factores)):
        for j in range(i+1, len(factores)):
            informacion_mutua.append(calcular_informacion_mutua(factores[i], factores[j]))

    grafo = nx.Graph()




def calcular_informacion_mutua(factor1, factor2):
    pass