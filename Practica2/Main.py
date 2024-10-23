# Input: Conjunto de Factores
# Output: 
import Factor as f
import EVCondicional as evc

def main():

    prob_d = {
        'd0': 0.6,
        'd1': 0.4
    }

    prob_e = {
        'e0': 0.8,
        'e1': 0.2
    }

    d = f.Factor('d', [], prob_d , propios=['d^0', 'd^1'], dependencias=['d'])

    e = f.Factor('e', [], prob_e, propios=['e^0', 'e^1'], dependencias=['e'])

    # Crear un conjunto de factores de ejemplo
    factores = [
        d,
        e
    ]
    
    # Crear una instancia de EVCondicional
    ev_condicional = evc.EVCondicional(factores)
    
    # Definir las variables a eliminar
    variables_a_eliminar = ['e']
    
    # Llamar al método eliminaVariablesCondicional
    ev_condicional.eliminaVariablesCondicional(d, e, variables_a_eliminar, factores)
    
    # Imprimir el resultado para verificar
    print("Factores después de eliminar variables condicionales:")
    for factor in ev_condicional.factores:
        print(factor)

if __name__ == "__main__":
    main()