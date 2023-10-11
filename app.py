import requests
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import os
import json
from datetime import date

app_title = 'Currency Converter'

key = '3070d0c0d6f725b85a332e63578efc9b'

type = "latest"

currency_filename = 'currencies.csv'

rate_filename = 'rates.json'

url = f'http://api.exchangeratesapi.io/v1/{type}?access_key={key}'

rates = {}

if not os.path.isfile(rate_filename):
    print('making a new file for the rates data')
    f = open(rate_filename, "w")
    r = requests.get(url)
    print(r.status_code)
    rates = r.json()
    json.dump(r.json(), f)
    f.close()
else:
    print('rates file exists')
    f = open(rate_filename, 'r')
    data = json.load(f)
    f.close()
    print(data['date'])
    print(str(date.today()))
    if data['date'] != str(date.today()):
        print('rates file out of date')
        f = open(rate_filename, 'w')
        r = requests.get(url)
        print(r.status_code)
        rates = r.json()
        json.dump(r.json(), f)
        f.close()
    else:
        print('rates file is up to date')
        rates = data



f = open(rate_filename, 'r')
data = json.load(f)
f.close()
currencies = data['rates']
currencies_options = list(data['rates'].keys())

currencies_count = len(currencies)

print(f'imported {currencies_count} currencies from {rate_filename}')

root = ThemedTk(theme="yaru")

ico = Image.open('icon.png')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

root.title(app_title)

selected_currency1 = tk.StringVar()
selected_currency2 = tk.StringVar()

if 'USD' in currencies_options:
    selected_currency1.set('USD')
else:
    selected_currency1 == currencies_options[0]

currency_amount = 1
result = 0

input_text = tk.Text(root, width=15, height=1)
result_label = ttk.Label(root, text = "Result: ")

def ConvertCurrency():
    currency_amount = float(input_text.get("1.0","end-1c"))
    if isinstance(currency_amount, float) and currency_amount > 0:
        result = currency_amount * currencies[selected_currency1.get()]
        result_label.config(text="Result: " + f"{result}")
    else :
        result_label.config(text="Result: " + "ERROR - NOT A VALID CURRENCY AMOUNT")

prompt_label1 = ttk.Label(root, text = "Enter the amount of Euros (EUR) you have and a currency to convert to.")
prompt_label1.pack()


input_text.pack()
dropdown1 = ttk.OptionMenu(root, selected_currency1, selected_currency1.get(),*currencies_options)
dropdown1.pack()

conv_b = ttk.Button(root, text = "Convert", command=ConvertCurrency)
conv_b.pack()

result_label.pack()

#response = requests.get("")
root.mainloop()