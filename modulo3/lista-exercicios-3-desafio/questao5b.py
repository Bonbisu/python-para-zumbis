'''
Faça um programa que peça um inteiro positivo e o mostre invertido.
ex 1234 gera 4321
'''
n = int(input('Digite um numero: '))
inv = 0
while n > 0:
    inv *= 10
    inv += n % 10
    n //= 10

print(inv)
