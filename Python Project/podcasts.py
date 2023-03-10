from tkinter import *
import webbrowser

root=Tk()
root.geometry('500x500')



def link(name,location):
    def callback():
        webbrowser.open_new(location)
        

    r=Button(root, text=name , bd = 10,command=callback)
    r.pack(side = 'top')

root.mainloop()

