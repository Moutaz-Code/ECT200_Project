from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook, Style
import tkinter.font as font
from tkcalendar import Calendar
from tkinter.messagebox import showinfo
from math import *
import random as rand
from calendar import month_name
from datetime import datetime

import os
os.system('cls')
##
base_fare
trip_direction = [1, 2]  # 1 or 2 ways
distance
rate_per_km
class_premium = [300, 850, 1600]  # Economy, Business, and first classes
demand_factor  # In this iteration, the multiplier should be between 0.7 and 1.4. This variable is a multiplier for days of the week, to simulate demand on a specific day which affects price.
age_factor = {
    "Adult": 200,
    "Infant": 75
}


##
tripDistance = eval(input("trip distance"))  # this is a placeholder
demandFactor = []


def bookFlightCost():
    ticketCost = (base_fare + (trip_direction*(rate_per_km*distance)
                               ) + class_premium+age_factor)*demand_factor


def Reschedule():
    # Select new date
    CostDiff = flightCost


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
# change width and relief later on, use for now to make organising easier=
frameText1.pack()

# frames in tab 2
frameText2 = ttk.Frame(frame2)
# change width and relief later on, use for now to make organising easier
frameText2.pack()

# frames in tab 3
frameText3 = ttk.Frame(frame3)
# change width and relief later on, use for now to make organising easier
frameText3.pack()

# labels for reference
label1 = ttk.Label(
    frameText1, text="Welcome to the booking tab! Here you can book a flight ticket using many options.")
label2 = ttk.Label(
    frameText2, text="Welcome to the managing tab! Here you can reschedule or cancel your ticket.")
label3 = ttk.Label(
    frameText3, text="Welcome to the status tab! Here you can check the status of your flight and ticket.")

label1.grid(column=1, row=1)
label2.grid(column=1, row=1)
label3.grid(column=1, row=1)

radio1
radio2
radio3

radio1.grid()
radio2.grid()
radio3.grid()

combobox1
combobox2

combobox1.grid()
combobox2.grid()

dropdownlist

dropdownlist.grid()

dropdownlist2
# this is for the passengers
dropdownlist2.grid()

datepicker_departure
datepicker_departure.grid()

datepicker_return
datepicker_return.grid()

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)
frame3.pack(fill='both', expand=True)

# add frames to notebook i.e. tabs
notebook.add(frame1, text='Book')
notebook.add(frame2, text='Manage')
notebook.add(frame3, text='Status')

root.mainloop()
