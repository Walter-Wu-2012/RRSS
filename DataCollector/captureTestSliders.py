# Import required Libraries
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
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
        label0 =tk.Label(self, text="Stress",font=SMALLFONT)
        label1 =tk.Label(self, text="Chaotic",font=SMALLFONT)
        label2 =tk.Label(self, text="Happiness",font=SMALLFONT)
        label3 =tk.Label(self, text="Energy",font=SMALLFONT)
        label4 =tk.Label(self, text="Focus",font=SMALLFONT)
        label0.grid(row = 0, column = 0, padx = 10, pady = 10)
        label1.grid(row = 1, column = 0, padx = 10, pady = 10)
        label2.grid(row = 2, column = 0, padx = 10, pady = 10)
        label3.grid(row = 3, column = 0, padx = 10, pady = 10)
        label4.grid(row = 4, column = 0, padx = 10, pady = 10)

        finishButton = tk.Button(self, text="Done", font=SMALLFONT, command=lambda: finishCommand())
        finishButton.grid(row=5,column=2, columnspan=2)
        current_value = tk.DoubleVar()
        slider = tk.ttk.Scale(
            self,
            from_=0,
            to=100,
            orient='horizontal',
            variable=current_value
        )
        slider.grid(row = 0,column = 1, padx = 10, pady =10)
        def finishCommand():
            file = open(self.textFilename,'a')
            file.write("Hello \n")
            file.close()
            self.destroy()
# Not used 
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
            self.title('Data Collection')
            self.textFilename = "text.txt"
            # label =tk.Label(self, text="Press if you dont know what to do")
            # label.pack()

            # face detector
            self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

            # def update():
            #     label.config(text=texts[random.randint(0,3)])
            # button = tk.Button(self, text="Button",command=lambda: update())
            # button.pack()
            # texts = ["Oh ok","What","Happy new year","stop pressing already"]

            #self.timeCounter=self.Counter(mainTk = self, increment = 10) # 600 for 10 minutes

            self.protocol("WM_DELETE_WINDOW",lambda: on_closing())

            self.timeLabel = tk.Label(self, text="Current Time: --------------",font=SMALLFONT)

            self.timeLabel.grid(row=0,column=0)
            label0 =tk.Label(self, text="Stress",font=SMALLFONT)
            label1 =tk.Label(self, text="Chaotic",font=SMALLFONT)
            label2 =tk.Label(self, text="Happiness",font=SMALLFONT)
            label3 =tk.Label(self, text="Energy",font=SMALLFONT)
            label4 =tk.Label(self, text="Focus",font=SMALLFONT)
            label0.grid(row = 1, column = 0, padx = 10, pady = 10)
            label1.grid(row = 2, column = 0, padx = 10, pady = 10)
            label2.grid(row = 3, column = 0, padx = 10, pady = 10)
            label3.grid(row = 4, column = 0, padx = 10, pady = 10)
            label4.grid(row = 5, column = 0, padx = 10, pady = 10)

            finishButton = tk.Button(self, text="Done", font=SMALLFONT, command=lambda: finishCommand())
            finishButton.grid(row=6,column=2, columnspan=2)
            self.current_value0 = tk.DoubleVar()
            self.current_value1 = tk.DoubleVar()
            self.current_value2 = tk.DoubleVar()
            self.current_value3 = tk.DoubleVar()
            self.current_value4 = tk.DoubleVar()
            self.current_values = [self.current_value0,self.current_value1,self.current_value2,self.current_value3,self.current_value4]
            slider0 = tk.Scale(self,from_=-1,to=1,resolution=0.1,length=200,width=10,
                orient='horizontal',variable=self.current_value0,command=self.slider_scroll)
            slider1 = tk.Scale(self,from_=-1,to=1,resolution=0.1,length=200,width=10,
                orient='horizontal',variable=self.current_value1,command=self.slider_scroll)
            slider2 = tk.Scale(self,from_=-1,to=1,resolution=0.1,length=200,width=10,
                orient='horizontal',variable=self.current_value2,command=self.slider_scroll)
            slider3 = tk.Scale(self,from_=-1,to=1,resolution=0.1,length=200,width=10,
                orient='horizontal',variable=self.current_value3,command=self.slider_scroll)
            slider4 = tk.Scale(self,from_=-1,to=1,resolution=0.1,length=200,width=10,
                orient='horizontal',variable=self.current_value4,command=self.slider_scroll)

            slider0.grid(row = 1,column = 1, padx = 10, pady =10)
            slider1.grid(row = 2,column = 1, padx = 10, pady =10)
            slider2.grid(row = 3,column = 1, padx = 10, pady =10)
            slider3.grid(row = 4,column = 1, padx = 10, pady =10)
            slider4.grid(row = 5,column = 1, padx = 10, pady =10)


            finishButton = tk.Button(self, text="Done", font=SMALLFONT, command=lambda: finishCommand())
            finishButton.grid(row=6,column=2, columnspan=2)



            # time counter part
            self.next_t = time.time()
            self.i=0
            self.done=False
            self.increment = 30*60 # set timer here
            self.t = time.localtime()
            self.filename = f"{self.t.tm_year:04}{self.t.tm_mon:02}{self.t.tm_mday:02}{self.t.tm_hour:02}{self.t.tm_min:02}{self.t.tm_sec:02}"
            print(f'Starting time: {self.t.tm_hour:02}:{self.t.tm_min:02}:{self.t.tm_sec:02}')
            self.textFilename = f"moodIndex{self.filename}.txt"
            self._run()

            
            def finishCommand():
                file = open('capturedImage/'+self.textFilename,'a')
                outputString = ''
                for current_value in self.current_values:
                    print(current_value.get())
                    outputString += str(current_value.get())+' '
                file.write(f'{self.filename}: {outputString}\n')
                file.close()
                for current_value in self.current_values:
                    current_value.set(0)
                messagebox.showinfo(title='Data Registered',message="Successfully retrieve data")
                return

            def on_closing():
                if messagebox.askokcancel("Quit", "Do you want to quit?"):
                    self.destroy()
                    self.currTimer.cancel()
                    sys.exit()
            


    def slider_scroll(self, event=None):
        return

    def _run(self):
            self.t = time.localtime()
            self.filename = f"{self.t.tm_year:04}{self.t.tm_mon:02}{self.t.tm_mday:02}{self.t.tm_hour:02}{self.t.tm_min:02}{self.t.tm_sec:02}"
            print(f'Capture time: {self.t.tm_hour:02}:{self.t.tm_min:02}:{self.t.tm_sec:02}')
            # saving image
            cam = cv2.VideoCapture(0)   # 0 -> index of camera
            s, img = cam.read()
            if s:
                faces = self.face_cascade.detectMultiScale(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), 1.1, 4)
                if len(faces)==1:
                    cv2.imwrite("capturedImage/"+self.filename+".jpg",img)
                    self.timeLabel.config(text="Latest Image Time: "+ self.filename)
                    messagebox.showinfo("New Capture","Please give info about mood index")
                    self.next_t+=self.increment
                else:
                    messagebox.showinfo("Face not found","Please take a picture again")
                    self.next_t+=5
            
            
            # create popup to tell user
            
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
 







