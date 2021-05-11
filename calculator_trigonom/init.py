"""
Created by Limon250
Date: 10.04.2021
Version 1.0
Python version 3.8.7 64-bit
"""

import sys
import math
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Trigonometric calculator")

bttn_list = [
                "sin", "cos", "tan", "ctg", "0", "30", "45", "60",
                "90", "120", "135", "150", "180", "210", "225",
                "240", "270", "300", "315", "330", "360", "=", "C",
                "Exit"
            ]
r = 1
c = 0

for i in bttn_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd, width=10).grid(row=r, column=c)
    c += 1
    if c > 3:
        c = 0
        r += 1

calc_entry = Entry(root, width=25)
calc_entry.grid(row=8, column=2, columnspan=5)

label = tk.Label(root, text="Результат: ")
label.grid(row=8, column=0, columnspan=3)

label1 = tk.Label(root, text="Не вводите ничего в поле!")
label1.grid(row=9, column=0, columnspan=3)

def calc(key):
    if key == "C":
        calc_entry.delete(0, END)
    elif key == "sin":
        calc_entry.insert(END, str("sin"))   
        func1(key)
    elif key == "cos":
        calc_entry.insert(END, str("cos"))
        func2()
    elif key == "tan":
        calc_entry.insert(END, str("tan"))
        func3()
    elif key == "ctg":
        calc_entry.insert(END, str("ctg"))
        func4()
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)
    
def func1(key):
    if key == "0":
        calc_entry.insert(END + str("0"))
    elif key == "30":
        calc_entry.insert(END + str("1/2"))

def func2(key):
    pass

def func3(key):
    pass

def func4(key):
    pass

def GH():
    webbrowser.open("https://github.com/Limon250/calc1.0.git")

def Inst():
    webbrowser.open("https://www.instagram.com/llsinnerll_/")

def gl():
    messagebox.showinfo("e-mail", "limon2502003@gmail.com")

def tg():
    messagebox.showinfo("Telegram", "@Ggwpdwp")

m = Menu(root)
root.config(menu = m)

m1 = Menu(m)
m.add_cascade(label = "Contact Me!", menu=m1)
m1.add_command(label = "Instagramm", command=Inst)
m1.add_command(label = "Gmail", command=gl)
m1.add_command(label = "Telegram", command=tg)

m2 = Menu(m)
m.add_cascade(label = "Source Code", menu=m2)
m2.add_command(label = "Open", command=GH)

root.mainloop()