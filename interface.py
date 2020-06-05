from tkinter import *
from PIL import Image, ImageTk, ImageFilter
okienko = Tk()
calosc = Canvas(okienko, width=700, height=400)
calosc.pack()
obraz = Image.open("popmaszynapic.png")
obraz = obraz.filter(ImageFilter.EDGE_ENHANCE_MORE)
obrazTk = ImageTk.PhotoImage(obraz)
calosc.create_image(350, 200, image=obrazTk)
okienko.mainloop()