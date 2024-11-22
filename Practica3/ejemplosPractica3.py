import Chow_Liu as cl

# Ejemplo de uso de la clase Chow-Liu
# Se crea un objeto de la clase Chow-Liu

#Ejemplo con 2 variables
distribucion_probabilidad = {
        ('a^0','b^0'): 0.21,
        ('a^0','b^1'): 0.14,
        ('a^1','b^0'): 0.09,
        ('a^1','b^1'): 0.06
    }

cl.ChowLiu(distribucion_probabilidad)

#Ejemplo con 3 variables
distribucion_probabilidad = {
        ('a^0','b^0','c^0'): 0.21,
        ('a^0','b^0','c^1'): 0.14,
        ('a^0','b^1','c^0'): 0.09,
        ('a^0','b^1','c^1'): 0.06,
        ('a^1','b^0','c^0'): 0.06,
        ('a^1','b^0','c^1'): 0.09,
        ('a^1','b^1','c^0'): 0.14,
        ('a^1','b^1','c^1'): 0.21
    }

cl.ChowLiu(distribucion_probabilidad)

#Ejemplo con 4 variables

distribucion_probabilidad = {
        ('a^0','b^0','c^0','d^0'): 0.21,
        ('a^0','b^0','c^0','d^1'): 0.14,
        ('a^0','b^0','c^1','d^0'): 0.09,
        ('a^0','b^0','c^1','d^1'): 0.06,
        ('a^0','b^1','c^0','d^0'): 0.06,
        ('a^0','b^1','c^0','d^1'): 0.09,
        ('a^0','b^1','c^1','d^0'): 0.14,
        ('a^0','b^1','c^1','d^1'): 0.21,
        ('a^1','b^0','c^0','d^0'): 0.21,
        ('a^1','b^0','c^0','d^1'): 0.14,
        ('a^1','b^0','c^1','d^0'): 0.09,
        ('a^1','b^0','c^1','d^1'): 0.06,
        ('a^1','b^1','c^0','d^0'): 0.06,
        ('a^1','b^1','c^0','d^1'): 0.09,
        ('a^1','b^1','c^1','d^0'): 0.14,
        ('a^1','b^1','c^1','d^1'): 0.21
    }

cl.ChowLiu(distribucion_probabilidad)

#Ejemplo con 5 variables

distribucion_probabilidad = {
        ('a^0','b^0','c^0','d^0','e^0'): 0.21,
        ('a^0','b^0','c^0','d^0','e^1'): 0.14,
        ('a^0','b^0','c^0','d^1','e^0'): 0.09,
        ('a^0','b^0','c^0','d^1','e^1'): 0.06,
        ('a^0','b^0','c^1','d^0','e^0'): 0.06,
        ('a^0','b^0','c^1','d^0','e^1'): 0.09,
        ('a^0','b^0','c^1','d^1','e^0'): 0.14,
        ('a^0','b^0','c^1','d^1','e^1'): 0.21,
        ('a^0','b^1','c^0','d^0','e^0'): 0.21,
        ('a^0','b^1','c^0','d^0','e^1'): 0.14,
        ('a^0','b^1','c^0','d^1','e^0'): 0.09,
        ('a^0','b^1','c^0','d^1','e^1'): 0.06,
        ('a^0','b^1','c^1','d^0','e^0'): 0.06,
        ('a^0','b^1','c^1','d^0','e^1'): 0.09,
        ('a^0','b^1','c^1','d^1','e^0'): 0.14,
        ('a^0','b^1','c^1','d^1','e^1'): 0.21,
        ('a^1','b^0','c^0','d^0','e^0'): 0.21,
        ('a^1','b^0','c^0','d^0','e^1'): 0.14,
        ('a^1','b^0','c^0','d^1','e^0'): 0.09
}

cl.ChowLiu(distribucion_probabilidad)





