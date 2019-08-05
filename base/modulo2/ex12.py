'''
Calcule a soma de numeros inteiros ate ser digitado zero
'''

soma = 0
cnt = 1
while True:
    n = int(input('Digite o %d numero (0 sai): ' % cnt))
    if n == 0:
        break
    soma += n
    cnt += 1
print('Soma: %d' % soma)
