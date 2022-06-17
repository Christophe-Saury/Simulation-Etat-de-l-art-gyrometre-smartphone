from tkinter import *

def submit():
    username = entry.get()
    print("Hello "+ username)


def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)
    
window = Tk()

window.title("Entry")

entry = Entry(window, font =("Arial",50), show='*')
entry.pack(side = LEFT  )

submit_button = Button(window, text ="submit", command= submit)
submit_button.pack(side= RIGHT)

delete_button = Button(window, text ="delete", command= delete)
delete_button.pack(side= RIGHT)

delete_button = Button(window, text ="backspace", command= backspace)
delete_button.pack(side= RIGHT)

window.mainloop()