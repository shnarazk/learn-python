#!/usr/bin/env python
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def dispPhoto(path):
    newImage = PIL.Image.open(path).resize((300, 300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)

root = tk.Tk()
root.geometry("300x300")
btn = tk.Button(text = "open file", command = openFile)
imageLabel = tk.Label()
btn.pack()
imageLabel.pack()
tk.mainloop() 
