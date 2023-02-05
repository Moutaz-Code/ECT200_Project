from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook, Style
import tkinter.font as font
from tkinter.messagebox import showinfo
from math import *
import random as rand
from calendar import month_name
from datetime import datetime

import os
os.system('cls')

# Create root window
root = Tk()
root.configure(background='DimGray')
root.title("Airline Ticket Booking System")
root.geometry('700x600')
# root.state('zoomed')

# Define colors
OriginCol = "#CBDDF6"
SelecCol = "#8ab3e6"

# Style the tabs
style = Style()
style.theme_create("TabbyStyle", parent="alt", settings={"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0]}}, "TNotebook.Tab": {"configure": {
                   "padding": [50, 10], "background": OriginCol}, "map": {"background": [("selected", SelecCol)], "expand": [("selected", [1, 1, 1, 0])]}}})
style.theme_use("TabbyStyle")

# Self explanatory...
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# create a notebook
notebook = ttk.Notebook(root, width=screen_width, height=screen_height)
notebook.pack(fill=BOTH, expand=True)

# create main frames of each tab
frame1 = ttk.Frame(notebook, width=screen_width, height=screen_height)
frame2 = ttk.Frame(notebook, width=screen_width, height=screen_height)
frame3 = ttk.Frame(notebook, width=screen_width, height=screen_height)

# frames in tab 1
frameText1 = ttk.Frame(frame1)
# change width and relief later on, use for now to make organising easier
frameText1['borderwidth'] = 5
frameText1['relief'] = 'sunken'
frameText1.pack()

# frames in tab 2
frameText2 = ttk.Frame(frame2)
# change width and relief later on, use for now to make organising easier
frameText2['borderwidth'] = 5
frameText2['relief'] = 'sunken'
frameText2.pack()

# frames in tab 3
frameText3 = ttk.Frame(frame3)
# change width and relief later on, use for now to make organising easier
frameText3['borderwidth'] = 5
frameText3['relief'] = 'sunken'
frameText3.pack()

# labels for reference
label1 = ttk.Label(frameText1, text="bruh")
label2 = ttk.Label(frameText2, text="bruh The sequel")
label3 = ttk.Label(frameText3, text="bruh The Prequel")

label1.pack(fill='both', expand=True)
label2.pack(fill='both', expand=True)
label3.pack(fill='both', expand=True)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)

# add frames to notebook i.e. tabs
notebook.add(frame1, text='Book')
notebook.add(frame2, text='Manage')
notebook.add(frame3, text='Status')

"""
rootFrame = ttk.Frame(root, padding="5 5 15 15")
rootFrame.grid(column=0, row=0, sticky=(N, W, E, S))
"""

root.mainloop()
