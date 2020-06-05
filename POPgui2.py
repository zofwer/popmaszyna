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
        przycisk1 = Button(main_window, text = "Bamboo", fg = "dark green", bg="sienna2", width=30, height=5,command = lambda: self.play_sample(0))
        przycisk1.grid(row = 1, column = 1)
        przycisk2 = Button(main_window, text = "Claves", fg = "navy", bg="tan4" , width=30, height=5,command = lambda: self.play_sample(1))
        przycisk2.grid(row = 2, column = 1)
        przycisk3 = Button(main_window, text = "gitara", fg = "dodger blue",bg="OliveDrab4" ,  width=30, height=5,command = lambda: self.play_sample(2))
        przycisk3.grid(row = 3, column = 1)
        przycisk4 = Button(main_window, text = "elektryk", fg = "yellow",bg="brown4" , width=30, height=5, command = lambda: self.play_sample(3))
        przycisk4.grid(row = 4, column = 1)
        przycisk5 = Button(main_window, text = "syntezator", fg = "goldenrod",bg="coral2" , width=30, height=5, command = lambda: self.play_sample(4))
        przycisk5.grid(row =1 , column = 2)
        przycisk6 = Button(main_window, text = "dzwonki", fg = "red",bg="navy" , width=30, height=5, command = lambda: self.play_sample(5))
        przycisk6.grid(row = 2, column = 2)
        przycisk7 = Button(main_window, text = "bass", fg = "deep pink",bg="dodger blue" ,  width=30, height=5,command = lambda: self.play_sample(6))
        przycisk7.grid(row = 3, column = 2)
        przycisk8 = Button(main_window, text = "dzwiek", fg = "cyan2",bg="yellow" , width=30, height=5, command = lambda: self.play_sample(7))
        przycisk8.grid(row = 4, column = 2)
        przycisk9 = Button(main_window, text = "dzwięk2", fg = "OliveDrab4",bg="goldenrod" , width=30, height=5, command = lambda: self.play_sample(8))
        przycisk9.grid(row = 1, column = 3)
        przycisk10 = Button(main_window, text = "dzwiek3", fg = "sienna2",bg="deep pink" , width=30, height=5, command = lambda: self.play_sample(9))
        przycisk10.grid(row = 2, column = 3)
        przycisk11 = Button(main_window, text = "piano", fg = "tan4",bg="magenta2" , width=30, height=5, command = lambda: self.play_sample(10))
        przycisk11.grid(row = 3, column = 3)
        przycisk12 = Button(main_window, text = "Shakuhachi", fg = "brown4",bg="dark green" ,  width=30, height=5,command = lambda: self.play_sample(11))
        przycisk12.grid(row = 4, column = 3)
        przycisk13 = Button(main_window, text = "skrzypce", fg = "coral2",bg="goldenrod" ,  width=30, height=5,command = lambda: self.play_sample(12))
        przycisk13.grid(row = 1, column = 4)
        przycisk14 = Button(main_window, text = "szczek", fg = "magenta2",bg="cyan2" , width=30, height=5, command = lambda: self.play_sample(13))
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

sample1 = "samples/Bamboo.wav"
sample2 = "samples/Claves.wav"
sample3 = "samples/gitara.wav"
sample4 = "samples/elektryk.wav"
sample5 = "samples/syntezator.wav"
sample6 = "samples/dzwonki.wav"
sample7 = "samples/Bass.wav"
sample8 = "samples/dzwiek.wav"
sample9 = "samples/dzwięk2.wav"
sample10 = "samples/dzwiek3.wav"
sample11 = "samples/piano.wav"
sample12 = "samples/Shakuhachi.wav"
sample13 = "samples/skrzypce.wav"
sample14 = "samples/szczek.wav"

lista_sampli = [sample1, sample2, sample3,sample4, sample5, sample6, sample7, sample8, sample9, sample10, sample11, sample12, sample13, sample14]

program = PopmaszynaGUI(glowne_okno)
glowne_okno.mainloop()
