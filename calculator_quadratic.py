import math, sys, webbrowser
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("Quadratic calculator")

bttn_list = [
                "Run", "Exit"
            ]

r = 1
c = 0

for i in bttn_list:
    rel = ""
    cmd = lambda x=i: calc(x)
    ttk.Button(root, text=i, command=cmd, width=10).grid(row=r, column=c)
    c += 1

calc_entry = Entry(root, width = 30)
calc_entry.grid(row=0, column=0, columnspan=5)

label = tk.Label(root, text="Корни будут равны")
label.grid(row=4, column=0, columnspan=5)

def calc():
    try:
        a = int(calc_entry.get())
        b = int(calc_entry.get())
        c = int(calc_entry.get())
        
        D = b**2 - 4*a*c
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)

        label.config(text="Корни будут равны {}".format(x1, x2))
    except ValueError:
        label.config(text="Ошибка, введите цифры")

root.mainloop()