# Input: Conjunto de Factores
# Output: 
import Factor as fac
import EVCondicional as evc
import time
import itertools
import EVMarginal as evm




def v1():

    # Ejercicio 2.3 de teoria

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
    a = fac.Factor('a', [], prob_a, propios=['a0', 'a1'], dependencias=[])
    b = fac.Factor('b', [], prob_b, propios=['b0', 'b1', 'b2'], dependencias=[])
    c = fac.Factor('c', ['a0', 'a1'], prob_c_a, propios=['c0', 'c1'], dependencias=['a'])
    d = fac.Factor('d', ['a0', 'a1', 'b0', 'b1', 'b2'], prob_d_a_b, propios=['d0', 'd1', 'd2'], dependencias=['a', 'b'])
    e = fac.Factor('e', ['b0', 'b1', 'b2'], prob_e_b, propios=['e0', 'e1'], dependencias=['b'])
    f = fac.Factor('f', ['c0', 'c1', 'd0', 'd1', 'd2'], prob_f_c_d, propios=['f0', 'f1', 'f2'], dependencias=['c', 'd'])

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

    start_time = time.time()
    ev_condicional.eliminaVariablesCondicional(A, B, variables_a_eliminar, factores)[0].imprimir()
    end_time = time.time()

    print(f"Tiempo de ejecución: {end_time - start_time} segundos")

    #Imprimir el resultado para verificar
    #print("Factores después de eliminar variables condicionales:")
    #print("###########################################################################")
    #print(factores[2])

    # Imprimir el resultado para verificar
    #print("Factores después de eliminar variables condicionales:")
    #for factor in ev_condicional.factores:
    #   print(factor)

def ejemploEVMarginal():
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



    f_D = fac.Factor('d', [], prob_d , propios=['d^0', 'd^1'], dependencias=['d'])
    #f_D.imprimir()

    f_E = fac.Factor('e', [], prob_e, propios=['e^0', 'e^1'], dependencias=['e'])
    #f_E.imprimir()

    f_C = fac.Factor('c', ['e^0', 'e^1'], prob_c_dado_e, propios=['c^0', 'c^1', 'c^2'],
                    dependencias=['c','e'])
    #f_C.imprimir()

    f_A = fac.Factor('a', ['d^0', 'd^1', 'e^0', 'e^1'], prob_a_dado_d_e, 
                    propios=['a^0', 'a^1', 'a^2'], dependencias=['a','d', 'e'])
    #f_A.imprimir()

    f_B = fac.Factor('b', ['a^0', 'a^1', 'a^2'],  prob_b_dado_a, propios=['b^0', 'b^1']
                    , dependencias=['a','b'])

    #f_B.imprimir()


    # Marginalización y dependencias


    '''Iteraciones: van a haber tantas iterciones como variables haya a eliminar'''


    factores = [f_A, f_E, f_C, f_D, f_B] #lista de factores que va cambiando segun la iteración


    # Definir las letras  
    letras = ['c', 'e', 'd', 'a']


    # Genera todas las permutaciones posibles y almacenarlas en una lista
    lista_permutaciones = [list(p) for p in itertools.permutations(letras)]

    probabilidad_b = evm.marginal(factores, lista_permutaciones[2])
    print(probabilidad_b)

def v2():
    # Tablas de probabilidad
    prob_x = {
        ('x0'): 0.7,
        ('x1'): 0.3
    }

    prob_y = {
        ('y0'): 0.5,
        ('y1'): 0.5
    }

    prob_z_x = {
        ('z0', 'x0'): 0.6,
        ('z0', 'x1'): 0.4,
        ('z1', 'x0'): 0.4,
        ('z1', 'x1'): 0.6
    }

    prob_w_y = {
        ('w0', 'y0'): 0.8,
        ('w0', 'y1'): 0.2,
        ('w1', 'y0'): 0.2,
        ('w1', 'y1'): 0.8
    }

    # Factores
    x = fac.Factor('x', [], prob_x, propios=['x0', 'x1'], dependencias=[])
    y = fac.Factor('y', [], prob_y, propios=['y0', 'y1'], dependencias=[])
    z = fac.Factor('z', ['x0', 'x1'], prob_z_x, propios=['z0', 'z1'], dependencias=['x'])
    w = fac.Factor('w', ['y0', 'y1'], prob_w_y, propios=['w0', 'w1'], dependencias=['y'])

    # Conjunto de factores
    factores = [x, y, z, w]

    # Variables a eliminar
    A = ['z']
    B = ['x1']

    ev_condicional = evc.EVCondicional(factores)
    variables_a_eliminar = ['x', 'y']

    start_time = time.time()
    ev_condicional.eliminaVariablesCondicional(A, B, variables_a_eliminar, factores)[0].imprimir()
    end_time = time.time()

    print(f"Tiempo de ejecución: {end_time - start_time} segundos")

def v3():
    # Tablas de probabilidad
    prob_p = {
        ('p0'): 0.4,
        ('p1'): 0.6
    }

    prob_q = {
        ('q0'): 0.3,
        ('q1'): 0.7
    }

    prob_r_p = {
        ('r0', 'p0'): 0.5,
        ('r0', 'p1'): 0.7,
        ('r1', 'p0'): 0.5,
        ('r1', 'p1'): 0.3
    }

    prob_s_q = {
        ('s0', 'q0'): 0.6,
        ('s0', 'q1'): 0.4,
        ('s1', 'q0'): 0.4,
        ('s1', 'q1'): 0.6
    }

    # Factores
    p = fac.Factor('p', [], prob_p, propios=['p0', 'p1'], dependencias=[])
    q = fac.Factor('q', [], prob_q, propios=['q0', 'q1'], dependencias=[])
    r = fac.Factor('r', ['p0', 'p1'], prob_r_p, propios=['r0', 'r1'], dependencias=['p'])
    s = fac.Factor('s', ['q0', 'q1'], prob_s_q, propios=['s0', 's1'], dependencias=['q'])

    # Conjunto de factores
    factores = [p, q, r, s]

    # Variables a eliminar
    A = ['r']
    B = ['p1', 's0']

    ev_condicional = evc.EVCondicional(factores)
    variables_a_eliminar = ['p', 'q']

    start_time = time.time()
    ev_condicional.eliminaVariablesCondicional(A, B, variables_a_eliminar, factores)[0].imprimir()
    end_time = time.time()

    print(f"Tiempo de ejecución: {end_time - start_time} segundos")

def v4():
    # Tablas de probabilidad
    prob_m = {
        ('m0'): 0.5,
        ('m1'): 0.5
    }

    prob_n = {
        ('n0'): 0.4,
        ('n1'): 0.6
    }

    prob_o_m = {
        ('o0', 'm0'): 0.7,
        ('o0', 'm1'): 0.3,
        ('o1', 'm0'): 0.3,
        ('o1', 'm1'): 0.7
    }

    prob_t_n = {
        ('t0', 'n0'): 0.6,
        ('t0', 'n1'): 0.4,
        ('t1', 'n0'): 0.4,
        ('t1', 'n1'): 0.6
    }

    # Factores
    m = fac.Factor('m', [], prob_m, propios=['m0', 'm1'], dependencias=[])
    n = fac.Factor('n', [], prob_n, propios=['n0', 'n1'], dependencias=[])
    o = fac.Factor('o', ['m0', 'm1'], prob_o_m, propios=['o0', 'o1'], dependencias=['m'])
    t = fac.Factor('t', ['n0', 'n1'], prob_t_n, propios=['t0', 't1'], dependencias=['n'])

    # Conjunto de factores
    factores = [m, n, o, t]

    # Variables a eliminar
    A = ['o']
    B = ['m1']

    ev_condicional = evc.EVCondicional(factores)
    variables_a_eliminar = ['m', 'n']

    start_time = time.time()
    ev_condicional.eliminaVariablesCondicional(A, B, variables_a_eliminar, factores)[0].imprimir()
    end_time = time.time()

    print(f"Tiempo de ejecución: {end_time - start_time} segundos")


def v5():
    # Tablas de probabilidad
    prob_g = {
        ('g0'): 0.6,
        ('g1'): 0.4
    }

    prob_h = {
        ('h0'): 0.5,
        ('h1'): 0.5
    }

    prob_i_g = {
        ('i0', 'g0'): 0.8,
        ('i0', 'g1'): 0.2,
        ('i1', 'g0'): 0.2,
        ('i1', 'g1'): 0.8
    }

    prob_j_h = {
        ('j0', 'h0'): 0.7,
        ('j0', 'h1'): 0.3,
        ('j1', 'h0'): 0.3,
        ('j1', 'h1'): 0.7
    }

    # Factores
    g = fac.Factor('g', [], prob_g, propios=['g0', 'g1'], dependencias=[])
    h = fac.Factor('h', [], prob_h, propios=['h0', 'h1'], dependencias=[])
    i = fac.Factor('i', ['g0', 'g1'], prob_i_g, propios=['i0', 'i1'], dependencias=['g'])
    j = fac.Factor('j', ['h0', 'h1'], prob_j_h, propios=['j0', 'j1'], dependencias=['h'])

    # Conjunto de factores
    factores = [g, h, i, j]

    # Variables a eliminar
    A = ['i']
    B = ['g1', 'j0']

    ev_condicional = evc.EVCondicional(factores)
    variables_a_eliminar = ['g', 'h']

    start_time = time.time()
    ev_condicional.eliminaVariablesCondicional(A, B, variables_a_eliminar, factores)[0].imprimir()
    end_time = time.time()

    print(f"Tiempo de ejecución: {end_time - start_time} segundos")

def v6():
    prob_a = {
    ('a0'): 0.4,
    ('a1'): 0.6
    }

    prob_b = {
        ('b0'): 0.5,
        ('b1'): 0.5
    }

    prob_c_a = {
        ('c0', 'a0'): 0.7,
        ('c0', 'a1'): 0.3,
        ('c1', 'a0'): 0.6,
        ('c1', 'a1'): 0.4
    }

    prob_d_b = {
        ('d0', 'b0'): 0.8,
        ('d0', 'b1'): 0.2,
        ('d1', 'b0'): 0.5,
        ('d1', 'b1'): 0.5
    }

    prob_e_c = {
        ('e0', 'c0'): 0.9,
        ('e0', 'c1'): 0.1,
        ('e1', 'c0'): 0.3,
        ('e1', 'c1'): 0.7
    }

    prob_f_d = {
        ('f0', 'd0'): 0.6,
        ('f0', 'd1'): 0.4,
        ('f1', 'd0'): 0.4,
        ('f1', 'd1'): 0.6
    }

    prob_g_e = {
        ('g0', 'e0'): 0.75,
        ('g1', 'e0'): 0.25,
        ('g0', 'e1'): 0.45,
        ('g1', 'e1'): 0.55
    }

    prob_h_f = {
        ('h0', 'f0'): 0.65,
        ('h0', 'f1'): 0.35,
        ('h1', 'f0'): 0.55,
        ('h1', 'f1'): 0.45
    }

    prob_i_g = {
        ('i0', 'g0'): 0.6,
        ('i0', 'g1'): 0.4,
        ('i1', 'g0'): 0.5,
        ('i1', 'g1'): 0.5
    }

    a = fac.Factor('a', [], prob_a, propios=['a0', 'a1'], dependencias=[])
    b = fac.Factor('b', [], prob_b, propios=['b0', 'b1'], dependencias=[])
    c = fac.Factor('c', ['a0', 'a1'], prob_c_a, propios=['c0', 'c1'], dependencias=['a'])
    d = fac.Factor('d', ['b0', 'b1'], prob_d_b, propios=['d0', 'd1'], dependencias=['b'])
    e = fac.Factor('e', ['c0', 'c1'], prob_e_c, propios=['e0', 'e1'], dependencias=['c'])
    f = fac.Factor('f', ['d0', 'd1'], prob_f_d, propios=['f0', 'f1'], dependencias=['d'])
    g = fac.Factor('g', ['e0', 'e1'], prob_g_e, propios=['g0', 'g1'], dependencias=['e'])
    h = fac.Factor('h', ['f0', 'f1'], prob_h_f, propios=['h0', 'h1'], dependencias=['f'])
    i = fac.Factor('i', ['g0', 'g1'], prob_i_g, propios=['i0', 'i1'], dependencias=['g'])

    factores = [a, b, c, d, e, f, g, h, i]

    A = ['i']
    B = ['a1', 'h0', 'd1']

    ev_condicional = evc.EVCondicional(factores)

    variables_a_eliminar = ['a', 'b', 'c', 'e', 'f']

    start_time = time.time()
    ev_condicional.eliminaVariablesCondicional(A, B, variables_a_eliminar, factores)[0].imprimir()
    end_time = time.time()

    print(f"Tiempo de ejecución: {end_time - start_time} segundos")

if __name__ == "__main__":
    #ejemploEVMarginal()
    #v1()
    #v2()
    #v3()
    #v4()
    #v5()
    v6()