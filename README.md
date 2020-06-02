# popmaszyna
from tkinter import *
from pygame import mixer

mixer.init()
glowne_okno = Tk()
glowne_okno.geometry('500x500')
glowne_okno.title("POPMASZYNA")


nazwa = Label(glowne_okno, text = "Sample")
nazwa.grid()

def play_music1():
    mixer.music.load(" ") #tu jest miejsce na sample
    mixer.music.play()


def play_music2():
    mixer.music.load(" ") #tu jest miejsce na sample
    mixer.music.play()


przycisk_play1 = Button(glowne_okno, text = "pierwszy dźwięk", fg = "red",  command = play_music1)
przycisk_play1.grid(row = 0, column = 0)
przycisk_play2 = Button(glowne_okno, text = "drugi dźwięk", fg = "green", command = play_music2)
przycisk_play2.grid(row = 2, column = 0)


glowne_okno.mainloop()
