from tkinter import *
import pygame.mixer

app = Tk()
app.title('DJ Mix')
app.geometry('250x100+200+100')

som = 'looperman-l-2714252-0176322-u-feel.wav'
mixer = pygame.mixer
mixer.init()


def start():
    track.play(loops=-1)


def stop():
    track.stop()


def termina():
    track.stop()
    app.destroy()


track = mixer.Sound(som)
start_button = Button(app, command=start, text='Start')
start_button.pack(side=LEFT)
stop_button = Button(app, command=stop, text='Stop')
stop_button.pack(side=RIGHT)

app.protocol('WM_DELETE_WINDOW', termina)
app.mainloop()
