'''
Substitua cada tigre por um animal diferente
'''

s = 'um tigre, dois tigres, tres tigres'
animals = ['macaco', 'cavalo', 'capivara']
i = 0
while i < len(animals):
    # substitui apenas 1 ocorrencia(primeira)
    s = s.replace('tigre', animals[i], 1)
    print(s)
    i += 1
print('Nova string: "%s"' % s)
