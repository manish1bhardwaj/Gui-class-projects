import tkinter as tk

root  = tk.Tk()
root.title("Python Home Page")
root.geometry("500x500")


f1 = tk.Frame(root, borderwidth = 5,relief ="sunken",bg = "grey")
f1.pack(side = "left" ,fill ="y")
f2 = tk.Frame(root, borderwidth = 5,relief ="sunken",bg = "grey")
f2.pack(side = "top" ,fill ="x")
l = tk.Label(f1,text = "PYTHON", fg = "black",font ="PetrovSans 16 bold")
l.pack()
l = tk.Label(f2,text = "Welcome everyone on my first frame ", fg = "black",font ="PetrovSans 16 bold")
l.pack()

root.mainloop()
