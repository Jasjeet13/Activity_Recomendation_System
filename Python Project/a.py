from tkinter import *

def go(event):
    cs=Lb.curselection()
    for list in cs:
        if list==0:
            from Happy import h 



top = Tk()
top.geometry('600x600')
top.title("CURRENT MOOD!!!")
Lb=Listbox(top, height = 100,width = 100,bd=70,bg = "black",font = "Helvetica 20 bold",fg="pink")
Lb.insert(0 , "Happy")
Lb.insert(1 , "Sad")
Lb.insert(2 , "Excited")
Lb.insert(3 , "Lovestruck")
Lb.insert(4 , "Nostalgic")
Lb.bind('<Double-1>', go)
Lb.pack()
top.mainloop()