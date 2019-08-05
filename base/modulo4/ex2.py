'''
Estudo de escopo de variável
'''


def muda_e_imprime(x=-1):
    a = 7
    print('"a" DENTRO da função:', a)
    if not x and x in 'nN':
        return a


# Alterar "a" global com função
a = 5
print('"a" ANTES de mudar:', a)
muda_e_imprime()
print('"a" DEPOIS de mudar:', a)
# selecionar rodar a função com ou sem retorno
x = input('Mudar "a" para 7? ')
# atribui 7 se True(qualquer valor) ou None se False(-1, "nN")
a = muda_e_imprime(x)
print('"a" DEPOIS da ATRIBUIÇÃO com retorno:', a)
print('=========================================')

# Redefinindo a função com "global a"
a = 5


def muda_e_imprime_global():
    global a
    a = 7
    print('"a" dentro da função:', a)


print('"a" antes de mudar:', a)
muda_e_imprime_global()
print('"a" depoide mudar:', a)
