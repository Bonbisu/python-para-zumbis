'''
Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar
as funções max e min.
'''

import random
lista = []
for i in range(10):
    lista.append(random.randint(1, 100))

lista.sort()
print('Maior:', lista[-1], 'Menor:', lista[0])
print('Lista Sorteada:', lista)
