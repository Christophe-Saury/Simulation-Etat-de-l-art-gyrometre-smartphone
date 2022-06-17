from tkinter import *
import time


# ....................... Variable declaration .........................


x=0
y=0
xe = 300
ye = 300
state = True


# ......................... Window Configuration .......................

def initialize_window():
    window = Tk()
    window.geometry("1400x780")
    window.title("Simulation Etat de l'Art")
    icon = PhotoImage(file= 'logoISEP.png')
    window.config(background="#326ba8")
    canvas = Canvas(window, height=500, width=500)
    
    return window, canvas


def create_circle(x, y, r, canvasName, color, w): # easier way to make a circle
    x0 = x - r
    y0 = y-r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill = color, width = w)   








def initialize_foucault():
    # Force de Coriolis
    canvas.create_oval(240,240,260,260, fill="purple", width=2)  # Id = 1 ; inside circle = center of pendule
    canvas.create_oval(50,50,450,450, width=2, dash=(1,100)) # Id = 2; outside circle = max trajectory of pendule
    main_circle = create_circle(30,30,7,canvas, "red", 1) # Id=3; mass position
    return main_circle
    
    
    
    
    

def initialize_pendule_simple():
    #No Force de Coriolis
    create_circle(250,225,8,canvas, "purple", 2)  # Id=4; inside circle = center of pendule
    main_circle2 = create_circle(250,450,7,canvas, "red", 1)  # mass position
    main_line2 = canvas.create_line(250,225,250,450, fill="black", width=1) # Id = 6
    canvas.create_arc(25, 0, 450, 450, extent =180,start =180, width =0, dash=(1,1)) #♠ id =7
    return main_circle2, main_line2







def hide_foucault(): 
    #canvas.itemconfig(1, state='hidden')
    #canvas.itemconfig(2, state='hidden')
   # canvas.itemconfig(3, state='hidden')
     canvas.itemconfig(1, state='hidden')
     canvas.itemconfig(2, state='hidden')
     canvas.itemconfig(3, state='hidden')
     canvas.itemconfig(4, state='normal')
     canvas.itemconfig(5, state='normal') # not showing up
     canvas.itemconfig(6, state='normal')
     canvas.itemconfig(7, state='normal')

    
    
    
def move_masse():
    if(state):
        canvas.move(main_circle2, xe, ye)
    


# ................................ Functions .................................
# Menu Functions .......................

def startSimul():
    update(xe,ye)
    #move_masse()
    print("hello")
    window.after(30, startSimul)




    
    
    #Entry functions ....................
    
def submit(entry):
    variable = entry.get()
    if(entry==entryLongueur):
        L = variable
    elif(entry == entryMasse):
        m = variable
    elif(entry == entryHauteur):
        h = variable
    elif (entry == entryDecalage):
        x0 = variable
    elif(entry == entryVitRot):
        vit_rot = variable

def delete(entry):
    entry.delete(0,END)


    


          
          
def create_circle(x, y, r, canvasName, color, w): # easier way to make a circle
    x0 = x - r
    y0 = y-r
    x1 = x + r
    y1 = y + r
    return canvasName.create_oval(x0, y0, x1, y1, fill = color, width = w)          



# ....................... Calculate Operations .........................


def draw_nocoriolis(x,y):
    create_circle(x,y,7,canvas, "red", 1) # mass position

def draw_coriolis(x,y):
    create_circle(x,y,7,canvas, "red", 1) # mass position

def update(xe,ye):
    xe = xe +1000
    ye = ye + 50
    


    



def create_init_widgetsandfunctions():
    
    def clearSimul():
        entryLongueur.delete(0,END)
        entryMasse.delete(0,END)
        entryHauteur.delete(0,END)
        entryDecalage.delete(0,END)
        entryVitRot.delete(0,END)
        
        
    def move_masse(xe,ye):
        if(state):
            canvas.move(main_circle2, xe, ye)
        
    def update(xe,ye):
        xe = xe +1000
        ye = ye + 50
        return xe,ye
        
    def startSimul():
        
        for x in range(20):
            update(xe,ye)
            move_masse(xe,ye)
            time.sleep(0.5)
            print("hello")
        print("finished")
    
    
    
    
    a = IntVar()
    
    def display():
        if(a.get()==1): # Force de Coriolis est présente
            
            entryVitRot.place(x=5, y =670)
            submitVitRot.place(x=230, y=670)
            deleteVitRot.place(x=280, y=670)
            VitesseRot.place(x=5, y= 620)
            print("a =1")
            
            canvas.itemconfig(1, state='normal')
            canvas.itemconfig(2, state='normal')
            canvas.itemconfig(3, state='normal')
            canvas.itemconfig(4, state='hidden')
            canvas.itemconfig(5, state='hidden')
            canvas.itemconfig(6, state='hidden')
            canvas.itemconfig(7, state='hidden')
       
            
        else:   # Pas de force de Coriolis
            
            VitesseRot.place_forget()
            entryVitRot.place_forget()
            submitVitRot.place_forget()
            deleteVitRot.place_forget()
            
            canvas.itemconfig(1, state='hidden')
            canvas.itemconfig(2, state='hidden')
            canvas.itemconfig(3, state='hidden')
            canvas.itemconfig(4, state='normal')
            canvas.itemconfig(5, state='normal')
            canvas.itemconfig(6, state='normal')
            canvas.itemconfig(7, state='normal')
        
            print("a=0")
    
    
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
    
    HauteurInitiale = Label(window, text="Hauteur initiale du smartphone", 
                    font =('Arial', 14),
                    fg = 'black', bg='white', 
                    relief = SUNKEN,
                    bd = 2,
                    padx = 0, pady = 0)
    
    DecalageInitial = Label(window, text="Decalage initial du smartphone par rapport au support", 
                    font =('Arial', 14),
                    fg = 'black', bg='white', 
                    relief = SUNKEN,
                    bd = 2,
                    padx = 0, pady = 0)
    
    VitesseRot = Label(window, text="Vitesse de rotation selon l'axe y", 
                    font =('Arial', 14),
                    fg = 'black', bg='white', 
                    relief = SUNKEN,
                    bd = 2,
                    padx = 0, pady = 0)
    
    check_Coriol = Checkbutton(window, text = "Force de Coriolis",
                               variable = a, onvalue=1, offvalue= 2,
                               command = display)
    
    check_Resist = Checkbutton(window, text = "Frottements")
    
    # Menu Bar  .......................................................  
    
    menubar = Menu(window)
    window.config(menu = menubar)
    
    
    
    
    simulMenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Simulation", menu = simulMenu)
    simulMenu.add_command(label ="Run Simulation", command = startSimul)
    simulMenu.add_command(label ="Clear Parameters", command = clearSimul)
    
    
    
    # ................. Create entries for parameters ........................
    # First parameter ......................
        
    
    entryLongueur = Entry(window, font =("Arial",14))
    submitLong = Button(window, text ="Submit", command=lambda:    submit(entryLongueur, L))
    deleteLong = Button(window, text ="Clear", command=lambda:   delete(entryLongueur))
        
    # Second Parameter
        
    entryMasse = Entry(window, font =("Arial",14))
    submitMasse = Button(window, text ="Submit", command=lambda:  submit(entryMasse))
    deleteMasse = Button(window, text ="Clear", command= lambda: delete(entryMasse))
        
        
    # Third Parameter
        
    entryHauteur = Entry(window, font =("Arial",14))
    submitHauteur = Button(window, text ="Submit", command=lambda:   submit(entryHauteur))
    deleteHauteur = Button(window, text ="Clear", command=lambda:   delete(entryHauteur))
        
        
    # Fourth Parameter
        
    entryDecalage = Entry(window, font =("Arial",14))
    submitDecalage = Button(window, text ="Submit", command=lambda:   submit(entryHauteur))
    deleteDecalage = Button(window, text ="Clear", command=lambda:   delete(entryHauteur))
        
        
    entryVitRot = Entry(window, font =("Arial",14))
    submitVitRot = Button(window, text ="Submit", command=lambda:   submit(entryHauteur))
    deleteVitRot = Button(window, text ="Clear", command=lambda:   delete(entryHauteur))


     # ........................ Placing the widgets ........................
    
    # ........................ Left Side Creation .........................
    # Place Labels :
    Titre.place(x=450, y=0)
    Texte_Parametrage.place(x=5, y=75)
    LongueurFil.place(x=5, y=170)
    MasseSmartphone.place(x=5, y=270)
    HauteurInitiale.place(x=5, y=370)
    DecalageInitial.place(x=5, y=470)
    
    # Place buttons
    check_Coriol.place(x=5, y=570)
    check_Resist.place(x=130, y=570)
    
    entryLongueur.place(x=5, y =200)
    submitLong.place(x=230, y=200)
    deleteLong.place(x=280, y=200)
    
    entryMasse.place(x=5, y =300)
    submitMasse.place(x=230, y=300)
    deleteMasse.place(x=280, y=300)
    
    entryHauteur.place(x=5, y =400)
    submitHauteur.place(x=230, y=400)
    deleteHauteur.place(x=280, y=400)
    
    entryDecalage.place(x=5, y =500)
    submitDecalage.place(x=230, y=500)
    deleteDecalage.place(x=280, y=500)
    
    
    
    
    
    # .......................... Right Side Creation ..................
    
    canvas.place(x = 800, y = 200)

    return a



    
    
def clear_screen():
    canvas.delete('all')
    

    
    
    
# ......................... END OF LEFT SIDE .........................


# ........................ START OF RIGHT SIDE .......................

# ......................... Canvas Creation .......................










    
    
window, canvas = initialize_window()
main_circle = initialize_foucault()
main_circle2, main_line2 = initialize_pendule_simple()
hide_foucault()
create_init_widgetsandfunctions()

 

    
# ...............................................................
#window.after(30, startSimul)
window.mainloop()