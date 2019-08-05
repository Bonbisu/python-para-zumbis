'''
Leia mensagem.txt e grave cripto.txt com todas as vogais trocadas por "*"
'''
input_file = open('mensagem.txt', 'r')
output_file = open('cripto.txt', 'w')
print('Mensagem carregada:')

for linha in input_file.readlines():
    print(linha)
    for letra in linha:
        if letra in 'aeiouAEIOUáéíóúÀàãõ':
            output_file.write('*')
        else:
            output_file.write(letra)

input_file.close()
output_file.close()

print('Criptografado com sucesso!')
