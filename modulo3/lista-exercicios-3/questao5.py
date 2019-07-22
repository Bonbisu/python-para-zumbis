'''
Dados dois números inteiros positivos, determinar o máximo divisor comum entre
eles usando o algoritmo de Euclides
'''

x = 0
a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segunto numero: '))
num = [a, b]
restos = []

while a % b != 0:
    resto = a % b
    restos.append(resto)
    a, b = b, resto
print('MDC(%d, %d): %d' % (num[0], num[1], restos[-1]))
