import tkinter as tk
import tkinter.ttk as ttk
from appGui import StudentlistingWidget
from scripts import Scripts

class Application():
    def __init__(self, master):
        base = Scripts(master)
        base.pack()
        master.mainloop()

if __name__ == "__main__":
    window = tk.Tk()
    window.geometry("1000x600")
    window.title("Student List Manipulator")
    app = Application(window)