import tkinter as tk

#design window
root = tk.Tk()
root.geometry("400x400")
root.minsize(100,100)
root.maxsize(300,400) 
root.title("Buttons testing")


def start():
    print("Play now ,Your game has been started !!")

    x = "X"
    
    while x=="X":
        def b1():
            global x
            global b1
            b1 = tk.Button(f1,text = "X",font ="RobotoSlab 10 bold",bg = "white",fg = "black",borderwidth=1,padx = 2,command = b1,width=7,height=5,relief ="solid")
            b1.grid(row  = 1 ,column = 1,padx = 1)
        def b2():
            print("")
        def b3():
            print("")
        def b4():
            print("")
        def b5():
            print("")
        def b6():
            print("")
        def b7():
            print("")
        def b8():
            print("")
        def b9():
            print("")
        x = "O"
        break

    while x == "O":
        def b1():
            global x
            local= b1
            b1 = tk.Button(f1,text = "O",font ="RobotoSlab 10 bold",bg = "white",fg = "black",borderwidth=1,padx = 2,command = b1,width=7,height=5,relief ="solid")
            b1.grid(row  = 1 ,column = 1,padx = 1)
        def b2():
            print("")
        def b3():
            print("")
        def b4():
            print("")
        def b5():
            print("")
        def b6():
            print("")
        def b7():
            print("")
        def b8():
            print("")
        def b9():
            print("")
        x = "O"
        break




    #Block one1
    f1 = tk.Frame(root,borderwidth=2,relief = "sunken",bg = "#cbeef3",)
    f1.grid(row = 1,column = 0)
    
    b1 = tk.Button(f1,text = "",bg = "white",fg = "black",borderwidth=1,padx = 2,command = b1,width=7,height=5,relief ="solid")
    b1.grid(row  = 2 ,column = 0,padx = 1)
    b2 = tk.Button(f1,text = "",bg = "white",fg = "black",borderwidth=1 ,padx = 2,command = b2,width=7,height=5,relief ="solid")
    b2.grid(row = 2,column =1,padx = 1)
    b3 = tk.Button(f1,text = "",bg = "white",fg = "black",borderwidth=1,padx = 2,command = b3,width=7,height=5,relief ="solid")
    b3.grid(row = 2,column = 2,padx = 1)


    #Block two
    f2 = tk.Frame(root,borderwidth=2,relief="sunken",bg = "#cbeef3" )
    f2.grid(row = 3,column =0,columnspan =3)
    b4 = tk.Button(f2,text = "",bg = "white",fg = "black",borderwidth=1,padx = 2,command = b4 ,width=7,height=5,relief ="solid")
    b4.grid(row = 3,column = 1,padx = 1)
    b5 = tk.Button(f2,text = "",bg = "white",fg = "black",borderwidth=1,padx = 2,command = b5,width=7,height=5 ,relief ="solid")
    b5.grid(row = 3,column = 2,padx = 1)
    b6 = tk.Button(f2,text = "",bg = "white",fg = "black",borderwidth=1,padx = 2,command = b6 ,width=7,height=5,relief ="solid")
    b6.grid(row = 3,column = 3,padx = 1)


    #Block third

    f3 = tk.Frame(root,borderwidth=2,relief="sunken",bg = "#cbeef3")
    f3.grid(row = 4,column =0,columnspan =3)
    b7 = tk.Button(f3,text = "",bg = "white",fg = "black",borderwidth=1,padx = 2,command = b7 ,width=7,height=5,relief="solid")
    b7.grid(row = 4,column = 1,padx = 1)
    b8 = tk.Button(f3,text = "",bg = "white",fg = "black",borderwidth=1,padx = 2,command = b8,width=7,height=5,relief ="solid")
    b8.grid(row = 4,column = 2,padx = 1)
    b9 = tk.Button(f3,text = "",bg = "white",fg = "black",borderwidth=1,padx = 2,command = b9,width=7,height=5,relief ="solid" )
    b9.grid(row = 4,column = 3,padx = 1)


#Start game here
    
start = tk.Button(root,text ="START",bg = "blue",fg = "white",borderwidth=3,padx = 1,command = start,width=12,height=2,relief = "sunken",font = "RobotoSlab 15 bold")
start.grid(row  = 0,column = 0,columnspan=2,pady =5)


#mainloop

root.mainloop()