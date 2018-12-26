import sys
#import json
import requests
from datetime import datetime

##r=requests.get('https://api.exchangeratesapi.io/latest HTTP/1.1')

<<<<<<< HEAD
=======


>>>>>>> caa3a768034ef219f41cbee30b828b0c34682e89

def pullCurrency():
#atm this function only pulls the currency information with Euro as base ###

    r = requests.get('https://api.exchangeratesapi.io/latest')
#provide unicode object     info = r.text
#####uncomment to provide datacheck    print(info)
    data = r.json()
    rates = data['rates']
#    return
    for rates in rates:
        print(rates)

def printRates():
    if type(rate) == 'dict':
        for rates in rates:
            print(rates)
    else:
        print('rates type is not dict')
    return data
def calc():
#    this is the magic python3 does not like this. rate.get needs to be a float
    pullCurrency()
    print(
    input_cur * rate.get(currency_select)


printRates()
calc()
