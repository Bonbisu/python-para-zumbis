labirinto = '''
+-----+-----+S+
|E    |     | |
| | +-+  -+ | |
| | |     | | |
| |   +---+   |
| | | |     | |
|   | | | | | |
|-----+S+-+-+ |
|     | | |   |
| +-+   | |  -|
| |-+-|   |-  |
| | | +---+-- |
|             |
+-------------+
'''

ENTRADA, LIVRE, PASSEI, SOLUCAO, SAIDA = 'E .oS'


def saiu(x, y):
    if lab[x][y] == SAIDA:
        return True
    if lab[x][y] in (ENTRADA, LIVRE):
        # marca o local que passou
        lab[x][y] = PASSEI
        # aqui a função é testada recursivamente nas quatro direções da posição
        # atual, garantindo assim que cada chamada da função irá testar os vizinhos "ao mesmo tempo"
        if saiu(x-1, y) or saiu(x+1, y) or saiu(x, y-1) or saiu(x, y+1):
            lab[x][y] = SOLUCAO
            return True
    else:
        return False


lab = []

# separar o labirinto em linhas e listar os caracteres
# assim formamos uma matiz lab[x][y]
for x in labirinto.splitlines():
    if len(x) > 0:
        x = list(x)
        lab.append(x)

# encontrar a ENTRADA do lab lido
for i in range(len(lab)):
    for j in range(len(lab[i])):
        if lab[i][j] == ENTRADA:
            x = i
            y = j
            break
# passando a entrada como parametro
if saiu(x, y):
    for linha in lab:
        print(''.join(linha))
else:
    print('A formiga vai morrer no labirinto')
