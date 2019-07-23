'''
Verifique se um numero inteiro positivo n é primo
'''

n = int(input('Digite um numero: '))
divisores = []
i = 1
while i <= n:
    if n % i == 0:
        divisores.append(i)
    i += 1
if len(divisores) == 2:
    print('%d é primo.' % n)
else:
    print('%d não é primo. É divisivel por: ' % (n), divisores[1:-1])
