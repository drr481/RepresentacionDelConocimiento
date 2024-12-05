import BC

numero = 0

def isComplete(BC):
    reglas = BC.reglas()
    hechos = BC.hechos()
    tablaReglas = generaTablaReglas(reglas)
    tablaHechos = {}
    for hecho in hechos:
        if (tablaHechos.isEmpty()):
            tablaHechos = generaTablaHechos(hecho)
        else:
            tablaHechos = tablaHechos.intersection(generaTablaHechos(hecho))
    C = tablaHechos.intersection(tablaReglas)
    return C.isSubset(BC.encadenamientoDelante())


def generaTablaReglas(reglas):
    pass

def generaTablaHechos(hechos):
    global numero
    nunVariables = 2**BC.variables().size()
    tabla = {}
    