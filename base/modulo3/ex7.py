'''
Faça um programa que leia uma palavra e troque as vogaois por "*"
'''

frase = input('Digite uma palavra ou frase: ')
nova_frase = ''

i = 0
while i < len(frase):
    if frase[i] in 'aeiouAEIOUáéíóúÁÉÍÓÚà':
        nova_frase += '*'
    else:
        nova_frase += frase[i]
    i += 1

# print('Frase original:"%s"' % frase)
print('Nova frase: "%s"' % nova_frase)
