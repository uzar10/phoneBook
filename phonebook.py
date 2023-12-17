import tkinter as tk 
from tkinter import ttk 



root    =   tk.Tk()
style   =   ttk.Style(root)
root.tk.call("source",  "forest-light.tcl")
root.tk.call("source",  "forest-dark.tcl")
style.theme_use("forest-dark")
root.mainloop()