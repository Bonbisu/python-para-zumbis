'''
Gere uma lista de 15 inteiros aleatórios entre 10 e 100 que sejam DISTINTOS ENTRE SI
'''
import random
lista = []
while len(lista) < 15:
    n = random.randint(10, 100)
    if n not in lista:
        lista.append(n)

lista.sort()
print('Lista:', lista)
