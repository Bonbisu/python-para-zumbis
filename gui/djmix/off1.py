'''
Criar um sampler
'''

from tkinter import *
import pygame.mixer

app = Tk()
app.title('DJ Mix')
app.geometry('250x100+200+100')

som = 'u-feel.wav'
mixer = pygame.mixer
mixer.init()


def termina():
    track.stop()
    app.destroy()


def muda():
    if tocando.get() == 1:
        track.play(loops=-1)
    else:
        track.stop()


musicas = []
with open('musicas.txt') as file:
    for l in file:
        musicas.append(l.rstrip())

print(musicas)
tracks = [mixer.Sound(som) for som in musicas]
tocando = IntVar()
[Checkbutton(app, variable=tocando, command=muda, text=som).pack()
 for som in tracks]


app.protocol('WM_DELETE_WINDOW', termina)
app.mainloop()
