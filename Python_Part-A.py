from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook, Style
import tkinter.font as font
from tkinter.messagebox import showinfo
from math import *
import random as rand
import calendar
from datetime import datetime


import os
os.system('cls')

base_fare = 300.0
# trip_direction = [1, 2]  # 1 or 2 ways this should be taken care of below in tkinter radio buttons

age_factor_list = [200.0, 75.0]
# In this iteration, the multiplier should be between 0.7 and 1.4. This variable is a multiplier for days of the week, to simulate demand on a specific day which affects price.
demand_factor = float(rand.uniform(0.7, 1.4))

distance = float(rand.randint(5000, 15000))
rate_per_km = float(rand.uniform(0.1, 1))


def show_cities():
    if trip_direction_special.get() == "True":
        MultiCity1_label.grid(row=2, column=3, sticky='w', pady=2, padx=5)
        Combobox_MultiCity1.grid(row=3, column=3, pady=5, padx=5)
        ###########################################################
        MultiCity2_label.grid(row=4, column=3, sticky='w', pady=2, padx=5)
        Combobox_MultiCity2.grid(row=5, column=3, pady=5, padx=5)
        ###########################################################
        MultiCity3_label.grid(row=6, column=3, sticky='w', pady=2, padx=5)
        Combobox_MultiCity3.grid(row=7, column=3, pady=5, padx=5)
    else:
        pass


def hide_cities():
    MultiCity1_label.grid_remove()
    Combobox_MultiCity1.grid_remove()
    ###########################################################
    MultiCity2_label.grid_remove()
    Combobox_MultiCity2.grid_remove()
    ###########################################################
    MultiCity3_label.grid_remove()
    Combobox_MultiCity3.grid_remove()


def show_return_date():
    Return_Date_Day_Label.grid(row=12, column=1, sticky='w', pady=2, padx=5)
    Return_Date_Day_Entry.grid(
        row=13, column=1, sticky='w', ipadx=6, pady=5, padx=5)

    Return_Date_Month_Label.grid(row=12, column=2, sticky='w', pady=2, padx=5)
    Return_Date_Month_Entry.grid(
        row=13, column=2, sticky='w', ipadx=6, pady=5, padx=5)


def hide_return_date():
    Return_Date_Day_Label.grid_remove()
    Return_Date_Day_Entry.grid_remove()

    Return_Date_Month_Label.grid_remove()
    Return_Date_Month_Entry.grid_remove()


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
style.configure('TButton', font=('American typewriter', 14),
                background='#232323', foreground='white')


# Self explanatory...
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

##########################
trip_direction = IntVar()
trip_direction_special = StringVar()
Departure_City = StringVar()
Arrival_City = StringVar()
MultiCity1 = StringVar()
MultiCity2 = StringVar()
MultiCity3 = StringVar()
Passenger_Adult = IntVar()
Passenger_Infant = IntVar()
class_premium = StringVar()
Departure_Date_Day = StringVar()
Departure_Date_Month = StringVar()
Return_Date_Day = StringVar()
Return_Date_Month = StringVar()
##########################
TotalCost = []


def getCost():
    for i in range(int(Passenger_Adult.get())):
        if class_premium.get().lower() == "Economy Class":
            class_premium_number = 300.0
        elif class_premium.get().lower() == "Business Class":
            class_premium_number = 850.0
        else:
            class_premium_number = 1600.0

        age_factor = float(Passenger_Adult.get())
        ticketCost = (base_fare + (float(trip_direction.get())*(rate_per_km*distance)) +
                      class_premium_number+age_factor_list[1])*demand_factor
        TotalCost.append(ticketCost)

    for i in range(int(Passenger_Infant.get())):
        if class_premium.get().lower() == "Economy Class":
            class_premium_number = 300.0
        elif class_premium.get().lower() == "Business Class":
            class_premium_number = 850.0
        else:
            class_premium_number = 1600.0

        age_factor = float(Passenger_Adult.get())
        ticketCost = (base_fare + (float(trip_direction.get())*(rate_per_km*distance)) +
                      class_premium_number+age_factor_list[1])*demand_factor
        TotalCost.append(ticketCost)


# create a notebook
notebook = ttk.Notebook(root, width=screen_width, height=screen_height)
notebook.pack(fill=BOTH, expand=True)

# create main frames of each tab
BookingMainFrame = ttk.Frame(
    notebook, width=screen_width, height=screen_height)
ManagingMainFrame = ttk.Frame(
    notebook, width=screen_width, height=screen_height)
StatusMainFrame = ttk.Frame(notebook, width=screen_width, height=screen_height)

# frame 1 of 2 for text in tab 1, for text
frameText1 = ttk.Frame(BookingMainFrame)
frameText1.pack(ipady=5)
###########################################################
sep1 = ttk.Separator(BookingMainFrame, orient='horizontal')
sep1.pack(fill='x')
# frame 2 of 2 for text in tab 1, for actual work
frameBookingMenu = ttk.Frame(BookingMainFrame)
frameBookingMenu.pack()


# labels for reference
label1 = ttk.Label(
    frameText1, text="Welcome to the booking tab! Here you can book a flight ticket using many options.")

label1.grid(column=1, row=1)


one_way = ttk.Radiobutton(frameBookingMenu, text='One way',
                          value="1", variable=trip_direction, command=lambda: [hide_cities(), hide_return_date()])
two_way = ttk.Radiobutton(frameBookingMenu, text='Return',
                          value="2", variable=trip_direction, command=lambda: [hide_cities(), show_return_date()])
multi_way = ttk.Radiobutton(frameBookingMenu, text='Multi-city',
                            value="True", variable=trip_direction_special, command=lambda: [show_cities(), show_return_date()])

two_way.grid(row=1, column=1, ipady=5, sticky='w')
one_way.grid(row=1, column=2, ipady=5, sticky='w')
multi_way.grid(row=1, column=3, ipady=5, sticky='w')


departure_label = ttk.Label(frameBookingMenu, text="Flying from:")
Combobox_Departure = ttk.Combobox(
    frameBookingMenu, textvariable=Departure_City)
Combobox_Departure['values'] = ('Aarhus', 'Abadan', 'Aberdeen', 'Abu Dhabi', 'Adana', 'Adiyaman', 'Akita', 'Al Ain',
                                'Albany', 'Albuquerque ', 'Beijing', 'Beirut', 'Belfast', 'Cambrigde', 'Den Haag ', 'Derby',
                                'Dhahran', 'Doha', 'Dubai', 'Dublin', 'Glasgow', 'Hammerfest', 'Hamilton', 'Istanbul')


arrival_label = ttk.Label(frameBookingMenu, text="Flying to:")
Combobox_Arrival = ttk.Combobox(frameBookingMenu, textvariable=Arrival_City)
Combobox_Arrival['values'] = ('Aarhus', 'Abadan', 'Aberdeen', 'Abu Dhabi', 'Adana', 'Adiyaman', 'Akita', 'Al Ain',
                              'Albany', 'Albuquerque ', 'Beijing', 'Beirut', 'Belfast', 'Cambrigde', 'Den Haag ', 'Derby',
                              'Dhahran', 'Doha', 'Dubai', 'Dublin', 'Glasgow', 'Hammerfest', 'Hamilton', 'Istanbul')

departure_label.grid(row=2, column=1, sticky='w', pady=2, padx=5)
Combobox_Departure.grid(row=3, column=1, pady=5, padx=5)

arrival_label.grid(row=2, column=2, sticky='w', pady=2, padx=5)
Combobox_Arrival.grid(row=3, column=2, pady=5, padx=5)
###############################################


MultiCity1_label = ttk.Label(frameBookingMenu, text="City #2:")
Combobox_MultiCity1 = ttk.Combobox(
    frameBookingMenu, textvariable=MultiCity1)
Combobox_MultiCity1['values'] = ('Aarhus', 'Abadan', 'Aberdeen', 'Abu Dhabi', 'Adana', 'Adiyaman', 'Akita', 'Al Ain',
                                 'Albany', 'Albuquerque ', 'Beijing', 'Beirut', 'Belfast', 'Cambrigde', 'Den Haag ', 'Derby',
                                 'Dhahran', 'Doha', 'Dubai', 'Dublin', 'Glasgow', 'Hammerfest', 'Hamilton', 'Istanbul')


MultiCity2_label = ttk.Label(frameBookingMenu, text="City #3:")
Combobox_MultiCity2 = ttk.Combobox(
    frameBookingMenu, textvariable=MultiCity2)
Combobox_MultiCity2['values'] = ('Aarhus', 'Abadan', 'Aberdeen', 'Abu Dhabi', 'Adana', 'Adiyaman', 'Akita', 'Al Ain',
                                 'Albany', 'Albuquerque ', 'Beijing', 'Beirut', 'Belfast', 'Cambrigde', 'Den Haag ', 'Derby',
                                 'Dhahran', 'Doha', 'Dubai', 'Dublin', 'Glasgow', 'Hammerfest', 'Hamilton', 'Istanbul')


MultiCity3_label = ttk.Label(frameBookingMenu, text="City #4:")
Combobox_MultiCity3 = ttk.Combobox(
    frameBookingMenu, textvariable=MultiCity3)
Combobox_MultiCity3['values'] = ('Aarhus', 'Abadan', 'Aberdeen', 'Abu Dhabi', 'Adana', 'Adiyaman', 'Akita', 'Al Ain',
                                 'Albany', 'Albuquerque ', 'Beijing', 'Beirut', 'Belfast', 'Cambrigde', 'Den Haag ', 'Derby',
                                 'Dhahran', 'Doha', 'Dubai', 'Dublin', 'Glasgow', 'Hammerfest', 'Hamilton', 'Istanbul')


###############################################


Passenger_Adult_Tkinter = ttk.Spinbox(
    frameBookingMenu, from_=1, to=9, textvariable=Passenger_Adult)
PassengerAdult_label = ttk.Label(
    frameBookingMenu, text="# of Adult Passengers:")

PassengerAdult_label.grid(row=4, column=1, sticky='w', pady=2, padx=5)
Passenger_Adult_Tkinter.grid(row=5, column=1, pady=5, padx=5)


Passenger_Infant_Tkinter = ttk.Spinbox(
    frameBookingMenu, from_=1, to=9, textvariable=Passenger_Infant)
PassengerInfant_label = ttk.Label(
    frameBookingMenu, text="# of Infant Passengers:")

PassengerInfant_label.grid(row=4, column=2, sticky='w', pady=2, padx=5)
Passenger_Infant_Tkinter.grid(row=5, column=2, pady=5, padx=5)


Combobox_Cabin_Class = ttk.Combobox(
    frameBookingMenu, textvariable=class_premium)
Combobox_Cabin_Class['values'] = [
    "Economy Class", "Business Class", "First Class"]
Combobox_Cabin_Class.grid(row=7, column=1, pady=5, padx=5)

Cabin_Class_Label = ttk.Label(frameBookingMenu, text="Choose Cabin Class")
Cabin_Class_Label.grid(row=6, column=1, sticky='w', pady=5, padx=5)


sep2 = ttk.Separator(frameBookingMenu, orient='horizontal')
sep2.grid(row=8, column=1, sticky='WE', columnspan=2)

# This next part was painful, tkcalendar is not working and it is 6am.

Departure_Date_Day_Entry = ttk.Entry(
    frameBookingMenu, textvariable=Departure_Date_Day)
Departure_Date_Day_Label = ttk.Label(
    frameBookingMenu, text="Enter Day of Departure: ")


Departure_Date_Month_Entry = ttk.Entry(
    frameBookingMenu, textvariable=Departure_Date_Month)
Departure_Date_Month_Label = ttk.Label(
    frameBookingMenu, text="Enter Month of Departure: ")


Return_Date_Day_Entry = ttk.Entry(
    frameBookingMenu, textvariable=Return_Date_Day)
Return_Date_Day_Label = ttk.Label(
    frameBookingMenu, text="Enter Day of Return: ")


Return_Date_Month_Entry = ttk.Entry(
    frameBookingMenu, textvariable=Return_Date_Month)
Return_Date_Month_Label = ttk.Label(
    frameBookingMenu, text="Enter Month of Return: ")

Departure_Date_Day_Label.grid(row=9, column=1, sticky='w', pady=2, padx=5)
Departure_Date_Day_Entry.grid(
    row=10, column=1, sticky='w', ipadx=6, pady=5, padx=5)

Departure_Date_Month_Label.grid(row=9, column=2, sticky='w', pady=2, padx=5)
Departure_Date_Month_Entry.grid(
    row=10, column=2, sticky='w', ipadx=6, pady=5, padx=5)

Return_Date_Day_Label.grid(row=11, column=1, sticky='w', pady=2, padx=5)
Return_Date_Day_Entry.grid(
    row=12, column=1, sticky='w', ipadx=6, pady=5, padx=5)

Return_Date_Month_Label.grid(row=11, column=2, sticky='w', pady=2, padx=5)
Return_Date_Month_Entry.grid(
    row=12, column=2, sticky='w', ipadx=6, pady=5, padx=5)


calcButton = Button(frameBookingMenu, text="Calculate", command=getCost())
calcButton.grid(row=20, column=2, sticky='s')
calcButton.config(bg="lightgray", fg="white")


# frame 1 of 2 for text in tab 2, for text
frameText2 = ttk.Frame(ManagingMainFrame)
frameText2.pack()
# frame 2 of 2 for text in tab 2, for actual work
frameManagingMenu = ttk.Frame(ManagingMainFrame)
frameManagingMenu.pack()

# frame 1 of 2 for text in tab 3, for text
frameText3 = ttk.Frame(StatusMainFrame)
frameText3.pack()
# frame 2 of 2 for text in tab 3, for actual work
frameStatusMenu = ttk.Frame(StatusMainFrame)
frameStatusMenu.pack()
label2 = ttk.Label(
    frameText2, text="Welcome to the managing tab! Here you can reschedule or cancel your ticket.")
label3 = ttk.Label(
    frameText3, text="Welcome to the status tab! Here you can check the status of your flight and ticket.")

label2.grid(column=1, row=1)
label3.grid(column=1, row=1)

BookingMainFrame.pack(fill='both', expand=True)
ManagingMainFrame.pack(fill='both', expand=True)
StatusMainFrame.pack(fill='both', expand=True)

# add frames to notebook i.e. tabs
notebook.add(BookingMainFrame, text='Book')
notebook.add(ManagingMainFrame, text='Manage')
notebook.add(StatusMainFrame, text='Status')

root.mainloop()
