from tkinter import *



def display():
    if(a.get()==1):
        
        
        
        
        print("Hello")
        
        
        
    else:
        
        
        
        print("no")





window = Tk()


a = IntVar()

check_button = Checkbutton(window, text = "Force de Coriolis",
                           variable = a, onvalue=1, offvalue=0,
                           command = display)
                           
                           
check_button1 = Checkbutton(window, text = "Frottement")
                            
check_button.pack(side=LEFT)
check_button1.pack(side=BOTTOM)

window.mainloop()