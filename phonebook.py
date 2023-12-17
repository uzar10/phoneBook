import tkinter as tk 
from tkinter import ttk 



root    =   tk.Tk()
type.ttk.Style(root)
root.tk.call("source",  "forest-dark.tcl")
root.tk.call("source",  "forest-light.tcl")
style.theme_use("forest-dark")
root.mainloop()