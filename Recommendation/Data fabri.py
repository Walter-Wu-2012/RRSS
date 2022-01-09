from tkinter import *
import os
import pandas as pd


LARGEFONT =("Verdana", 35)
NORMALFONT =("Verdana", 20)
SMALLFONT = ("Verdana", 13)


def submit(i):
    global df
    df2 = pd.DataFrame([[uid.get(), Stress.get(), Chaotic.get(),
                             Happiness.get(),
                             Energy.get(),
                             Focus.get(), list["Activity list"][i], 5]], columns=column_list)
    df = pd.concat([df, df2], ignore_index=True)
    print(df)
    i=i+1
    if i == 14:
        root.destroy()
    df1 = pd.DataFrame(df)
    Activity = Label(root, text=list["Activity list"][i], padx=100, pady=100, bg='white', font=SMALLFONT)
    Activity.grid(row=2, column=3, rowspan=6)

    Sub = Button(root, text="Submit", font=NORMALFONT, command=lambda: submit(i))
    Sub.grid(row=8, column=1, columnspan=2, padx=10, pady=5, sticky='we')
    df1.to_csv(os.getcwd() + '/rec' + '.csv', index=False)
    Stress.delete(0, "end")
    Chaotic.delete(0, "end")
    Happiness.delete(0, "end")
    Energy.delete(0, "end")
    Focus.delete(0, "end")



root = Tk()
root.title('Data fabrication for Recommander System')
global i
global user_id
global df
user_id = ''
i=0
column_list = ["user id", "Stress", "Chaotic", "Happiness", "Energy", "Focus", "Activity id", "Rating"]
df = pd.DataFrame(columns=column_list)
list = pd.read_csv(os.getcwd() + '/Activity list' + '.csv', header=0)
margin1 = Label(root, text="", padx=20, pady=20)
margin1.grid(row=0, column=0)
label = Label(root, text="Please input most suitable situation \n for the Activity shown.", font=NORMALFONT, padx=10,
                 pady=10)
label.grid(row=1, column=1)

uid = Entry(root, font=SMALLFONT, bg="light cyan", width=5)
uid.grid(row=2, column=2, padx=10, pady=5, sticky='e')
uid.insert(END, user_id)
uidL = Label(root, text="User_id", font=SMALLFONT)
uidL.grid(row=2, column=1, padx=10, pady=5)




Sid = ''
Stress = Entry(root, font=SMALLFONT, bg="light cyan", width=5)
Stress.grid(row=3, column=2, padx=10, pady=5, sticky='e')
Stress.insert(END, Sid)
StressL = Label(root, text="Stress_id", font=SMALLFONT)
StressL.grid(row=3, column=1, padx=10, pady=5)

Cid = ''
Chaotic = Entry(root, font=SMALLFONT, bg="light cyan", width=5)
Chaotic.grid(row=4, column=2, padx=10, pady=5, sticky='e')
Chaotic.insert(END, Cid)
ChaoticL = Label(root, text="Chaotic_id", font=SMALLFONT)
ChaoticL.grid(row=4, column=1, padx=10, pady=5)

Hid = ''
Happiness = Entry(root, font=SMALLFONT, bg="light cyan", width=5)
Happiness.grid(row=5, column=2, padx=10, pady=5, sticky='e')
Happiness.insert(END, Hid)
HappinessL = Label(root, text="Happiness_id", font=SMALLFONT)
HappinessL.grid(row=5, column=1, padx=10, pady=5)

Eid = ''
Energy = Entry(root, font=SMALLFONT, bg="light cyan", width=5)
Energy.grid(row=6, column=2, padx=10, pady=5, sticky='e')
Energy.insert(END, Eid)
EnergyL = Label(root, text="Energy_id", font=SMALLFONT)
EnergyL.grid(row=6, column=1, padx=10, pady=5)

Fid = ''
Focus = Entry(root, font=SMALLFONT, bg="light cyan", width=5)
Focus.grid(row=7, column=2, padx=10, pady=5, sticky='e')
Focus.insert(END, Fid)
FocusL = Label(root, text="Focus_id", font=SMALLFONT)
FocusL.grid(row=7, column=1, padx=10, pady=5)

Sub = Button(root, text="Submit", font=NORMALFONT, command=lambda: submit(i))
Sub.grid(row=8, column=1, columnspan=2, padx=10, pady=5, sticky='we')

Activity = Label(root, text=list["Activity list"][i], padx=100, pady=100, bg='white',font=SMALLFONT)
Activity.grid(row=2, column=3, rowspan=6)

root.mainloop()