'''
REVISÃO - Adivinhar um numero aleatório dando dicas (gordox) alto ou baixo
Melhor resolvido com busca binária
'''

from random import randint


def chutar(chute):
    global menor
    global maior
    if chute == sorteado:
        print('Você acertou!')
        return True
    else:
        if chute < sorteado:
            menor = chute
            print('Mais alto!')
        else:
            maior = chute
            print('Mais baixo!')
        return False


menor, maior = 1, 100
tentativas = 0
sorteado = randint(menor, maior)
saiu = []

print('Jogo de advinação', sorteado)

while True:
    chute = randint(menor, maior)
    while chute in saiu:
        chute = randint(menor, maior)
    print('Menor %d, Maior %d. CHUTE: %d ' % (menor, maior, chute))
    if chutar(chute):
        break
    saiu.append(chute)
    tentativas += 1
print('Fim de jogo.', tentativas, sorted(saiu))
