# Imprimir os numeros pares entre 0 e um numero fornecido usando if

fim = int(input('Digite o ultimo numero: '))
x = 0
while x <= fim:
    if x % 2 == 0:
        print(x)
    x += 1
