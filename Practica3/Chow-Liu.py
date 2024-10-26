from dataclasses import astuple
import itertools
from math import log2
from matplotlib import pyplot as plt
import networkx as nx
from numpy import split

def algoritmo1(distribucion_probabilidad):

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

    #variables = [variable.upper() for variable in variables]
    print(f"Variables: {variables}")

    for variable in variables:
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
                        if llave[0][0] == variable[0] :
                            
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

if __name__ == "__main__":

    

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
  

    algoritmoPaso1 = algoritmo1(distribucion_probabilidad)
    print(f"Grafo: {algoritmoPaso1[0]}\n Informacion mutua: {algoritmoPaso1[1]}")
   
    
    

    

            