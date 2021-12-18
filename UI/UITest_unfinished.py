
import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter.constants import *
from tkinter.scrolledtext import ScrolledText
from typing import Text
import random  
 
LARGEFONT =("Verdana", 35)
NORMALFONT =("Verdana", 20)
SMALLFONT = ("Verdana", 10)  

class tkinterApp(tk.Tk):
     
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("800x600")
    
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
        for F in (StartPage, Page1, Page2, Settings, ActivityAdviceRange):
  
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
  
# first window frame startpage
  
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
         
        # label of frame Layout 2
        label = ttk.Label(self, text ="Meow!, how are you today? ", font = LARGEFONT)
        label.place(x=0,y=40,anchor='center')
        # putting the grid in its place by using
        # grid
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
        button1 = tk.Button(self, text ="Page 1", font=NORMALFONT,
        command = lambda : controller.show_frame(Page1))
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
        
  
        ## button to show frame 2 with text layout2
        button2 = tk.Button(self, text ="Page 2",
        command = lambda : controller.show_frame(Page2))
        button2['font'] = NORMALFONT
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)

        ## button to show frame 2 with text layout2
        button3 = tk.Button(self, text ="SETTINGS",
        command = lambda : controller.show_frame(Settings))
        button3['font'] = NORMALFONT
        # putting the button in its place by
        # using grid
        button3.grid(row = 3, column = 1, padx = 10, pady = 10)

        ## button to show frame 2 with text layout2
        button4 = tk.Button(self, text ="HISTORY LOGS",
        command = lambda : controller.show_frame(Page2))
        button4['font'] = NORMALFONT
        # putting the button in its place by
        # using grid
        button4.grid(row = 4, column = 1, padx = 10, pady = 10)
  
          
  
  
# second window frame page1
class Page1(tk.Frame):
     
    def __init__(self, parent, controller):
         
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 1", font = LARGEFONT)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="StartPage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place
        # by using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button2 = ttk.Button(self, text ="Page 2",
                            command = lambda : controller.show_frame(Page2))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  
  
# third window frame page2
class Page2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
  
        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
     
        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)
  
  
  # third window frame page2
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
  
        # button to show frame 3 with text
        # layout3
        button2 = tk.Button(self, text ="General Settings", font=NORMALFONT,
                            command = lambda : controller.show_frame(Settings))
     
        # putting the button in its place by
        # using grid
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
        label.grid(row = 2, column = 2, padx = 10, pady = 10, columnspan=2)
        # button to show frame 2 with text
        # layout2
        def back():
            controller.show_frame(StartPage)
            
        button1 = tk.Button(self, text ="BACK", font=NORMALFONT,
                            command = lambda: back())
        #button1 = tk.Button(self, text ="BACK", font=NORMALFONT,
        #                    command = lambda : controller.show_frame(StartPage))

        # putting the button in its place by
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)
  
        # button to show frame 3 with text
        # layout3
        button2 = tk.Button(self, text ="General Settings", font=NORMALFONT,
                            command = lambda : controller.show_frame(Settings))
     
        # putting the button in its place by
        # using grid
        button2.grid(row = 1, column = 2, padx = 10, pady = 10)

        # button to show frame 3 with text
        # layout3
        button3 = tk.Button(self, text ="Activity Range", font=NORMALFONT,
                            command = lambda : controller.show_frame(StartPage))
     
        # putting the button in its place by
        # using grid
        button3.grid(row = 1, column = 3, padx = 10, pady = 10)

        
        # activity box and activity status box
        self.ActivityBar = tk.Scrollbar(self)
        self.ActivityBar.grid(row = 3, column = 4, padx = 0, pady = 0, sticky="nsw")
        self.ActivityList = tk.Listbox(self, width=30, height=20, yscrollcommand = self.yscroll1 ,font =SMALLFONT)
        self.ActivityStatusList = tk.Listbox(self, width=30, height=20, yscrollcommand = self.yscroll2, font = SMALLFONT)
        for activity in DatabaseActivityList.keys():
            self.ActivityList.insert(END, DatabaseActivityList[activity][0])
            self.ActivityStatusList.insert(END, DatabaseActivityList[activity][1])
        

        self.ActivityList.grid( row = 3, column = 2, padx = 0, pady = 10, columnspan=1, sticky="e")
        self.ActivityStatusList.grid( row = 3, column = 3, padx = 0, pady = 10, columnspan=1, sticky="e")

        self.ActivityBar.config( command = self.ActivityList.yview)

        #searchbar
        self.SearchBar = tk.Text(self, bg = "light cyan", width=20, height=1, font=SMALLFONT)
        self.SearchBar.grid(row = 4, column = 2, sticky= 'e')
        self.SearchBar.insert(END, 'Search Here')

        self.SearchBarButton = tk.Button(self, width=12, text='Find', command=self.search)
        self.SearchBarButton.grid(row = 4, column = 3)

        # variable for searching
        self.searchTemp = ''
        self.foundTempIndex = 0
        self.activityList = self.ActivityList.get(0,self.ActivityList.size())

    def yscroll1(self, *args):
        if self.ActivityStatusList.yview() != self.ActivityList.yview():
            self.ActivityStatusList.yview_moveto(args[0])
        self.ActivityBar.set(*args)

    def yscroll2(self, *args):
        if self.ActivityList.yview() != self.ActivityStatusList.yview():
            self.ActivityList.yview_moveto(args[0])
            print(args)
        self.ActivityBar.set(*args)

    def yview(self, *args):
        self.ActivityList.yview(*args)
        self.ActivityStatusList.yview(*args)

    def search(self,*args):
        # Get value from searchbox

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
                self.popUpNotFound()
                return
                
        # move to percent
        #self.ActivityStatusList.yview_moveto('0.2')

        # move to searched
        self.ActivityStatusList.see(self.foundTempIndex)
        self.ActivityList.selection_clear(0,self.ActivityList.size())
        self.ActivityList.selection_set(self.foundTempIndex)

    def popUpNotFound(self):
        self.popUp = tk.Tk()
        print(str(self.winfo_rootx())+' '+str(self.winfo_rooty()))
        self.popUp.geometry(f"200x100+{self.winfo_rootx()+400-100}+{self.winfo_rooty()+300-50}")
        self.popUpNotFoundText = tk.Label(self.popUp, text="No results",font=SMALLFONT)
        self.popUpNotFoundText.place(x=100,y=40,anchor='center')
        self.popUpDestroyButton = tk.Button(self.popUp, text="OK",font=SMALLFONT,command=self.popUp.destroy)
        self.popUpDestroyButton.place(x=100,y=70,anchor='center')





    global RFreq
    RFreq = 45
    global CuteFriend
    CuteFriend = "ON"
    global DatabaseActivityList
    DatabaseActivityList = {}
    for line in range(50):
        DatabaseActivityList[line]=["Activity number "+str(line), random.choice((1,2,3))]
    
    

# Driver Code
app = tkinterApp()
app.mainloop()