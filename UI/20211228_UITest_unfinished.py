import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import *
from tkinter.scrolledtext import ScrolledText
from typing import Text
import random  
from operator import itemgetter
# For graph
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backend_bases import key_press_handler
# axis formatter
from matplotlib.ticker import FuncFormatter
import math
from PIL import Image,ImageTk
import os
import time

LARGEFONT =("Verdana", 35)
NORMALFONT =("Verdana", 20)
SMALLFONT = ("Verdana", 13)  

class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("1000x800")
        self.title('Advisor')
        # Variable


        # creating a container
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {} 
  
        # iterating through a tuple consisting
        # of the different page layouts


        for F in (StartPage, ChillRecom, WorkRecom, Settings, ActivityAdviceRange, HistoryLogPage, ScanningBufferPage):
  
            frame = F(container, self)
  
            # initializing frame of that object from
            # startpage, page1, page2 respectively with
            # for loop
            self.frames[F] = frame
  
            frame.grid(row = 0, column = 0, sticky ="nsew")
  
        self.show_frame(StartPage)
  
    # to display the current frame passed as
    # parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
  
# Main menu
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        margin1=tk.Label(self, text="", padx=20,pady=20)
        margin1.grid(row=0, column=0)
        label = tk.Label(self, text ="Meow! How is it going? \n Let's start with a mood scan", font = NORMALFONT,padx=10, pady=10)
        label.grid(row=1,column=2)

        self.meow = Image.open("meow1.jpg")
        self.meow = ImageTk.PhotoImage(file="meow1.jpg")
        self.meowLabel = tk.Label(self,text='helloooo',image=self.meow)
        self.meowLabel.grid(row=2,column=2,rowspan=4, columnspan=2)
      
        giveAdv = tk.Button(self, text ="GIVE ME ADVICE", font=NORMALFONT,
        command = lambda : controller.show_frame(ScanningBufferPage), padx=10, pady=10)
        giveAdv.grid(row = 2, column = 1, ipadx = 10, ipady = 10)
        
  
        ## button to show frame 2 with text layout2
        viewSchAct = tk.Button(self, text ="VIEW SCHEDULE & ACTIVITY",
        command = lambda : controller.show_frame(StartPage), padx=10, pady=10)
        viewSchAct['font'] = NORMALFONT
        viewSchAct.grid(row = 3, column = 1, ipadx = 10, ipady = 10)

        ## button to show frame 2 with text layout2
        button3 = tk.Button(self, text ="SETTINGS", padx=10, pady=10,
        command = lambda : controller.show_frame(Settings))
        button3['font'] = NORMALFONT
        button3.grid(row = 4, column = 1, ipadx = 10, ipady = 10)

        ## button to show frame 2 with text layout2
        button4 = tk.Button(self, text ="HISTORY LOGS", padx=10, pady=10,
        command = lambda : controller.show_frame(HistoryLogPage))
        button4['font'] = NORMALFONT
        button4.grid(row = 5, column = 1, ipadx = 10, ipady = 10)


        def goToScan():
            if random.randint(0,1) == 0:
                controller.show_frame(ChillRecom)
            else:
                controller.show_frame(WorkRecom)
    def update(self):
        return

class ScanningBufferPage(tk.Frame):
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="PLEASE WAIT, MEOW. LET ME ANALYZE YOUR MOOD", font = NORMALFONT)
        label.pack(side=TOP)

        self.meow = Image.open("meow1.jpg")
        self.meow = ImageTk.PhotoImage(file="meow1.jpg")
        self.meowLabel = tk.Label(self,text='helloooo',image=self.meow)
        self.meowLabel.pack(side=TOP)

        self.goButton = tk.Button(self,text='Please wait',font=LARGEFONT)
        self.goButton.pack(side=TOP)



    def updateBufferPage(self):
        self.goButton = tk.Button(self,text='Go',font=LARGEFONT)
        self.goButton.pack(side=TOP)
        
    def goNext(self):
        print(random.randint(0,1))
        if random.randint(0,1) == 0:
            self.controller.show_frame(ChillRecom)
        else:
            self.controller.show_frame(WorkRecom)   



class ChillRecom(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def back():
            controller.show_frame(StartPage)
            
        button1 = tk.Button(self, text ="BACK", font=SMALLFONT,
                            command = lambda: back())
        button1.grid(row = 1, column = 1, padx = 10, pady = 10, rowspan= 2)

        self.margin1 = tk.Label(self, text="", padx=20, pady=20)
        self.margin1.grid(row=0,column=0)

        self.frame1 = tk.Frame(self, pady=100)
        self.frame1.grid(row=1, column=1, rowspan=2, columnspan=3)
        self.frame2 = tk.Frame(self)
        self.frame2.grid(row=3, column=1)
        self.frame3 = tk.Frame(self)
        self.frame3.grid(row=3, column=2)
        self.frame4 = tk.Frame(self)
        self.frame4.grid(row=3, column=3)

        self.top = tk.Label(self.frame1, text='Meow meow meeee ow ow ow meow meow meow woof woof')
        self.top.grid(row=1, column=2, rowspan=2, columnspan=4)
        self.skip = tk.Button(self.frame1, text='SKIP ALL', padx=22, font=SMALLFONT)
        self.skip.grid(row=1, column=6)
        self.other = tk.Button(self.frame1, text='OTHER CHOICES', padx=1, font=SMALLFONT)
        self.other.grid(row=2, column=6)

        self.meow = Image.open("meow1.jpg")
        self.meow = self.meow.resize((150, 150), Image.ANTIALIAS)
        self.meow1 = ImageTk.PhotoImage(self.meow)

        k=110
        i=54
        j=49

        self.tl1 = tk.Label(self.frame2, text="Activity #1", font=SMALLFONT).grid(row=4, column=1, columnspan=2)
        self.Image1 = tk.Label(self.frame2, image=self.meow1).grid(row=5, column=1, columnspan=2)
        self.bl1 = tk.Label(self.frame2, text="Description #1", font=SMALLFONT).grid(row=6, column=1, columnspan=2)
        self.accept1 = tk.Button(self.frame2, text='YES', padx=k, font=SMALLFONT).grid(row=7, column=1, columnspan=2)
        self.deny1 = tk.Button(self.frame2, text='NO', padx=i, font=SMALLFONT).grid(row=8, column=1)
        self.skip1 = tk.Button(self.frame2, text='SKIP', padx=j, font=SMALLFONT).grid(row=8, column=2)

        self.tl2 = tk.Label(self.frame3, text="Activity #2", font=SMALLFONT).grid(row=4, column=3, columnspan=2)
        self.Image2 = tk.Label(self.frame3, image=self.meow1).grid(row=5, column=3, columnspan=2)
        self.bl2 = tk.Label(self.frame3, text="Description #2", font=SMALLFONT).grid(row=6, column=3, columnspan=2)
        self.accept2 = tk.Button(self.frame3, text='YES', padx=k, font=SMALLFONT).grid(row=7, column=3, columnspan=2)
        self.deny2 = tk.Button(self.frame3, text='NO', padx=i, font=SMALLFONT).grid(row=8, column=3)
        self.skip2 = tk.Button(self.frame3, text='SKIP', padx=j, font=SMALLFONT).grid(row=8, column=4)

        self.tl3 = tk.Label(self.frame4, text="Activity #3", font=SMALLFONT).grid(row=4, column=5, columnspan=2)
        self.Image3 = tk.Label(self.frame4, image=self.meow1).grid(row=5, column=5, columnspan=2)
        self.bl3 = tk.Label(self.frame4, text="Description #3", font=SMALLFONT).grid(row=6, column=5, columnspan=2)
        self.accept3 = tk.Button(self.frame4, text='YES', padx=k, font=SMALLFONT).grid(row=7, column=5, columnspan=2)
        self.deny3 = tk.Button(self.frame4, text='NO', padx=i, font=SMALLFONT).grid(row=8, column=5)
        self.skip3 = tk.Button(self.frame4, text='SKIP', padx=j, font=SMALLFONT).grid(row=8, column=6)

        self.margin2 = tk.Label(self, text="", padx=20, pady=20, font=SMALLFONT).grid(row=9, column=7)

class WorkRecom(tk.Frame):
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)

        self.margin1 = tk.Label(self, text="", padx=20, pady=20)
        self.margin1.grid(row=0,column=0)
        def back():
            controller.show_frame(StartPage)
            
        button1 = tk.Button(self, text ="BACK", font=SMALLFONT,
                            command = lambda: back())
        button1.grid(row = 1, column = 1, padx = 10, pady = 10, rowspan= 2)
        
        self.frame1 = tk.Frame(self, pady=100)
        self.frame1.grid(row=1, column=1, rowspan=2, columnspan=3)
        self.frame2 = tk.Frame(self)
        self.frame2.grid(row=3, column=1)
        self.frame3 = tk.Frame(self)
        self.frame3.grid(row=3, column=2)
        self.frame4 = tk.Frame(self)
        self.frame4.grid(row=3, column=3)

        self.top = tk.Label(self.frame1, text='Meow meow meeee ow ow ow meow meow meow woof woof')
        self.top.grid(row=1, column=2, rowspan=2, columnspan=4)
        self.skip = tk.Button(self.frame1, text='SKIP ALL', padx=22, font=SMALLFONT)
        self.skip.grid(row=1, column=6)
        self.other = tk.Button(self.frame1, text='OTHER CHOICES', padx=1, font=SMALLFONT)
        self.other.grid(row=2, column=6)

        self.meow = Image.open("meow1.jpg")
        self.meow = self.meow.resize((150, 150), Image.ANTIALIAS)
        self.meow1 = ImageTk.PhotoImage(self.meow)

        k=110
        i=54
        j=49

        self.tl1 = tk.Label(self.frame2, text="Activity #1", font=SMALLFONT).grid(row=4, column=1, columnspan=2)
        self.Image1 = tk.Label(self.frame2, image=self.meow1).grid(row=5, column=1, columnspan=2)
        self.bl1 = tk.Label(self.frame2, text="Description #1", font=SMALLFONT).grid(row=6, column=1, columnspan=2)
        self.accept1 = tk.Button(self.frame2, text='YES', padx=k, font=SMALLFONT).grid(row=7, column=1, columnspan=2)
        self.deny1 = tk.Button(self.frame2, text='NO', padx=i, font=SMALLFONT).grid(row=8, column=1)
        self.skip1 = tk.Button(self.frame2, text='SKIP', padx=j, font=SMALLFONT).grid(row=8, column=2)

        self.tl2 = tk.Label(self.frame3, text="Activity #2", font=SMALLFONT).grid(row=4, column=3, columnspan=2)
        self.Image2 = tk.Label(self.frame3, image=self.meow1).grid(row=5, column=3, columnspan=2)
        self.bl2 = tk.Label(self.frame3, text="Description #2", font=SMALLFONT).grid(row=6, column=3, columnspan=2)
        self.accept2 = tk.Button(self.frame3, text='YES', padx=k, font=SMALLFONT).grid(row=7, column=3, columnspan=2)
        self.deny2 = tk.Button(self.frame3, text='NO', padx=i, font=SMALLFONT).grid(row=8, column=3)
        self.skip2 = tk.Button(self.frame3, text='SKIP', padx=j, font=SMALLFONT).grid(row=8, column=4)

        self.tl3 = tk.Label(self.frame4, text="Activity #3", font=SMALLFONT).grid(row=4, column=5, columnspan=2)
        self.Image3 = tk.Label(self.frame4, image=self.meow1).grid(row=5, column=5, columnspan=2)
        self.bl3 = tk.Label(self.frame4, text="Description #3", font=SMALLFONT).grid(row=6, column=5, columnspan=2)
        self.accept3 = tk.Button(self.frame4, text='YES', padx=k, font=SMALLFONT).grid(row=7, column=5, columnspan=2)
        self.deny3 = tk.Button(self.frame4, text='NO', padx=i, font=SMALLFONT).grid(row=8, column=5)
        self.skip3 = tk.Button(self.frame4, text='SKIP', padx=j, font=SMALLFONT).grid(row=8, column=6)

        self.margin2 = tk.Label(self, text="", padx=20, pady=20, font=SMALLFONT).grid(row=9, column=7)

class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="GENERAL SETTINGS", font = NORMALFONT)
        label.grid(row = 2, column = 2, padx = 10, pady = 10, columnspan=2)
        # button to show frame 2 with text
        # layout2
        def back():
            RFreq = RecommendationFreq.get("1.0", "end-1c")
            controller.show_frame(StartPage)

        def toActivityRange():
            controller.show_frame(ActivityAdviceRange)
            
        button1 = tk.Button(self, text ="BACK", font=NORMALFONT,
                            command = lambda: back())
        #button1 = tk.Button(self, text ="BACK", font=NORMALFONT,
        #                    command = lambda : controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # layout3
        button2 = tk.Button(self, text ="General Settings", font=NORMALFONT,
                            command = lambda : controller.show_frame(Settings))
        button2.grid(row = 1, column = 2, padx = 10, pady = 10)

        # button to show frame 3 with text
        # layout3
        button3 = tk.Button(self, text ="Activity Range", font=NORMALFONT,
                            command = lambda : toActivityRange())
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 1, column = 3, padx = 10, pady = 10)

        # Asking for cute friend
        def CuteFriendToggle():
    
            if CuteFriendButton.config('text')[-1] == 'ON':
                CuteFriend = "OFF"
                CuteFriendButton.config(text='OFF',bg='red',fg='white')
            else:
                CuteFriend = "ON"
                CuteFriendButton.config(text='ON',bg='green',fg='white')

        label = ttk.Label(self, text ="Cute Friend", font = SMALLFONT)
        label.grid(row = 4, column = 2, padx = 10, pady = 10)
        CuteFriendButton = tk.Button(self, text="ON", font=SMALLFONT, bg='green',fg='white', command=CuteFriendToggle)
        CuteFriendButton.grid(row = 4, column = 3, padx = 10, pady = 10)

        # Asking for recommendation frequency
        label = ttk.Label(self, text ="Ask for recommendation every", font = SMALLFONT)
        label.grid(row = 5, column = 2, padx = 10, pady = 10)    
        label = ttk.Label(self, text ="minutes", font = SMALLFONT)
        label.grid(row = 5, column = 4, padx = 10, pady = 10)    

        RecommendationFreq = tk.Text(self, font=NORMALFONT, bg = "light cyan", height=1, width=5)
        RecommendationFreq.grid(row = 5, column = 3, padx = 10, pady = 10)
        RecommendationFreq.insert(END,RFreq)

class ActivityAdviceRange(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="ACTIVITY ADVICE RANGE", font = NORMALFONT)
        label.grid(row = 2, column = 2, padx = 10, pady = 10, columnspan=3)

        def back():
            controller.show_frame(StartPage)
            
        # BACK button
        button1 = tk.Button(self, text ="BACK", font=NORMALFONT,
                            command = lambda: back())
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # Go to General Settings
        button2 = tk.Button(self, text ="General Settings", font=NORMALFONT,
                            command = lambda : controller.show_frame(Settings))
        button2.grid(row = 1, column = 2, padx = 10, pady = 10)

        # Go to Activity Range Button
        button3 = tk.Button(self, text ="Activity Range", font=NORMALFONT,
                            command = lambda : controller.show_frame(StartPage))
        button3.grid(row = 1, column = 3, padx = 10, pady = 10, columnspan=2)

        # activity box and activity status box
        self.ActivityBar = tk.Scrollbar(self) # Scrollbar
        self.ActivityList = tk.Listbox(self, width=30, height=20, yscrollcommand = self.yscroll1 ,font =SMALLFONT) # Activity Name List
        self.ActivityTypeList = tk.Listbox(self, width=10, height=20, yscrollcommand = self.yscroll2, font = SMALLFONT) # Activity Type List
        self.ActivityStatusList = tk.Listbox(self, width=10, height=20, yscrollcommand = self.yscroll3, font = SMALLFONT) # Activity Like Status List

        # List Reference for Sorting
        self.ActivityListRef = []
        for activity in DatabaseActivityList.keys():
            # Assume activity from database is already sorted
            self.ActivityListRef.append(DatabaseActivityList[activity])

            self.ActivityList.insert(END, DatabaseActivityList[activity][0])
            self.ActivityTypeList.insert(END,DatabaseActivityList[activity][1])
            self.ActivityStatusList.insert(END, DatabaseActivityList[activity][2])

        # Location of the boxes
        self.ActivityBar.grid(row = 4, column = 5, padx = 0, pady = 0, sticky="nsw")
        self.ActivityList.grid( row = 4, column = 2, padx = 0, pady = 0, columnspan=1, sticky="we") # Name
        self.ActivityTypeList.grid( row = 4, column = 3, padx = 0, pady = 0, columnspan=1, sticky="nswe") # Type
        self.ActivityStatusList.grid( row = 4, column = 4, padx = 0, pady = 0, columnspan=1, sticky="nswe") # Status
        self.ActivityBar.config( command = self.ActivityList.yview)

        # Sorting button
        self.NameSortingButton = tk.Button(self, text ="Name", font=SMALLFONT,
                            command = lambda: self.sortName())
        self.NameSortingButton.grid(row = 3, column = 2, padx = 0, pady = 0, sticky="ew")
        self.TypeSortingButton = tk.Button(self, text ="Type", font=SMALLFONT,
                            command = lambda: self.sortType())
        self.TypeSortingButton.grid(row = 3, column = 3, padx = 0, pady = 0, sticky="ew")
        self.StatusSortingButton = tk.Button(self, text ="Like Status", font=SMALLFONT,
                            command = lambda: self.sortLikeStatus())
        self.StatusSortingButton.grid(row = 3, column = 4, padx = 0, pady = 0, sticky="ew")
        # For Reverse Sorting
        self.sortStatus = "Name"

        # Search the activity list
        # searchbar
        self.SearchBar = tk.Text(self, bg = "light cyan", width=20, height=1, font=SMALLFONT)
        self.SearchBar.grid(row = 5, column = 2, sticky= 'e')
        self.SearchBar.insert(END, 'Search Here')
        # search button
        self.SearchBarButton = tk.Button(self, width=12, text='Find', command=self.search, font=SMALLFONT)
        self.SearchBarButton.grid(row = 5, column = 3)

        # variable for searching
        self.searchTemp = ''
        self.foundTempIndex = 0


    def sortName(self):
        if self.sortStatus != "Name":
            self.ActivityListRef = sorted(self.ActivityListRef, key=itemgetter(0))
            self.sortStatus = "Name"
        else:
            self.ActivityListRef = sorted(self.ActivityListRef, key=itemgetter(0), reverse=True)
            self.sortStatus = "Name2"
        # Clear current
        self.ActivityList.delete(0,END)
        self.ActivityStatusList.delete(0,END)
        self.ActivityTypeList.delete(0,END)
        # Fill with new
        for activity in self.ActivityListRef:
            self.ActivityList.insert(END, activity[0])
            self.ActivityTypeList.insert(END,activity[1])      
            self.ActivityStatusList.insert(END, activity[2])    

    def sortType(self):
        if self.sortStatus != "Type":
            self.ActivityListRef = sorted(self.ActivityListRef, key=itemgetter(1))
            self.sortStatus = "Type"
        else:
            self.ActivityListRef = sorted(self.ActivityListRef, key=itemgetter(1), reverse=True)
            self.sortStatus = "Type2"
        # Clear current
        self.ActivityList.delete(0,END)
        self.ActivityStatusList.delete(0,END)
        self.ActivityTypeList.delete(0,END)
        # Fill with new
        for activity in self.ActivityListRef:
            self.ActivityList.insert(END, activity[0])
            self.ActivityTypeList.insert(END,activity[1])      
            self.ActivityStatusList.insert(END, activity[2])

    def sortLikeStatus(self):
        if self.sortStatus != "Status":
            self.ActivityListRef = sorted(self.ActivityListRef, key=itemgetter(2))
            self.sortStatus = "Status"
        else:
            self.ActivityListRef = sorted(self.ActivityListRef, key=itemgetter(2), reverse=True)
            self.sortStatus = "Status2"
        # Clear current
        self.ActivityList.delete(0,END)
        self.ActivityStatusList.delete(0,END)
        self.ActivityTypeList.delete(0,END)
        # Fill with new
        for activity in self.ActivityListRef:
            self.ActivityList.insert(END, activity[0])
            self.ActivityTypeList.insert(END,activity[1])      
            self.ActivityStatusList.insert(END, activity[2])

    # when scroll on name
    def yscroll1(self, *args):
        if self.ActivityStatusList.yview() != self.ActivityList.yview():
            self.ActivityStatusList.yview_moveto(args[0])
            self.ActivityTypeList.yview_moveto(args[0])
        self.ActivityBar.set(*args)

    # when scroll on like
    def yscroll2(self, *args):
        if self.ActivityList.yview() != self.ActivityTypeList.yview():
            self.ActivityList.yview_moveto(args[0])
            self.ActivityTypeList.yview_moveto(args[0])
            print(args)
        self.ActivityBar.set(*args)

    # when scroll on typelist
    def yscroll3(self, *args):
        if self.ActivityList.yview() != self.ActivityStatusList.yview():
            self.ActivityList.yview_moveto(args[0])
            self.ActivityTypeList.yview_moveto(args[0])
            print(args)
        self.ActivityBar.set(*args)

    def yview(self, *args):
        self.ActivityList.yview(*args)
        self.ActivityStatusList.yview(*args)

    def search(self,*args):
        # Get value from searchbox

        self.activityList = self.ActivityList.get(0,self.ActivityList.size())

        if self.searchTemp != self.SearchBar.get("1.0", "end-1c"):
            self.searchTemp = self.SearchBar.get("1.0", "end-1c")
            self.foundTempIndex = 0


        #print(self.SearchBar.get("1.0", "end-1c"))

        # Find matching
        #print(self.activityList)

        for i in range(len(self.activityList)):
            if self.searchTemp.lower()in self.activityList[i].lower():
                if self.foundTempIndex<i:
                    self.foundTempIndex = i
                    break

            if i==len(self.activityList)-1:
                self.searchTemp = ''
                self.search(args)
                # self.popUpNotFound()
                return
                
        # move to percent
        #self.ActivityStatusList.yview_moveto('0.2')

        # move to searched
        self.ActivityStatusList.see(self.foundTempIndex)
        self.ActivityList.selection_clear(0,self.ActivityList.size())
        self.ActivityList.selection_set(self.foundTempIndex)

    def popUpNotFound(self):
        self.popUp = tk.Tk()
        # print(str(self.winfo_rootx())+' '+str(self.winfo_rooty())) # location to place the popup
        self.popUp.geometry(f"200x100+{self.winfo_rootx()+400-100}+{self.winfo_rooty()+300-50}")
        self.popUpNotFoundText = tk.Label(self.popUp, text="No results",font=SMALLFONT)
        self.popUpNotFoundText.place(x=100,y=40,anchor='center')
        self.popUpDestroyButton = tk.Button(self.popUp, text="OK",font=SMALLFONT,command=self.popUp.destroy)
        self.popUpDestroyButton.place(x=100,y=70,anchor='center')

class HistoryLogPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Label
        label = ttk.Label(self, text ="History Logs ", font = LARGEFONT, anchor=CENTER)
        label.grid(row = 0, column = 2, padx = 10, pady = 10, columnspan=3)

        # Back Button
        def goBack(*args):
            controller.show_frame(StartPage)
            
        backButton = tk.Button(self, text ="BACK", font=NORMALFONT,
                            command = lambda: goBack())
        backButton.grid(row=0, column = 1, padx = 10)

        # Settings for History Logs
        labelRange = ttk.Label(self, text ="Range ", font = SMALLFONT)
        labelRange.grid(row = 1, column = 1, padx = 10, pady = 10, sticky='e')
        labelStartingDate = ttk.Label(self, text ="Starting Date ", font = SMALLFONT)
        labelStartingDate.grid(row = 2, column = 1, padx = 10, pady = 10, sticky='e')
        labelStartingTime = ttk.Label(self, text ="Starting Time ", font = SMALLFONT)
        labelStartingTime.grid(row = 3, column = 1, padx = 10, pady = 10, sticky='e')
        labelMoodIndex = ttk.Label(self, text ="Mood Index ", font = SMALLFONT)
        labelMoodIndex.grid(row = 4, column = 1, padx = 10, pady = 10, sticky='e')

        HistoryRange = ['8 Hours','12 Hours','24 Hours']
        MoodIndex = ['Happiness', 'Energy', 'Stress&Worries','Chaotic','Focus']
        historyDict

        global HistoryRangeClicked
        global StartingDateClicked
        global MoodIndexClicked
        HistoryRangeClicked = tk.StringVar()
        StartingDateClicked = tk.StringVar()
        MoodIndexClicked = tk.StringVar()

        # For date menu
        def changeDateToDateText(date):
            monthsList= ['month', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'] 
            return f"{int(date[6:8])} {monthsList[int(date[4:6])]} {date[0:4]}"

        def changeDateTextToDate(dateText):
            dateTextList = dateText.split(' ')
            monthsKey=  {   'January':'01',
                            'February':'02',
                            'March':'03',
                            'April':'04',
                            'May':'05',
                            'June':'06',
                            'July':'07',
                            'August':'08',
                            'September':'09',
                            'October':'10',
                            'November':'11',
                            'December':'12'	}
            return f"{dateTextList[2]}{monthsKey[dateTextList[1]]}{int(dateTextList[0]):02}"

        # initial menu text
        HistoryRangeClicked.set( "8 Hours" )
        StartingDateClicked.set(changeDateToDateText(list(historyDict.keys())[-1]))
        MoodIndexClicked.set( "Happiness" )

        # Create Dropdown menu
        dropRange = tk.OptionMenu( self , HistoryRangeClicked , *HistoryRange )
        dropRange.config(font=SMALLFONT)
        dropRange.grid(row = 1, column = 2, padx = 10, pady = 5, sticky='we', columnspan=2)
        dropRangeMenu = self.nametowidget(dropRange.menuname)
        dropRangeMenu.config(font=SMALLFONT)

        dropStartingDate = tk.OptionMenu( self , StartingDateClicked , 
        *list([changeDateToDateText(date) for date in sorted(historyDict.keys(),reverse=True)]))
        dropStartingDate.config(font=SMALLFONT)
        dropStartingDate.grid(row = 2, column = 2, padx = 10, pady = 5, sticky='we', columnspan=2)
        dropStartingDateMenu = self.nametowidget(dropStartingDate.menuname)
        dropStartingDateMenu.config(font=SMALLFONT)
        
        dropMoodIndex = tk.OptionMenu( self , MoodIndexClicked , *MoodIndex)
        dropMoodIndex.config(font=SMALLFONT)
        dropMoodIndex.grid(row = 4, column = 2, padx = 10, pady = 5, sticky='we', columnspan=2)
        dropMoodIndexMenu = self.nametowidget(dropMoodIndex.menuname)
        dropMoodIndexMenu.config(font=SMALLFONT)
        
        # Fill menu for Starting Time
        startingTime = '08'
        startingTimeBox = tk.Entry(self, font=SMALLFONT, bg = "light cyan", width=5)
        startingTimeBox.grid(row = 3, column = 2, padx = 10, pady = 5, sticky='e')
        startingTimeBox.insert(END,startingTime)
        startingTimeLabel = ttk.Label(self, text =".00", font = SMALLFONT)
        startingTimeLabel.grid(row = 3, column = 3, padx = 10, pady= 5, sticky='w')

        # Create Graph Button
        graphButton = tk.Button(self, text ="Create Graph", font=SMALLFONT, command = lambda: createMoodIndexGraph())
        graphButton.grid(row = 5, column = 1, padx = 10, pady = 5, sticky= 'we', columnspan=3)

        # history listbox
        self.HistoryBar = tk.Scrollbar(self) # Scrollbar
        self.TimeList = tk.Listbox(self, width=10, height=10, yscrollcommand = self.yscroll1 ,font =SMALLFONT) # Time List
        self.MoodIndexList = tk.Listbox(self, width=10, height=10, yscrollcommand = self.yscroll2, font = SMALLFONT) # Mood Index List
        self.ActivityPickedList = tk.Listbox(self, width=10, height=10, yscrollcommand = self.yscroll3, font = SMALLFONT) # Recommendation Picked List
        
        self.HistoryBar.grid(row = 7, column = 5, padx = 0, pady = 0, sticky="nsw")
        self.TimeList.grid( row = 7, column = 2, padx = 0, pady = 0, columnspan=1, sticky="we") # Name
        self.MoodIndexList.grid( row = 7, column = 3, padx = 0, pady = 0, columnspan=1, sticky="nswe") # Type
        self.ActivityPickedList.grid( row = 7, column = 4, padx = 0, pady = 0, columnspan=1, sticky="nswe") # Status
        self.HistoryBar.config( command = self.TimeList.yview)

        self.TimeListButton = tk.Button(self, text ="Time", font=SMALLFONT)
        self.TimeListButton.grid(row = 6, column = 2, padx = 0, pady = 0, sticky="ew")
        self.MoodIndexListButton = tk.Button(self, text ="Mood Index", font=SMALLFONT)
        self.MoodIndexListButton.grid(row = 6, column = 3, padx = 0, pady = 0, sticky="ew")
        self.ActivityPickedListButton = tk.Button(self, text ="Activity", font=SMALLFONT)
        self.ActivityPickedListButton.grid(row = 6, column = 4, padx = 0, pady = 0, sticky="ew")

        # transform data to plottable data for graph and table
        def createDataForGraph(historyDictionary, configuration):
            print("Configuration: ",configuration)
            print(changeDateTextToDate(configuration[1]))
            print("History Dict Keys: ",historyDictionary.keys())

            if int(configuration[0].split(' ')[0])+int(configuration[2])>24: #whether next day's data is needed or not
                print("Bring next date")

            x = []
            xName = []
            activityList = []
            y = []

            for timeName in historyDictionary[changeDateTextToDate(configuration[1])].keys():
                time = self.createTimeFromTimeName(timeName)
                # print(time)
                value = historyDictionary[changeDateTextToDate(configuration[1])][timeName]
                # print(value)
                if time >= int(configuration[2]) and time<= int(configuration[2])+int(configuration[0].split(' ')[0]):
                    x.append(time)
                    # -----------------------add mood index -------------------------
                    y.append(value[0])
                    activityList.append(value[1])

            print("x: ",x)    
            print("y: ",y)
            print("Activity: ",activityList)
            return [x, y, activityList, configuration[3]]

        # plot mood index graph (in createMoodIndexGraph(*args))
        def createMoodIndexGraphFromData(data):
            # not found
            if len(data[0])==0:
                self.popUpNotFound()
                return

            fig = matplotlib.pyplot.Figure(figsize=(5,2.7), dpi=100)
            ax = fig.add_subplot(111)
            moodIndexIndex = {'Happiness':2, 'Energy':3, 'Stress&Worries':0,'Chaotic':1,'Focus':4}
            ax.plot(data[0],[value[moodIndexIndex[data[3]]] for value in data[1]])
            ax.set_title(f'{data[3]}')
            ax.set_ylim([-1,1])
            # ax.xaxis.set_major_locator(MultipleLocator(1))
            ax.xaxis.set_major_formatter(FuncFormatter(timeFormatter)) 

            # add just axis
            canvas = FigureCanvasTkAgg(fig, master=self)
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 4, padx = 10, pady= 5, sticky='w', columnspan = 2, rowspan = 5)

            # add data to listbox

            self.addDataToHistoryListbox(data)
            return

        # main function for mood index graph
        def createMoodIndexGraph(*args):
            startingTime = startingTimeBox.get()
            print(startingTime)
            self.focus()
            createMoodIndexGraphFromData(createDataForGraph(historyDict, [HistoryRangeClicked.get(), StartingDateClicked.get(), startingTime, MoodIndexClicked.get()]))
            return

        # formatter for graph's x axis
        def timeFormatter(time,y):
            return f"{int(time)+(time-int(time))*60/100:.2f}"

        # Bind enter to starting time entering box
        startingTimeBox.bind('<Return>', createMoodIndexGraph)

        # create initial graph
        createMoodIndexGraphFromData(createDataForGraph(historyDict, ['24 Hours', StartingDateClicked.get(), '0', MoodIndexClicked.get()]))
   

    # scroll for history listbox    
    def yscroll1(self, *args):
        if self.MoodIndexList.yview() != self.TimeList.yview():
            self.MoodIndexList.yview_moveto(args[0])
            self.ActivityPickedList.yview_moveto(args[0])
        self.HistoryBar.set(*args)

    def yscroll2(self, *args):
        if self.TimeList.yview() != self.MoodIndexList.yview():
            self.TimeList.yview_moveto(args[0])
            self.ActivityPickedList.yview_moveto(args[0])
        self.HistoryBar.set(*args)

    def yscroll3(self, *args):
        if self.TimeList.yview() != self.ActivityPickedList.yview():
            self.TimeList.yview_moveto(args[0])
            self.MoodIndexList.yview_moveto(args[0])
        self.HistoryBar.set(*args)

    def popUpNotFound(self):
        self.popUp = tk.Tk()
        print(str(self.winfo_rootx())+' '+str(self.winfo_rooty()))
        self.popUp.geometry(f"200x100+{self.winfo_rootx()+400-100}+{self.winfo_rooty()+300-50}")
        self.popUpNotFoundText = tk.Label(self.popUp, text="No results",font=SMALLFONT)
        self.popUpNotFoundText.place(x=100,y=40,anchor='center')
        self.popUpDestroyButton = tk.Button(self.popUp, text="OK",font=SMALLFONT,command=self.popUp.destroy)
        self.popUpDestroyButton.place(x=100,y=70,anchor='center')

    # add data to history listbox at the bottom
    def addDataToHistoryListbox(self,data):
        # add data to listbox
        self.TimeList.delete(0,END)
        self.MoodIndexList.delete(0,END)
        self.ActivityPickedList.delete(0,END)
        moodIndexIndex = {'Happiness':2, 'Energy':3, 'Stress&Worries':0,'Chaotic':1,'Focus':4}
        selectedMoodValue = [value[moodIndexIndex[data[3]]] for value in data[1]]
        for i in range(len(data[0])):
            self.TimeList.insert(END, self.createTimeNameFromTime(data[0][i]))
            self.MoodIndexList.insert(END, selectedMoodValue[i]) #index based on what mood index
            self.ActivityPickedList.insert(END, data[2][i])

    # transform 10.5 to 10.30 for example
    def createTimeNameFromTime(self,time):
        return f"{int(time)+(time-int(time))*60/100:.2f}"

    # transform 10.30 to 10.5 for example
    def createTimeFromTimeName(self,time):
        time = time.split('.')
        return int(time[0])+int(time[1])/60

# Settings Variable Database
RFreq = 45
CuteFriend = "ON"

# Activity Database
DatabaseActivityList = {}
for line in range(50):
    DatabaseActivityList[line]=["Activity number "+str(line), random.choice(("Exercise","Entertainment","Routine")), random.choice((1,2,3))]

# History Database
historyDict = {}
exampleDay = {}
historyDict['20211213'] = {}
historyDict['20211214'] = {}
historyDict['20211215'] = {}
historyDict['20211216'] = {}
for i in range(16):
    historyDict['20211213'][f"{i+5:02}"+'.30'] = [[-((i^2-1+random.randint(0,5)+j)%16)/8+1 for j in range(5)], DatabaseActivityList[random.randint(0,49)][0] ]
    historyDict['20211214'][f"{i+5:02}"+'.30'] = [[-((i^2+i+random.randint(0,5)+j)%16)/8+1 for j in range(5)], DatabaseActivityList[random.randint(0,49)][0] ]
    historyDict['20211215'][f"{i+5:02}"+'.30'] = [[-((i^2+random.randint(0,5)+j)%16)/8+1 for j in range(5)], DatabaseActivityList[random.randint(0,49)][0] ]
    historyDict['20211216'][f"{i+5:02}"+'.30'] = [[-((i^2+1+random.randint(0,5+j))%16)/8+1 for j in range(5)], DatabaseActivityList[random.randint(0,49)][0] ]
#print(historyDict)
    


# Driver Code
app = tkinterApp()
app.mainloop()