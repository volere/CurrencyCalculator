import json
import sys
#import grabandread.py
from tkinter import *
import tkinter.messagebox as box


info = "usethis.json"
file = open(info, 'r')
n = file.read()

scoop = json.loads(n)
rate = scoop['rates']  #singles out rates section


window = Tk()

window.title('Currency Calculator')

label = Label(window, text = 'Currency Calculator')
label.pack(padx = 200 , pady = 50)
frame = Frame(window)
entry = Entry(frame)

#listbox = Listbox(master)
#listbox.pack()

#listbox.insert(END, "a list entry")

#for item in ["one", "two", "three", "four"]:
#    listbox.insert(END, item)


listbox = Listbox(frame)
lb = Listbox(frame)

#listbox = Listbox(master)
#listbox.pack()
#lb = Listbox(selectmode=EXTENDED)

#for rates in rate:
#    listbox.insert(END, '{}: {}'.format(rates, rate[rates]))
#    self.listbox.insert(END, key)
#self.data = data
#self.lb.delete(0, END) # clear



#for rates, value in rate:


for rates in rate:
    listbox.insert(END, '{}: {}'.format(rates, rate[rates]))


#When querying the list, simply fetch the items from the data attribute,
#using the selection as an index:

#items = self.lb.curselection()
#items = [self.data[float(item)] for item in items]




#TODO print individual values with selected rates
def conversion() :

#TODO something, anything
    listbox.get(listbox.curselection())

    entry = listbox.get(listbox.curselection())

    cheese = rate.get(codeSelec)
#    items = self.listbox.curselection()
#    items = [self.data[float(item)] for item in items]


#    box.showinfo('Selection', 'Your Choice:' , )
    box.showinfo('Selection:     '  + listbox.get(listbox.curselection()))
#    items = self.listbox.curselection()


    return
###

btn = Button(frame, text = 'Calculate', command = conversion)
btn.pack(side = RIGHT, padx = 5)
entry.pack(side = RIGHT, padx = 10, pady = 10)
listbox.pack(side= LEFT)
frame.pack(padx = 30, pady = 30)


window.mainloop()
