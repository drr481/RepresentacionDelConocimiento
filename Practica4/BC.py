class BC:

    def __init__(self, hechos, reglas):
        self.hechos = hechos
        self.reglas = reglas

    def encadenamientoAdelante(self):

        while True:
            bandera = False
            for regla in self.reglas:
                if (regla in reglas and regla[0] in hechos) and not regla[1] in hechos:
                    if (regla[1].isLiteral()):
                        self.hechos.append(regla[1])
                    else:
                        self.reglas.append(regla[1])
                    bandera = True
            if not bandera:
                break
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
                return self.operando1
            else:
                return False
    

if __name__ == '__main__':

    # Literales

    Llueve = True
    Mojado = True

    # Hechos
    
    op1 = BC.operacion(None, Llueve, None)
    
    hechos = [op1]

    # Reglas
    
    op3 = BC.operacion('=>', Llueve, Mojado)

    reglas = [
        op3
    ]

    bc = BC(hechos, reglas)
    print(bc.encadenamientoAdelante())

