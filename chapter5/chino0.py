#!/usr/bin/env python
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L")
    grayImage = grayImage.resize((8,8), PIL.Image.Resampling.LANCZOS)
    displImage = PIL.ImageTk.PhotoImage(grayImage.resize((300, 300), resample=0))
    imageLabel.configure(image = displImage)
    imageLabel.image = displImage

def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        data = imageToData(fpath)

root = tk.Tk()
root.geometry("400x400")

btn = tk.Button(root, text = "open an image file", command = openFile)
imageLabel = tk.Label()

btn.pack()
imageLabel.pack()

tk.mainloop()