import Factor as factor

def marginal(factores, variables):
    """
    Calcula la marginal de un conjunto de variables en una lista de factores.

    :param factores: lista de factores
    :param variables: lista de variables en orden
    :return: factor marginal de las variables
    """

    eliminar = variables.pop()
    print(eliminar)
    lista = []
    for i in range(len(factores)):
        print(factores[i].variables)
        if eliminar in factores[i].variables:
            lista.append(factores[i])
            factores.delete(i)
    if (len(lista) == 1):
        factores.append(factor.marginalizacion(lista, eliminar))
    else:
        producto = lista[0]
        for i in range(len(lista) - 1):
            producto = factor.producto_de_factores(producto, lista[i + 1])
        marginal = factor.marginalizacion(producto, eliminar)
        factores.append(marginal)
        return factores
    
f_D = factor.Factor('D', [], [[0.6], [0.4]], propios=['d^0', 'd^1'])


f_E = factor.Factor('E', [], [[0.8], [0.2]], propios=['e^0', 'e^1'])


f_C = factor.Factor('C', ['e^0', 'e^1'], [[0.6, 0.3, 0.1], [0.3, 0.4, 0.3]], propios=['c^0', 'c^1', 'c^2'])


f_A = factor.Factor('A', ['d^0', 'd^1', 'e^0', 'e^1'], [[0.3, 0.4, 0.3], [0.1, 0.2, 0.7], [0.7, 0.2, 0.1], [0.2, 0.3, 0.5]], propios=['a^0', 'a^1', 'a^2'])


f_B = factor.Factor('B', ['a^0', 'a^1', 'a^2'], [[0.7, 0.3], [0.4, 0.6], [0.1, 0.9]], propios=['b^0', 'b^1'])

factores = [f_D, f_E, f_C, f_A, f_B]
variables = ["c"]
print("Empezamos")
print(marginal(factores, variables))