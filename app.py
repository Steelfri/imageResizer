import tkinter as tk 
import PySimpleGUI as sg
from tkinter import filedialog, Text
from PIL import Image, ImageTk
import os

def openimage():
	photo = filedialog.askopenfilename(initialdir="/", title="Select image to resize",
										 filetypes=(("steelfri.fr", "*.png"), ("all files", "*.*")))

root = tk.Tk(className="ImageResizer")
root.geometry("500x500")

def Take_input():
    heightt = inputtxt.get("1.0", "end-1c")
  
h = tk.Label(text = "Height :")
input1 = tk.Text(root, height = 1,
                width = 20,
                bg = "light yellow")

w = tk.Label(text = "Width :")
input2 = tk.Text(root, height = 1,
                width = 20,
                bg = "light yellow")

heightsave = input1.get(0)
widthsave = input2.get(0)

def savesize():
	print(heightsave)
	print(widthsave)
	
Done = tk.Button(root, text="Done",
 				padx=10, pady=5,
  				fg="white", bg="#000001",
  				command=savesize)


h.pack()
input1.pack()
w.pack()
input2.pack()
Done.pack()

root.iconbitmap(r"C:\Users\assis\Desktop\SteelfriLauncher\assets\logo.ico")

chooseImage = tk.Button(root, text="Choose Image", padx=10, pady=5, fg="white", bg="#000001", command=openimage)
chooseImage.pack()

root.mainloop()	

