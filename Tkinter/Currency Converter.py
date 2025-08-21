import tkinter as tk
from tkinter import ttk
import requests

# Function to fetch exchange rates
def get_exchange_rate(from_currency, to_currency):
    api_key = "80c3767b7a23fbbcec1258db"  # Replace with your API key
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        exchange_rate = data['conversion_rates'].get(to_currency)
        return exchange_rate
    else:
        return None

# Function to perform currency conversion
def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_var.get()
    to_currency = to_currency_var.get()
    
    exchange_rate = get_exchange_rate(from_currency, to_currency)
    
    if exchange_rate:
        converted_amount = amount * exchange_rate
        result_label.config(text=f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        result_label.config(text="Error: Unable to fetch exchange rate")

# Set up the main application window
app = tk.Tk()
app.title("Currency Converter")

# Amount entry
amount_label = tk.Label(app, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry = tk.Entry(app)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

# From currency dropdown
from_currency_var = tk.StringVar(app)
from_currency_var.set("USD")  # Default value
from_currency_label = tk.Label(app, text="From:")
from_currency_label.grid(row=1, column=0, padx=10, pady=10)
from_currency_dropdown = ttk.Combobox(app, textvariable=from_currency_var, values=["USD", "EUR", "GBP", "INR", "JPY", "CAD"],state="readonly")
from_currency_dropdown.grid(row=1, column=1, padx=10, pady=10)

# To currency dropdown
to_currency_var = tk.StringVar(app)
to_currency_var.set("EUR")  # Default value
to_currency_label = tk.Label(app, text="To:")
to_currency_label.grid(row=2, column=0, padx=10, pady=10)
to_currency_dropdown = ttk.Combobox(app, textvariable=to_currency_var, values=["USD", "EUR", "GBP", "INR", "JPY", "CAD"],state="readonly")
to_currency_dropdown.grid(row=2, column=1, padx=10, pady=10)

# Convert button
convert_button = tk.Button(app, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, pady=20)

# Result label
result_label = tk.Label(app, text="", font=("Arial", 14))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the application
app.mainloop()
