from tkinter import *
from time import strftime

class DigitalClock:
    def __init__(self):
        self.root = Tk()
        self.root.title("Digital Clock")
        self.root.resizable(False, False)
        self.root.geometry("420x180+500+200")
        self.root.configure(bg="SpringGreen")
        self.label = Label(self.root,font=("arial", 40, "bold"), bg="SpringGreen3", fg="purple4",width=10,height=1)
        self.label.place(x=50,y=50)

        self.update_time()
        self.root.mainloop()

    def update_time(self):
        current_time = strftime('%I:%M:%S %p')
        self.label.config(text=current_time)
        self.label.after(1000, self.update_time)

clock = DigitalClock()

