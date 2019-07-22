'''
Faça um programa que leia um vetor de dez numeros reais e mostre-os na ordem inversa
'''

vetor = []
x = 1
while x <= 10:
    vetor.append(float(input('Digite o %dº número: ' % (x))))
    x += 1
x -= 2
while x >= 0:
    print(vetor[x])
    x -= 1
