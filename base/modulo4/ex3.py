'''
Defina uma funçao "embaralha" que retorne as letras de uma string misturada
'''
import random


def embaralha(s):
    """
    Recebe uma sring e a retorna embaralhada
    """
    l = list(s)
    random.shuffle(l)
    return ''.join(l)


w = input('Digite uma palavra: ')
print('Embaralhado:', embaralha(w))
