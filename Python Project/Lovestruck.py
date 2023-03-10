from tkinter import *
from tkinter.ttk import *


def love(event):
    cs=l.curselection()
    for list in cs:
        if list==0:
            from songs import button
            button()
            
        if list==1:
            from podcasts  import link
            link('Podcast-1',r'https://youtu.be/n-SVPsGMPi8')
            link('Podcast-2',r'https://youtu.be/wnj82mO2YmQ')

        if list==2:
            root = Tk()
            root.geometry('1000x1000')
            Label(root, text = 'Yeh Jawani Hai Deewani', font =('Verdana', 10),).pack(side = TOP, pady = 20)
            photo = PhotoImage(file = r"C:\\Users\\jasje\\Desktop\\Lovestruck movies\\WhatsApp Image 2022-12-17 at 6.22.34 PM_171x255.png")
            Button(root,image = photo).pack(side = TOP)

            Label(root, text = 'The Fault In Our Stars', font =('Verdana', 10),).pack(side = TOP, pady = 20)
            photo2 = PhotoImage(file =r"C:\\Users\\jasje\\Desktop\\Lovestruck movies\\WhatsApp Image 2022-12-17 at 6.22.48 PM_171x251.png")
            Button(root,image = photo2).pack(side = TOP)

            root.mainloop()



        if list==3:
            pass

        if list==4:
            pass

top = Tk()
top.geometry('400x400')
top.title("Activities")
l=Listbox(top, height = 100,width = 100,bd=20,bg = "black",font = "Helvetica 20 bold",fg="pink")
l.insert(0 , "Songs")
l.insert(1 , "Podcasts")
l.insert(2 , "Movies")
l.insert(3 , "Creative Ideas")
l.bind('<Double-1>', love)
l.pack()

top.mainloop()