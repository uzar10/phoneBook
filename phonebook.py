import tkinter as tk 
from tkinter import ttk 
import datetime
from openpyxl import Workbook

# function of the switch mode button 
def switchMode():
    if modeSwitch.instate(["selected"]):
        style.theme_use("forest-light")
    else:
        style.theme_use("forest-dark")

def showFrame(frame):
    frame.grid(row=0, column=1, padx=20, pady=10)
    introFrame.grid_forget()

def switchToListFrame():
    introFrame.grid_forget()
    showFrame(listFrame)

def switchToInsertFrame():
    introFrame.grid_forget()
    showFrame(insertFrame)

def switchToSearchFrame():
    introFrame.grid_forget()
    showFrame(searchFrame)

def switchToSortFrame():
    introFrame.grid_forget()
    showFrame(sortFrame)

def switchToDeleteFrame():
    introFrame.grid_forget()
    showFrame(deleteFrame)

def backToMainMenu():
    listFrame.grid_forget()
    insertFrame.grid_forget()
    searchFrame.grid_forget()
    sortFrame.grid_forget()
    deleteFrame.grid_forget()
    introFrame.grid(row=0, column=0)

# loading data into a table in the listFrame
def loadData():
    path    =   "contacts.xlsx"
    workbook=   opnepyxl.load_workbook(path)
    sheet   =   workbook.active

    listValues  =   list(sheet.values)

    for columnName  in  listValues[0]:
        treeView.heading(columnName,    text=columnName)
    
    for valueTuple  in  listValues[1:]:
        treeView.insert('',tk.END,values=valueTuple)

# inserting the new contacts into excel file
def insertContact():
    fullName=   fullNameEntry.get()
    address =   addressEntry.get()
    email   =   emailEntry.get()
    telephone=  telEntry.get()
    mobile  =   mobileEntry.get()

    # insert row into excel sheet
    path    =   "contacts.xlsx" 
    workbook    =   opnepyxl.load_workbook(path)
    sheet   =   workbook.active
    rowValues   =   [fullName,address,email,telephone,mobile]
    sheet.append(rowValues)
    workbook.save(path)

    # insert row into treeView
    treeView.insert('',tk.END,values=rowValues)

    # clear the values
    fullNameEntry.delete(0,"end")
    # fullNameEntry.insert(0, "Full Name")
    addressEntry.delete(0,"end")
    # addressEntry.insert(0,"Address")
    emailEntry.delete(0,"end")
    # emailEntry.insert(0, "Email")
    telEntry.delete(0,"end")
    # telEntry.insert(0,"Telephone Number")
    mobileEntry.delete(0,"end")
    # mobileEntry.insert(0,"Mobile Number")


root    =   tk.Tk()
root.title('Phone Book')
style   =   ttk.Style(root)
root.tk.call("source",  "forest-light.tcl")
root.tk.call("source",  "forest-dark.tcl")
style.theme_use("forest-dark")

# frame   =   ttk.Frame(root)
# frame.pack()
# intro frame
introFrame  =   ttk.Frame(root)
introFrame.pack()
# Buttons
# listing button
listingButton   =   ttk.Button(introFrame,   text="List the Contacts",  command = switchToListFrame)
listingButton.grid(row=0,   column =1,  padx=5, pady=[0,5], sticky= "nsew")
# inserting button  
insertingButton   =   ttk.Button(introFrame,   text="Insert a new Contacts",  command = switchToInsertFrame)
insertingButton.grid(row=1,   column =1,  padx=5, pady=[0,5], sticky= "nsew")
# searching Button
searchingButton   =   ttk.Button(introFrame,   text="Searching a Contacts", command = switchToSearchFrame)
searchingButton.grid(row=2,   column =1,  padx=5, pady=[0,5], sticky= "nsew")
# sorting button
sortingButton   =   ttk.Button(introFrame,   text="Sort the Contacts",command = switchToSortFrame)
sortingButton.grid(row=3,   column =1,  padx=5, pady=[0,5], sticky= "nsew")
# deleting button
deletingButton   =   ttk.Button(introFrame,   text="Delete a Contacts", command = switchToDeleteFrame)
deletingButton.grid(row=4,   column =1,  padx=5, pady=[0,5], sticky= "nsew")
#  line 2 separate
separator   =   ttk.Separator(introFrame)
separator.grid(row=5,   column=1,   padx=[20,10],   pady=10,    sticky="ew")

# switching mode button
modeSwitch  =   ttk.Checkbutton(introFrame,    text="Switch mode", style="Switch", command = switchMode)
modeSwitch.grid(row=6,  column=1,   padx=5, pady=10 ,   sticky="nsew")


# insert frame
insertFrame =   ttk.LabelFrame(introFrame,   text    =   "insert new contact")
insertFrame.grid(row=0,  column=1,  padx=20,    pady=10)
#full name entry
nameEntryFrame   =   ttk.LabelFrame(insertFrame, text="Full Name")
nameEntryFrame.grid(row=0,column=0   ,padx=5,    pady=[0,5],   sticky=  "nsew")
fullNameEntry = ttk.Entry(nameEntryFrame)
fullNameEntry.grid(row=0,   column=0   ,padx=5,    pady=[0,5],   sticky=  "nsew")
#address entry
addressEntryFrame    =   ttk.LabelFrame(insertFrame, text="Address")
addressEntryFrame.grid(row   =   1,column=0,padx=5,    pady=[0,5],   sticky=  "nsew")
addressEntry = ttk.Entry(addressEntryFrame)
addressEntry.grid(row=0,   column=0   ,padx=5,    pady=[0,5],   sticky=  "nsew")
#email entry
emailEntryFrame  =   ttk.LabelFrame(insertFrame, text="Email")
emailEntryFrame.grid(row=2,  column=0,padx=5,    pady=[0,5],   sticky=  "nsew")
emailEntry = ttk.Entry(emailEntryFrame)
emailEntry.grid(row=0,   column=0   ,padx=5,    pady=[0,5],   sticky=  "nsew")
#telephone entry
telEntryFrame   =   ttk.LabelFrame(insertFrame, text="Telephone")
telEntryFrame.grid(row=3,   column=0,padx=5,    pady=[0,5],   sticky=  "nsew")
telEntry = ttk.Entry(telEntryFrame)
telEntry.grid(row=0,   column=0   ,padx=5,    pady=[0,5],   sticky=  "nsew")
#mobile number entry
mobileEntryFrame    =   ttk.LabelFrame(insertFrame, text="Mobile Number")
mobileEntryFrame.grid(row=4,    column=0,padx=5,    pady=[0,5],   sticky=  "nsew")
mobileEntry = ttk.Entry(mobileEntryFrame)
mobileEntry.grid(row=0,   column=0   ,padx=5,    pady=[0,5],   sticky=  "nsew")

# insert button
insertButton    =   ttk.Button(insertFrame, text="Insert",  command = insertContact)
insertButton.grid(row=5,   column=0   ,padx=5,    pady=[0,5],   sticky=  "nsew")

# back to main menu button
backButton = ttk.Button(root, text="Back to Main Menu", command=backToMainMenu)
backButton.pack(padx=5, pady=[0,5], fill="x")

# list frame 
listFrame =   ttk.LabelFrame(introFrame,  text="List of the contacts")
listFrame.grid(row=0,  column=1,   pady=10)

# scroll Bar
treeScroll  =   ttk.Scrollbar(listFrame)
treeScroll.pack(side="right"   ,   fill    ="y")

cols    =   ("Full Name",   "Address"   ,   "Email" ,   "Telephone" ,   "Mobile Number")
treeView    =   ttk.Treeview(listFrame, show="headings" ,
        yscrollcommand=treeScroll.set,   column= cols,   height =   10)
treeView.column("Full Name" ,  width=100)
treeView.column("Address" , width=100)
treeView.column("Email" ,   width=100)
treeView.column("Telephone" ,   width=50)
treeView.column("Mobile Number" ,   width=50)
treeView.pack()
treeScroll.config(command=treeView.yview)

# Search frame


root.mainloop()