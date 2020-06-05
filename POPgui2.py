import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk, ImageFilter
from tkinter import messagebox
from functools import partial
from pygame import mixer
import random
import sounddevice as sd
import numpy as np

class PopmaszynaGUI(Frame,object):

    def __init__(self,master):
        super(PopmaszynaGUI, self).__init__(master)
        self.master.title("Popmaszyna")
        self.master.geometry("700x400")
        self.pack()
        self.start_button()
        self.akcja_menu()
        mixer.init()

    def start_button(self):
        global obrazTk
        przycisk1 = Button(background, text = "START!", fg = "red", command = self.akcja_main_window)
        przycisk1.place(x = 310, y = 300)

    def akcja_menu(self):
        pasek_menu = Menu(glowne_okno)
        first_menu = Menu(pasek_menu, tearoff = 0)
        first_menu.add_command(label = "Autorzy", command = self.show_authors)
        first_menu.add_command(label = "Quit Popmaszyna", command = glowne_okno.quit)
        pasek_menu.add_cascade(label = "Opcje", menu = first_menu)
        glowne_okno.config(menu = pasek_menu)

    def akcja_main_window(self):
        main_window = Tk()
        main_window.geometry("700x700")
        main_window.title("Popmaszyna")
        przycisk1 = Button(main_window, text = "1 DZIWIĘK", fg = "dark green", bg="sienna2", width=30, height=5,command = lambda: self.play_sample(0))
        przycisk1.grid(row = 1, column = 1)
        przycisk2 = Button(main_window, text = "2 DZIWIĘK", fg = "navy", bg="tan4" , width=30, height=5,command = lambda: self.play_sample(1))
        przycisk2.grid(row = 2, column = 1)
        przycisk3 = Button(main_window, text = "3 DZIWIĘK", fg = "dodger blue",bg="OliveDrab4" ,  width=30, height=5,command = lambda: self.play_sample(2))
        przycisk3.grid(row = 3, column = 1)
        przycisk4 = Button(main_window, text = "4 DZIWIĘK", fg = "yellow",bg="brown4" , width=30, height=5, command = lambda: self.play_sample(3))
        przycisk4.grid(row = 4, column = 1)
        przycisk5 = Button(main_window, text = "5 DZIWIĘK", fg = "goldenrod",bg="coral2" , width=30, height=5, command = lambda: self.play_sample(4))
        przycisk5.grid(row =1 , column = 2)
        przycisk6 = Button(main_window, text = "6 DZIWIĘK", fg = "red",bg="navy" , width=30, height=5, command = lambda: self.play_sample(5))
        przycisk6.grid(row = 2, column = 2)
        przycisk7 = Button(main_window, text = "7 DZIWIĘK", fg = "deep pink",bg="dodger blue" ,  width=30, height=5,command = lambda: self.play_sample(6))
        przycisk7.grid(row = 3, column = 2)
        przycisk8 = Button(main_window, text = "8 DZIWIĘK", fg = "cyan2",bg="yellow" , width=30, height=5, command = lambda: self.play_sample(7))
        przycisk8.grid(row = 4, column = 2)
        przycisk9 = Button(main_window, text = "9 DZIWIĘK", fg = "OliveDrab4",bg="goldenrod" , width=30, height=5, command = lambda: self.play_sample(8))
        przycisk9.grid(row = 1, column = 3)
        przycisk10 = Button(main_window, text = "10 DZIWIĘK", fg = "sienna2",bg="deep pink" , width=30, height=5, command = lambda: self.play_sample(9))
        przycisk10.grid(row = 2, column = 3)
        przycisk11 = Button(main_window, text = "11 DZIWIĘK", fg = "tan4",bg="magenta2" , width=30, height=5, command = lambda: self.play_sample(10))
        przycisk11.grid(row = 3, column = 3)
        przycisk12 = Button(main_window, text = "12 DZIWIĘK", fg = "brown4",bg="dark green" ,  width=30, height=5,command = lambda: self.play_sample(11))
        przycisk12.grid(row = 4, column = 3)
        przycisk13 = Button(main_window, text = "13 DZIWIĘK", fg = "coral2",bg="goldenrod" ,  width=30, height=5,command = lambda: self.play_sample(12))
        przycisk13.grid(row = 1, column = 4)
        przycisk14 = Button(main_window, text = "14 DZIWIĘK", fg = "magenta2",bg="cyan2" , width=30, height=5, command = lambda: self.play_sample(13))
        przycisk14.grid(row = 2, column = 4)


    def play_sample(self, numer):
        global lista_sampli
        mixer.music.load(lista_sampli[numer])
        mixer.music.play()

    def show_authors(self):
        messagebox.showinfo("Autorzy programu", "Julia Naklicka \nAleksandra Draszewska \nKarolina Kulikowska \nZofia Wereszko")

glowne_okno = Tk()
background = Canvas(glowne_okno, width=700, height=400)
background.pack()
obraz = Image.open("popmaszynapic.png")
obrazTk = ImageTk.PhotoImage(obraz)
background.create_image(350,200, image = obrazTk, anchor = CENTER)

sample1 = "Bamboo.wav"
sample2 = "Claves.wav "
sample3 = "gitara.wav"
sample4 = "elektryk.wav"
sample5 = "syntezator.wav"
sample6 = "dzwonki.wav"
sample7 = "bass.wav"
sample8 = "dzwiek.wav"
sample9 = "dzwięk2.wav"
sample10 = "dzwiek3.wav"
sample11 = "piano.wav"
sample12 = "Shakuhachi.wav"
sample13 = "skrzypce.wav"
sample14 = "szczek.wav"



lista_sampli = [sample1, sample2, sample3,sample4, sample5, sample6, sample7, sample8, sample9, sample10, sample11, sample12, sample13, sample14]

program = PopmaszynaGUI(glowne_okno)
glowne_okno.mainloop()
