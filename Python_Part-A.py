from tkinter import *
from tkinter import ttk 
from math import *
import random as rand
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

window = Tk()
window.title("Feet to Meters")

windowFrame = ttk.Frame(window, padding="5 5 15 15")
windowFrame.grid(column=0, row=0, sticky=(N, W, E, S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

feet = StringVar() 
feet_entry = ttk.Entry(windowFrame, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
ttk.Label(windowFrame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(windowFrame, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(windowFrame, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(windowFrame, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(windowFrame, text="meters").grid(column=3, row=2, sticky=W)

for child in windowFrame.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
window.bind("<Return>", calculate)

window.mainloop()