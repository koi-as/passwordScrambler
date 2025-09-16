import tkinter as tk
from tkinter import *
import random

# set up a window to display text and obtain user input using tk win
# accept user input as string
# take string and randomize placement of characters
# take new randomized string, and randomize cahracters within the string
# use keyboard only characters so the scrambled password can be used normally
# a-z, A-Z, 0-9, !@#$%^&*?
# that should be a fine enough set of characters

# create the window object and set size and title
win=tk.Tk()
win.geometry('750x750')
win.title('The Great Scrambler')

# initialize vars
password=StringVar()
product=StringVar()
charList='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*?'

# set up functions
def shuffle():
    x=password.get()
    strList=list(x)
    random.shuffle(strList)
    y=''.join(strList)
    product.set(y)

def scramble():
    x=password.get()
    shuffled=random.sample(charList, len(x))
    y=''.join(shuffled)
    product.set(y)

# set up window elements
Entry(win, textvariable=password, width=20, font=('Courier', 25), relief=GROOVE).place(relx=.5, rely=.3, anchor=CENTER)
Entry(win, textvariable=product, width=20, font=('Courier', 25), relief=GROOVE).place(relx=.5, rely=.7, anchor=CENTER)
Button(win, width=12, text='SHUFFLE IT!', command=shuffle, relief=GROOVE, bg='light green').place(relx=.4, rely=.5, anchor=CENTER)
Button(win, width=12, text='SCRAMBLE IT!', command=scramble, relief=GROOVE, bg='orange').place(relx=.6, rely=.5, anchor=CENTER)

win.mainloop()