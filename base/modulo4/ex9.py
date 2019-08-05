'''
Leia "mensagem.txt" e grave "cripto.txt" com todas a vogais trocadas por '*'
'''
input_file = 'mensagem.txt'
output_file = 'cripto.txt'
cripto = []
with open(input_file, 'r') as f:
    print('Mensagem carregada:', f)
    for l in f.readlines():
        s = ''
        for char in l:
            if char in 'aeiouAEIOUáéíóúÀàãõ':
                s += '*'
            else:
                s += char
        cripto.append(s)
print('Mensagem cifrada:', ' '.join(cripto))

with open(output_file, 'w') as f:
    for l in cripto:
        f.write(l)

print('Criptografado com sucesso!')
