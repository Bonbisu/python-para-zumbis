class int42(int):
    def __init__(self, n):
        int.__init__(n)

    # toda soma retorna 42
    def __add__(a, b):
        return 42

    # todo inteiro retorna o valor 42 em print
    def __str__(n):
        return '42'
