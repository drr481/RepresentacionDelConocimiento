import Factor as f
import EVMarginal

class Expresion:
    def __init__(self, A, B):
        self.A = A
        self.B = B

class EVCondicional:

    def __init__(self, conjuntoFactores):
        self.conjuntoFactores = conjuntoFactores

    def eliminaVariablesCondicional(self, A, B, variables, conjuntoFactores):

        self.exp = Expresion(A, B)

        variablesAEliminar = []

        # Elimina las hojas
        #self.eliminaHojas(conjuntoFactores)
        #print("Conjunto de factores después de eliminar hojas:")
        #for i in conjuntoFactores:
        #    i.imprimir()            

        # Eliminar los valores de exp.B de conjuntoFactores en caso de sean valores explicitos en vez de variables
        for factor in conjuntoFactores:
            for i in self.exp.B:
                if i in factor.valores_variablesdep:
                    f.eliminadependencias(factor, i)
                    self.exp.B.remove(i)

        # Ordenar las variables a eliminar
        variablesAEliminar = self.ordenaVariables(variables, conjuntoFactores)

        var_aux = [var.identificador for var in variablesAEliminar]
        numerador = [EVMarginal.marginal(conjuntoFactores, var_aux)]
        #print("Numerador =>  ")
        print("Denominador => ")
        denominador = EVMarginal.marginal(numerador, self.exp.A)

        return numerador / denominador
    
    def eliminaHojas(self, conjuntoFactores):
        lista = []
        return self.eliminaHojasRecursivo(conjuntoFactores, lista, conjuntoFactores[0])

    def eliminaHojasRecursivo(self, conjuntoFactores, lista, nodo):
            
        lista.append(nodo)
    
        for i in self.buscaHijos(nodo):
            if i not in lista:
                self.eliminaHojasRecursivo(conjuntoFactores, lista, i)
            
        if self.esHoja(nodo, conjuntoFactores):
            conjuntoFactores.remove(nodo)

    def esHoja(self, nodo, conjuntoFactores):

        bool = False
        for i in conjuntoFactores:
            if nodo.identificador not in i.dependencias and nodo.identificador not in self.exp.B:
                bool =  True
        return bool
        

    def ordenaVariables(self, variables, conjuntoFactores):
        if self.esArbol(conjuntoFactores):
            return self.posorden(variables, conjuntoFactores)
        else:
            return self.minimosVecinos(variables, conjuntoFactores)
        
    def esArbol(self, conjuntoFactores):
        listaExplorados = []
        return self.esArbolRecursivo(conjuntoFactores, listaExplorados, conjuntoFactores[0])
    
    def esArbolRecursivo(self, conjuntoFactores, listaExplorados, nodo):
        
        listaExplorados.append(nodo)

        nodoDependencias = []
        for i in conjuntoFactores:
            if i.identificador in nodo.dependencias:
                nodoDependencias.append(i)

        for i in nodoDependencias:
            if i not in listaExplorados:
                return self.esArbolRecursivo(conjuntoFactores, listaExplorados, i)
            else:
                return False
            
        return True
    
    def posorden(self, variables, conjuntoFactores):
        listaExplorados = []
        return self.posordenRecursivo(variables, conjuntoFactores, listaExplorados, conjuntoFactores[0])

    def posordenRecursivo(self, variables, conjuntoFactores, listaExplorados, nodo):
            
        nodoDependencias = []
        for i in conjuntoFactores:
            if i.identificador in nodo.dependencias:
                nodoDependencias.append(i)

        for i in nodoDependencias:
            self.posordenRecursivo(variables, conjuntoFactores, listaExplorados, i)
        
        listaExplorados.append(nodo)

        return listaExplorados
    
    def minimosVecinos(self, variables, conjuntoFactores):
        
        newVar = []
        for j in variables:
            for i in conjuntoFactores:
                if i.identificador == j:
                    newVar.append(i)

        vecinos_dict = {var: 0 for var in newVar}
        
        for factor in conjuntoFactores:
            for var in newVar:
                if var.identificador in factor.dependencias:
                    # Suma 1 al valor de la llave var en vecinos_dict
                    vecinos_dict[var] += 1


        # Ordena vecinos_dict de menor a mayor en función del valor de sus llaves
        vecinos_dict = dict(sorted(vecinos_dict.items(), key=lambda item: item[1]))

        return list(vecinos_dict.keys())

    def buscaDependencias(self, factor):
        dependencias = []

        for i in self.conjuntoFactores:
            if factor.identificador in i.dependencias:
                dependencias.append(i)

        return dependencias

    def buscaHijos(self, factor):

        hijos = []
        for i in self.conjuntoFactores:
            if factor.identificador in i.dependencias:
                hijos.append(i)
        
        return hijos
