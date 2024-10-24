# Input: Conjunto de Factores
# Output: 
import Factor as fac
import EVCondicional as evc

def main():

    # Crea las tablas de probabilidad
    prob_a = {
        ('a0'): 0.6,
        ('a1'): 0.4
    }

    prob_b = {
        ('b0'): 0.4,
        ('b1'): 0.4,
        ('b2'): 0.2
    }

    prob_c_a = {
        ('c0','a0'): 0.8,
        ('c0','a1'): 0.2,
        ('c1','a0'): 0.6,
        ('c1','a1'): 0.4
    }

    prob_e_b = {
        ('e0','b0'): 0.6,
        ('e0','b1'): 0.6,
        ('e0','b2'): 0.4,
        ('e1','b0'): 0.4,
        ('e1','b1'): 0.4,
        ('e1','b2'): 0.6,
    }

    prob_d_a_b = {
        ('d0','a0','b0'): 0.8,
        ('d0','a0','b1'): 0.7,
        ('d0','a0','b2'): 0.6,
        ('d0','a1','b0'): 0.7,
        ('d0','a1','b1'): 0.5,
        ('d0','a1','b2'): 0.3,
        ('d1','a0','b0'): 0.1,
        ('d1','a0','b1'): 0.2,
        ('d1','a0','b2'): 0.2,
        ('d1','a1','b0'): 0.1,
        ('d1','a1','b1'): 0.2,
        ('d1','a1','b2'): 0.3,
        ('d2','a0','b0'): 0.1,
        ('d2','a0','b1'): 0.1,
        ('d2','a0','b2'): 0.2,
        ('d2','a1','b0'): 0.2,
        ('d2','a1','b1'): 0.3,
        ('d2','a1','b2'): 0.4
    }

    prob_f_c_d = {
        ('f0','c0','d0'): 0.6,
        ('f0','c0','d1'): 0.5,
        ('f0','c0','d2'): 0.4,
        ('f0','c1','d0'): 0.5,
        ('f0','c1','d1'): 0.3,
        ('f0','c1','d2'): 0.1,
        ('f1','c0','d0'): 0.2,
        ('f1','c0','d1'): 0.3,
        ('f1','c0','d2'): 0.3,
        ('f1','c1','d0'): 0.2,
        ('f1','c1','d1'): 0.3,
        ('f1','c1','d2'): 0.4,
        ('f2','c0','d0'): 0.2,
        ('f2','c0','d1'): 0.2,
        ('f2','c0','d2'): 0.3,
        ('f2','c1','d0'): 0.3,
        ('f2','c1','d1'): 0.4,
        ('f2','c1','d2'): 0.5
    }

    # Crea los factores de 'a' a 'f'
    a = fac.Factor('a', [], prob_a, propios=['a0', 'a1'], dependencias=['a'])
    b = fac.Factor('b', [], prob_b, propios=['b0', 'b1', 'b2'], dependencias=['b'])
    c = fac.Factor('c', ['a0', 'a1'], prob_c_a, propios=['c0', 'c1'], dependencias=['c', 'a'])
    d = fac.Factor('d', ['a0', 'a1', 'b0', 'b1', 'b2'], prob_d_a_b, propios=['d0', 'd1', 'd2'], dependencias=['d', 'a', 'b'])
    e = fac.Factor('e', ['b0', 'b1', 'b2'], prob_e_b, propios=['e0', 'e1'], dependencias=['e', 'b'])
    f = fac.Factor('f', ['c0', 'c1', 'd0', 'd1', 'd2'], prob_f_c_d, propios=['f0', 'f1', 'f2'], dependencias=['f', 'c', 'd'])

    # Crear el conjunto de factores
    factores = [a, b, c, d, e, f]

    #Crea los valores de la expresión
    A = ['f']
    B = ['b2', 'd1']
    
    # Crear una instancia de EVCondicional
    ev_condicional = evc.EVCondicional(factores)
    
    # Definir las variables a eliminar
    variables_a_eliminar = ['a', 'c']
    
    # Llamar al método eliminaVariablesCondicional
    #ev_condicional.eliminaVariablesCondicional(A, B, variables_a_eliminar, factores)
    print("###########################################################################")
    print(factores[2])

    # Imprimir el resultado para verificar
    print("Factores después de eliminar variables condicionales:")
    #for factor in ev_condicional.factores:
    #    print(factor)

if __name__ == "__main__":
    main()