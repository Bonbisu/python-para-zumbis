'''
Faca um programa que leia o arquivo "alice.txt" e conte o numero de ocorrencias
de cada palavra no texto. Obs: para saber os caracteres especiais use "import string"
e utilize string.punctuation

### Está contando mais vezes, precisa consertar o tratamento
'''
import string


def no_punctuation(linha):
    s = ''
    for char in linha:
        if char not in string.punctuation:
            s += char
    return s


palavras = {}
with open('alice.txt') as file:
    for l in file.readlines():
        l = no_punctuation(l.lower()).split()
        for w in l:
            if w in palavras:
                palavras[w] += 1
            else:
                palavras[w] = 1

print('Alice aparece %s vezes' % palavras['alice'])
