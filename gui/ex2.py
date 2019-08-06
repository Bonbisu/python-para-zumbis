import pygame.mixer
from time import sleep
sounds = pygame.mixer
sounds.init()


def espera_tocar(sound):
    while pygame.mixer.get_busy():
        sleep(1)
        pass


certos = 0
errados = 0
opcao = int(input('Aperte 1- Certo, 2- Errado e 0- Finalizar'))


while opcao != 0:
    if opcao == 1:
        sounds.music.load('yes.wav')
        sounds.music.play()
        certos += 1
    if opcao == 2:
        s2 = sounds.Sound('ohno.wav')
        espera_tocar(s2.play())
        errados += 1
    opcao = int(input('Aperte 1- Certo, 2- Errado e 0- Finalizar'))


print('Certos: ', certos, 'Errados:', errados)
