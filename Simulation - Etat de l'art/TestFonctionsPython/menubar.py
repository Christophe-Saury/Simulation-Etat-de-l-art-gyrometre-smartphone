from tkinter import *

window = Tk()

menubar = Menu(window)
window.config(menu = menubar)

def openFile():
    print("File has been opened")

def saveFile():
    print("File has been saved")

def quit():
    print("File has been exited")
    
settingsMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Settings", menu = settingsMenu)

simulMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Simulation", menu = simulMenu)
simulMenu.add_command(label ="Open", command = openFile)
simulMenu.add_command(label ="Save", command = saveFile)
simulMenu.add_separator()
simulMenu.add_command(label ="Exit", command = quit)

window.mainloop()