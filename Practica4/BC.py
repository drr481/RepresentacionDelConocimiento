class BC:

    def __init__(self, hechos, reglas):
        self.hechos = hechos
        self.reglas = reglas

    def encadenamientoAdelante(self):
        while True:
            bandera = False
            for regla in self.reglas:
                if regla[1] in self.hechos and regla[2] in self.hechos and regla[3] not in self.hechos:
                    self.hechos.append(regla[3])
                    bandera = True
            if not bandera:
                break
        return self.hechos
    
    def hechos(self):
        return self.hechos 
    
    def reglas(self):
        return self.reglas
    
    class operacion:
        def __init__(self, operador, operando1, operando2):
            self.operador = operador
            self.operando1 = operando1
            self.operando2 = operando2
        
        def operador(self):
            return self.operador
        
        def operando1(self):
            return self.operando1
        
        def operando2(self):
            return self.operando2
        
        def evaluar(self):
            if self.operador == 'and':
                return self.evaluar(self.operando1) and self.evaluar(self.operando2)
            elif self.operador == 'or':
                return self.evaluar(self.operando1) or self.evaluar(self.operando2)
            elif self.operador == 'not':
                return not self.evaluar(self.operando1)
            elif self.operador == '=>':
                return not self.evaluar(self.operando1) or self.evaluar(self.operando2)
            else:
                return False
    

if __name__ == '__main__':
    hechos = ['Ed', 'Ev', 'Es', 'A', 'C']
    reglas = [
        ['hola', 'Ed', 'A', 'P'],
        ['Si', 'Ev', 'C', 'S'],
        ['Si', 'Ed', 'P', 'S'],
        ['Si', 'Es', 'P', 'S'],
        ['Si', 'Ev', 'S', 'N'],
        ['Si', 'Ed', 'S', 'P'],
        ['Si', 'Ed', 'A', 'P', 'D']
    ]
    bc = BC(hechos, reglas)
    print(bc.encadenamientoAdelante())

