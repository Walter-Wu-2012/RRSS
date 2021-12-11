from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Advisor')

margin1=Label(root, text="", padx=20,pady=20).grid(row=0, column=0)

Welcome= Label(root, text="Meow! How is it going? \n Let's start with a mood scan",padx=10, pady=10).grid(row=1,column=2)

meow=ImageTk.PhotoImage(Image.open("meow1.jpg"))
meowLabel = Label(image=meow).grid(row=2,column=2,rowspan=4)

GiveAdv = Button(root, text='GIVE ME ADVICE',padx=10,pady=10).grid(row=2, column=1, ipadx=10, ipady=10)
View = Button(root, text='VIEW SCHEDULE & ACTIVITY',padx=10,pady=10).grid(row=3, column=1, ipadx=10, ipady=10)
Setting = Button(root, text='SETTINGS',padx=10,pady=10).grid(row=4, column=1, ipadx=10, ipady=10)
History = Button(root, text='HISTORY LOGS',padx=10,pady=10).grid(row=5, column=1, ipadx=10, ipady=10)

margin2=Label(root, text="", padx=20,pady=20).grid(row=6,column=3)

root.mainloop()