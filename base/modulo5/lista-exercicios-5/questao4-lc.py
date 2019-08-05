'''
Questão D. Daniela é uma pessoa muito supersticiosa. Para ela, um número é sortudo
se ele contém o dígito 2 mas não o dígito 7. Então, na opinião dela, quantos números
sortudos existem entre 18644 e 33087, incluindo os extremos?
Resposta: 7995
List Comprehension
'''

print(len([i for i in range(18644, 33088)
           if '2' in str(i) and '7' not in str(i)]))
