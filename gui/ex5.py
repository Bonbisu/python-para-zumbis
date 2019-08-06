import pygame.mixer
from time import sleep
from tkinter import *
app = Tk()
app.title('Show de calouros')
app.geometry('300x100+200+100')

sounds = pygame.mixer
sounds.init()

certos = errados = 0


def espera_tocar(sound):
    while pygame.mixer.get_busy():
        sleep(1)
        pass


def musica_certa():
    global certos
    s = sounds.Sound('yes.wav')
    espera_tocar(s.play())
    certos += 1


def musica_errada():
    global errados
    s = sounds.Sound('ohno.wav')
    espera_tocar(s.play())
    errados += 1


b1 = Button(app, text='Certo', width=10, command=musica_certa)
b1.pack(side='left', padx=10, pady=10)

b2 = Button(app, text='Errado', width=10, command=musica_errada)
b2.pack(side='right', padx=10, pady=10)

app.mainloop()
