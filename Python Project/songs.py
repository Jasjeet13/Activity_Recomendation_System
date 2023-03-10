from tkinter import *
from tkinter import messagebox
win=Tk()
can1=Canvas(win,bg='black',height=1000,width=1000)
filename=PhotoImage(file="C:\\Users\\jasje\\Desktop\\Lovestruck movies\\WhatsApp Image 2022-12-17 at 6.22.34 PM_171x255.png")
image=can1.create_image(500,200,anchor=CENTER,image=filename)
filename2=PhotoImage(file="C:\\Users\\jasje\\Desktop\\Lovestruck movies\\WhatsApp Image 2022-12-17 at 6.22.48 PM_171x251.png")
image2=can1.create_image(500,500,anchor=CENTER,image=filename2)
can1.pack()
win.mainloop()

