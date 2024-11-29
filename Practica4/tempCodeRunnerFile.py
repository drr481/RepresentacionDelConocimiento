import copy

class BC:

    def __init__(self, hechos, reglas):
        self.hechos = hechos
        self.reglas = reglas

    def encadenamientoAdelante(self):
        print("Encadenameinto hacia adelante")
        i = 0
        while True:
            i += 1
            continuar = False
            for regla in self.reglas:
                print(regla.getOperando1().evaluar())
                if (regla.getOperador() == "=>") and ((regla.getOperando1.evaluar()) and (not (regla.getOperando2() in hechos))):
                    #print("Operando2: ", regla.getOperando2())
                    self.hechos.append(regla.getOperando2())
                    self.reglas.append(regla.getOperando2())
                    continuar = True #Si se añaden nuevos hechos, se debe seguir iterando
            if (continuar == True):
                break
            if i == 10:
                break #Para evitar bucles infinitos
        print("Salgo del ciclo")
        return self.hechos
    
    def getHechos(self):
        return self.hechos 
    
    def getReglas(self):
        return self.reglas
    
    class operacion:
        def __init__(self, operador, operando1, operando2):
            self.operador = operador
            self.operando1 = operando1
            self.operando2 = operando2
            self.valor = None            
        
        def getOperador(self):
            return self.operador
        
        def getOperando1(self):
            return self.operando1
        
        def getOperando2(self):
            return self.operando2
        
        def isLiteral(self):
            return self.operando2 == None
        
        def evaluar(self):
            if self.operador == 'and':
                return self.evaluar(self.operando1) and self.evaluar(self.operando2)
            elif self.operador == 'or':
                return self.evaluar(self.operando1) or self.evaluar(self.operando2)
            elif self.operador == 'not':
                return not self.evaluar(self.operando1)
            elif self.operador == '=>':
                return not self.evaluar(self.operando1) or self.evaluar(self.operando2)
            elif self.operador == None:
                if (self.operador in hechos):
                    return True
                else:
                    return None
            else:
                return False
        
        def __str__(self):
            return "(" + str(self.operador) + ", " + str(self.operando1) + ", " + str(self.operando2) + ")"
    

if __name__ == '__main__':

    # Literales
    lit1 = BC.operacion(None, "Llueve", None)
    lit2 = BC.operacion(None, "Mojado", None)

    # Hechos
    
    op1 = BC.operacion("not", lit1, None)
    op2 = BC.operacion(None, lit2, None)
    
    hechos = [op1]
    aux = copy.deepcopy(hechos)

    print("Hechos:")
    for i in aux:
        print(i)

    # Reglas
    
    op3 = BC.operacion('=>',lit1, lit2)

    reglas = [op3]

    print("Reglas:")
    for i in reglas:
        print(i)

    bc = BC(aux, reglas)
    bc.encadenamientoAdelante()
    #print(type(bc.getHechos()))
    print("Solución:")
    for i in bc.getHechos():
        if i not in hechos:
            print(i)

