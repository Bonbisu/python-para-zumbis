'''
Faça um programa que leia quatro notas, mostre as notas e a média na tela
'''

i = 0
notas = []
soma = 0
while i < 4:
    notas.append(float(input('Digite a %d nota: ' % (i+1))))
    soma += notas[i]
    i += 1

print('Notas: ', notas)
print('Média: %.2f' % (soma/4))
