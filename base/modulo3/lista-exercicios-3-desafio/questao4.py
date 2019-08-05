'''
Dado um número inteiro positivo, determine a sua decomposição em fatores primos 
calculando tambem a multiplicidade de cada fator
'''

n = int(input('Digite um numero: '))
for i in range(2, n):
    while n % i == 0:
        print(i)
        n = n/i
