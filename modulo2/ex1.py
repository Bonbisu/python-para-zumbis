# Pergunte a velocidade de um carro, supondo um valor interiro. Caso ultrapasse 110 km/h, exiba uma mensagem dizendo que o usuário foi multado, cobrando R$5,00 por km acima de 110.

velocidade_medida = int(input('Insira a velocidade: '))
multa = (velocidade_medida - 110)*5
if velocidade_medida > 110:
    print('Usuário %d km/h acima da velocidade permitida. Multa: R$ %.2f.' %
          (velocidade_medida - 110, multa))
