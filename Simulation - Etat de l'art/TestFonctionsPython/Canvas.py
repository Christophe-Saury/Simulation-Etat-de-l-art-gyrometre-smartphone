from tkinter import *

window = Tk()
window.geometry("1400x780")
window.config(background="#326ba8")




def create_circle(x, y, r, canvasName, color, w): # easier way to make a circle
    x0 = x - r
    y0 = y-r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill = color, width = w)
    
    

#met un fonction draw et une fonction update draw pour faire fonctionner la simulation
canvas = Canvas(window, height=500, width=500)
canvas.create_line(0,0,500,500, fill="blue", width=5)
canvas.create_line(0,500,500,0, fill="blue", width=5)
#canvas.create_rectangle(50,50,250,250, fill="purple", width=2)
canvas.create_oval(240,240,260,260, fill="purple", width=2)  # inside circle = center of pendule
canvas.create_oval(50,50,450,450, width=2) # outside circle = max trajectory of pendule
create_circle(30,30,20,canvas, "red", 2) 



canvas.pack(side = RIGHT)

window.mainloop()