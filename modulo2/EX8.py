'''
Calculo da soma de dez numeros inteiros

A diferença entre um contador e um acumilador é que
nos contadores o valor adicionado é constante e,
nos acumuladores, variável.

'''

n = 1  # contador
soma = 0  # acumulador
while n <= 10:
    x = int(input('Digite o %d numero:' % n))
    soma = soma+x
    n += 1
print('Soma:', soma)
