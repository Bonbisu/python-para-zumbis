'''
Ler e imprimir as linhas dos arquivos
'''

# Non-Pythonic
# arquivo = open('numeros.txt', 'r')
# for linha in arquivo.readlines():
#     print(linha)
# arquivo.close()

# Pythonic Way

with open('numeros.txt') as f:
    print(f.read())
