import tkinter as tk
from tkinter import messagebox, font
import requests

def get_live_rate():
    url = "https://api.exchangerate-api.com/v4/latest/GBP"
    response = requests.get(url)
    data = response.json()
    return data['rates']['INR']

def convert_currency():
    amount = entry_amount.get()
    
    # Validation: Check if the input is empty
    if not amount.strip():
        messagebox.showerror("Input Error", "Please enter an amount in GBP.")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")
        return

    rate = get_live_rate()
    result = amount * rate
    label_result.config(text=f"₹ {result:.2f}")

# Setting up the GUI
root = tk.Tk()
root.title("GBP to INR Converter")

# Setting up the window size and centering it
root.geometry("500x350")
root.eval('tk::PlaceWindow . center')

# Font configuration
custom_font = font.Font(family="Bahnschrift SemiLight Condensed", size=14)

# Configuring the overall theme
root.configure(bg='black')

# Label for amount input
label_amount = tk.Label(root, text="Enter amount in GBP:", font=custom_font, fg='white', bg='black')
label_amount.pack(pady=10)

# Entry widget for amount input (larger size)
entry_amount = tk.Entry(root, font=custom_font, width=30, fg='white', bg='black', insertbackground='white')
entry_amount.pack(pady=5, ipady=10)  # Increased internal padding for a bigger box

# Button to trigger conversion
convert_button = tk.Button(root, text="Convert", font=custom_font, fg='white', bg='black', command=convert_currency)
convert_button.pack(pady=15)

# Label to display result
label_result = tk.Label(root, text="₹ 0.00", font=("Bahnschrift SemiLight Condensed", 16), fg='white', bg='black')
label_result.pack(pady=20)

# Run the application
root.mainloop()
