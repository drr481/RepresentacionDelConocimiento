import Factor as f
import EVMarginal

class Expresion:
    def __init__(self, A, B):
        self.A = A
        self.B = B

class EVCondicional:

    def __init__(self, conjuntoFactores):
        self.conjuntoFactores = conjuntoFactores
    '''
    def eliminaVariablesCondicional(self, A, B, variables, conjuntoFactores):

        self.exp = Expresion(A, B)

        variablesAEliminar = []

        # Elimina las hojas
        self.eliminaHojas(conjuntoFactores)
        #print("Conjunto de factores después de eliminar hojas:")
        #for i in conjuntoFactores:
        #    print("Factor: " + i.identificador)         

        # Eliminar los valores de exp.B de conjuntoFactores en caso de sean valores explicitos en vez de variables
        for factor in conjuntoFactores:
            for i in self.exp.B:
                if i in factor.valores_variablesdep:
                    print(i)
                    f.eliminadependencias(factor, i)
                    self.exp.B.remove(i)

        print("Conjunto de factores después de eliminar valores fijos:")
        for i in conjuntoFactores:
            i.imprimir()         


        # Ordenar las variables a eliminar
        variablesAEliminar = self.ordenaVariables(variables, conjuntoFactores)

        var_aux = [var.identificador for var in variablesAEliminar]
        #print("Numerador =>  ")
        numerador = [EVMarginal.marginal(conjuntoFactores, var_aux)]
        #print(numerador[0])

        #print("Denominador => ")
        denominador = EVMarginal.marginal(numerador, self.exp.A)
        #print(denominador)
        print("Solucion: ")
        return self.divideFactores(numerador, denominador)
    '''

    def eliminaVariablesCondicional(self, A, B,variables, conjuntoFactores):

        self.exp = Expresion(A, B)

        variablesAEliminar = []
        variablesElim = variables

        # Elimina las hojas
        self.eliminaHojas(conjuntoFactores)
        #print("Conjunto de factores después de eliminar hojas:")
        #for i in conjuntoFactores:
        #    print("Factor: " + i.identificador)        
       

        # Eliminar los valores de exp.B de conjuntoFactores en caso de sean valores explicitos en vez de variables
        for factor in conjuntoFactores:
            for variableElim in variablesElim:

                #Compruebo si la variable a eliminar esta en alguna dependencia de un factor y si todos los elementos de self.exp.B estan en los propios o en los valores de las variables dependientes
                if  variableElim in factor.dependencias and  all(any(elemento in lista for lista in [factor.propios, factor.valores_variablesdep]) for elemento in self.exp.B):
                
                    f.eliminadependencias(factor, self.exp.B)
                

        print("Conjunto de factores después de eliminar valores fijos:")
        for i in conjuntoFactores:
            i.imprimir()         


        # Ordenar las variables a eliminar
        variablesAEliminar = self.ordenaVariables(variables, conjuntoFactores)

        var_aux = [var.identificador for var in variablesAEliminar]
        print("Numerador =>  ")
        numerador = [EVMarginal.marginal(conjuntoFactores, var_aux)]
        print(numerador[0])

        print("Denominador => ")
        denominador = EVMarginal.marginal(numerador, self.exp.A)
        print(denominador)
        print("Solucion: ")
        return self.divideFactores(numerador, denominador)

    def eliminaHojas(self, conjuntoFactores):
        lista = []
        return self.eliminaHojasRecursivo(conjuntoFactores, lista, conjuntoFactores[0])

    def eliminaHojasRecursivo(self, conjuntoFactores, lista, nodo):
        
        for i in conjuntoFactores:
            if self.esHoja(i, conjuntoFactores):
                conjuntoFactores.remove(i)

    def esHoja(self, nodo, conjuntoFactores):

        bool = True
        for i in conjuntoFactores:
            if nodo.identificador in i.dependencias or nodo.identificador in self.exp.B or nodo.identificador in self.exp.A:
                bool =  False

        return bool
        

    def ordenaVariables(self, variables, conjuntoFactores):
        if self.esArbol(conjuntoFactores):
            #print("Posorden")
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

        for i in self.buscaDependencias(nodo):
            if i.identificador in variables:
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

    def divideFactores(self, numerador, denominador):
        
        if denominador == []:
            return numerador
        
        if isinstance(denominador, (int, float)):
            for factor in numerador:
                for val in factor.valores:
                    factor.valores[val] /= denominador
        
        return numerador