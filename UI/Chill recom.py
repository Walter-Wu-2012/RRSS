from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Advisor')

margin1 = Label(root, text="", padx=20, pady=20).grid(row=0,column=0)

frame1 = Frame(root, pady=100).grid(row=1, column=1, rowspan=2, columnspan=3)
frame2 = Frame(root).grid(row=3, column=1)
frame3 = Frame(root).grid(row=3, column=2)
frame4 = Frame(root).grid(row=3, column=3)


top = Label(frame1, text='Meow meow meeee ow ow ow meow meow meow woof woof').grid(row=1, column=2, rowspan=2, columnspan=4)
skip = Button(frame1, text='SKIP ALL', padx=22).grid(row=1, column=6)
other = Button(frame1, text='OTHER CHOICES', padx=1).grid(row=2, column=6)

meow = Image.open("meow1.jpg")
meow = meow.resize((150, 150), Image.ANTIALIAS)
meow1 = ImageTk.PhotoImage(meow)

k=110
i=54
j=49

tl1 = Label(frame2, text="Activity #1").grid(row=4, column=1, columnspan=2)
Image1 = Label(frame2, image=meow1).grid(row=5, column=1, columnspan=2)
bl1 = Label(frame2, text="Description #1").grid(row=6, column=1, columnspan=2)
accept1 = Button(frame2, text='YES', padx=k).grid(row=7, column=1, columnspan=2)
deny1 = Button(frame2, text='NO', padx=i).grid(row=8, column=1)
skip1 = Button(frame2, text='SKIP', padx=j).grid(row=8, column=2)

tl2 = Label(frame3, text="Activity #2").grid(row=4, column=3, columnspan=2)
Image2 = Label(frame3, image=meow1).grid(row=5, column=3, columnspan=2)
bl2 = Label(frame3, text="Description #2").grid(row=6, column=3, columnspan=2)
accept2 = Button(frame3, text='YES', padx=k).grid(row=7, column=3, columnspan=2)
deny2 = Button(frame3, text='NO', padx=i).grid(row=8, column=3)
skip2 = Button(frame3, text='SKIP', padx=j).grid(row=8, column=4)

tl3 = Label(frame4, text="Activity #3").grid(row=4, column=5, columnspan=2)
Image3 = Label(frame4, image=meow1).grid(row=5, column=5, columnspan=2)
bl3 = Label(frame4, text="Description #3").grid(row=6, column=5, columnspan=2)
accept3 = Button(frame4, text='YES', padx=k).grid(row=7, column=5, columnspan=2)
deny3 = Button(frame4, text='NO', padx=i).grid(row=8, column=5)
skip3 = Button(frame4, text='SKIP', padx=j).grid(row=8, column=6)




margin2 = Label(root, text="", padx=20, pady=20).grid(row=9, column=7)

root.mainloop()