from dataclasses import astuple
import itertools
from math import log2
import random
from matplotlib import pyplot as plt
import networkx as nx



def ChowLiu(distribucion_probabilidad):
    

    #Paso 1: Encuentra el grafo completo tras calcular la informacion mutua que contiene las aristas con un determinado peso
    grafoPaso1 = Paso1ChowLiu(distribucion_probabilidad)
    #print(f"Grafo: {grafoPaso1[0]}\n Informacion mutua: {grafoPaso1[1]}")
    informacion_mutua = grafoPaso1[1]
    
    #Paso 2:Encuentra el arbol de recubrimiento maximo
    arbol_recubrimiento_maximo = Paso2ChowLiu(grafoPaso1[0], grafoPaso1[1])
  
    #Paso 3: Convierte el arbol de recubrimiento maximo en un arbol que tenga un nodo raiz y que es dirigido y muestra el arbol
    
    variable = random.choice(extraer_variables(informacion_mutua))
    Paso3ChowLiu(variable, arbol_recubrimiento_maximo)


def Paso1ChowLiu (distribucion_probabilidad):

    informacion_mutua = {}
    lista_tablas_distribucion = []
    variables = extraer_variables(distribucion_probabilidad)

    #Convertir a minusculas
    variables = [variable.lower() for variable in list(sorted(set(variables)))]
    lista_combinaciones = [list(p) for p in itertools.combinations(variables, 2)]
    nueva_lista_combinaciones = lista_combinaciones.copy()

    for variable in variables:
        lista_combinaciones.append(variable)
    
    #Obtengo las tablas de distribucion de probabilidad
    for i in range(len(lista_combinaciones)):
        lista_tablas_distribucion.append(extrae_tablas_distribucion(lista_combinaciones[i], distribucion_probabilidad))

    for i in range(len(nueva_lista_combinaciones)):
        informacion_mutua[tuple (nueva_lista_combinaciones[i])] = calcular_informacion_mutua(nueva_lista_combinaciones[i], lista_tablas_distribucion, nueva_lista_combinaciones, variables)

    
    informacion_mutua = {tuple(vertice.upper() for vertice in k): v for k, v in informacion_mutua.items()}

    #Creo un grafo completo que estará compuesto por las aristas que son las llaves del diccionario de la informacion mutua con un determinado peso
    grafo_completo = nx.Graph()


    variables = [variable.upper() for variable in variables]
    #print(f"Variables: {variables}")

    for variable in variables:
        print(f"Variable: {variable}")
        grafo_completo.add_node(variable)

    for llave, valor in informacion_mutua.items():
        #print(f"llave[0]: {llave[0]}")
        #print(f"llave[1]: {llave[1]}")
        #print(f"Valor: {valor}")
        grafo_completo.add_edge(llave[0], llave[1], weight=valor)
    
    #Dibujar el grafo
    #pos = nx.spring_layout(grafo_completo)
    #nx.draw(grafo_completo, pos, with_labels=True, node_color='skyblue', node_size=2500, font_size=10, font_color='black', font_weight='bold')
    #labels = nx.get_edge_attributes(grafo_completo, 'weight')
    #nx.draw_networkx_edge_labels(grafo_completo, pos, edge_labels=labels)
    #plt.show()

    #print(f"Informacion mutua: {informacion_mutua}")
       
    return grafo_completo, informacion_mutua

def Paso2ChowLiu (grafo_completo, informacion_mutua):


    '''
        
        lista_pesos_ordenados = []
        lista_nodos = []
        lista_aristas = []
        arbol_recubrimiento_maximo = nx.Graph()

        for aristas in grafo_completo.edges.data('weight'):
            print(type(aristas))
            for peso in aristas:
                if isinstance(peso, float):
                    print(f"Pesos de las aristas: {peso}")
                    lista_pesos_ordenados.append(peso)
        
        #Ordenar los pesos de las aristas de mayor a menor
        lista_pesos_ordenados = sorted(lista_pesos_ordenados, reverse=True)
        
        print(f"Lista de pesos ordenados: {lista_pesos_ordenados}")
        
    '''

    lista_nodos = []
    lista_aristas = []
    arbol_recubrimiento_maximo = nx.Graph()
    lista_variables = extraer_variables(informacion_mutua)
    print(f"Lista_variables Paso2: {lista_variables}")
    informacion_mutua_nuevo = dict(sorted(informacion_mutua.items(), key= lambda peso:peso[0], reverse= True))
    

        

    for arista in informacion_mutua_nuevo.keys():
        print(f"Arista pASO2: {arista}")

        if arista[0] not in lista_nodos:
            lista_nodos.append(arista[0])
            lista_aristas.append(arista)
        
        if arista[1] not in lista_nodos:
            lista_nodos.append(arista[1])
            lista_aristas.append(arista)
        
        if lista_nodos == lista_variables:
            break

    #Eliminar las aristas duplicadas
    #lista_aristas = list(set(lista_aristas))
    #print(f"Lista_Aristas sin duplicar:{lista_aristas}")

    #print(f"Lista de nodos: {lista_nodos}")
    #print(f"Lista de aristas: {lista_aristas}")
    
    #Creo el arbol de expansion maximo
    for vertice in lista_nodos:
    
        arbol_recubrimiento_maximo.add_node(vertice)
    
    for arista in lista_aristas:
        arbol_recubrimiento_maximo.add_edge(arista[0], arista[1], weight=informacion_mutua[arista])
    
    return arbol_recubrimiento_maximo
    #Dibujar el grafo
    #pos = nx.spring_layout(arbol_recubrimiento_maximo)
    #nx.draw(arbol_recubrimiento_maximo, pos, with_labels=True, node_color='skyblue', node_size=2500, font_size=10, font_color='black', font_weight='bold')
    #labels = nx.get_edge_attributes(arbol_recubrimiento_maximo, 'weight')
    #nx.draw_networkx_edge_labels(arbol_recubrimiento_maximo, pos, edge_labels=labels)
    #plt.show()
     
    #Ordena el mapa con los pesos de las aristas de mayor a menor
    #informacion_mutua = dict(sorted(informacion_mutua.items(), key=lambda item: item[1], reverse=True))
    #print(f"Mapa de informacion mutua ordenado: {informacion_mutua}")

    #Se puede usar el algoritmo de Prim o Kruskal para obtener el arbol de expansion minima
    #Podemos implementar esto desde 0
    #arbol_expansion_minima = nx.maximum_spanning_tree(grafo_completo, algorithm= 'prim', weight='weight')
    #print(f"Arbol de expansion minima: {arbol_expansion_minima.edges}")

    

def Paso3ChowLiu (raiz, arbol_recubrimiento_maximo):

    
    lista_aristas = AsignaDependencias(raiz, arbol_recubrimiento_maximo, [])

    print(f"Lista de aristas: {lista_aristas}")
    arbol_raiz = nx.DiGraph()

    for arista in lista_aristas:
        
        arbol_raiz.add_edge(arista[0], arista[1])
    
    pos = nx.spring_layout(arbol_raiz)
    nx.draw(arbol_raiz, pos, with_labels=True, node_color='skyblue', node_size=2500, font_size=10, font_color='black', font_weight='bold')
    plt.show()

    return arbol_raiz

    

def AsignaDependencias (raiz, arbol_recubrimiento_maximo, lista):
    
    return  AsignaDependenciasRec(raiz, arbol_recubrimiento_maximo, lista)
    
def AsignaDependenciasRec (raiz, arbol_recubrimiento_maximo, lista):

   
    
    
    #print(f"len(arbol_recubrimiento_maximo.neighbors()): {len(list(arbol_recubrimiento_maximo.neighbors(raiz)))}")
    #print(f"Lista: {lista}")
   
    if len(list(arbol_recubrimiento_maximo.neighbors(raiz))) == 0:
        
        return lista

    for i in list(set(arbol_recubrimiento_maximo.neighbors(raiz))):
        tupla = (raiz, i)
        #print(f"Arista: {tupla}")
        lista.append(tupla)
        arbol_recubrimiento_maximo.remove_edge(raiz, i)
        AsignaDependenciasRec(i, arbol_recubrimiento_maximo, lista)

    return lista
    

     

def calcular_informacion_mutua(lista_combinaciones_num, lista_tablas_distribucion, nueva_lista_combinaciones, variables):
   
    lista_dist_prob_denominador = {}
    #print(f"Lista de combinaciones: {lista_combinaciones_num}")
    #print(f"Lista de tablas de distribucion: {lista_tablas_distribucion}")

    #Mapa de distribucion de probabilidad que contiene las probabilidades del numerador
    dist_prob_numerador = numerador(lista_tablas_distribucion, lista_combinaciones_num, nueva_lista_combinaciones)

    #print(f"Numerador: {dist_prob_numerador}")
    #print(f"Lista de combinaciones despues de nunm: {lista_combinaciones_num}")
    variables_nuevas = []

    lista_combinaciones_denominador = nueva_lista_combinaciones.copy()

    for variable in variables:
        lista_combinaciones_denominador.append(variable)

    for variable in lista_combinaciones_num: #Obtengo las variables para el denominador
        variables_nuevas.append(variable)
    pass

    #Mapa de distribucion de probabilidad que contiene las probabilidades del denominador
    lista_dist_prob_denominador = denominador(variables_nuevas, lista_tablas_distribucion, lista_combinaciones_denominador)
    
    print(f"Dist_prob_numerador: {dist_prob_numerador}")
    print(f"Dist_prob_denominador: {lista_dist_prob_denominador}")

    

    #Obtengo los valores que deben haber en el numerador y denominador

    informacion_mutua = 0
    op_denominador = 1
    lista_op_numerador = []
    lista_op_denom = []

    
    for llavenum, valornum in dist_prob_numerador.items():
        lista_op_numerador.append(valornum)

        #Lo vuelvo a inciializar a 1 para que obtenga el siguiente denominador 
        op_denominador = 1 

        for llavedenom, valordenom in lista_dist_prob_denominador.items():
            
            
            if llavenum[0] == llavedenom or llavenum[1] == llavedenom:
                op_denominador *= valordenom

        #Agrego el denominador a la lista de operaciones   
        lista_op_denom.append(op_denominador)      
               
        

    #print(f"Lista de operaciones numerador: {lista_op_numerador}")
    #print(f"Lista de operaciones denominador: {lista_op_denom}")
    
        

    #Calculo la informacion mutua

    for i in range(len(lista_op_numerador)):
            
        #print(f"Lista de operaciones numerador: {lista_op_numerador[i]}")
        #print(f"Lista de operaciones denominador: {lista_op_denom[i]}")
        #print(f"Informacion mutua antes: {informacion_mutua}")
        informacion_mutua += lista_op_numerador[i] * log2(lista_op_numerador[i]/lista_op_denom[i])
        #print(f"Informacion mutua: {informacion_mutua}")

    return round(informacion_mutua,6)



def numerador(lista_tablas_distribucion, lista_combinaciones_num, nueva_lista_combinaciones):

    numerador = {}
    #print("Numerador")
    
    #print(f"Lista de tablas de distribucion: {lista_tablas_distribucion}")
    #Obtengo las tablas de distribucion de probabilidad que quiero según lo que quiero calcular
    #distribucion_probabilidad = {}
    for i in range(len(nueva_lista_combinaciones)):
        for llave, valor in lista_tablas_distribucion[i].items():

            #Compruebo si de las 2 variables que estoy buscando, la llave de la tabla de distribucion de probabilidad es igual a las 2 variables 
            if len(lista_combinaciones_num) == 2 and isinstance(llave, tuple):
                if llave[0][0] == lista_combinaciones_num[0] and llave[1][0] == lista_combinaciones_num[1]:
                    #print(f"lista_tabla_distribuciones[{i}]: {llave}")
                    #distribucion_probabilidad = lista_tabla_distribuciones[i].copy()
                    numerador[llave] = valor
            elif len(lista_combinaciones_num) == 1 and isinstance(llave, str):  
                if llave[0][0] == lista_combinaciones_num[0] :
                    #print(f"lista_tabla_distribuciones[{i}]: {llave}")
                    #distribucion_probabilidad = lista_tabla_distribuciones[i].copy()
                    numerador[llave] = valor
    

    return numerador


def denominador(variables_nuevas, lista_tablas_distribucion, nueva_lista_combinaciones):

    denominador1 = {}
    #print("Denominador")
    #print(f"Variables nuevas: {variables_nuevas}")
    #print(f"Lista de tablas de distribucion: {lista_tablas_distribucion[0]}")
    #print(f"Lista de combinaciones: {nueva_lista_combinaciones}")
    

    for variable in variables_nuevas:
        for i in range(len(nueva_lista_combinaciones)):
            #print(f"i: {i}")
            for llave,valor in lista_tablas_distribucion[i].items():

                #print(f"llave denom bucle: {llave}")

                #Compruebo si de las 2 variables que estoy buscando, la llave de la tabla de distribucion de probabilidad es igual a las 2 variables 
                #if isinstance(llave, tuple):
                    #if llave[0][0] == variable[0] and llave[1][0] == variable[1]:
                       
                        #denominador1[llave] = valor
                        #print(f"Denominador: {denominador1}")
                if isinstance(llave, str):  
                        if llave[0][0] == variable :
                            
                            denominador1[llave] = valor
                        #print(f"Denominador: {denominador1}")

    #print(f"Denominadorfinal: {denominador1}")
    
    return denominador1

def extrae_tablas_distribucion(lista_combinaciones, distribucion_probabilidad):

    
    nueva_distribucion_probabilidad_2_variables = {}
    
    # Redondear los valores
    nueva_distribucion_probabilidad_nuevo = marginaliza_distribucion_probabilidad(lista_combinaciones, distribucion_probabilidad, nueva_distribucion_probabilidad_2_variables) 
    

    return nueva_distribucion_probabilidad_nuevo


def marginaliza_distribucion_probabilidad(variables, distribucion_probabilidad, nueva_distribucion_probabilidad_2_variables):

    
    for llave, valor in distribucion_probabilidad.items():
     
        nueva_llave = tuple(filtro for filtro in llave for variable in variables if variable in filtro[0])
        #print(nueva_llave)
        
        # Si la nueva llave es una tupla de un solo elemento, convertirla a string
        if len(nueva_llave) == 1:
            nueva_llave = nueva_llave[0]
        
        # Agregar la nueva llave al mapa_nuevo
        # Verificamos si la nueva_llave ya está en el diccionario para evitar sobreescribir
        if nueva_llave in nueva_distribucion_probabilidad_2_variables:
            nueva_distribucion_probabilidad_2_variables[nueva_llave] += valor  # Si la llave ya existe, combinar los valores
        else:
            nueva_distribucion_probabilidad_2_variables[nueva_llave] = valor
    
    # Redondear los valores
    #print(f"nueva_distribucion_probabilidad_2_variables: {nueva_distribucion_probabilidad_2_variables}")
    nueva_distribucion_probabilidad_2_variables = {k: round(v, 6) for k, v in nueva_distribucion_probabilidad_2_variables.items()} 
    

    return nueva_distribucion_probabilidad_2_variables


def extraer_variables(distribucion_probabilidad):

    variables = []

    #Extraer variables de la distribucion de probabilidad
    for llave in distribucion_probabilidad.keys():
        for tupla in llave:
            variables.append(tupla[0])

    #Eliminar duplicados
    variables = list(sorted(set(variables)))

    #Convertir a mayusculas
    variables = [variable.upper() for variable in list(set(variables))]

    return variables

#if __name__ == "__main__":

    
    '''
    distribucion_probabilidad = {
        ('a^0','b^0','c^0'): 0.21,
        ('a^0','b^0','c^1'): 0.14,
        ('a^0','b^1','c^0'): 0.09,
        ('a^0','b^1','c^1'): 0.06,
        ('a^1','b^0','c^0'): 0.06,
        ('a^1','b^0','c^1'): 0.09,
        ('a^1','b^1','c^0'): 0.14,
        ('a^1','b^1','c^1'): 0.21
    }

    ChowLiu(distribucion_probabilidad)
    '''


    

            