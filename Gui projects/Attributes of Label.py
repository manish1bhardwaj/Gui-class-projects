import tkinter  as tk

root  = tk.Tk()
root.geometry("500x500")
root.title("LABEL ATTRIBUTES")

lable = tk.Label(text = '''A GUI uses a combination of technologies and devices 
to provide a platform that users can interact with, for the tasks
of gathering and producing information. A series of elements conforming
a visual language have evolved to represent information stored in computers.''',bg ="grey",fg = "black",padx = 40,pady = 40,font = "RobotoSlab 19 bold",borderwidth =5,relief = "solid",)
lable.pack()

root.mainloop()