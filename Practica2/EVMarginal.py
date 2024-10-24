import itertools
import Factor as factor



def marginal(factores, variables):
    
    

    def marginalrecursivo(factores, variables, tau):

        if variables == []:
            return tau
        
        variableEliminar = variables.pop(0)
        #print("Variable a eliminar: " + variableEliminar)
        factores_eliminar = []

        #print("Factores: " + str(factores))
        for f in factores:
            #print(f)
            if variableEliminar in f.dependencias:
                factores_eliminar.append(f)
   
        if factores_eliminar == []:
            return tau

        #print("####################################################")

        # Nueva lista excluyendo los elementos de lista_a_eliminar
        nuevo_factores = [f for f in factores if f not in factores_eliminar]


        #print("factores tras eliminacion:", factores)
        #print("factores a eliminar:", factores_eliminar)   
        
        
        resultado_marginalizacion = factor.marginalizacion(factores_eliminar, variableEliminar)
        resultado_eliminacion = factor.eliminacion(resultado_marginalizacion, variableEliminar)
        nuevo_factores.append(resultado_eliminacion)
        
        return marginalrecursivo(nuevo_factores, variables, resultado_eliminacion)
    
    if variables == []:
        raise ValueError("La lista está vacía")
    if factores == []:
        raise ValueError("No hay factores")
    
   

    return marginalrecursivo(factores, variables, None)
    
    

    
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



f_D = factor.Factor('d', [], prob_d , propios=['d^0', 'd^1'], dependencias=['d'])
#f_D.imprimir()

f_E = factor.Factor('e', [], prob_e, propios=['e^0', 'e^1'], dependencias=['e'])
#f_E.imprimir()

f_C = factor.Factor('c', ['e^0', 'e^1'], prob_c_dado_e, propios=['c^0', 'c^1', 'c^2'],
                dependencias=['c','e'])
#f_C.imprimir()

f_A = factor.Factor('a', ['d^0', 'd^1', 'e^0', 'e^1'], prob_a_dado_d_e, 
                propios=['a^0', 'a^1', 'a^2'], dependencias=['a','d', 'e'])
#f_A.imprimir()

f_B = factor.Factor('b', ['a^0', 'a^1', 'a^2'],  prob_b_dado_a, propios=['b^0', 'b^1']
                , dependencias=['a','b'])

#f_B.imprimir()


# Marginalización y dependencias


'''Iteraciones: van a haber tantas iterciones como variables haya a eliminar'''


factores = [f_A, f_E, f_C, f_D, f_B] #lista de factores que va cambiando segun la iteración


# Definir las letras  
letras = ['c', 'e', 'd', 'a']


# Genera todas las permutaciones posibles y almacenarlas en una lista
lista_permutaciones = [list(p) for p in itertools.permutations(letras)]

#probabilidad_b = marginal(factores, lista_permutaciones[2])
#print(probabilidad_b)



