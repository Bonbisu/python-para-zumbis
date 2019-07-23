'''
Dados dois números inteiros positivos, determinar o máximo divisor comum entre
eles usando o algoritmo de Euclides
'''

a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segunto numero: '))

while a%b != 0:
    a, b = b, a%b
print('MDC: %d' % b)
