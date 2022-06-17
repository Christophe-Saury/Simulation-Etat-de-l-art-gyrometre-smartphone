from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Simulation Etat de l'Art")

icon = PhotoImage(file= 'logoISEP.png')
window.iconphoto(False,icon)

window.config(background="#326ba8")



#Creating a label widget
myLabel = Label(window, text="Hello World!", 
                font =('Arial', 40, 'bold'),
                fg = 'white', bg='black', 
                relief = RAISED,
                bd = 10,
                padx = 50, pady = 50,
                image = icon, compound='bottom')
#Shoving the label onto the screen
myLabel.place(x=0, y=0) #Can also use .pack

window.mainloop()
