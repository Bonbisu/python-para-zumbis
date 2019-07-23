'''
 Dizemos que um número natural é triangular se ele é produto de três números naturais
consecutivos. Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n,
verificar se n é triangular.
'''

n = int(input('Digite o numero: '))
x = 0
# caso o produto dos 3 ultrapasse 'n' será usado o valor anterior para comparar
while x*(x+1)*(x+2) < n:
    x += 1
if x*(x+1)*(x+2) == n:
    print('%d é triangular.' % n)
else:
    print('%d não é triangular.' % n)
