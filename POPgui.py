
from tkinter import *
from PIL import Image, ImageTk, ImageFilter
from tkinter import messagebox

class PopmaszynaGUI(Frame,object):

    def __init__(self,master):
        super(PopmaszynaGUI, self).__init__(master)
        self.master.title("Popmaszyna")
        self.master.geometry("700x400")
        self.pack()
        self.start_button()
        self.akcja_menu()



    def start_button(self):
        global obrazTk
        przycisk1 = Button(background, text = "START!", fg = "red", command = self.akcja_main_window)
        przycisk1.place(x = 310, y = 300)


    def akcja_menu(self):
        pasek_menu = Menu(glowne_okno)
        first_menu = Menu(pasek_menu, tearoff = 0)
        first_menu.add_command(label = "Autorzy", command = self.show_authors)
        first_menu.add_command(label = "Exit", command = glowne_okno.quit)
        pasek_menu.add_cascade(label = "Opcje", menu = first_menu)
        glowne_okno.config(menu = pasek_menu)

    def akcja_main_window(self):
        main_window = Tk()
        main_window.geometry("700x700")
        main_window.title("Popmaszyna")

    def show_authors(self):
        messagebox.showinfo("Autorzy programu", "Julia Naklicka \nAleksandra Draszewska \nKarolina Kulikowska \nZofia Wereszko")



glowne_okno = Tk()
background = Canvas(glowne_okno, width=700, height=400)
background.pack()
obraz = Image.open("popmaszynapic.png")
obrazTk = ImageTk.PhotoImage(obraz)
background.create_image(350,200, image = obrazTk, anchor = CENTER)

program = PopmaszynaGUI(glowne_okno)
glowne_okno.mainloop()
