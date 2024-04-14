import tkinter  as tk

root  = tk.Tk()
root.geometry("400x500")
root.title("LABEL ATTRIBUTES")

lable = tk.Label(text = 'Ready',bg ="red",fg = "black",padx = 10,pady = 5,font = "RobotoSlab 19 bold",borderwidth =2,relief = "solid")
lable.pack(padx =10,pady = 5 ,side = "bottom",fill = "x")

root.mainloop()