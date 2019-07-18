# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.

cigarros_dia = int(input('Insira a quantidade de cigarros fumados por dia: '))
anos_fumo = int(input('Há quantos anos você fuma? '))

tempo_vida_perdido_ano = (cigarros_dia * 10)*365
total = tempo_vida_perdido_ano * anos_fumo
dias = (total/60)/24
horas = (dias - int(dias))*24
minutos = (horas - int(horas))*60

print('Você reduziu sua vida em %d dias, %d horas, %d minutos fumando.' %
      (dias, horas, minutos))
