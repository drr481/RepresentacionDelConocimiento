import BC

def encadenamientoAdelante(hechos, reglas):
    while True:
        bandera = False
        for regla in reglas:
            if regla[1] in hechos and regla[2] in hechos and regla[3] not in hechos:
                hechos.append(regla[3])
                bandera = True
        if not bandera:
            break
    return hechos