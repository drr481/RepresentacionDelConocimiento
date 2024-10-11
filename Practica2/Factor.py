import numpy as np

class Factor:
    def __init__(self, identificador, variables, valores, propios):
        """
        Inicializa un factor.
        - identificador: un carácter que identifica el nodo.
        - variables: lista de variables de las que depende el nodo.
        - valores: matriz de valores que representan el factor (condicionada a las variables).
        - propios: lista de valores propios que el nodo puede tomar.
        """
        self.identificador = identificador  # Identificador del nodo (carácter)
        self.variables = variables  # Variables de las que depende el nodo
        self.valores = np.array(valores)  # Matriz que representa las probabilidades condicionales del nodo dado sus variables
        self.propios = propios  # Lista de valores propios del nodo

    def __str__(self):
        return f"Factor({self.identificador}: {self.variables},\n{self.valores})"

    def imprimir(self):
        """
        Imprime las variables y los valores propios asociados al factor (el nodo).
        """
        print(f"Factor del nodo {self.identificador}:")
        print(f"Variables de las que depende: {self.variables}")
        print(f"Valores propios del nodo: {self.propios}")
        print(f"Valores:\n{self.valores}\n")


def eliminacion(factor, variable_a_eliminar):
    """
    Elimina una variable de las que dependen los valores del factor. 
    """
    if variable_a_eliminar not in factor.variables:
        raise ValueError(f"La variable {variable_a_eliminar} no está en el factor.")
    
    idx = factor.variables.index(variable_a_eliminar)
    nuevas_variables = [v for v in factor.variables if v != variable_a_eliminar]
    nueva_matriz = np.delete(factor.valores, idx, axis=1)
    
    nuevo_factor = Factor(factor.identificador, nuevas_variables, nueva_matriz, factor.propios)
    print(f"Eliminando la variable {variable_a_eliminar} del factor del nodo {factor.identificador}:")
    nuevo_factor.imprimir()
    
    return nuevo_factor


def producto_de_factores(factor1, factor2):
    """
    Realiza el producto de dos factores, buscando las variables comunes entre ellos
    para ajustar las probabilidades condicionales. Los valores resultantes se multiplican
    cuando coinciden las variables en común.
    """
    variables_comunes = [v for v in factor1.variables if v in factor2.variables]
    if not variables_comunes:
        raise ValueError("No hay variables comunes para realizar el producto.")

    nuevas_variables = list(set(factor1.variables + factor2.variables))
    nueva_matriz = np.zeros((factor1.valores.shape[0], factor2.valores.shape[-1]))

    for i, fila1 in enumerate(factor1.valores):
        for j, fila2 in enumerate(factor2.valores):
            if all(fila1[factor1.variables.index(v)] == fila2[factor2.variables.index(v)] for v in variables_comunes):
                nueva_matriz[i] = fila1 * fila2
    
    nuevo_factor = Factor(factor1.identificador + "-" + factor2.identificador, nuevas_variables, nueva_matriz, factor1.propios)
    print(f"Producto de los factores del nodo {factor1.identificador} y nodo {factor2.identificador}:")
    nuevo_factor.imprimir()

    return nuevo_factor


def marginalizacion(factor, variable_a_eliminar):
    """
    Realiza la marginalización de un factor sobre una variable, lo que implica eliminar la variable
    y sumar los valores correspondientes en la matriz. 
    """
    if variable_a_eliminar not in factor.variables:
        raise ValueError(f"La variable {variable_a_eliminar} no está en el factor.")
    
    idx = factor.variables.index(variable_a_eliminar)
    nuevas_variables = [v for v in factor.variables if v != variable_a_eliminar]
    nueva_matriz = np.sum(factor.valores, axis=idx)
    
    nuevo_factor = Factor(factor.identificador, nuevas_variables, nueva_matriz, factor.propios)
    print(f"Marginalización sobre la variable {variable_a_eliminar} en el nodo {factor.identificador}:")
    nuevo_factor.imprimir()
    
    return nuevo_factor


def dependencias(factor):
    """
    Devuelve una lista de las variables de las que depende un factor. 
    """

    listaVariables = []

    for i in factor.variables:
        x = i.split('^')[0]
        if x not in listaVariables:
            listaVariables.append(x)

    return listaVariables

def getIdentificador(factor):
    """
    Devuelve el identificador del factor.
    """
    return factor.identificador

#### PRUEBA ####
# Definición de los factores con las variables de las que dependen y sus propios valores.

f_D = Factor('D', [], [[0.6], [0.4]], propios=['d^0', 'd^1'])
f_D.imprimir()

f_E = Factor('E', [], [[0.8], [0.2]], propios=['e^0', 'e^1'])
f_E.imprimir()

f_C = Factor('C', ['e^0', 'e^1'], [[0.6, 0.3, 0.1], [0.3, 0.4, 0.3]], propios=['c^0', 'c^1', 'c^2'])
f_C.imprimir()

f_A = Factor('A', ['d^0', 'd^1', 'e^0', 'e^1'], [[0.3, 0.4, 0.3], [0.1, 0.2, 0.7], [0.7, 0.2, 0.1], [0.2, 0.3, 0.5]], propios=['a^0', 'a^1', 'a^2'])
f_A.imprimir()

f_B = Factor('B', ['a^0', 'a^1', 'a^2'], [[0.7, 0.3], [0.4, 0.6], [0.1, 0.9]], propios=['b^0', 'b^1'])
f_B.imprimir()

# Marginalización y dependencias
f_B_marginalizado = marginalizacion(f_B, 'a^0')

dependencias_A = dependencias(f_A)
print(f"Las variables de las que depende el nodo A son: {dependencias_A}")





