'''
Verifique se uma palavra é palíndrome
'''

frase = input('Digite uma palavra ou frase: ')

# tratamento da frase => sem espaços e sem case sensitive
frase_limpa = frase.replace(' ', '').lower()
frase_inversa = frase[::-1].replace(' ', '').lower()

if frase_limpa == frase_inversa:
    print('"%s" é palindrome.' % frase)
else:
    print('"%s" não é palindrome' % frase)
