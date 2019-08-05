'''
Faça um programa que leia um vetor de 5 numeros inteiros e mostre o vetor
'''
x = 1
vetor = []
while x <= 5:
    vetor.append(int(input('Digite o %dº número: ' % x)))
    x += 1

print('Vetor:', vetor)
