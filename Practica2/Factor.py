import numpy as np

class Factor:
    def __init__(self, identificador, valores_variablesdep, valores, propios, dependencias):
        """
        Inicializa un factor.
        - identificador: un carácter que identifica el nodo.
        - variables: lista de variables de las que depende el nodo.
        - valores: matriz de valores que representan el factor (condicionada a las variables).
        - propios: lista de valores propios que el nodo puede tomar.
        """
        self.identificador = identificador  # Identificador del nodo (carácter)
        self.valores_variablesdep = valores_variablesdep  # Valores propios de las variables de las que depende el nodo
        self.valores = valores  # Mapa que representa las probabilidades condicionales del nodo dado sus variables
        self.propios = propios  # Lista de valores propios del nodo
        self.dependencias = dependencias  # Lista de variables de las que depende el nodo

    def __str__(self):
        return f"Factor({self.identificador}: {self.valores_variablesdep},\n{self.valores}, \n{self.dependencias})"

    def imprimir(self):
        """
        Imprime las variables y los valores propios asociados al factor (el nodo).
        """
        print(f"Factor del nodo {self.identificador}:")
        print(f"Valores propios de las variables de las que depende: {self.valores_variablesdep}")
        print(f"Valores propios del nodo: {self.propios}")
        print(f"Dependencias: {self.dependencias}")
        print(f"Valores:\n{self.valores}\n")


def eliminacion(factores_marginalizados, variable_a_eliminar):
    """
    Elimina una variable de las que dependen los valores del factor. 
    """
    if variable_a_eliminar not in factores_marginalizados.dependencias:
        raise ValueError(f"La variable {variable_a_eliminar} no está en el factor.")
    
    factores_marginalizados.dependencias.remove(variable_a_eliminar) # Eliminar la variable de las dependencias del factor marginalizado

    nuevos_valores = {}
    

    for llave, valor in factores_marginalizados.valores.items():
        # Filtrar los elementos de la tupla que no contengan 'verde'
        nueva_llave = tuple(filtro for filtro in llave if variable_a_eliminar not in filtro)
        
        # Si la nueva llave es una tupla de un solo elemento, convertirla a string
        if len(nueva_llave) == 1:
            nueva_llave = nueva_llave[0]
        

        
        # Agregar la nueva llave al mapa_nuevo
        # Verificamos si la nueva_llave ya está en el diccionario para evitar sobreescribir
        if nueva_llave in nuevos_valores:
            nuevos_valores[nueva_llave] += valor  # Si la llave ya existe, combinar los valores
        else:
            nuevos_valores[nueva_llave] = valor
        
   # Redondear los valores al final antes de imprimir
    nuevos_valores = {k: round(v, 4) for k, v in nuevos_valores.items()} 
    


    print(f"nuevos_valores: {nuevos_valores}")
    
    nuevo_factor = Factor(factores_marginalizados.identificador,None, nuevos_valores, factores_marginalizados.propios, factores_marginalizados.dependencias)
    print(f"Eliminando la variable {variable_a_eliminar} del factor del nodo {factores_marginalizados.identificador}:")
    nuevo_factor.imprimir()
    
    return nuevo_factor


def producto_de_factores(factor1, factor2):
    """
    Realiza el producto de dos factores, buscando las variables comunes entre ellos
    para ajustar las probabilidades condicionales. Los valores resultantes se multiplican
    cuando coinciden las variables en común.
    """

    if (factor1.valores == {} or factor2.valores == {}) or \
        (isinstance(factor1.valores, dict) == False or isinstance(factor2.valores, dict) == False):

        raise ValueError("No hay valores en los factores para realizar el producto.")
    
    if factor1.dependencias == [] or factor2.dependencias == []:
        raise ValueError("No hay variables de dependencia en los factores para realizar el producto.")

    
    variables_comunes = [v for v in factor1.dependencias if v in factor2.dependencias ]
    
    print("Producto de factores")
    print(f"factor1: {factor1.dependencias}")
    print(f"factor2: {factor2.dependencias}")
    print(f"variables_dep: {set(factor1.dependencias + factor2.dependencias)}")
    if variables_comunes == []:
        raise ValueError("No hay variables comunes para realizar el producto.")

    #nuevas_variables = list(set(factor1.valores_variablesdep + factor1.propios + factor2.propios+ factor2.valores_variablesdep))
    print(f"factor1.valores: {factor1.valores}")
    print(f"factor1.valores.llaves: {factor1.valores.keys()}")
    print(f"factor2.valores: {factor2.valores}")
    print(f"factor2.valores.llaves: {factor2.valores.keys()}")

    encontrada = False
    nuevos_valores = {}
    for llaves in factor2.valores.keys():
        for llaves2 in factor1.valores.keys(): 
            if isinstance(llaves2, tuple):   #Si es una tupla    
                if llaves in llaves2: #Si la llave del factor 2 está en la llave del factor 1
                    valores1 = factor2.valores[llaves]
                    valores2 = factor1.valores[llaves2]
                    nuevos_valores[llaves2] = valores1 * valores2
            elif isinstance(llaves, tuple):  #Si es una tupla
                if llaves2 in llaves: #Si la llave del factor 1 está en la llave del factor 2
                    valores1 = factor2.valores[llaves]
                    valores2 = factor1.valores[llaves2]
                    nuevos_valores[llaves] = valores2 * valores1
                
     # Redondear los valores al final antes de imprimir
    nuevos_valores = {k: round(v, 4) for k, v in nuevos_valores.items()} 

    '''
    print(f"nuevos_valores: {nuevos_valores}")

    print(f"factor2.valores: {factor2.valores}")
   
    #print(f"nuevas_variables: {nuevas_variables}")
    print(f"factor1.dependencias: {factor1.dependencias}")
    print(f"factor2.dependencias: {factor2.dependencias}")
    print(f"variables_comunes: {variables_comunes}")
    '''
  
    
    nuevo_factor = Factor(factor1.identificador + "-" + factor2.identificador, None, nuevos_valores, [], list(set(factor1.dependencias + factor2.dependencias)))
    print(f"Producto de los factores del nodo {factor1.identificador} y nodo {factor2.identificador}:")
    nuevo_factor.imprimir()

    return nuevo_factor


def marginalizacion(lista_factores, variable_a_marginar):
    """
    Realiza la marginalización de un factor sobre una variable, lo que implica eliminar la variable
    y sumar los valores correspondientes en la matriz. 
    """
    

    if len(lista_factores) == 0:
        raise ValueError("No hay factores para realizar la marginalización.")
    
    if variable_a_marginar not in lista_factores[0].dependencias:
        raise ValueError(f"La variable {variable_a_marginar} no está en el factor.")
    
    if len(lista_factores) == 1:
        
       
        nuevas_variables = [v for v in lista_factores[0].dependencias if v != variable_a_marginar]
        nuevo_factor = Factor(lista_factores[0].identificador, None,  lista_factores[0].valores, lista_factores[0].propios, lista_factores[0].dependencias)
        
        nuevo_factor.imprimir()


    
    else:
       
        nuevo_factor =  lista_factores[0]

        # Iterar sobre los elementos de lista_factores comenzando desde el segundo elemento
        for factor in lista_factores[1:]:
            nuevo_factor = producto_de_factores(nuevo_factor, factor)

                    
    
    return nuevo_factor




def getIdentificador(factor):
    """
    Devuelve el identificador del factor.
    """
    return factor.identificador

if __name__ == "__main__":
    
    #### PRUEBA ####
    # Definición de los factores con las variables de las que dependen y sus propios valores.

   
    prob_d = {
        'd0': 0.6,
        'd1': 0.4
    }
    prob_a_dado_d_e = {
        ('a0','d0', 'e0'): 0.3, 
        ('a0','d1', 'e0'): 0.7, 
        ('a1','d0', 'e0'): 0.4, 
        ('a1','d1', 'e0'): 0.2,  
        ('a2','d0', 'e0'): 0.3,  
        ('a2','d1', 'e0'): 0.1, 
        ('a0','d0', 'e1'): 0.1,  
        ('a0','d1', 'e1'): 0.2, 
        ('a1','d0', 'e1'): 0.2,  
        ('a1','d1', 'e1'): 0.3,
        ('a2','d0', 'e1'): 0.7,     
        ('a2','d1', 'e1'): 0.5,  
    }
    prob_e = {
        'e0': 0.8,
        'e1': 0.2
    }

    

    prob_c_dado_e = {
        ('c0','e0'): 0.6,  
        ('c0','e1'): 0.3,  
        ('c1','e0'): 0.3,
        ('c1','e1'): 0.4,
        ('c2','e0'): 0.1,
        ('c2','e1'): 0.3

    }

    prob_b_dado_a = {
        ('a0','b0'): 0.7,  
        ('a0','b1'): 0.3,  
        ('a1','b0'): 0.4,  
        ('a1','b1'): 0.6, 
        ('a2','b0'): 0.1, 
        ('a2','b1'): 0.9  
    }

    

    f_D = Factor('d', [], prob_d , propios=['d^0', 'd^1'], dependencias=['d'])
    #f_D.imprimir()

    f_E = Factor('e', [], prob_e, propios=['e^0', 'e^1'], dependencias=['e'])
    #f_E.imprimir()

    f_C = Factor('c', ['e^0', 'e^1'], prob_c_dado_e, propios=['c^0', 'c^1', 'c^2'],
                 dependencias=['c','e'])
    #f_C.imprimir()

    f_A = Factor('a', ['d^0', 'd^1', 'e^0', 'e^1'], prob_a_dado_d_e, 
                 propios=['a^0', 'a^1', 'a^2'], dependencias=['a','d', 'e'])
    #f_A.imprimir()

    f_B = Factor('b', ['a^0', 'a^1', 'a^2'],  prob_b_dado_a, propios=['b^0', 'b^1']
                 , dependencias=['a','b'])

    #f_B.imprimir()

    
    # Marginalización y dependencias


    '''Iteraciones: van a haber tantas iterciones como variables haya a eliminar'''

    '''Primera iteración'''
    factores = [f_C] 
    #factores = [f_A, f_E, f_C, f_D, f_B] #lista de factores que va cambiando segun la iteración
    lista_variables = ['c','e','d','a'] #lista con el orden de las variables a eliminar
    

    #Marginalización de la variable C
    lista_variables1 = ['c']
    f_c_marginalizado = marginalizacion(factores, lista_variables[0])

    #Eliminación de la variable C
    f_c_eliminacion= eliminacion(f_c_marginalizado, lista_variables[0])
    print(f"Factor resultante tras la eliminación de la variable (1 iter) {f_c_eliminacion}:")


    '''Segunda iteración'''
    factores = [f_A, f_E, f_c_eliminacion]
    #factores = [f_A, f_E, f_C, f_D, f_B] #lista de factores que va cambiando segun la iteración
    lista_variables1 = ['c','e']

    #Marginalización de la variable E
    
    f_a_e_c_resultante = marginalizacion(factores, lista_variables[1])
    print(f"Factor resultante tras el segundo produto de la variable (2 iter) {f_a_e_c_resultante}:")

    
    #Eliminación de la variable E
    f_a_e_c_eliminacion= eliminacion(f_a_e_c_resultante, lista_variables[1])
    print ("Eliminacion paso 2 variables:",f_a_e_c_eliminacion)
    
    
    '''Tercera iteración'''
    factores = [f_D, f_a_e_c_eliminacion]
    #factores = [f_A, f_E, f_C, f_D, f_B] #lista de factores que va cambiando segun la iteración
    lista_variables1 = ['c','e','d']

    #Marginalización de la variable D
    f_a_e_c_d_producto = marginalizacion(factores, lista_variables[2])
    print(f"Factor resultante tras el producto de la variable (3 iter) {f_a_e_c_d_producto}:")

    #Eliminación de la variable D
    f_a_e_c_d_eliminacion = eliminacion(f_a_e_c_d_producto, lista_variables[2])
    print(f"Factor resultante tras la eliminación de la variable (3 iter) {f_a_e_c_d_eliminacion}:")

    '''Cuarta iteración'''

    factores = [f_B, f_a_e_c_d_eliminacion]
    #factores = [f_A, f_E, f_C, f_D, f_B] #lista de factores que va cambiando segun la iteración
    lista_variables1 = ['c','e','d','a']

    f_a_e_c_d_b_producto =  marginalizacion(factores, lista_variables[3])
    print(f"Factor resultante tras el producto de la variable (4 iter) {f_a_e_c_d_b_producto}:")

    #Eliminación de la variable A
    f_a_e_c_d_b_eliminacion = eliminacion(f_a_e_c_d_b_producto, lista_variables[3])
    print(f"Factor resultante tras la eliminación de la variable (4 iter) {f_a_e_c_d_b_eliminacion}:")
    
    
    