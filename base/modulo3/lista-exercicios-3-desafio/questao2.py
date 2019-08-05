'''
Indique como um troco deve ser dado utilizando-se um número mínimo de notas. Seu
algoritmo deve ler o valor da conta a ser paga e o valor do pagamento efetuado desprezando
os centavos. Suponha que as notas para troco sejam as de 50, 20, 10, 5, 2 e 1 reais, e que
nenhuma delas esteja em falta no caixa.
'''

conta = int(input('Digite o valor da conta a ser paga: '))
pagto = int(input('Digite o valor do pagto efetuado: '))
notas = [50, 20, 10, 5, 2, 1]
notas_troco = []
i = 0
if pagto < conta:
    print('Dinheiro insuficiente!')
else:
    troco = pagto-conta
    while troco != 0:
        for nota in notas:
            notas_troco.append(troco/nota)
            troco -= nota*int(troco/nota)

print('TROCO:')
for nota in notas:
    print('%d notas de %d.' %
          (notas_troco[notas.index(nota)], nota))
