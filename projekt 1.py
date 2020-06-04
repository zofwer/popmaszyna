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

def Muzyczka7():
    mixer.music.load("bass.wav") #tu jest miejsce na sample
    mixer.music.play()
def Muzyczka8():
    mixer.music.load("brzdęk.wav") #tu jest miejsce na sample
    mixer.music.play()
def Muzyczka9():
        mixer.music.load("dzwiek.wav") #tu jest miejsce na sample
        mixer.music.play()

def Muzyczka10():
    mixer.music.load("dzwięk2.wav") #tu jest miejsce na sample
    mixer.music.play()
def Muzyczka11():
    mixer.music.load("dzwiek3.wav") #tu jest miejsce na sample
    mixer.music.play()
def Muzyczka12():
    mixer.music.load("Kalimba-C4.wav") #tu jest miejsce na sample
    mixer.music.play()
def Muzyczka13():
    mixer.music.load("piano.wav") #tu jest miejsce na sample
    mixer.music.play()
def Muzyczka14():
    mixer.music.load("Shakuhachi.wav") #tu jest miejsce na sample
    mixer.music.play()
def Muzyczka15():
    mixer.music.load("skrzypce.wav") #tu jest miejsce na sample
    mixer.music.play()
def Muzyczka16():
    mixer.music.load("szczek.wav") #tu jest miejsce na sample
    mixer.music.play()
def Muzyczka17():
    mixer.music.load("taaa.wav") #tu jest miejsce na sample
    mixer.music.play()
def Muzyczka18():
    mixer.music.load("troba.wav") #tu jest miejsce na sample
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
przycisk6 = Button(glowne_okno, text = "DZWONKI", fg = "red", command = Muzyczka6)
przycisk6.grid(row =6 , column = 1)
przycisk7 = Button(glowne_okno, text = "BASS", fg = "red", command = Muzyczka7)
przycisk7.grid(row =7 , column = 1)

przycisk8 = Button(glowne_okno, text = "BRZDĘK", fg = "red", command = Muzyczka8)
przycisk8.grid(row =8 , column = 1)
przycisk9 = Button(glowne_okno, text = "DZIWIĘK", fg = "red", command = Muzyczka9)
przycisk9.grid(row =9 , column = 1)
przycisk10 = Button(glowne_okno, text = "DZWIĘK 2", fg = "red", command = Muzyczka10)
przycisk10.grid(row =10 , column = 1)
przycisk11 = Button(glowne_okno, text = "DZIWIĘK 3", fg = "red", command = Muzyczka11)
przycisk11.grid(row =11, column = 1)
przycisk12 = Button(glowne_okno, text = "KALIMBA", fg = "red", command = Muzyczka12)
przycisk12.grid(row =12, column = 1)
przycisk13 = Button(glowne_okno, text = "PIANINO", fg = "red", command = Muzyczka13)
przycisk13.grid(row =13 , column = 1)
przycisk14 = Button(glowne_okno, text = "SHAKUHACHI", fg = "red", command = Muzyczka14)
przycisk14.grid(row =14 , column = 1)
przycisk15 = Button(glowne_okno, text = "SKRZYPCE", fg = "red", command = Muzyczka15)
przycisk15.grid(row =15 , column = 1)
przycisk16 = Button(glowne_okno, text = "SZCZEKNIĘCIE", fg = "red", command = Muzyczka16)
przycisk16.grid(row = 16, column = 1)
przycisk17 = Button(glowne_okno, text = "TAIKO", fg = "red", command = Muzyczka17)
przycisk17.grid(row = 17, column = 1)
przycisk18 = Button(glowne_okno, text = "TRĄBA", fg = "red", command = Muzyczka18)
przycisk18.grid(row =18 , column = 1)




glowne_okno.mainloop()
