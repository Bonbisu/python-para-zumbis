# Converta uma temperatura digitada em Fahrenheint para Celsius. F = 9*C/5 + 32

fahrenheint = float(input('Insira a temperatura em graus Fahrenheint: '))
celsius = ((fahrenheint - 32)/9)*5

print('A temperatura em graus Celsius é %.1f ºC' % celsius)
