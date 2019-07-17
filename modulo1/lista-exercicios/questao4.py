# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario_atual = float(input('Insira o salario atual: '))
aumento = float(input('Insira o aumento em porcentagem:'))

salario_ajustado = (salario_atual * aumento/100) + salario_atual

print('O salario ajustado é R$ %.2f' % salario_ajustado)
