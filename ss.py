import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root = tk.Tk()
canvas1 = tk.Canvas(root, width=300, height=300, bg="blue")
canvas1.pack()


def takeScreenshot():
    myscreenshot = pyautogui.screenshot()
    save_path = asksaveasfilename()
    myscreenshot.save(save_path+ "ss.png")


myButton =tk.Button(text="Take Screenshot" , command=takeScreenshot, font=10, bg="white", fg="black")
canvas1.create_window(150,150,window=myButton)


mainloop()