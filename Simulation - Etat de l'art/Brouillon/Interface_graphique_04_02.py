from tkinter import *



# ......................... Window Configuration .......................

window = Tk()
window.geometry("1400x780")
window.title("Simulation Etat de l'Art")
icon = PhotoImage(file= 'logoISEP.png')
canvas = Canvas(window, height=500, width=500)
window.config(background="#326ba8")



# ....................... Variable declaration .........................

a = IntVar()
t = 0
x = 100
y = 100





# ................................ Functions .................................
# Menu Functions .......................




    
    
    #Entry functions ....................
    
def submit(entry):
    variable = entry.get()
    if(entry==entryLong):
        L = variable
    elif(entry == entryMasse):
        m = variable
    elif(entry == entryAngle):
        h = variable
    elif (entry == entryLatit):
        x0 = variable
    #elif(entry == entryVitRot):
     #   vit_rot = variable
     
     
def submitAll():
    L = entryLong.get()
    m = entryMasse.get()
    h = entryAngle.get()
    x0 = entryLatit.get()
    print(L)
    print(m)
    print(h)
    print(x0)

        
        
        
        
        
def delete(entry):
    entry.delete(0,END)


    
def display():
    if(a.get()==1): # Force de Coriolis est présente
        
       # entryVitRot.place(x=5, y =670)
        #submitVitRot.place(x=230, y=670)
        #deleteVitRot.place(x=280, y=670)
        #VitesseRot.place(x=5, y= 620)
 
        
        canvas.itemconfig(1, state='normal')
        canvas.itemconfig(2, state='normal')
        canvas.itemconfig(3, state='normal')
        canvas.itemconfig(4, state='hidden')
        canvas.itemconfig(5, state='hidden')
        canvas.itemconfig(6, state='hidden')
        canvas.itemconfig(7, state='hidden')
   
        
    else:   # Pas de force de Coriolis
        
       # VitesseRot.place_forget()
        #entryVitRot.place_forget()
        #submitVitRot.place_forget()
        #deleteVitRot.place_forget()
        
        canvas.itemconfig(1, state='hidden')
        canvas.itemconfig(2, state='hidden')
        canvas.itemconfig(3, state='hidden')
        canvas.itemconfig(4, state='normal')
        canvas.itemconfig(5, state='normal')
        canvas.itemconfig(6, state='normal')
        canvas.itemconfig(7, state='normal')
    
   

          
          
def create_circle(x, y, r, canvasName, color, w): # easier way to make a circle
    x0 = x - r
    y0 = y-r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill = color, width = w)          

def clearSimul():
    entryLong.delete(0,END)
    entryMasse.delete(0,END)
    entryAngle.delete(0,END)
    entryLatit.delete(0,END)
  #  entryVitRot.delete(0,END)
  
def printSimul():
    print("l = " + L)
    print("m = " + m)
    print("angle = " + h)
    print("L = " + x0)


# ....................... Calculate Operations .........................


def draw_nocoriolis(x,y):
    create_circle(x,y,7,canvas, "red", 1) # mass position

def draw_coriolis(x,y):
    create_circle(x,y,7,canvas, "red", 1) # mass position

def update(t,x,y):
    t=t+1
    x = x +10
    y = y + 10
    

def updateScreen():
    while(t<20):
        update(t,x,y)
        draw_coriolis(x, y)
    





# .......................... Widgets creation .........................


# ......................... Left Side Creation .........................


# ........................... Labels creation .........................

Titre = Label(window, text="Simulation Etat de l'Art", 
                    font =('Arial', 40, 'bold'),
                    fg = 'white', bg='black', 
                    relief = RAISED,
                    bd = 10,
                    padx = 5, pady = 5)
    
Texte_Parametrage = Label(window, text="Paramètres de la simulation à définir", 
                    font =('Arial', 18, 'bold'),
                    fg = 'white', bg='black', 
                    relief = RAISED,
                    bd = 5,
                    padx = 0, pady = 0)
    
LongueurFil = Label(window, text="Longueur du fil", 
                    font =('Arial', 14),
                    fg = 'black', bg='white', 
                    relief = SUNKEN,
                    bd = 2,
                    padx = 0, pady = 0)
    
MasseSmartphone = Label(window, text="Masse du smartphone", 
                    font =('Arial', 14),
                    fg = 'black', bg='white', 
                    relief = SUNKEN,
                    bd = 2,
                    padx = 0, pady = 0)
    
AngleInitial = Label(window, text="Angle Initial (en °)", 
                    font =('Arial', 14),
                    fg = 'black', bg='white', 
                    relief = SUNKEN,
                    bd = 2,
                    padx = 0, pady = 0)
    
Latitude = Label(window, text="Latitude (Paris = 48.52)", 
                    font =('Arial', 14),
                    fg = 'black', bg='white', 
                    relief = SUNKEN,
                    bd = 2,
                    padx = 0, pady = 0)
    
#VitesseRot = Label(window, text="Vitesse de rotation selon l'axe y", 
 #                   font =('Arial', 14),
  #                  fg = 'black', bg='white', 
   #                 relief = SUNKEN,
    #                bd = 2,
     #               padx = 0, pady = 0)
    
check_Coriol = Checkbutton(window, text = "Animation Pendule de Foucault",
                           variable = a, onvalue=1, offvalue= 2,
                            command = display)
    
check_Resist = Checkbutton(window, text = "Frottements")

# Menu Bar  .......................................................  

menubar = Menu(window)
window.config(menu = menubar)




simulMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Simulation", menu = simulMenu)
simulMenu.add_command(label ="Run Simulation", command = submitAll)
simulMenu.add_command(label ="Run Animation", command = updateScreen)
simulMenu.add_command(label ="Clear Parameters", command = clearSimul)
simulMenu.add_command(label ="Print Parameters", command = printSimul)



# ................. Create entries for parameters ........................
# First parameter ......................
    
entryLong = Entry(window, font =("Arial",14))
#submitLong = Button(window, text ="Submit", command=lambda:    submit(entryLong))
deleteLong = Button(window, text ="Clear", command=lambda:   delete(entryLong))
    
# Second Parameter
    
entryMasse = Entry(window, font =("Arial",14))
#submitMasse = Button(window, text ="Submit", command=lambda:  submit(entryMasse))
deleteMasse = Button(window, text ="Clear", command= lambda: delete(entryMasse))
    
    
# Third Parameter
    
entryAngle = Entry(window, font =("Arial",14))
#submitAngle = Button(window, text ="Submit", command=lambda:   submit(entryAngle))
deleteAngle = Button(window, text ="Clear", command=lambda:   delete(entryAngle))
    
    
# Fourth Parameter
    
entryLatit = Entry(window, font =("Arial",14))
#submitLatit = Button(window, text ="Submit", command=lambda:   submit(entryLatit))
deleteLatit = Button(window, text ="Clear", command=lambda:   delete(entryLatit))
    
    
#entryVitRot = Entry(window, font =("Arial",14))
#submitVitRot = Button(window, text ="Submit", command=lambda:   submit(entryVitRot))
#deleteVitRot = Button(window, text ="Clear", command=lambda:   delete(entryVitRot))



# ......................... END OF LEFT SIDE .........................


# ........................ START OF RIGHT SIDE .......................

# ......................... Canvas Creation .......................



canvas.place(x = 800, y = 200)
# Force de Coriolis
canvas.create_oval(240,240,260,260, fill="purple", width=2)  # inside circle = center of pendule
canvas.create_oval(50,50,450,450, width=2, dash=(1,100)) # outside circle = max trajectory of pendule
main_circle = create_circle(30,30,7,canvas, "red", 1) # mass position

# No Force de Coriolis
create_circle(250,225,8,canvas, "purple", 2)  # inside circle = center of pendule
main_circle2 =create_circle(250,450,7,canvas, "red", 1)  # mass position
main_line2 = canvas.create_line(250,225,250,450, fill="black", width=1)
canvas.create_arc(25, 0, 450, 450, extent =180,start =180, width =0, dash=(1,1))

canvas.itemconfig(1, state='hidden')
canvas.itemconfig(2, state='hidden')
canvas.itemconfig(3, state='hidden')







# ........................ Placing the widgets ........................

# ........................ Left Side Creation .........................

Titre.place(x=450, y=0)
Texte_Parametrage.place(x=5, y=75)
LongueurFil.place(x=5, y=170)
MasseSmartphone.place(x=5, y=270)
AngleInitial.place(x=5, y=370)
Latitude.place(x=5, y=470)

# Place buttons
check_Coriol.place(x=5, y=570)
check_Resist.place(x=210, y=570)

entryLong.place(x=5, y =200)
#submitLong.place(x=230, y=200)
deleteLong.place(x=230, y=200)

entryMasse.place(x=5, y =300)
#submitMasse.place(x=230, y=300)
deleteMasse.place(x=230, y=300)

entryAngle.place(x=5, y =400)
#submitAngle.place(x=230, y=400)
deleteAngle.place(x=230, y=400)

entryLatit.place(x=5, y =500)
#submitLatit.place(x=230, y=500)
deleteLatit.place(x=230, y=500)

# .......................... Right Side Creation ..................





# ...............................................................

window.mainloop()