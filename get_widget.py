import tkinter as tk
from tkinter import ttk

def button_func():
    # get the content of the entry 
    entry_text = entry.get()

    # update the label with entry 
    # lable.config(text = entry.get())
    label['text'] = entry.get()

    'To get all the options you have with a widget use print(label.configure)'


# window 
window= tk.Tk()
window.geometry('300x200')
window.title('Getting and setting widgets')


#widgets
label = ttk.Label(master = window, text = 'Some text')
label.pack()

entry = ttk.Entry(master= window)
entry.pack()


button = ttk.Button(master = window,text = 'The button', command = button_func) 
button.pack()

def reset_func():
    label['text']='some text'
    entry['state']='enabled'

excercise_button = ttk.Button(master = window, text = 'exercise button', command = reset_func)
excercise_button.pack()

#run 
window.mainloop()



