import Factor as f
import EVMarginal

class Expresion:
    def __init__(self, A, B):
        self.A = A
        self.B = B

class EVCondicional:

    def __init__(self, conjuntoFactores):
        self.conjuntoFactores = conjuntoFactores

    def eliminaVariablesCondicional(self, exp, variables, conjuntoFactores):

        nuevosFactores = []
        variablesAEliminar = []

        # Elimina las hojas
        self.eliminaHojas(conjuntoFactores)

        # Eliminar los valores de exp.B de conjuntoFactores en caso de sean valores explicitos en vez de variables
        

        # Ordenar las variables a eliminar

        # Escogemos los factores que contienen la variable a eliminar

        # Llamamos a la funcion elimina, que recive los factores anteriores y la variable a eliminar

        # Repetimos los dos pasos anteriores hasta que no queden variables a eliminar

        return nuevosFactores, variablesAEliminar
    
    def eliminaHojas(self, factores):
        pass

    def ordenaVariables(self, variables, conjuntoFactores, raiz):
        if self.esArbol(conjuntoFactores, raiz):
            return self.posorden(variables, conjuntoFactores, raiz)
        else:
            return self.minimosVecinos(variables, conjuntoFactores)
        
    def esArbol(self, conjuntoFactores, raiz):
        listaExplorados = []
        return self.esArbolRecursivo(conjuntoFactores, listaExplorados, conjuntoFactores[raiz])
    
    def esArbolRecursivo(self, conjuntoFactores, listaExplorados, nodo):
        
        listaExplorados.append(nodo)

        for i in nodo.vecinos:
            if i not in listaExplorados:
                return self.esArbolRecursivo(conjuntoFactores, listaExplorados, i)
            else:
                return False
            
        return True
    
    def posorden(self, variables, conjuntoFactores, raiz):
        listaExplorados = []
        return self.posordenRecursivo(variables, conjuntoFactores, listaExplorados, conjuntoFactores[raiz])

    def posordenRecursivo(self, variables, conjuntoFactores, listaExplorados, nodo):
            
        for i in nodo.vecinos:
            self.posordenRecursivo(variables, conjuntoFactores, listaExplorados, i)
        
        listaExplorados.append(nodo)

        return listaExplorados
    
    def minimosVecinos(self, variables, conjuntoFactores):
        
        lista = []
        vecinos_dict = {var: 0 for var in variables}
        
        for factor in conjuntoFactores:
            for var in variables:
                if var in factor.variables:
                    vecinos_dict[var] = vecinos_dict[var] + 1
