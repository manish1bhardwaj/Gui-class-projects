from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.geometry("500x600")
root.minsize(200,400)

image = Image.open("E:\pexels-james-wheeler-414612.jpg")
photo = ImageTk.PhotoImage(image)
my_image = Label(image = photo)
my_image.pack()


root.mainloop()