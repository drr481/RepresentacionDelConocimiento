def marginal(factores, variables):
    """
    Calcula la marginal de un conjunto de variables en una lista de factores.

    :param factores: lista de factores
    :param variables: lista de variables en orden
    :return: factor marginal de las variables
    """



    ### Recursiva (lista)
    ### if len(lista)== 1: return lista
    ### else: sustituir 0 y 1 por producto(lista[0],lista[1])
    ### return recursiva (lista[1:]) a,b,c (a*b,c) (a*b*c)
