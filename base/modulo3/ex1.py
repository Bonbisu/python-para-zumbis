'''
Calcule a média de 5 notas
'''

notas = [10, 7, 8.5, 9, 7.7]
x = 0
soma = 0
while x < 5:
    soma += notas[x]
    x += 1

print('Média do aluno: %.2f' % (soma/x))
