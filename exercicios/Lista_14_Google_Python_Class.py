#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Exercícios extras para listas

# D. Dada uma lista de números retorna uma lista sem os elementos repetidos


def remove_iguais(nums):
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return sorted(dic.keys())


# E. Cripto desafio!!
# Dada uma frase, você deve retirar todas as letras repetidas das palavras
# e ordenar as letras que sobraram
# Exemplo: 'ana e mariana gostam de banana' vira 'an e aimnr agmost de abn'
# Dicas: tente transformar cada palavra em um conjunto,
# depois tente ordenar as letras e montar uma string com o resultado.
# Utilize listas auxiliares se facilitar


def cripto(frase):
    nova_frase = ''
    for word in frase.split():
        w = {}
        for letra in word:
            if letra not in w:
                w[letra] = 1
            else:
                w[letra] += 1
        nova_frase += ''.join(sorted(w.keys())) + ' '
    return nova_frase.rstrip()


# F. Derivada de um polinômio
# Os coeficientes de um polinômio estão numa lista na ordem do seu grau.
# Você deverá devolver uma lista com os coeficientes da derivada.
# Exemplo: [3, 2, 5, 2] retorna [2, 10, 6]
# A derivada de 3 + 2x + 5x^2 + 2x^3 é 2 + 10x + 6x^2


def derivada(coef):
    pd = []
    for i in range(1, len(coef)):
        pd.append(coef[i]*i)
    return pd

# G. Soma em listas invertidas
# Colocamos os dígitos de dois números em listas ao contrário
# 513 vira [3, 1, 5] e 295 vira [5, 9, 2]
# [3, 1, 5] + [5, 9, 2] = [8, 0, 8]
# Não vale converter a lista em número para somar diretamente


def soma(n1, n2):
    resultado = []
    resto = 0
    for i in range(len(n1)):
        soma = n1[i] + n2[i] + resto
        if len(str(soma)) > 1:
            resto = int(str(soma)[0])
        else:
            resto = 0
        resultado.append(int(str(soma)[-1]))
    if resto:
        resultado.append(resto)
    return resultado


# H. Anagrama
# Verifique se duas palavras são anagramas,
# isto é são uma é permutação das letras da outra
# anagrama('aberto', 'rebato') = True
# anagrama('amor', 'ramo') = True
# anagrama('aba', 'baba') = False


def anagrama(s1, s2):
    if len(s1) == len(s2):
        return len(s1) == len([x for x in s1 if x in s2])
    return False


def test(obtido, esperado):
    if obtido == esperado:
        prefixo = ' Parabéns!'
    else:
        prefixo = ' Ainda não'
    print('%s obtido: %s esperado: %s' %
          (prefixo, repr(obtido), repr(esperado)))


def main():
    print('remove_iguais')
    test(remove_iguais([2, 2, 1, 3]), [1, 2, 3])
    test(remove_iguais([2, 2, 3, 2, 3]), [2, 3])
    test(remove_iguais([]), [])

    print()
    print('cripto')
    test(cripto('ana e mariana gostam de banana'),
         'an e aimnr agmost de abn')
    test(cripto('Batatinha quando nasce esparrama pelo chão'),
         'Bahint adnoqu acens aemprs elop choã')

    print()
    print('derivada de polinômio')
    test(derivada([3, 0, 4, 3, 5]), [0, 8, 9, 20])
    test(derivada([4, 16, 1]), [16, 2])

    print()
    print('soma em listas invertidas')
    test(soma([5, 2, 3, 4], [9, 8, 7, 8]), [4, 1, 1, 3, 1])
    test(soma([3, 1, 5], [5, 9, 2]), [8, 0, 8])


'''
    print()
    print('anagrama')
    test(anagrama('aberto', 'rebato'), True)
    test(anagrama('amor', 'roma'), True)
    test(anagrama('ramo', 'amor'), True)
    test(anagrama('baba', 'aba'), False)
    test(anagrama('casa', 'cassa'), False)

'''
if __name__ == '__main__':
    main()
