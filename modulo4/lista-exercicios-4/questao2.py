'''
Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na lista PAR e os
números ímpares na lista IMPAR. Imprima as três listas
'''
import random

par = []
impar = []
n = []
for i in range(20):
    n.append(random.randint(1, 100))
    if n[i] % 2 == 0:
        par.append(n[i])
    else:
        impar.append(n[i])

par.sort()
impar.sort()
n.sort()
print('Pares:', par)
print('Impares:', impar)
print('Numeros sorteados:', n)
