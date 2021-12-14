from tkinter import *
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


def create(title, date, description, expected_hour, expected_min, diff):
    if isinstance(expected_hour, int) or isinstance(expected_min, int):
        messagebox.showerror("Wrong input", "Please input integer in time expected.")
        return
    conn = sqlite3.connect("event_book.db")
    c = conn.cursor()
    # create database. Just need to create it once.
    c.execute("INSERT INTO events VALUES (:title, :date, :description, :expected_h, :expected_mn, :expected_diff)",
            {
                'title': title,
                'date': date,
                'description': description,
                'expected_h': expected_hour,
                'expected_mn': expected_min,
                'expected_diff': diff
            }
            )


    conn.commit()
    conn.close()

    title1.delete(0, END)
    description1.delete(0, END)
    expected_hour1.delete(0, END)
    expected_min1.delete(0, END)


#show events on the chosen date
def show(date):
    global top
    top = Toplevel()
    top.title('Advisor')

    conn = sqlite3.connect("event_book.db")
    c = conn.cursor()

    c.execute("SELECT *, oid FROM events")
    records = c.fetchall()
    Title = Label(top, text='Title', padx=5).grid(row=1,column=1)
    da = Label(top, text='Date/Deadline', padx=5).grid(row=1, column=2)
    de = Label(top, text='Description', padx=5).grid(row=1, column=3)
    ex = Label(top, text='Expected time', padx=5).grid(row=1, column=4)
    di = Label(top, text='Difficulty', padx=5).grid(row=1, column=5)
    i=0
    save_record = []
    for record in records:
        if record[1] == cal.get_date():
            save_record.append(record)
            Label(top, text=save_record[i][0]).grid(row=i+2, column=1)
            Label(top, text=save_record[i][1]).grid(row=i + 2, column=2)
            Button(top, text="Show", command=lambda i=i: popup(save_record[i][0], save_record[i][2])).grid(row=i + 2, column=3)
            Label(top, text=str(save_record[i][3]) + " hours and " + str(save_record[i][4]) + " minutes").grid(row=i + 2, column=4)
            Label(top, text=save_record[i][5]).grid(row=i + 2, column=5)
            icon = PhotoImage(file='edit.png')
            b = Button(top, image=icon, width=20, height=20, command=lambda i=i: edit_event(save_record[i]))
            b.image = icon
            b.grid(row=i + 2, column=6)
            Button(top, text="x", bg='red', fg='white', padx=5, command=lambda i=i: delete_event(save_record[i][6])).grid(row=i + 2, column=7)
            i+=1

    conn.commit()
    conn.close()


def edit_event(save_record):
    global top2
    top2 = Toplevel()
    top2.title('Advisor')
    global title1_editor
    global description1_editor
    global difficulty_editor
    global expected_hour1_editor
    global expected_min1_editor
    global date_editor
    global oid
    oid = save_record[6]

    title1_editor = Entry(top2, width=30)
    title1_editor.grid(row=2, column=2)
    l1 = Label(top2, text="Title", padx=30).grid(row=2, column=1)

    description1_editor = Entry(top2, width=30)
    description1_editor.grid(row=3, column=2)
    l2 = Label(top2, text="Description", padx=30).grid(row=3, column=1)

    global clicked
    clicked = StringVar(top2)
    clicked.set(str(save_record[5]))
    difficulty_editor = OptionMenu(top2, clicked, "0", "1", "2", "3", "4", "5")
    difficulty_editor.config(width=24)
    difficulty_editor.grid(row=4, column=2)
    l3 = Label(top2, text="Difficulty", padx=30).grid(row=4, column=1)

    expected_hour1_editor = Entry(top2, width=30)
    expected_hour1_editor.grid(row=6, column=2)
    l4 = Label(top2, text="Expected time", padx=30).grid(row=5, column=1)
    l5 = Label(top2, text="hours", padx=30).grid(row=6, column=1)

    expected_min1_editor = Entry(top2, width=30)
    expected_min1_editor.grid(row=7, column=2)
    l6 = Label(top2, text="minutes", padx=30).grid(row=7, column=1)

    date_editor = Entry(top2, width=30)
    date_editor.grid(row=8, column=2)
    l7 = Label(top2, text="Date", padx=30).grid(row=8, column=1)

    title1_editor.insert(0, save_record[0])
    description1_editor.insert(0, save_record[2])
    expected_hour1_editor.insert(0, save_record[3])
    expected_min1_editor.insert(0, save_record[4])
    date_editor.insert(0, save_record[1])

    save_button = Button(top2, text="Save changes", command=update).grid(row=9, columnspan=2)



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
        date = :d,
        description = :de,
        expected_h = :eh,
        expected_mn = :em,
        expected_diff = :dif
        WHERE oid = :oid""",
        {
            't': title1_editor.get(),
            'd': date_editor.get(),
            'de': description1_editor.get(),
            'eh': expected_hour1_editor.get(),
            'em': expected_min1_editor.get(),
            'dif': int(clicked.get()),
            'oid': oid
        })

    conn.commit()
    conn.close()
    top2.destroy()
    top.destroy()


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
    top.destroy()


#show all events
def showall():
    global top
    top = Toplevel()
    top.title('Advisor')

    conn = sqlite3.connect("event_book.db")
    c = conn.cursor()
    # create database. Just need to create it once.
    c.execute("SELECT *, oid FROM events")
    records = c.fetchall()
    Title = Label(top, text='Title', padx=5).grid(row=1, column=1)
    da = Label(top, text='Date/Deadline', padx=5).grid(row=1, column=2)
    de = Label(top, text='Description', padx=5).grid(row=1, column=3)
    ex = Label(top, text='Expected time', padx=5).grid(row=1, column=4)
    di = Label(top, text='Difficulty', padx=5).grid(row=1, column=5)
    i = 0
    save_record = []
    for record in records:
        save_record.append(record)
        Label(top, text=save_record[i][0]).grid(row=i + 2, column=1)
        Label(top, text=save_record[i][1]).grid(row=i + 2, column=2)
        Button(top, text="Show", command=lambda i=i: popup(save_record[i][0], save_record[i][2])).grid(row=i + 2,
                                                                                                       column=3)
        Label(top, text=str(save_record[i][3]) + " hours and " + str(save_record[i][4]) + " minutes").grid(
            row=i + 2, column=4)
        Label(top, text=save_record[i][5]).grid(row=i + 2, column=5)
        Button(top, text="x", bg='red', fg='white', padx=5,
               command=lambda i=i: delete_event(save_record[i][6])).grid(row=i + 2, column=7)
        icon = PhotoImage(file='edit.png')
        b = Button(top, image=icon, width=20, height=20, command=lambda i=i: edit_event(save_record[i]))
        b.image = icon
        b.grid(row=i + 2, column=6)
        i += 1

    conn.commit()
    conn.close()


def popup(text1, text2):
    messagebox.showinfo(text1, text2)
    return


cal = Calendar(root, selectmode='day',
               date_pattern='y-mm-dd')
cal.grid(row=1, columnspan=3)

title1 = Entry(root, width=30)
title1.grid(row=2, column=2)
l1 = Label(root, text="Title", padx=30).grid(row=2, column=1)

description1 = Entry(root, width=30)
description1.grid(row=3, column=2)
l2 = Label(root, text="Description", padx=30).grid(row=3, column=1)

clicked = StringVar()
clicked.set("0")
difficulty = OptionMenu(root, clicked, "0","1","2","3","4","5")
difficulty.config(width=24)
difficulty.grid(row=4, column=2)
l3 = Label(root, text="Difficulty", padx=30).grid(row=4, column=1)

expected_hour1 = Entry(root, width=30)
expected_hour1.grid(row=6, column=2)
l4 = Label(root, text="Expected time", padx=30).grid(row=5, column=1)
l5 = Label(root, text="hours", padx=30).grid(row=6, column=1)

expected_min1 = Entry(root, width=30)
expected_min1.grid(row=7, column=2)
l6 = Label(root, text="minutes", padx=30).grid(row=7, column=1)

date = cal.get_date()



conn = sqlite3.connect("event_book.db")
c = conn.cursor()
#create database. Just need to create it once.
'''c.execute("""CREATE TABLE events (
        title text,
        date text,
        description text,
        expected_h integer,
        expected_mn integer,
        expected_diff integer
        )""")'''
button1 = Button(root, text="Create events", command=lambda: create(title1.get(), cal.get_date(), description1.get(), expected_hour1.get(), expected_min1.get(), clicked.get()))
button1.grid(row=8, column=1)

button1 = Button(root, text="Show events", command=lambda: show(date))
button1.grid(row=8, column=2)

button2 = Button(root, text="Show all events", padx=70, command=showall)
button2.grid(row=9, columnspan=5)

label_b = Label(root, text="Choose date on the calendar to show events, create event's date or task's deadline.\n For events, choose difficulty as 0.")
label_b.grid(row=10, columnspan=3)
conn.commit()
conn.close()
# Execute Tkinter
root.mainloop()