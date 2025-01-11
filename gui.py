# importing libraries
import tkinter as tk
from tkinter import*
from tkinter import Message, Text
import cv2
import os
import tkinter.ttk as ttk
import tkinter.font as font

window = tk.Tk()
window.title("Object_detection")
window.configure(background ='white')
window.grid_rowconfigure(0, weight = 1)
window.grid_columnconfigure(0, weight = 1)
message = tk.Label(
	window, text ="object_detection",
	bg ="green", fg = "white", width = 50,
	height = 3, font = ('times', 30, 'bold'))
	
message.place(x = 200, y = 20)






# The function below is used for checking
# whether the text below is number or not ?
def run():
    os.system('main.py')
btn = Button(window, text="Object detection", bg="black",width = 30, height = 3,fg="white",command=run)
btn.grid(column=144, row=122)

def run1():
    os.system('automated_mediaplayer.py')

btn1  = Button(window, text="Hand gesture control", bg="black",width = 30, height = 3,fg="white",command=run1)
btn1.grid(column=144, row=125)


window.mainloop()
