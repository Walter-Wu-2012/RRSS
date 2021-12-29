from tkinter import *
import os
from tkinter import ttk
from PIL import ImageTk, Image
from tkcalendar import Calendar
from calendar import monthrange
import sqlite3
from tkinter import messagebox
# Create Object
root = Tk()
root.title('Advisor')
# Set geometry
root.geometry()


def create(date):
    ms = messagebox.askyesno("Save change", "Are you sure you want to save changes?")
    if ms == 0:
        return

    if isinstance(expected_hour1, int) or isinstance(expected_min1, int):
        messagebox.showerror("Wrong input", "Please input integer in time expected.")
        return

    if title1.get() == '' or description1.get() == '':
        messagebox.showerror("Wrong input", "Please write event title and brief description of the event.")
        return

    conn = sqlite3.connect("event_book.db")
    c = conn.cursor()
    # create database. Just need to create it once.
    c.execute("INSERT INTO events VALUES (:title, :comment, :date, :description, :expected_h, :expected_mn, :expected_diff, :importance)",
            {
                'title': title1.get(),
                'comment': comvar.get(),
                'date': date,
                'description': description1.get(),
                'expected_h': expected_hour1.get(),
                'expected_mn': expected_min1.get(),
                'expected_diff': clicked.get(),
                'importance': clicked2.get()
            }
            )


    conn.commit()
    conn.close()

    top.destroy()
    root.destroy()


def add_event(date):
    global top
    global clicked
    global comvar
    global title1
    global description1
    global expected_hour1
    global expected_min1

    top = Toplevel()
    top.title('Advisor')
    Label(top, text="Add new event").grid(row=1, columnspan=2)
    title1 = Entry(top, width=30)
    title1.grid(row=2, column=2)
    l1 = Label(top, text="Title", padx=30).grid(row=2, column=1)

    description1 = Entry(top, width=30)
    description1.grid(row=3, column=2)
    l2 = Label(top, text="Description", padx=30).grid(row=3, column=1)

    comvar = StringVar()
    comvar.set('Life')
    commentMenu = OptionMenu(top, comvar, 'Life', 'Study', 'Work', 'Entertainment', 'Special', 'Other')
    commentMenu.config(width=24)
    commentMenu.grid(row=4, column=2)
    l23 = Label(top, text="Event type", padx=30).grid(row=4, column=1)

    clicked = StringVar()
    clicked.set("0")
    difficulty = OptionMenu(top, clicked, "0", "1", "2", "3", "4", "5")
    difficulty.config(width=24)
    difficulty.grid(row=5, column=2)
    l3 = Label(top, text="Difficulty", padx=30).grid(row=5, column=1)

    global clicked2
    clicked2 = StringVar()
    clicked2.set("0")
    importance = OptionMenu(top, clicked2, "0", "1", "2", "3", "4", "5")
    importance.config(width=24)
    importance.grid(row=6, column=2)
    l34 = Label(top, text="Importance", padx=30).grid(row=6, column=1)

    expected_hour1 = Entry(top, width=30)
    expected_hour1.grid(row=8, column=2)
    l4 = Label(top, text="Expected time", padx=30).grid(row=7, column=1)
    l5 = Label(top, text="hours", padx=30).grid(row=8, column=1)

    expected_min1 = Entry(top, width=30)
    expected_min1.grid(row=9, column=2)
    l6 = Label(top, text="minutes", padx=30).grid(row=9, column=1)

    savechanges = Button(top, text='Save changes', command=lambda: create(date)).grid(row=10, column=1, columnspan=2)


#show all events
def showall():
    global top
    top = Toplevel()
    top.title('Advisor')

    conn = sqlite3.connect("event_book.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM events")
    records = c.fetchall()
    Title = Label(root, text='Title', padx=5).grid(row=10, column=1)
    ty = Label(top, text='Type', padx=5).grid(row=10, column=2)
    da = Label(top, text='Date/Deadline', padx=5).grid(row=10, column=3)
    de = Label(top, text='Description', padx=5).grid(row=10, column=4)
    ex = Label(top, text='Expected time', padx=5).grid(row=10, column=5)
    di = Label(top, text='Difficulty', padx=5).grid(row=10, column=6)
    im = Label(top, text='Importance', padx=5).grid(row=10, column=7)
    i = 0
    save_record = []
    for record in records:
        save_record.append(record)
        Label(top, text=save_record[i][0]).grid(row=i + 11, column=1)
        Label(top, text=save_record[i][1]).grid(row=i + 11, column=2)
        Label(top, text=save_record[i][2]).grid(row=i + 11, column=3)
        Button(top, text="Show", command=lambda i=i: popup(save_record[i][0], save_record[i][3])).grid(row=i + 11,
                                                                                                        column=4)
        Label(top, text=str(save_record[i][4]) + " hours and " + str(save_record[i][5]) + " minutes").grid(
            row=i + 11, column=5)
        Label(top, text=save_record[i][6]).grid(row=i + 11, column=6)
        Label(top, text=save_record[i][7]).grid(row=i + 11, column=7)
        Button(top, text="x", bg='red', fg='white', padx=5,
               command=lambda i=i: delete_event(save_record[i][8])).grid(row=i + 11, column=9)
        icon = PhotoImage(file='edit.png')
        b = Button(top, image=icon, width=20, height=20, command=lambda i=i: edit_event(save_record[i]))
        b.image = icon
        b.grid(row=i + 11, column=8)
        i += 1

    conn.commit()
    conn.close()


#show events on the chosen date
def show(date):
    global top
    top = Toplevel()
    top.title('Advisor')

    conn = sqlite3.connect("event_book.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM events")
    records = c.fetchall()
    Title = Label(top, text='Title', padx=5).grid(row=10, column=1)
    ty = Label(top, text='Type', padx=5).grid(row=10, column=2)
    da = Label(top, text='Date/Deadline', padx=5).grid(row=10, column=3)
    de = Label(top, text='Description', padx=5).grid(row=10, column=4)
    ex = Label(top, text='Expected time', padx=5).grid(row=10, column=5)
    di = Label(top, text='Difficulty', padx=5).grid(row=10, column=6)
    im = Label(top, text='Importance', padx=5).grid(row=10, column=7)
    i=0
    save_record = []
    for record in records:
        if record[2] == cal.get_date():
            save_record.append(record)
            Label(top, text=save_record[i][0]).grid(row=i + 11, column=1)
            Label(top, text=save_record[i][1]).grid(row=i + 11, column=2)
            Label(top, text=save_record[i][2]).grid(row=i + 11, column=3)
            Button(top, text="Show", command=lambda i=i: popup(save_record[i][0], save_record[i][3])).grid(row=i + 11,
                                                                                                            column=4)
            Label(top, text=str(save_record[i][4]) + " hours and " + str(save_record[i][5]) + " minutes").grid(
                row=i + 11, column=5)
            Label(top, text=save_record[i][6]).grid(row=i + 11, column=6)
            Label(top, text=save_record[i][7]).grid(row=i + 11, column=7)
            Button(top, text="x", bg='red', fg='white', padx=5,
                   command=lambda i=i: delete_event(save_record[i][8])).grid(row=i + 11, column=9)
            icon = PhotoImage(file='edit.png')
            b = Button(top, image=icon, width=20, height=20, command=lambda i=i: edit_event(save_record[i]))
            b.image = icon
            b.grid(row=i + 11, column=8)
            i += 1

    conn.commit()
    conn.close()


def edit_event(save_record):
    global top2
    top2 = Toplevel()
    top2.title('Advisor')
    global oid
    oid = save_record[8]

    global clicked
    global comvar
    global title1
    global description1
    global expected_hour1
    global expected_min1
    global date_editor

    Label(top2, text="Add new event").grid(row=1, columnspan=2)
    title1 = Entry(top2, width=30)
    title1.grid(row=2, column=2)
    l1 = Label(top2, text="Title", padx=30).grid(row=2, column=1)

    description1 = Entry(top2, width=30)
    description1.grid(row=3, column=2)
    l2 = Label(top2, text="Description", padx=30).grid(row=3, column=1)

    comvar = StringVar()
    comvar.set(save_record[1])
    commentMenu = OptionMenu(top2, comvar, 'Life', 'Study', 'Work', 'Entertainment', 'Special', 'Other')
    commentMenu.config(width=24)
    commentMenu.grid(row=4, column=2)
    l23 = Label(top2, text="Event type", padx=30).grid(row=4, column=1)

    clicked = StringVar()
    clicked.set(save_record[6])
    difficulty = OptionMenu(top2, clicked, "0", "1", "2", "3", "4", "5")
    difficulty.config(width=24)
    difficulty.grid(row=5, column=2)
    l3 = Label(top2, text="Difficulty", padx=30).grid(row=5, column=1)

    global clicked2
    clicked2 = StringVar()
    clicked2.set(save_record[7])
    importance = OptionMenu(top2, clicked2, "0", "1", "2", "3", "4", "5")
    importance.config(width=24)
    importance.grid(row=6, column=2)
    l34 = Label(top2, text="Importance", padx=30).grid(row=6, column=1)

    expected_hour1 = Entry(top2, width=30)
    expected_hour1.grid(row=8, column=2)
    l4 = Label(top2, text="Expected time", padx=30).grid(row=7, column=1)
    l5 = Label(top2, text="hours", padx=30).grid(row=8, column=1)

    expected_min1 = Entry(top2, width=30)
    expected_min1.grid(row=9, column=2)
    l6 = Label(top2, text="minutes", padx=30).grid(row=9, column=1)

    date_editor = Entry(top2, width=30)
    date_editor.grid(row=10, column=2)
    l7 = Label(top2, text="Date", padx=30).grid(row=10, column=1)
    title1.insert(0, save_record[0])

    date_editor.insert(0, save_record[2])
    description1.insert(0, save_record[3])
    expected_hour1.insert(0, save_record[4])
    expected_min1.insert(0, save_record[5])


    save_button = Button(top2, text="Save changes", command=update).grid(row=11, column=1, columnspan=2)



def update():
    ymmdd = date_editor.get()
    y=ymmdd[:4]
    mm=ymmdd[5:7]
    dd=ymmdd[8:10]
    #print(y + mm + dd)

    if ymmdd[4] != "-" or ymmdd[7] != "-":
        messagebox.showerror(message="Wrong date format! Please input date in yyyy-mm-dd format.")
        return
    elif isinstance(int(y), int) == 0:
        messagebox.showerror(message="Invalid year input!")
        return
    elif int(y) < 1900 or int(y) > 2100:
        messagebox.showerror(message="Year out of range!")
        return
    elif int(mm) < 0 or int(mm) > 12:
        messagebox.showerror(message="Wrong month input!")
        return
    elif int(dd) < 0 or int(dd) > monthrange(int(y), int(mm))[1]:
        messagebox.showerror(message="Wrong day input!")
        return

    ms = messagebox.askyesno("Save change", "Are you sure you want to save changes?")
    if ms == 0:
        return


    conn = sqlite3.connect("event_book.db")
    c = conn.cursor()
    c.execute("""UPDATE events SET
        title = :t,
        comment = :com,
        date = :d,
        description = :de,
        expected_h = :eh,
        expected_mn = :em,
        expected_diff = :dif,
        importance = :im
        WHERE oid = :oid""",
        {
            't': title1.get(),
            'com': comvar.get(),
            'd': date_editor.get(),
            'de': description1.get(),
            'eh': expected_hour1.get(),
            'em': expected_min1.get(),
            'dif': int(clicked.get()),
            'im': int(clicked2.get()),
            'oid': oid
        })

    conn.commit()
    conn.close()

    try:
        top2
        top2.destroy()
    except NameError:
        root.destroy()
    root.destroy()


def delete_event(i):
    global top
    ms = messagebox.askyesno("Delete event", "Are you sure you want to delete this event/task?")
    if ms == 0:
        return
    conn = sqlite3.connect("event_book.db")
    c = conn.cursor()

    c.execute("DELETE from events WHERE oid=" + str(i))
    conn.commit()
    conn.close()
    try:
        top
        top.destroy()
    except NameError:
        root.destroy()
    root.destroy()


def popup(text1, text2):
    messagebox.showinfo(text1, text2)
    return


cal = Calendar(root, selectmode='day',
               date_pattern='y-mm-dd')
cal.grid(row=1, columnspan=10)

date = cal.get_date()

conn = sqlite3.connect("event_book.db")
c = conn.cursor()
#what kind of event it is? About study/work? Comment column. Add importance?
#create database. Just need to create it once.
'''c.execute("""CREATE TABLE events (
        title text,
        comment text,
        date text,
        description text,
        expected_h integer,
        expected_mn integer,
        expected_diff integer,
        importance integer
        )""")'''
#button1 = Button(root, text="Create events", command=lambda: create(title1.get(), cal.get_date(), description1.get(), expected_hour1.get(), expected_min1.get(), clicked.get()))
button1 = Button(root, text="Add events", command=lambda: add_event(date))
button1.grid(row=8, column=4)

button1 = Button(root, text="Show events", command=lambda: show(date))
button1.grid(row=8, column=5)

button2 = Button(root, text="Show all events", padx=70, command=showall)
button2.grid(row=9, columnspan=10)

c.execute("SELECT *, oid FROM events")
records = c.fetchall()
Title = Label(root, text='Title', padx=5).grid(row=10, column=1)
ty = Label(root, text='Type', padx=5).grid(row=10, column=2)
da = Label(root, text='Date/Deadline', padx=5).grid(row=10, column=3)
de = Label(root, text='Description', padx=5).grid(row=10, column=4)
ex = Label(root, text='Expected time', padx=5).grid(row=10, column=5)
di = Label(root, text='Difficulty', padx=5).grid(row=10, column=6)
im = Label(root, text='Importance', padx=5).grid(row=10, column=7)
i = 0
save_record = []
for record in records:
    save_record.append(record)
    Label(root, text=save_record[i][0]).grid(row=i + 11, column=1)
    Label(root, text=save_record[i][1]).grid(row=i + 11, column=2)
    Label(root, text=save_record[i][2]).grid(row=i + 11, column=3)
    Button(root, text="Show", command=lambda i=i: popup(save_record[i][0], save_record[i][3])).grid(row=i + 11,
                                                                                                   column=4)
    Label(root, text=str(save_record[i][4]) + " hours and " + str(save_record[i][5]) + " minutes").grid(
        row=i + 11, column=5)
    Label(root, text=save_record[i][6]).grid(row=i + 11, column=6)
    Label(root, text=save_record[i][7]).grid(row=i + 11, column=7)
    Button(root, text="x", bg='red', fg='white', padx=5,
           command=lambda i=i: delete_event(save_record[i][8])).grid(row=i + 11, column=9)
    icon = PhotoImage(file='edit.png')
    b = Button(root, image=icon, width=20, height=20, command=lambda i=i: edit_event(save_record[i]))
    b.image = icon
    b.grid(row=i + 11, column=8)
    i += 1

#label_b = Label(root, text="Choose date on the calendar to show events, create event's date or task's deadline.\n For events, choose difficulty as 0.")
#label_b.grid(row=10, columnspan=3)
conn.commit()
conn.close()
# Execute Tkinter
root.mainloop()
