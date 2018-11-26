import json
import sys
#import grabandread.py
from tkinter import *
import tkinter.messagebox as box



info = "usethis.json"
file = open(info, 'r')
n = file.read()
self = json.loads(n)
rate = self['rates']
data = rate.values()
print(data)

window = Tk()
window.title('Currency Calculator')
label = Label(window, text = 'Currency Calculator')
label.pack(padx = 200 , pady = 50)
frame = Frame(window)
entry = Entry(frame)

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



#for rates, value in rate
for rates in rate:
    listbox.insert(END, '{}: {}'.format(rates, rate[rates]))
##


#When querying the list, simply fetch the items from the data attribute,
#using the selection as an index:

#items = self.lb.curselection()
#items = [self.data[float(item)] for item in items]




#TODO print individual values with selected rates
def conversion():


#TODO something, anythinpring

#    items = self.listbox.curselection()
#    items = [self.data[float(item)] for item in items]
    print(type(rate()))
    print(listbox.get(listbox.curselection()))

    entry = listbox.get(listbox.curselection())

    print(type(entry))
    print(entry[0:5])

    box.showinfo('Selection', 'Your Choice:' , )
    box.showinfo(entry)
#    items = self.listbox.curselection()


    return
###

btn = Button(frame, text = 'Calculate', command = conversion)
btn.pack(side = RIGHT, padx = 5)
entry.pack(side = RIGHT, padx = 10, pady = 10)
listbox.pack(side= LEFT)
frame.pack(padx = 30, pady = 30)


window.mainloop()
