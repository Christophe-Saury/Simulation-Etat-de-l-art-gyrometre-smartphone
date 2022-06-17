from tkinter import *

window =Tk()

def submit():
    username = entry.get()
    print("Hello "+ username)


def delete():
    entry.delete(0,END)

def backspace():
    entry.delete(len(entry.get())-1,END)
    


frame= Frame(window, bg="pink", bd=5, relief=SUNKEN)
frame.place(x=0, y=0)

entry = Entry(frame, font =("Arial",14)).pack(side = LEFT)

submit_button = Button(frame, text ="Submit", command= submit).pack(side = LEFT)

delete_button = Button(frame, text ="Clear", command= delete).pack(side = LEFT)


entry = Entry(frame, font =("Arial",14)).pack(side = BOTTOM)

submit_button = Button(frame, text ="Submit", command= submit).pack(side = LEFT )

delete_button = Button(frame, text ="Clear", command= delete).pack(side = LEFT )

#button = Button(frame, text ="W", font=("Consolas",25),width =3).pack(side=TOP)
#button = Button(frame, text ="A", font=("Consolas",25),width =3).pack(side=LEFT)
#button = Button(frame, text ="S", font=("Consolas",25),width =3).pack(side=LEFT)
#button = Button(frame, text ="D", font=("Consolas",25),width =3).pack(side=LEFT)

window.mainloop()
