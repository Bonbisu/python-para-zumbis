'''
Calcule o fatorial de um numero inteiro n
'''

x = 1
fatorial = 1
n = int(input('Digite n: '))
while x <= n:
    fatorial *= x
    x += 1
print('Fatorial de %d: %d' % (n, fatorial))
