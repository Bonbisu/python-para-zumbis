'''
Seletiva Facebook Hackaton 2013
Dados dois inteiros positivos n e k, gerar todos os binários entre os inteiros 0 e 2**n-1, inclusive. Estes binários serão sorteados em ordem descrescente segundo o números de 1s existentes. Caso haja empate escolhemos o menor valor númerico. Retorne o k-ésimo elemento da lista sorteada. Dicas: use count, bin e uma função para sortear por outra chave.
 
Ex.: n = 3 e k = 5
['0b111', '0b11', '0b101', '0b110', '0b1', '0b10', '0b100', '0b0']
quinto elemento '0b1'

n = 4 
['0b1111', '0b111', '0b1011', '0b1101', '0b1110', '0b11', '0b101', '0b110', '0b1001', '0b1010', '0b1100', '0b1', '0b10', '0b100', '0b1000', '0b0']

n = 5 
['0b11111', '0b1111', '0b10111', '0b11011', '0b11101', '0b11110', '0b111', '0b1011', '0b1101', '0b1110', '0b10011', '0b10101', '0b10110', '0b11001', '0b11010', '0b11100', '0b11', '0b101', '0b110', '0b1001', '0b1010', '0b1100', '0b10001', '0b10010', '0b10100', '0b11000', '0b1', '0b10', '0b100', '0b1000', '0b10000', '0b0']

'''


def hack(n, k):
    def f(s):
        return s.count('1')
    binarios = []
    for x in range(2**n):
        binarios.append(bin(x))
    binarios.sort(key=f, reverse=True)
    return binarios[k-1]


def hack_oneline(n, k):
    return sorted([bin(x) for x in range(2**n)], key=lambda s: s.count('1'), reverse=True)[k-1]


n = 4
['0b1111', '0b111', '0b1011', '0b1101', '0b1110', '0b11', '0b101', '0b110',
    '0b1001', '0b1010', '0b1100', '0b1', '0b10', '0b100', '0b1000', '0b0']
print('%21s %s' % ('Hack N4K7:', hack(n, 7)))
print('%21s %s' % ('Hack oneline N4K7:', hack_oneline(n, 7)))

n = 5
['0b11111', '0b1111', '0b10111', '0b11011', '0b11101', '0b11110', '0b111', '0b1011', '0b1101', '0b1110', '0b10011', '0b10101', '0b10110', '0b11001', '0b11010',
    '0b11100', '0b11', '0b101', '0b110', '0b1001', '0b1010', '0b1100', '0b10001', '0b10010', '0b10100', '0b11000', '0b1', '0b10', '0b100', '0b1000', '0b10000', '0b0']

print('%21s %s' % ('Hack N5K14:', hack(n, 7)))
print('%21s %s' % ('Hack oneline N5K14:', hack_oneline(n, 7)))
