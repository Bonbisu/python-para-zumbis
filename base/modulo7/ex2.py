'''
REVISÃO - Adivinhar o numero 42 dando dicas (gordox) alto ou baixo
'''

chute = 0
while chute != 42:
    chute = int(input('Digite um número: '))
    if chute == 42:
        print('Você acertou!')
    else:
        if chute < 42:
            print('Mais alto!')
        else:
            print('Mais baixo!')
print('Fim de jogo.')
