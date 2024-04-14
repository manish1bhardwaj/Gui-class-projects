import tkinter as tk



class counterApp:
    def __init__(self,mainwindow):
        self.geometry('200x100')
        self.title('Counter App')
        mainwindow = self
        mainwindow.geometry
        var=tk.IntVar(value=0)
        def my_fun1():
            data=var.get()+1
            var.set(data)
            if data>=10:
                lbl1.config(fg='red')
            else:
                lbl1.config(fg='green')
        def my_fun2():
            data=var.get()-1
            if data<0:
                pass
            else:
                var.set(data)
            if data>=10:
                lbl1.config(fg='red')
            else:
                lbl1.config(fg='green')
    
lbl1=tk.Label(textvariable=var,font=('BOLD',30))
lbl1.pack()
bt1=tk.Button(text='Increament',command=my_fun1)
bt1.pack(side=tk.LEFT)
bt2=tk.Button(text='Decreament',command=my_fun2)
bt2.pack(side=tk.RIGHT)

root  = tk.Tk()
root.geometry("300x400")
root.title("Counter App")

root.mainloop()
#koi operation chahiye to cget use karo
#koi operation agar hame perform krna ho toh lb.config