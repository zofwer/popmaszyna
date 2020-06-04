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
        przycisk1 = Button(main_window, text = "pierwszy dźwięk", fg = "gold",  command = lambda: self.play_sample(0))
        przycisk1.grid(row = 1, column = 0) #można pokombinować z ułożeniem buttonów
        przycisk2 = Button(main_window, text = "drugi dźwięk", fg = "indian red", command = lambda: self.play_sample(1))
        przycisk2.grid(row = 2, column = 0) #można pokombinować z ułożeniem buttonów
        # miejsce na reszte przycisków

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

sample1 = " " #miejsce na nazwe sampla
sample2 = " " #miejsce na nazwe sampla
sample3 = " " #miejsce na nazwe sampla
lista_sampli = [sample1, sample2, sample3] #tu trzeba dodać dalej te wszystkie sample

program = PopmaszynaGUI(glowne_okno)
glowne_okno.mainloop()
