from tkinter import *
import pygame.mixer

app = Tk()
app.title('DJ Mix')
som = 'u-feel.wav'
mixer = pygame.mixer
mixer.pre_init(buffer=300)  # diminui o delay inicial da musica
mixer.init()


def termina():
    track.stop()
    app.destroy()


def muda():
    if tocando.get() == 1:
        track.play(loops=-1)
    else:
        track.stop()


def muda_volume(v):
    track.set_volume(volume.get())


track = mixer.Sound(som)

tocando = IntVar()
tocar = Checkbutton(app, variable=tocando, command=muda, text=som)
tocar.pack(side=LEFT)

volume = DoubleVar()
volume.set(track.get_volume())

escala = Scale(variable=volume, from_=0.0, to=1.0, resolution=0.01,
               command=muda_volume, label='Volume', orient=HORIZONTAL, sliderlength=7, length=200)
escala.pack(side=RIGHT)

app.protocol('WM_DELETE_WINDOW', termina)
app.mainloop()
