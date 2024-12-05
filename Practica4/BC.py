import copy
import time

class BC:

    def __init__(self, hechos, reglas):
        print("Constructor de hechos")
        self.hechos = hechos
        x=[]
        for i in hechos:
            x.append(i)
        
        for i in range(1,len(hechos)):
            aux = len(x)
            
            for j in range(aux):
                for k in hechos:
                    if not k == x[j]:
                        x.append(BC.operacion("and",k,x[j]))

        for i in x:
            self.hechos.append(i)

        self.reglas = reglas

    def encadenamientoAdelante(self):
        print("Encadenameinto hacia adelante")
        while True:
            bandera = False
            for regla in self.reglas:
                print("Regla: " + str(regla))
                print(str( regla.getOperando1() in self.hechos) + " " + str(not (regla.getOperando2() in self.hechos)))
                if (regla.getOperador() == "=>") and ((regla.getOperando1() in self.hechos) and (not (regla.getOperando2() in self.hechos))):
                    self.hechos.append(regla.getOperando2())
                    print("Conclusion lógica : " + str(regla.getOperando2()))
                    #self.reglas.append(regla.getOperando2())
                    bandera = True
            print("##############################################")
            print("bandera: " + str(bandera))
            time.sleep(1)
            if bandera:
                break
        #print("Salgo del ciclo")
        return self.hechos
    
    def esCompleto(self):
        # Obtener todos los hechos posibles derivados de las reglas
        hechos_derivados = set(str(h) for h in self.encadenamientoAdelante())
        
        # Obtener todos los hechos esperados (modelos lógicos posibles)
        hechos_esperados = set(str(h) for h in self.hechos)
        for regla in self.reglas:
            if regla.getOperador() == "=>":
                hechos_esperados.add(str(regla.getOperando2()))
        
        # Verificar si todos los hechos esperados son derivables
        return hechos_esperados.issubset(hechos_derivados)

    
    def getHechos(self):
        return self.hechos 
    
    def getReglas(self):
        return self.reglas

    def generar_combinaciones_and(self, hechos):
        if len(hechos) < 2:
            return hechos
        combinaciones = []
        for i in range(len(hechos)):
            for j in range(i + 1, len(hechos)):
                combinaciones.append(BC.operacion("and", hechos[i], hechos[j]))

        return combinaciones

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
                return True
            else:
                return False
        
        def __str__(self):
            return "(" + str(self.operador) + ", " + str(self.operando1) + ", " + str(self.operando2) + ")"

        def __eq__(self, value: object) -> bool:
            return self.operador == value.operador and self.operando1 == value.operando1 and self.operando2 == value.operando2

if __name__ == '__main__':

    # Literales
    
    A = BC.operacion(None, "A", None)
    B = BC.operacion(None, "B", None)
    C = BC.operacion(None, "C", None)
    D = BC.operacion(None, "D", None)
    E = BC.operacion(None, "E", None)
    F = BC.operacion(None, "F", None)
    '''
    
    Llueve = BC.operacion(None, "Llueve", None)
    Nieva = BC.operacion(None, "Nieva", None)
    Mojado = BC.operacion(None, "Mojado", None)
    '''
    # Hechos
    
    hechos = [B]
    
    #hechos = [Llueve, Nieva, Mojado]
    aux = []

    print("Hechos:")
    for i in hechos:
        print(i)
        aux.append(i)

    # Reglas
    
    reglas = [
        BC.operacion("=>", BC.operacion("and",A,C), E),
        BC.operacion("=>", B, C),
        BC.operacion("=>", BC.operacion("and",B,D), F),
        BC.operacion("=>", C, D)
    ]
    '''
    
    reglas = [
        BC.operacion("=>", BC.operacion("or",Llueve,Nieva), Mojado)
    ]
    '''
    print("Reglas:")
    for i in reglas:
        print(i)

    bc = BC(aux, reglas)
    bc.encadenamientoAdelante()
    print(type(bc.getHechos()))
    print("¿El encadenamiento es completo? " + str(bc.esCompleto()))

