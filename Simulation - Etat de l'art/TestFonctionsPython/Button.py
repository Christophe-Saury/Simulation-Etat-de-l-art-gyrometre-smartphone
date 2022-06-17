from tkinter import *

count = 0
def click():
    global count
    count += 1
    print(count)
    
window = Tk()
window.title("Button")

button = Button(window, text ="click me", command = click,
                fg="white", bg="black", 
                activeforeground = "black", activebackground = "white",)
button.pack()
window.mainloop()