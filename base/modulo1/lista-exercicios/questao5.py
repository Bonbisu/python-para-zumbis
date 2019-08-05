# Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco_produto = float(input('Insira o preço do produto: '))
desconto = int(input('Insira o desconto: '))

total = preco_produto - (preco_produto*desconto/100)
print('O preço do produto com %d%% de desconto é %.2f' % (desconto, total))
