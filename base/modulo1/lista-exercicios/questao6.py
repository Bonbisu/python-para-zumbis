# Calcule o horas de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem.

distancia = int(input('Qual a distancia a percorrer em km? '))
velocidade = int(input('Qual será a velocidade média da viagem? '))

horas = distancia/velocidade
minutos = (horas - int(horas))*60
print('O horas esperado de viagem é de %d horas e %d minutos.' % (horas, minutos))
