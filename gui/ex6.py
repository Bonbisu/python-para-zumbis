import pygame.mixer
from time import sleep
from tkinter import *
app = Tk()
app.title('Show de calouros')
app.geometry('300x100+200+100')

sounds = pygame.mixer
sounds.init()

certos = IntVar()
errados = IntVar()
certos.set(0)
errados.set(0)


def espera_tocar(sound):
    while pygame.mixer.get_busy():
        sleep(1)
        pass


def musica_certa():
    certos.set(certos.get()+1)
    s = sounds.Sound('yes.wav')
    espera_tocar(s.play())


def musica_errada():
    errados.set(errados.get()+1)
    s = sounds.Sound('ohno.wav')
    espera_tocar(s.play())


label = Label(app, text='Aperte os botões:', height=3)
label.pack()
label1 = Label(app, textvariable=certos)
label1.pack(side='left')
label2 = Label(app, textvariable=errados)
label2.pack(side='right')


b1 = Button(app, text='Certo', width=10, command=musica_certa)
b1.pack(side='left', padx=10, pady=10)

b2 = Button(app, text='Errado', width=10, command=musica_errada)
b2.pack(side='right', padx=10, pady=10)


app.mainloop()
