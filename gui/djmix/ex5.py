'''
Recursão

"Para enrender recursão,
é preciso primeiro entender recursão"
                            - folclore
"Ao tentar resolver o problema,
encontrei obstáculos dentro de obstáculos.
Por isso, adotei uma solução recursiva."
                            - um aluno

if <caso simples>:
    return <resposta>
else:
    <lógica para reduzir a instância>
    <chamar a função na instância menor>
    <compor a resposta baseada na instância menor>
    return <resposta>
'''


from functools import lru_cache  # last result used


def contagem(n):
    print(n)
    if n > 0:
        return contagem(n-1)


print('cont10')
contagem(10)


def fat(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fat(n-1)


print('fat4', fat(4))


def pot(x, n):
    if n == 0:
        return 1
    else:
        return x*pot(x, n-1)


print('pot2**3', pot(2, 3))
print('RUIM')


def fibruim(n):
    print('fibruim(%d)' % n)

    if n <= 2:
        return 1
    else:
        return fibruim(n-1) + fibruim(n-2)


fibruim(10)
print('CACHE')


fib_cache = {}


def fibcache(n):
    print('fibcache(%d)' % n)
    if n <= 2:
        return 1
    else:
        if n not in fib_cache:
            fib_cache[n] = fibcache(n-1) + fibcache(n-2)
        return fib_cache[n]


fibcache(10)
print('LIB')


# otimizado com biblioteca


@lru_cache(maxsize=None)  # decorator de functools
# descarta as funçoes menos chamadas e armazena em cache as mais usadas
def fiblib(n):
    print('fiblib(%d)' % n)
    if n <= 2:
        return 1
    return fiblib(n-1) + fiblib(n-2)


fiblib(10)


def mdc(a, b):
    if a % b == 0:
        return b
    else:
        return mdc(b, a % b)


print(mdc(24, 15))


def soma(n):
    if n < 10:
        return n
    else:
        return n % 10 + soma(n//10)


print(soma(123))


def inv(s):
    if s == '':
        return s
    else:
        return inv(s[1:]) + s[0]


print(inv('abacate'))
