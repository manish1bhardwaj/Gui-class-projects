from tkinter import *

root = Tk()

root.geometry("500x400")
lb1 = Label(text = "KRISHNA")
lb1.pack()
Photo = PhotoImage(file="E:\Krishna.png")
photo_label = Label(image =Photo)
photo_label.pack()

root.mainloop()