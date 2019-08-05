'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
tinta a serem compradas e o preço total. Obs. : somente são vendidos um número
inteiro de latas.
'''

area_pintar = float(input('Digite a área a ser pintada: '))
if area_pintar % 54 == 0:
    latas_tinta = area_pintar/54
else:
    latas_tinta = int(area_pintar/54)+1

preco_total = latas_tinta*80

print('Serão necessários %d latas de tinta. Total a pagar R$ %.2f' %
      (latas_tinta, preco_total))
