from tkinter import *
from pygame import mixer
import random
import sounddevice as sd
import numpy as np


mixer.init()

glowne_okno = Tk()
glowne_okno.geometry('600x500')
glowne_okno.title("POPMASZYNA")


nazwa = Label(glowne_okno, text = "POPMASZYNA, WYBIERZ OPCJĘ:")
nazwa.grid()
def Muzyczka1():
    mixer.music.load("Bamboo.wav ") #tu jest miejsce na sample
    mixer.music.play()


def Muzyczka2():
    mixer.music.load("Claves.wav ") #tu jest miejsce na sample
    mixer.music.play()

def Muzyczka3():
    mixer.music.load("gitara.wav ") #tu jest miejsce na sample
    mixer.music.play()

def Muzyczka4():
    mixer.music.load("elektryk.wav ") #tu jest miejsce na sample
    mixer.music.play()

def Muzyczka5():
    mixer.music.load("syntezator.wav ") #tu jest miejsce na sample
    mixer.music.play()

def Muzyczka6():
    mixer.music.load("dzwonki.wav ") #tu jest miejsce na sample
    mixer.music.play()

def losowa_melodia1(fs = 44100, amplituda_sygnalu = 1, dlugosc_dzwieku = 1):
    for i in range(5):
        czestotliwosc_tonu = random.randint(100,500)
        czas = np.arange(0, 1, 1/fs)
        sygnal = amplituda_sygnalu * np.sin(2 * np.pi * czestotliwosc_tonu * czas)
        sd.play(sygnal)
        sd.wait()

def losowa_melodia2(fs = 44100, amplituda_sygnalu = 2,dlugosc_dzwieku=1):
    for i in range(15):
        czestotliwosc_tonu = random.randint(100,500)
        czas = np.arange(0, 1, 1/fs)
        sygnal = amplituda_sygnalu * np.sin(2 * np.pi * czestotliwosc_tonu * czas)
        sd.play(sygnal)
        sd.wait()

przycisk1 = Button(glowne_okno, text = "BĘBNY", fg = "gold",  command = Muzyczka1)
przycisk1.grid(row = 1, column = 1)
przycisk2 = Button(glowne_okno, text = "COŚ", fg = "indian red", command = Muzyczka2)
przycisk2.grid(row = 2, column = 1)
przycisk3 = Button(glowne_okno, text = "GITARA", fg = "coral", command = Muzyczka3)
przycisk3.grid(row = 3, column = 1)
przycisk4 = Button(glowne_okno, text = "GITARA ELEKTRYCZNA", fg = "salmon", command = Muzyczka4)
przycisk4.grid(row = 4, column = 1)
przycisk5 = Button(glowne_okno, text = "SYNTEZATOR", fg = "red", command = Muzyczka5)
przycisk5.grid(row = 5, column = 1)
przycisk5 = Button(glowne_okno, text = "DZWONKI", fg = "red", command = Muzyczka6)
przycisk5.grid(row = 6, column = 1)
przycisk6 = Button(glowne_okno, text = "krótka losowa melodia", fg = "hot pink", command = losowa_melodia1)
przycisk6.grid(row = 7, column = 1)
przycisk7 = Button(glowne_okno, text = "długa losowa melodia", fg = "maroon", command = losowa_melodia2)
przycisk7.grid(row = 8, column = 1)

glowne_okno.mainloop()
