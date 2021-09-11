'''
 Simple bilingual dictionary
 by Turi
 Github: https://github.com/turinaf
'''

'''
 GUI for the dictionary.
'''
import tkinter as tk
# from tkinter.constants import COMMAND
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
countLabel = tk.Label(fLabels, text="Found: ", background='grey', foreground='white', padx='2', pady='2')
lCount = tk.Label(fLabels, border=1, text=" ", background='white', pady='2', padx='2')
countLabel.pack(side='left')
lCount.pack(side='left')
fLabels.pack(side='left')


# Label for word, parts of speech and corresponding chinese meaning. Result label, rLabel
rLabel = tk.Frame(frame, border=4, pady='20')
# Another frame for the selected word with its indicator.
wordF = tk.Frame(rLabel, border=4, padx=20)
wordF.grid(row=0, column=0)
wDiscription = tk.Label(wordF, background='grey', foreground='white', text='Word: ', pady='4', padx='4')
wLabel = tk.Label(wordF, background='white', relief='sunken', text="  ", border=1,padx='4', pady='4')
wDiscription.pack(side='left')
wLabel.pack(side='left')
# wLabel.pack(side='left')

sPartF = tk.Frame(rLabel, border=4, padx=20)
sPartF.grid(row=1, column=0)
sPartlabel = tk.Label(sPartF, background='grey', foreground='white', text='Category: ', pady='4', padx='4')
speechPart = tk.Label(sPartF, background='white', text=" ", relief='sunken', padx='4', pady='4')
sPartlabel.pack(side='left')
speechPart.pack(side='left')
# speechPart.pack(side='left')

meaningF = tk.Frame(rLabel, border=4, padx=20)
meaningF.grid(row=2, column=0)
meaningLabel = tk.Label(meaningF, background='grey', foreground='white', text='Meaning: ', pady='4', padx='4')
mLabel = tk.Label(meaningF, background='white', text=" ", relief='sunken', padx='4', pady='4')
meaningLabel.pack(side='left')
mLabel.pack(side='left')
# mLabel.pack(side='left')

rLabel.pack(anchor='s', fill='x', side='right')
# rLabel.place(y='430', x='20')




win.mainloop()