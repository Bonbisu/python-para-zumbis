'''
Defina uma função fatorial.
'''


def fatorial(n):
    """ Calcula o fatorial de um número """
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return f


for i in range(1, 5):
    print(fatorial(i))
