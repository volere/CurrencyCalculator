#!/usr/bin/python3



import sys
import os
import json

info = "usethis.json"
file = open(info, 'r')
n = file.read()


scoop = json.loads(n)
rate = scoop['rates']  #singles out rates section

def doMath():
    print(rate)
    print( 'base currency:' + scoop.get('base'))


#TODO validate form, make it so that the input does not need quotations
#add to interface

    input_cur = float(input('choose amount:'))


    print(input_cur * rate.get('USD'))
    return

doMath();


#for rate in sorted(rate):
#    cur_rate = rate[rate]
#    print("{} ({})".format,rate))
#



#for rates in what:
#    print(rates)
