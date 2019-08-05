'''
Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também
divisíveis por 7?
Resposta: 183
'''
n = 0
for i in range(1067, 3627):
    if i % 2 == 0 and i % 7 == 0:
        n += 1

print(n)
