import tkinter as tk 
from tkinter import ttk 



root    =   tk.Tk()
style   =   ttk.Style(root)
root.tk.call("source",  "forest-light.tcl")
root.tk.call("source",  "forest-dark.tcl")
style.theme_use("forest-dark")

frame   =   ttk.Frame(root)
frame.pack()
insertFrame =   ttk.LabelFrame(frame,   text    =   "insert new contact")
insertFrame.grid(row    =   0,  column  =   1)
#full name entry
fullNameEntry = ttk.Entry(insertFrame)
fullNameEntry.insert(0,"Full Name")
fullNameEntry.bind("<FocusIn>",lambda   e:fullNameEntry.delete('0','end'))
fullNameEntry.grid(row=0,   column=0   ,   sticky=  "ew")
#address entry
addressEntry = ttk.Entry(insertFrame)
addressEntry.insert(0,"Address")
addressEntry.bind("<FocusIn>",lambda   e:addressEntry.delete('0','end'))
addressEntry.grid(row=1,   column=0   ,   sticky=  "ew")
#email entry
EmailEntry = ttk.Entry(insertFrame)
EmailEntry.insert(0,"Email")
EmailEntry.bind("<FocusIn>",lambda   e:EmailEntry.delete('0','end'))
EmailEntry.grid(row=2,   column=0   ,   sticky=  "ew")
#telephone entry
telEntry = ttk.Entry(insertFrame)
telEntry.insert(0,"telephone")
telEntry.bind("<FocusIn>",lambda   e:telEntry.delete('0','end'))
telEntry.grid(row=3,   column=0   ,   sticky=  "ew")
#mobile number entry
mobileEntry = ttk.Entry(insertFrame)
mobileEntry.insert(0,"Mobile Number")
mobileEntry.bind("<FocusIn>",lambda   e:mobileEntry.delete('0','end'))
mobileEntry.grid(row=4,   column=0   ,   sticky=  "ew")

root.mainloop()