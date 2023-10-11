# Currency Converter
This is an application built in python using TKinter, ttkthemes and requests as well as the [exchangerates](https://exchangeratesapi.io/) forex API to convert Euros to other currencies.
# Usage
First install requests, tkinter, and ttkthemes
`pip install requests tk ttkthemes`
Then run the app
`python app.py`
# Limitations
Due to using the free API plan on [exchangerates](https://exchangeratesapi.io/), the application can only convert from Euros, however any amount of Euros can be entered and any currency listed on exchangerates can be converted to.
# Features
Besides the obvious feature of converting currency, the application will check if it has been used today, if not, it will create a file to store the daily rates so the API usage can be reduced. If the current date doesn't match the date in the API request data stored in the rates.json file, it will be updated with the current days rates.
