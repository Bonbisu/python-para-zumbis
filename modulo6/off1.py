'''
Estudo de objetos

Tudo em python é um objeto. 
'''

# podemos criar uma string vazia
s = str()
print(s)

# podemos  ver os possiveis métodos (funções) de uma string
dir(s)

# os métodos sublinhados, como __add__ são metodos reservados
print('Usando + :', 'abacate'+'mamão')
# o "+" é um açucar sintatico e chama o metodo __add__ da str
print('Usando __add__(): ', 'abacate'.__add__('mamão'))
