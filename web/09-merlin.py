# testar no python tutor com calma
def enumeracoes(itens):
    n = len(itens)
    s = [0]*(n+1)
    k = 0
    while True:
        if s[k] < n:
            s[k+1] = s[k]+1
            k += 1
        else:
            s[k-1] += 1
            k -= 1
        if k == 0:
            break
        else:
            lista = []
            for j in range(1, k+1):
                lista.append(itens[s[j]-1])
            yield lista


def combinacoes(itens, n):
    if n == 0:
        yield []
    else:
        for i in range(len(itens)):
            for cc in combinacoes(itens[:i] + itens[i+1:], n-1):
                yield [itens[i]]+cc


def permutacoes(itens):
    return (combinacoes(itens, len(itens)))


print('Permutaçoes')
for p in permutacoes(['Adriano', 'Bruno', 'Diogo', 'Eclis', 'Gabriel', 'Leandro']):
    print(p)

print('Enumeracoes')
for p in enumeracoes(['Jessica', 'Fernanda', 'Pamela', 'Renata']):
    print(p)
