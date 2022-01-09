# Import required Libraries
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import LEFT, RIGHT
from PIL import Image, ImageTk
import cv2
import threading
import time
from datetime import datetime,timedelta
import random
import sys

LARGEFONT =("Verdana", 35)
NORMALFONT =("Verdana", 20)
SMALLFONT = ("Verdana", 13)  



# Not used
class MoodAsker(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # print(str(self.winfo_rootx())+' '+str(self.winfo_rooty())) # location to place the popup
        self.geometry("700x350")
        buttonValue= [["OFF", "OFF", "OFF"],["OFF", "OFF", "OFF"],["OFF", "OFF", "OFF"],["OFF", "OFF", "OFF"],["OFF", "OFF", "OFF"]]
        label0 =tk.Label(self, text="Stress",font=SMALLFONT)
        mood0button0 = tk.Button(self, text="LOW", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(0,0))
        mood0button1 = tk.Button(self, text="NORMAL", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(0,1))
        mood0button2 = tk.Button(self, text="HIGH", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(0,2))
        label1 =tk.Label(self, text="Chaotic",font=SMALLFONT)
        mood1button0 = tk.Button(self, text="LOW", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(1,0))
        mood1button1 = tk.Button(self, text="NORMAL", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(1,1))
        mood1button2 = tk.Button(self, text="HIGH", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(1,2))
        label2 =tk.Label(self, text="Happiness",font=SMALLFONT)
        mood2button0 = tk.Button(self, text="LOW", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(2,0))
        mood2button1 = tk.Button(self, text="NORMAL", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(2,1))
        mood2button2 = tk.Button(self, text="HIGH", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(2,2))
        label3 =tk.Label(self, text="Energy",font=SMALLFONT)
        mood3button0 = tk.Button(self, text="LOW", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(3,0))
        mood3button1 = tk.Button(self, text="NORMAL", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(3,1))
        mood3button2 = tk.Button(self, text="HIGH", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(3,2))
        label4 =tk.Label(self, text="Focus",font=SMALLFONT)
        mood4button0 = tk.Button(self, text="LOW", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(4,0))
        mood4button1 = tk.Button(self, text="NORMAL", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(4,1))
        mood4button2 = tk.Button(self, text="HIGH", font=SMALLFONT, bg='red',fg='white', command=lambda: buttonToggle(4,2))
        label0.grid(row = 0, column = 0, padx = 10, pady = 10)
        mood0button0.grid(row = 0, column = 1, padx = 10, pady = 10)
        mood0button1.grid(row = 0, column = 2, padx = 10, pady = 10)
        mood0button2.grid(row = 0, column = 3, padx = 10, pady = 10)
        label1.grid(row = 1, column = 0, padx = 10, pady = 10)
        mood1button0.grid(row = 1, column = 1, padx = 10, pady = 10)
        mood1button1.grid(row = 1, column = 2, padx = 10, pady = 10)
        mood1button2.grid(row = 1, column = 3, padx = 10, pady = 10)
        label2.grid(row = 2, column = 0, padx = 10, pady = 10)
        mood2button0.grid(row = 2, column = 1, padx = 10, pady = 10)
        mood2button1.grid(row = 2, column = 2, padx = 10, pady = 10)
        mood2button2.grid(row = 2, column = 3, padx = 10, pady = 10)
        label3.grid(row = 3, column = 0, padx = 10, pady = 10)
        mood3button0.grid(row = 3, column = 1, padx = 10, pady = 10)
        mood3button1.grid(row = 3, column = 2, padx = 10, pady = 10)
        mood3button2.grid(row = 3, column = 3, padx = 10, pady = 10)
        label4.grid(row = 4, column = 0, padx = 10, pady = 10)
        mood4button0.grid(row = 4, column = 1, padx = 10, pady = 10)
        mood4button1.grid(row = 4, column = 2, padx = 10, pady = 10)
        mood4button2.grid(row = 4, column = 3, padx = 10, pady = 10)

        everyToggleButton = [mood0button0,mood0button1,mood0button2
        ,mood1button0,mood1button1,mood1button2
        ,mood2button0,mood2button1,mood2button2
        ,mood3button0,mood3button1,mood3button2
        ,mood4button0,mood4button1,mood4button2]


        finishButton = tk.Button(self, text="Done", font=SMALLFONT, command=lambda: finishCommand())
        finishButton.grid(row=5,column=2, columnspan=2)

        def finishCommand():
            file = open(self.textFilename,'a')
            file.write("Hello \n")
            file.close()
            self.destroy()

        def buttonToggle(moodNumber,buttonNumber):
            buttonValue[moodNumber] = ["OFF", "OFF", "OFF"]
            buttonValue[moodNumber][buttonNumber] = "ON"
            print(buttonValue)
            for i in range(moodNumber*3,moodNumber*3+3):
                moodNumberToCheck = i//3
                buttonNumberToCheck = i%3
                if buttonValue[moodNumberToCheck][buttonNumberToCheck] == 'ON':
                    everyToggleButton[i].config(bg='green',fg='white')
                else:
                    everyToggleButton[i].config(bg='red',fg='white')



    
class Counter():
    def __init__(self, increment):
        self.next_t = time.time()
        self.i=0
        self.done=False
        self.increment = increment
        self.t = time.localtime()
        self.filename = f"{self.t.tm_year:04}{self.t.tm_mon:02}{self.t.tm_mday:02}{self.t.tm_hour:02}{self.t.tm_min:02}{self.t.tm_sec:02}"
        print(f'Starting time: {self.t.tm_hour:02}:{self.t.tm_min:02}:{self.t.tm_sec:02}')
        self.textFilename = f"moodIndex{self.filename}.txt"
        file = open(self.textFilename,'a')
        file.close()
        self._run()

    def _run(self):
        self.t = time.localtime()
        self.filename = f"{self.t.tm_year:04}{self.t.tm_mon:02}{self.t.tm_mday:02}{self.t.tm_hour:02}{self.t.tm_min:02}{self.t.tm_sec:02}"
        print(f'Capture time: {self.t.tm_hour:02}:{self.t.tm_min:02}:{self.t.tm_sec:02}')
        # saving image
        cam = cv2.VideoCapture(0)   # 0 -> index of camera
        s, img = cam.read()
        if s: 
            cv2.imwrite("capturedImage2/"+self.filename+".jpg",img)
        self.next_t+=self.increment
        self.i+=1
        if not self.done:
            self.currTimer = threading.Timer( self.next_t - time.time(), self._run)
            self.currTimer.start()
    
    def stop(self):
        self.done=True
        

class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
            
            # __init__ function for class Tk
            tk.Tk.__init__(self, *args, **kwargs)
            # Set the size of the window
            self.geometry("700x350")
            self.title('Get Picture')
            self.textFilename = "text.txt"
            # label =tk.Label(self, text="Press if you dont know what to do")
            # label.pack()

            # def update():
            #     label.config(text=texts[random.randint(0,3)])
            # button = tk.Button(self, text="Button",command=lambda: update())
            # button.pack()
            # texts = ["Oh ok","What","Happy new year","stop pressing already"]

            #self.timeCounter=self.Counter(mainTk = self, increment = 10) # 600 for 10 minutes

            self.protocol("WM_DELETE_WINDOW",lambda: on_closing())

            self.timeLabel = tk.Label(self, text="Current Time: --------------",font=SMALLFONT)

            self.buttonValue= [["OFF", "OFF", "OFF"],["OFF", "OFF", "OFF"],["OFF", "OFF", "OFF"],["OFF", "OFF", "OFF"],["OFF", "OFF", "OFF"]]
            label0 =tk.Label(self, text="Stress",font=SMALLFONT)
            mood0button0 = tk.Button(self, text="LOW", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(0,0))
            mood0button1 = tk.Button(self, text="NORMAL", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(0,1))
            mood0button2 = tk.Button(self, text="HIGH", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(0,2))
            label1 =tk.Label(self, text="Chaotic",font=SMALLFONT)
            mood1button0 = tk.Button(self, text="LOW", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(1,0))
            mood1button1 = tk.Button(self, text="NORMAL", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(1,1))
            mood1button2 = tk.Button(self, text="HIGH", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(1,2))
            label2 =tk.Label(self, text="Happiness",font=SMALLFONT)
            mood2button0 = tk.Button(self, text="LOW", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(2,0))
            mood2button1 = tk.Button(self, text="NORMAL", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(2,1))
            mood2button2 = tk.Button(self, text="HIGH", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(2,2))
            label3 =tk.Label(self, text="Energy",font=SMALLFONT)
            mood3button0 = tk.Button(self, text="LOW", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(3,0))
            mood3button1 = tk.Button(self, text="NORMAL", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(3,1))
            mood3button2 = tk.Button(self, text="HIGH", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(3,2))
            label4 =tk.Label(self, text="Focus",font=SMALLFONT)
            mood4button0 = tk.Button(self, text="LOW", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(4,0))
            mood4button1 = tk.Button(self, text="NORMAL", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(4,1))
            mood4button2 = tk.Button(self, text="HIGH", font=SMALLFONT, bg='white',fg='black', command=lambda: buttonToggle(4,2))
            self.timeLabel.grid(row=0,column=0)
            label0.grid(row = 1, column = 0, padx = 10, pady = 10)
            mood0button0.grid(row = 1, column = 1, padx = 10, pady = 10)
            mood0button1.grid(row = 1, column = 2, padx = 10, pady = 10)
            mood0button2.grid(row = 1, column = 3, padx = 10, pady = 10)
            label1.grid(row = 2, column = 0, padx = 10, pady = 10)
            mood1button0.grid(row = 2, column = 1, padx = 10, pady = 10)
            mood1button1.grid(row = 2, column = 2, padx = 10, pady = 10)
            mood1button2.grid(row = 2, column = 3, padx = 10, pady = 10)
            label2.grid(row = 3, column = 0, padx = 10, pady = 10)
            mood2button0.grid(row = 3, column = 1, padx = 10, pady = 10)
            mood2button1.grid(row = 3, column = 2, padx = 10, pady = 10)
            mood2button2.grid(row = 3, column = 3, padx = 10, pady = 10)
            label3.grid(row = 4, column = 0, padx = 10, pady = 10)
            mood3button0.grid(row = 4, column = 1, padx = 10, pady = 10)
            mood3button1.grid(row = 4, column = 2, padx = 10, pady = 10)
            mood3button2.grid(row = 4, column = 3, padx = 10, pady = 10)
            label4.grid(row = 5, column = 0, padx = 10, pady = 10)
            mood4button0.grid(row = 5, column = 1, padx = 10, pady = 10)
            mood4button1.grid(row = 5, column = 2, padx = 10, pady = 10)
            mood4button2.grid(row = 5, column = 3, padx = 10, pady = 10)


            everyToggleButton = [mood0button0,mood0button1,mood0button2
            ,mood1button0,mood1button1,mood1button2
            ,mood2button0,mood2button1,mood2button2
            ,mood3button0,mood3button1,mood3button2
            ,mood4button0,mood4button1,mood4button2]


            finishButton = tk.Button(self, text="Done", font=SMALLFONT, command=lambda: finishCommand())
            finishButton.grid(row=6,column=2, columnspan=2)



            # time counter part
            self.next_t = time.time()
            self.i=0
            self.done=False
            self.increment = 30 # set timer here
            self.t = time.localtime()
            self.filename = f"{self.t.tm_year:04}{self.t.tm_mon:02}{self.t.tm_mday:02}{self.t.tm_hour:02}{self.t.tm_min:02}{self.t.tm_sec:02}"
            print(f'Starting time: {self.t.tm_hour:02}:{self.t.tm_min:02}:{self.t.tm_sec:02}')
            self.textFilename = f"moodIndex{self.filename}.txt"
            file = open(self.textFilename,'a')
            file.close()
            self._run()

            
            def finishCommand():
                file = open('capturedImage2/'+self.textFilename,'a')
                outputString = ''
                for moodIndex in self.buttonValue:
                    if moodIndex[0]=='ON':
                        outputString+='L'
                    elif moodIndex[1]=='ON':
                        outputString+='M'
                    elif moodIndex[2]=='ON':
                        outputString+='H'
                    else:
                        outputString+='X'
                file.write(f'{self.filename}: {outputString}\n')
                file.close()
                

                #reset
                self.buttonValue= [["OFF", "OFF", "OFF"],["OFF", "OFF", "OFF"],["OFF", "OFF", "OFF"],["OFF", "OFF", "OFF"],["OFF", "OFF", "OFF"]]
                for button in everyToggleButton:
                    button.config(bg='white',fg='black')
                print(self.filename)
                messagebox.showinfo(title='Data Registered',message="Successfully retrieve data")

            def buttonToggle(moodNumber,buttonNumber):
                self.buttonValue[moodNumber] = ["OFF", "OFF", "OFF"]
                self.buttonValue[moodNumber][buttonNumber] = "ON"
                print(self.buttonValue)
                for i in range(moodNumber*3,moodNumber*3+3):
                    moodNumberToCheck = i//3
                    buttonNumberToCheck = i%3
                    if self.buttonValue[moodNumberToCheck][buttonNumberToCheck] == 'ON':
                        everyToggleButton[i].config(bg='#90EE90',fg='black')
                    else:
                        everyToggleButton[i].config(bg='white',fg='black')


            def on_closing():
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    self.destroy()
                    self.currTimer.cancel()
                    sys.exit()

    def _run(self):
            self.t = time.localtime()
            self.filename = f"{self.t.tm_year:04}{self.t.tm_mon:02}{self.t.tm_mday:02}{self.t.tm_hour:02}{self.t.tm_min:02}{self.t.tm_sec:02}"
            print(f'Capture time: {self.t.tm_hour:02}:{self.t.tm_min:02}:{self.t.tm_sec:02}')
            # saving image
            cam = cv2.VideoCapture(0)   # 0 -> index of camera
            s, img = cam.read()
            if s: 
                cv2.imwrite("capturedImage2/"+self.filename+".jpg",img)
            self.timeLabel.config(text="Latest Image Time: "+ self.filename)
            
            # create popup to tell user
            messagebox.showinfo("New Capture","Please give info about mood index")

            self.next_t+=self.increment
            self.i+=1
            if not self.done:
                self.currTimer = threading.Timer( self.next_t - time.time(), self._run)
                self.currTimer.start()

    def stop(self):
        self.done=True


            

if __name__=='__main__':
    
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        app = tkinterApp()
        app.mainloop()
    else:
        print('please check your camera')
        messagebox.showerror(title="Error", message="Camera Not Found")
 





    # Create a Label to capture the Video frames

    # cap= cv2.VideoCapture(0)

    # # Define function to show frame
    # def show_frames():
    #    cv2image= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    #    img = Image.fromarray(cv2image)
    #    imgtk = ImageTk.PhotoImage(image = img)
    #    label.imgtk = imgtk
    #    label.configure(image=imgtk)
    #    label.after(20, show_frames)

    # show_frames()


