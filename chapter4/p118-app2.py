#!/usr/bin/env python
import tkinter as tk

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
def dispLabel():
    lbl.configure(text = "こんにちわ")

btn = tk.Button(text="PUSH", command = dispLabel)

lbl.pack()
btn.pack()
tk.mainloop()

