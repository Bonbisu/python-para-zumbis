class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2

    def canal_acima(self):
        self.canal += 1
        print('Trocou o canal para cima:', self.canal)

    def canal_abaixo(self):
        self.canal -= 1
        print('Trocou o canal para baixo:', self.canal)

    def trocar_canal(self, x):
        self.canal = x
        print('Trocou para o canal:', self.canal)


tv = Televisao()
print('Tv ligada:', tv.ligada)
print('Canal:', tv.canal)
tv.canal_acima()
tv.canal_abaixo()
tv.trocar_canal('Faustão')
