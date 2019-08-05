'''
Faça um programa que crie dois vetores com 10 elementos aleatórios entre 1 e 100. Gere um
terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores. Imprima os três vetores.
'''
import random
v1 = []
v2 = []
v3 = []
for i in range(10):
    v1.append(random.randint(1, 100))
    v2.append(random.randint(1, 100))

v1.sort()
v2.sort()
for i in range(len(v1)):
    v3.append(v1[i])
    v3.append(v2[i])

print('Vetor 1:', v1)
print('Vetor 2:', v2)
print('Vetor 3:', v3)
