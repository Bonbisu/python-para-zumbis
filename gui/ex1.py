import pygame.mixer

sounds = pygame.mixer
sounds.init()


def espera_e_toca(canal):
    while canal.get_busy():
        pass


s = sounds.Sound('heartbeat.wav')
espera_e_toca(s.play())
s2 = sounds.Sound('buzz.wav')
espera_e_toca(s2.play())
s3 = sounds.Sound('ohno.wav')
espera_e_toca(s3.play())
s4 = sounds.Sound('carhorn.wav')
espera_e_toca(s3.play())
