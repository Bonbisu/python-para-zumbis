'''
Faça um programa que leia um vetor de 10 caracteres minusculos, e diga quantas 
consoantes foram lidas
'''

i = 0
vetor = []
consoantes = 0
while i < 10:
    l = input('Digite uma letra minuscula: ')
    vetor.append(l)
    i += 1
    if l.lower() not in 'aeiou':
        consoantes += 1

print('Numero de consoantes:', consoantes)
