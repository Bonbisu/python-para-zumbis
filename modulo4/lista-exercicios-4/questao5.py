'''
Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras
“python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para
minúsculas e de remover antes os caracteres especiais.
'''

s = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'
new_s = []
for char in [',', ':', '.']:
    new_s = s.replace(char, '')

lista = []
quatro = []
for i in new_s.split():
    if i[0] in 'python' or i[-1] in 'python':
        lista.append(i)
        if len(i) > 4:
            quatro.append(i)
print('Palavras que começam ou terminam com "p y t h o n: "', lista, len(lista))
print('Com mais de 4 caracteres:', quatro, len(quatro))
