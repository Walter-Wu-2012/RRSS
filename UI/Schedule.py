from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from calendar import monthrange

root = Tk()
root.title('Advisor')

yr = 2021
m = 11
mt = IntVar(value=m)
yrt = IntVar(value=yr)
mtst = StringVar(value="Dec")
yrtst = StringVar(value=str(yrt.get()))

def pre():
    global k
    try:
        k
    except NameError:
        k=0
    else:
        k = k + 1
    if m - k < 0:
        mt.set((m - k) % 12)
        yrt.set(yr + (m - k) // 12)
    elif m - k > 11:
        mt.set((m - k) % 12)
        yrt.set(yr + (m - k) // 12)
    else:
        mt.set(m - k)
        yrt.set(yr)
    mtst.set(month_list[mt.get()])
    yrtst.set(str(yrt.get()))
    return


def nex():
    global k
    try:
        k
    except NameError:
        k = 0
    else:
        k = k - 1
    if m - k < 0:
        mt.set((m - k) % 12)
        yrt.set(yr + (m - k) // 12)
    elif m - k > 11:
        mt.set((m - k) % 12)
        yrt.set(yr + (m - k) // 12)
    else:
        mt.set(m - k)
        yrt.set(yr)
    mtst.set(month_list[mt.get()])
    yrtst.set(str(yrt.get()))
    return


try:
    k
except NameError:
    k=0

month_list = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

#margin1 = Label(root, text="", padx=20, pady=20).grid(row=0, column=0)

sch = Label(root, text="SCHEDULE").grid(row=0, column=0, columnspan=7)

left = Button(root, text="<<", command=pre).grid(row=1, column=0)
right = Button(root, text=">>", command=nex).grid(row=1, column=6)
month = ttk.Button(root, textvariable=mtst).grid(row=1, column=1, columnspan=3)
year = ttk.Button(root, textvariable=yrtst).grid(row=1, column=4, columnspan=2)

bord = "ridge"
bdwidth = 1

mond = Label(root, text="Mon", relief=bord, borderwidth=bdwidth).grid(row=2, column=0)
tue = Label(root, text="Tue", relief=bord, borderwidth=bdwidth).grid(row=2, column=1)
wed = Label(root, text="Wed", relief=bord, borderwidth=bdwidth).grid(row=2, column=2)
thu = Label(root, text="Thu", relief=bord, borderwidth=bdwidth).grid(row=2, column=3)
fri = Label(root, text="Fri", relief=bord, borderwidth=bdwidth).grid(row=2, column=4)
sat = Label(root, text="Sat", relief=bord, borderwidth=bdwidth).grid(row=2, column=5)
sun = Label(root, text="Sun", relief=bord, borderwidth=bdwidth).grid(row=2, column=6)

frame = Frame(root).grid(row=3, column=0, rowspan=23-4+1, columnspan=7)
j=2

button=[]
for i in range(1, monthrange(yrt.get(), mt.get()+1)[1]+1, 1):
    frame1 = ttk.Frame(frame, relief=bord, borderwidth=bdwidth).grid(row=4*((j+i-1)//7)+3, column=(j+i-1)%7, rowspan=4)
    button.append(ttk.Button(frame, text=str(i)).grid(row=4*((j+i-1)//7)+3, column=(j+i-1)%7))

#margin2 = Label(root, text="", padx=20, pady=20).grid(row=20, column=20)

root.mainloop()
