import tkinter as tk

root = tk.Tk()
root.geometry("400x400")
root.title("Use of Entry And Grid")

def getvals():
    print(uservalue.get())
    print(passvalue.get())


l1 = tk.Label(root,text = "Username",font = "cosmic 10 bold")
l1.grid(row = 0,column = 0)
l2 = tk.Label(root,text = "Password",font = "cosmic 10 bold")
l2.grid(row = 1,column = 0)


uservalue = tk.StringVar() 
passvalue = tk.StringVar()


userentry = tk.Entry(root, textvariable = uservalue).grid(row =0,column = 1,padx = 10)
passentry = tk.Entry(root, textvariable = passvalue).grid(row =1,column = 1,padx = 10)

b1 = tk.Button(root,text = "Login",bg = "blue",fg = "white",font = "RobotoSlab 10 bold",borderwidth=3,relief ="solid",command = getvals)
b1.grid(columnspan =2 ,pady = 8)



root.mainloop()