

import tkinter as tk
from tkinter.constants import COMMAND
from typing import Text
import dict_data
from tkinter import messagebox as mb

win = tk.Tk()
win.title("My dictionary")
win.geometry("650x600")
# win.eval('tk::PlaceWindow . top')

frame = tk.Frame(win)
frame.pack(fill='both', pady='20', padx='20')

def searchKey(key):
    wListBox.delete(0, tk.END)

    key = bar.get() 
    if key != "":
        matchedList = obj.search(key)
        showMatched(matchedList)
    # else:
    #     mb.showerror("Erro", "Please enter your word")


def showMatched(matchedList):
    for i in range(len(matchedList)):
        wListBox .insert(i, matchedList[i][0])
    lCount['text'] = str(len(matchedList))+" words(s) found."

def getSelection():
    #clearing previously occupying words and its meaning from labels
    wLabel['text'] = ""
    speechPart['text'] = ""
    mLabel['text'] = ""

    index = wListBox.curselection()[0]
    word = wListBox.get(index)
    if word:
        # mb.showinfo("Result", "Selected word is {}".format(word))
        word_dict = obj.define1(word)
        wLabel['text'] = word_dict[0]
        combined = []
        for i in range(len(word_dict)-1):
            combined.append(str(word_dict[i+1]).split("."))
        # print(combined)
        for item in combined:
            speechPart['text'] += str(item[0])+", "
            mLabel['text'] += str(item[1])+", "


# search bar
search_bar = tk.Frame(frame, relief='flat')
bar = tk.Entry(search_bar, relief='flat', width=65)
# bar.insert(0, "Enter search key")
bar.bind("<Key>", searchKey)
bar.pack(side='left', padx='5', pady='5')
bar.place(height=30)
sbutton = tk.Button(search_bar, text='search', command=searchKey)
sbutton.pack(side='right')
search_bar.pack(side='top', fill='x')

# dictionary object
obj = dict_data.Dict()

# Listbox for matching words
listFrame = tk.Frame(frame, relief='flat')
wListBox = tk.Listbox(listFrame, background='white', height="20", selectmode='SINGLE', highlightcolor='blue', relief='flat')
wListBox.bind("<<ListboxSelect>>", lambda x: getSelection())
wListBox .pack(side='top', fill='x', pady='20')
listFrame.pack(fill='x')

# Labels for the result and counting
fLabels = tk.Frame(frame, relief="sunken", border=1)
lCount = tk.Label(fLabels, border=1, text=" ", background='white', pady='2', padx='2')
lCount.pack(side='left')
fLabels.pack(side='left')


# Label for word, parts of speech and corresponding chinese meaning
rLabel = tk.Frame(frame, border=4, pady='20')
wLabel = tk.Label(rLabel, background='white', relief='sunken', text="  ", border=1,padx='4', pady='4',)
wLabel.grid(row=0, column=0)
# wLabel.pack(side='left')

speechPart = tk.Label(rLabel, background='white', text=" ", relief='sunken', padx='4', pady='4',)
speechPart.grid(row=0, column=1)
# speechPart.pack(side='left')

mLabel = tk.Label(rLabel, background='white', text=" ", relief='sunken', padx='4', pady='4')
mLabel.grid(row=0, column=2)
# mLabel.pack(side='left')

rLabel.pack(anchor='s', fill='x', side='right')
# rLabel.place(y='430', x='20')




win.mainloop()