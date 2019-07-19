'''
Faça um Programa que leia três números e mostre o maior e o menor deles
'''
a = int(input('Digite o primeiro numero: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro numero: '))


if a >= b and a >= c:
    print('%d é maior' % a)
elif b >= c:
    print('%d é maior' % b)
else:
    print('%d é maior' % c)


if a <= b and a <= c:
    print('%d é menor' % a)
elif b <= c:
    print('%d é menor' % b)
else:
    print('%d é menor' % c)
