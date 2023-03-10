from tkinter import * 
from tkinter.ttk import *

# creating tkinter window
root = Tk()
root.geometry('1000x1000')


    Label(root, text = 'Yeh Jawani Hai Deewani', font =('Verdana', 10),).pack(side = TOP, pady = 20)
    photo = PhotoImage(file = r"C:\\Users\\jasje\\Desktop\\Lovestruck movies\\WhatsApp Image 2022-12-17 at 6.22.34 PM_171x255.png")
    Button(root,image = photo).pack(side = TOP)

    Label(root, text = 'The Fault In Our Stars', font =('Verdana', 10),).pack(side = TOP, pady = 20)
    photo2 = PhotoImage(file =r"C:\\Users\\jasje\\Desktop\\Lovestruck movies\\WhatsApp Image 2022-12-17 at 6.22.48 PM_171x251.png")
    Button(root,image = photo2).pack(side = TOP)

root.mainloop()