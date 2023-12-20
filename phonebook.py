import tkinter as tk 
from tkinter import ttk 

def switchMode():
    if modeSwitch.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")

root    =   tk.Tk()
style   =   ttk.Style(root)
root.tk.call("source",  "forest-light.tcl")
root.tk.call("source",  "forest-dark.tcl")
style.theme_use("forest-dark")

frame   =   ttk.Frame(root)
frame.pack()
# intro frame
introFrame  =   ttk.LabelFrame(frame,   text="Intro")
introFrame.grid(row=0,column=1, padx=20  ,pady=10)
# Buttons
# listing button
listingButton   =   ttk.Button(introFrame,   text="List the Contacts")
listingButton.grid(row=0,   column =1,  padx=5, pady=[0,5], sticky= "nsew")
# inserting button  
insertingButton   =   ttk.Button(introFrame,   text="Insert a new Contacts")
insertingButton.grid(row=1,   column =1,  padx=5, pady=[0,5], sticky= "nsew")
# searching Button
searchingButton   =   ttk.Button(introFrame,   text="Searching a Contacts")
searchingButton.grid(row=2,   column =1,  padx=5, pady=[0,5], sticky= "nsew")
# sorting button
sortingButton   =   ttk.Button(introFrame,   text="Sort the Contacts")
sortingButton.grid(row=3,   column =1,  padx=5, pady=[0,5], sticky= "nsew")
# deleting button
deletingButton   =   ttk.Button(introFrame,   text="Delete a Contacts")
deletingButton.grid(row=4,   column =1,  padx=5, pady=[0,5], sticky= "nsew")
#  line 2 separate
separator   =   ttk.Separator(introFrame)
separator.grid(row=5,   column=1,   padx=[20,10],   pady=10,    sticky="ew")

# switching mode button
modeSwitch  =   ttk.Checkbutton(introFrame,    text="Switch mode", style="Switch", command = switchMode)
modeSwitch.grid(row=6,  column=1,   padx=5, pady=10 ,   sticky="nsew")


# # insert frame
# insertFrame =   ttk.LabelFrame(frame,   text    =   "insert new contact")
# insertFrame.grid(row=0,  column=1,  padx=20,    pady=10)
# #full name entry
# fullNameEntry = ttk.Entry(insertFrame)
# fullNameEntry.insert(0,"Full Name")
# fullNameEntry.bind("<FocusIn>",lambda   e:fullNameEntry.delete('0','end'))
# fullNameEntry.grid(row=0,   column=0   ,padx=5,    pady=[0,5],   sticky=  "ew")
# #address entry
# addressEntry = ttk.Entry(insertFrame)
# addressEntry.insert(0,"Address")
# addressEntry.bind("<FocusIn>",lambda   e:addressEntry.delete('0','end'))
# addressEntry.grid(row=1,   column=0   ,padx=5,    pady=[0,5],   sticky=  "ew")
# #email entry
# EmailEntry = ttk.Entry(insertFrame)
# EmailEntry.insert(0,"Email")
# EmailEntry.bind("<FocusIn>",lambda   e:EmailEntry.delete('0','end'))
# EmailEntry.grid(row=2,   column=0   ,padx=5,    pady=[0,5],   sticky=  "ew")
# #telephone entry
# telEntry = ttk.Entry(insertFrame)
# telEntry.insert(0,"telephone")
# telEntry.bind("<FocusIn>",lambda   e:telEntry.delete('0','end'))
# telEntry.grid(row=3,   column=0   ,padx=5,    pady=[0,5],   sticky=  "ew")
# #mobile number entry
# mobileEntry = ttk.Entry(insertFrame)
# mobileEntry.insert(0,"Mobile Number")
# mobileEntry.bind("<FocusIn>",lambda   e:mobileEntry.delete('0','end'))
# mobileEntry.grid(row=4,   column=0   ,padx=5,    pady=[0,5],   sticky=  "ew")

# # insert button
# insertButton    =   ttk.Button(insertFrame, text="Insert")
# insertButton.grid(row=5,   column=0   ,padx=5,    pady=[0,5],   sticky=  "nsew")


# list frame 
listFrame =   ttk.LabelFrame(frame,   text    =   "All the Contacts")
listtFrame.grid(row=0,  column=1,  padx=20,    pady=10)

root.mainloop()