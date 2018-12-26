import json
import sys
from tkinter import *
import tkinter.messagebox as box
import requests


r = requests.get('https://api.exchangeratesapi.io/latest')

info = r.json()

rate = info['rates']
data = rate.values()
print(data)

window = Tk()
window.title('Currency Calculator')
label = Label(window, text = 'Currency Calculator')
label.pack(padx = 200 , pady = 50)
frame = Frame(window)
entry = Entry(frame)

listbox = Listbox(frame, exportselection=False)
lb = Listbox(frame)


for rates in rate:
    listbox.insert(END, '{}: {}'.format(rates, rate[rates]))
def conversion():

###called by button click.


    detail = entry.get()
    magic = listbox.get(listbox.curselection())
    print(rate.values())
    print(type(magic))
    selec = magic[0:5]
    multiplier = float(magic.lstrip(magic[0:5]))

    print(detail)
    jello = float(detail)
    print(multiplier)
    jelloMulti = multiplier * jello

    print(jelloMulti)

    box.showinfo('selec', detail + "  " + selec + ' is {} euro'  .format(jelloMulti))
    return

btn = Button(frame, text = 'Calculate', command = conversion)
btn.pack(side = RIGHT, padx = 5)
entry.pack(side = RIGHT, padx = 10, pady = 10)
listbox.pack(side= LEFT)
frame.pack(padx = 30, pady = 30)


window.mainloop()
