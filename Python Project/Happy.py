from tkinter import *

def h(event):
    cs=l.curselection()
    for list in cs:
        if list==0:
            from happy_songs_ import a
            
            from songs import button
            button(name,location)
        if list==1:
            from podcasts import link
            link('')

        if list==2:
            pass

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
l.bind('<Double-1>', h)
l.pack()

top.mainloop()

"C:\Users\jasje\Desktop\Dreams unfold.mpeg"
"C:\Users\jasje\Desktop\Ek Mai or Ek Tu.mpeg"
"C:\Users\jasje\Desktop\Khaab.mp3"
"C:\Users\jasje\Desktop\Kesariya(PagalWorld.com.se).mp3"





"C:\Users\jasje\Desktop\Shawn_Mendes_It_ll_Be_Okay_(thinkNews.com.ng).mp3"
"C:\Users\jasje\Desktop\Alec_Benjamin_Let_Me_Down_Slowly_(thinkNews.com.ng).mp3"
"C:\Users\jasje\Desktop\Wakh Ho Jana.mp3"
"C:\Users\jasje\Desktop\new_192_Taare - Sidhu Moosewala.mp3"
"C:\Users\jasje\Desktop\Jo Tu Na Mila - Asim Azhar.mp3"