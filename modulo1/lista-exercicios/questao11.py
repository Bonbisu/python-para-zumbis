# Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado a um milhão.

potencia = 2 ** 1000000
print('Existem %d digitos em 2 elevado a um milhão' % len(str(potencia)))
