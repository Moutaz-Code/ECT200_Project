import tkinter as tk
from tkinter import ttk
import calendar

def calculate_cost(base_fare, distance, rate_per_km, class_premium, time_of_booking_factor, demand_factor, additional_services, age_factor, destinations, dates):
    cost = base_fare + distance * rate_per_km + class_premium + time_of_booking_factor + demand_factor + additional_services + age_factor
    for destination, date in zip(destinations, dates):
        cost += destination_premiums[destination] + time_of_booking_factors[date.month]
    return cost

def display_cost(cost):
    result_label.config(text="The estimated cost of the ticket is: $" + str(cost))

def get_inputs():
    base_fare = float(base_fare_entry.get())
    distance = float(distance_entry.get())
    rate_per_km = float(rate_per_km_entry.get())
    class_premium = float(class_premium_entry.get())
    time_of_booking_factor = float(time_of_booking_factor_entry.get())
    demand_factor = float(demand_factor_entry.get())
    additional_services = float(additional_services_entry.get())
    age_factor = float(age_factor_entry.get())
    destinations = [city_var.get() for city_var in city_vars]
    dates = [return_date_var.get(), departure_date_var.get()] + [city_date_var.get() for city_date_var in city_date_vars]
    cost = calculate_cost(base_fare, distance, rate_per_km, class_premium, time_of_booking_factor, demand_factor, additional_services, age_factor, destinations, dates)
    display_cost(cost)

app = tk.Tk()
app.title("Airplane Ticket Cost Calculator")
app.geometry("800x800")

# Base Fare
base_fare_label = ttk.Label(app, text="Base Fare:")
base_fare_label.grid(row=0, column=0)

base_fare_entry = ttk.Entry(app)
base_fare_entry.grid(row=0, column=1)

# Distance
distance_label = ttk.Label(app, text="Distance:")
distance_label.grid(row=1, column=0)

distance_entry = ttk.Entry(app)
distance_entry.grid(row=1, column=1)

# Rate per KM
rate_per_km_label = ttk.Label(app, text="Rate per KM:")
rate_per_km_label.grid(row=2, column=0)

rate_per_km_entry = ttk.Entry(app)
rate_per_km_entry.grid(row=2, column=1)

additional_services_label = ttk.Label(app, text="Additional Services:")
additional_services_label.pack()

additional_services_entry = ttk.Entry(app)
additional_services_entry.pack()

age_factor_label = ttk.Label(app, text="Age Factor:")
age_factor_label.pack()

age_factor_entry = ttk.Entry(app)
age_factor_entry.pack()

departure_date_label = ttk.Label(app, text="Departure Date:")
departure_date_label.pack()

departure_date_entry = ttk.Entry(app)
departure_date_entry.pack()

return_date_label = ttk.Label(app, text="Return Date:")
return_date_label.pack()

return_date_entry = ttk.Entry(app)
return_date_entry.pack()

destination_list_label = ttk.Label(app, text="Destination List:")
destination_list_label.pack()

destination_list_entry = ttk.Entry(app)
destination_list_entry.pack()

destination_dates_label = ttk.Label(app, text="Destination Dates:")
destination_dates_label.pack()

destination_dates_entry = ttk.Entry(app)
destination_dates_entry.pack()

result_label = ttk.Label(app)
result_label.pack()

calculate_button = ttk.Button(app, text="Calculate", command=get_inputs)
calculate_button.pack()

app.mainloop()