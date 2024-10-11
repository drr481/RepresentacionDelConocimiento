# Input: Conjunto de Factores
# Output: 
import Factor as f

f_A = f.Factor('A', ['d^0', 'd^1', 'e^0', 'e^1'], [[0.3, 0.4, 0.3], [0.1, 0.2, 0.7], [0.7, 0.2, 0.1], [0.2, 0.3, 0.5]], propios=['a^0', 'a^1', 'a^2'])

f_A.imprimir()
print(f.dependencias(f_A))