# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

distancia_percorrida = float(input('Insira a distancia percorrida em km: '))
dias_alugado = int(
    input('Insira a quantidade de dias que o carro foi alugado: '))

total = (dias_alugado*60) + (distancia_percorrida*.15)

print('O total a pagar pelo aluguel do carro é R$ %.2f.' % total)
