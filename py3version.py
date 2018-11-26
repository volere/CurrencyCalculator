#!/usr/bin/python3



import sys
import os
import json

info = "usethis.json"
file = open(info, 'r')
what = file.read()

scoop = json.loads(n)

##################rates info??? gonna need some looks#########
#####Theese commands convert the response into json/dictformat why is this nessacery?
##json.loads literally undos new & n f'n dumbdumb
################################
#data = what.json()
rate = scoop['rates']  #singles out rates section
print(rate)
###############################################################
###############################
#TODO validate form, make it so that the input does not need quotations
#add to interface

input_cur = float(input('choose amount:'))
currency_select = input('choose currency code: ')


cheese = rate.get(currency_select)

print(input_cur * cheese)




#date = datetime.strptime(data['date'], "%Y-%m-%d")



#for rate in sorted(rate):
#    cur_rate = rate[rate]
#    print("{} ({})".format,rate))
#



#for rates in what:
#    print(rates)
