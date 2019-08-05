'''
Questão C. Entre 1067 e 3627 (inclusive), quantos números são pares e também
divisíveis por 7?
Resposta: 183
List Comprehension
'''

print(len([k for k in range(1067, 3627) if k % 2 == 0 and k % 7 == 0]))
