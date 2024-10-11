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
        self.eliminaHojas(conjuntoFactores, exp, variables)

        # Eliminar los valores de exp.B de conjuntoFactores en caso de sean valores explicitos en vez de variables
        for factor in conjuntoFactores:
            for i in exp.B:
                if i in factor.propios:
                    factor.propios.remove(i)

        # Ordenar las variables a eliminar
        variablesAEliminar = self.ordenaVariables(variables, conjuntoFactores, exp.B)

        # Por cada variable a eliminar, marginalizamos esa variable
            # Agrupamos los factores que dependen de la variable a eliminar
            # Marginalizamos los factores agrupados
            # Sustituimos 

        return nuevosFactores, variablesAEliminar
    
    def eliminaHojas(self, factores, exp, variables):
        lista = []
        for i in factores:
            self.elimina_hojas_recursivo(factores, i, lista, exp, variables)

    def elimina_hojas_recursivo(self, factores, nodo, lista, exp, variables):
        lista.append(nodo)
        for hijo in f.dependencias(nodo):
            if hijo not in lista:
                self.elimina_hojas_recursivo(factores, hijo, lista, exp, variables)
        
        if self.esHoja(nodo, factores) and nodo not in exp.A and nodo not in exp.B and nodo not in variables:
            factores.remove(nodo)

    def esHoja(self, factor, factores):
        for fac in factores:
            if factor in f.dependencias(fac):
                return False
        return True

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
        
        vecinos_dict = {var: 0 for var in variables}
        
        for factor in conjuntoFactores:
            for var in variables:
                if var in f.dependencias(factor):
                    vecinos_dict[var] += 1

        vecinos_dict = dict(sorted(vecinos_dict.items(), key=lambda item: item[1]))

        return list(vecinos_dict.keys())