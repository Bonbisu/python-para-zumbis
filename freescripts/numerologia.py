#!/usr/bin/python
# title			:numerologia.py.py
# description	:Calculadora para numerologia simples
# author			:bonbisu
# date			:20190723
# version		:0.0.1
# usage			:python numerologia.py.py
# notes			:
# python_version	:3.6.8
# ==============================================================================

n = input('n: ')
lista = list(n)

while len(lista) > 1:
    soma = 0
    for i in lista:
        soma += int(i)
    lista = list(str(soma))

print('Resultado:', soma)
