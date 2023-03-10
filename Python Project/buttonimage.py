import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()


photo = PhotoImage(file = "C:\\Users\\jasje\\Desktop\\Movies\\Yeh Jawaani Hai Deewani_jpeg (2).png")
photoimage = photo.subsample(1, 1)

r=Button(root, image = photoimage)
r.pack(side = BOTTOM, pady = 50)

photo1 = PhotoImage(file = "C:\\Users\\jasje\\Desktop\\Movies\\Yeh Jawaani Hai Deewani_jpeg (2).png")
photoimage1 = photo1.subsample(1, 1)

r1=Button(root, image = photoimage1)
r1.pack(side = BOTTOM, pady = 50)

photo2 = PhotoImage(file = "C:\\Users\\jasje\\Desktop\\Movies\\Yeh Jawaani Hai Deewani_jpeg (2).png")
photoimage2 = photo2.subsample(1, 1)

r2=Button(root, image = photoimage2)
r2.pack(side = BOTTOM, pady = 50)

photo3 = PhotoImage(file = "C:\\Users\\jasje\\Desktop\\Movies\\Yeh Jawaani Hai Deewani_jpeg (2).png")
photoimage3 = photo3.subsample(1, 1)

r3=Button(root, image = photoimage3)
r3.pack(side = BOTTOM, pady = 50)

photo4 = PhotoImage(file = "C:\\Users\\jasje\\Desktop\\Movies\\Yeh Jawaani Hai Deewani_jpeg (2).png")
photoimage4 = photo4.subsample(1, 1)

r4=Button(root, image = photoimage4)
r4.pack(side = BOTTOM, pady = 50)

 
mainloop()