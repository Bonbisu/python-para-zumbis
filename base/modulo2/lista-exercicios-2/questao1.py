'''
Faça um Programa que peça os três lados de um triângulo. 
O programa deverá informar se os valores podem ser
um triângulo. 
Indique, caso os lados formem um triângulo, 
se o mesmo é: equilátero, isósceles ou escaleno.
'''

a = int(input('Insira a medida do lado a: '))
b = int(input('Insira a medida do lado b: '))
c = int(input('Insira a medida do lado c: '))

if ((abs(b-c) < a)and(a < b+c)) or ((abs(a-c) < b)and(b < a+c)) or ((abs(a-b) < c)and(c < a+b)):
    print('O triangulo %dx%dx%d é ' % (a, b, c), end='')
    if a == b == c:
        print('equilátero')
    elif a == b or b == c or a == c:
        print('isósceles')
    else:
        print('escaleno')
else:
    print('Não pode ser triangulo!')
    print('Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.')
