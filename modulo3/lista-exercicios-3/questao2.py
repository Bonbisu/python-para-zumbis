'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''
while True:
    user = input('Digite o nome do usuario: ')
    password = input('Digite a senha: ')
    if user.lower().strip() != password.lower().strip():
        print('Usuario %s logado.' % user)
        break
    else:
        print('O usuário não pode ser igual a senha!')
