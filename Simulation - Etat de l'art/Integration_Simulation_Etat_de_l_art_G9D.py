from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cmath as c
from math import pi
from math import sqrt
import turtle



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
    
     
def runSimulation():
    # Debut des calculs et de l'affichage des résultats
    
    def initialise():
        while True :
            try :
                global end
                global dt
                global t
                global teta
                global m
                global l
                global g
                global teta_zero
                global L
                global t
                global end


                end = 10000    #temps de simulation
                dt = 0.05
                t= np.linspace(0,end,int(150/dt)) # vecteur temps, discrétiser avec un pas de dt
                m = float(entryMasse.get())
                l = float(entryLong.get())      
                g = float(9.81)    
                teta =[]
                teta_zero = float(entryAngle.get()) 
                L = float(entryLatit.get()) 
                L = (L*pi/180) 
                if (teta_zero <= 90 and teta_zero >= -90) and (L <= 90 and L>= -90):
                    break
            except TypeError:
                pass
       
    initialise()

    j = complex(0,1)                                                                
    teta.append(teta_zero*pi/180)      #conversion en radian de teta                    
    
    Omega = (7.29)*(10**-5)            # La vitesse de rotation de la Terre sur elle-même c'est l'une des causes même de l'effet Coriolis 
    w = ((24*3600))/np.sin(L)          # vitesse angulaire
    omega_prime = np.sqrt(Omega**2 + w**2) # omega_prime est une variable mathématique qui nous aidera dans le calcul
    a = l*np.cos(teta_zero)              # C'est la position initiale du pendule dans le repère cartésien

    accel_ang =[] # On calcul l'acceération angulaire dans la base (ur,uteta,uz)
    vit_ang = []  
    accel_ang.append(0)
    vit_ang.append(0)
    sol = slice(0,len(t),20)

    """ Calcul de la vitesse angulaire """
    for k in range(1,len(t)):
        vit_ang.append(vit_ang[k-1]+accel_ang[k-1]*dt)
        teta.append(teta[k-1] + vit_ang[k]*dt)
        accel_ang.append(-(g/l)*np.sin(teta[k]))

    vit_angX = np.zeros_like(vit_ang)
    vit_angY = np.zeros_like(vit_ang)


    plt.figure('1')
    plt.subplot(3,1,1)
    plt.title("Vitesse angulaire pendule simple")
    plt.plot(t[sol],vit_angX[sol],'yellow',label = 'x')
    plt.xlabel("t en (s)")
    plt.ylabel("(rad/s) ")
    plt.legend()

    plt.subplot(3,1,2)
    plt.plot(t[sol],vit_angY[sol], 'red', label = 'y')
    plt.xlabel("t en (s)")
    plt.ylabel("(rad/s) ")
    plt.legend()

    plt.subplot(3,1,3)
    plt.plot(t[sol],vit_ang[sol],'blue', label = 'z')
    plt.xlabel("t en (s)")
    plt.ylabel("(rad/s) ")
    plt.legend()

    plt.show()
        
    """ Plot X,Z
    Via une projection on trouve la position dans le repère (X,Y,Z)"""

                                         
    X = l*np.sin(teta)         
    Z = l*(1-np.cos(teta))                                     


    """Mouvement suivant l'axe Y,Z force de Coriolis
    Nous nous plaçons à Paris Latitude 48.85 latitude Nord
    On fixe pour conditions initiales x = l*cos(teta), pendule laché sans vitesse initiale
     C = X + iY"""
    
    C = a*(np.cos(w*t) + j*(Omega/omega_prime)*np.sin(omega_prime*t))*np.exp(-j*Omega*t)    # Equation du mouvement du pendule de Foucault s'obtient en résolvant un système d'équation différentielle couplée 
    A = C.real
    B = C.imag
    P = []
    R = []

    """ Calcul vitesse angulaire """
    
    Vitesse_ang = [0]
    for k in C :
        P.append(c.phase(k)) # On calcul le vecteur phase 
        R.append(abs(k))     # On calcul le module
    Len = len(R)
    for i in range(1,Len):
        Vitesse_ang.append((R[i]-R[i-1])/(t[i]-t[i-1]))

    Vitesse_angX = np.zeros_like(Vitesse_ang)
    Vitesse_angY = np.zeros_like(Vitesse_ang)

    plt.figure('2')

    
    plt.subplot(3,1,1)
    plt.title("vitesse angulaire pendule Foucault")
    plt.plot(t[sol],Vitesse_angX[sol],'yellow', label = 'x')
    plt.xlabel("t en (s)")
    plt.ylabel("(rad/s) ")
    plt.legend()

    plt.subplot(3,1,2)
    plt.plot(t[sol],Vitesse_angY[sol],'red', label = 'y')
    plt.xlabel("t en (s)")
    plt.ylabel("(rad/s) ")
    plt.legend()

    plt.subplot(3,1,3)
    plt.plot(t[sol],Vitesse_ang[sol],'blue', label= 'z')
    plt.xlabel("t en (s)")
    plt.ylabel("(rad/s) ")
    plt.legend()

    plt.show()
    
                                         
    
    """ pendule avec amortissements dus au frottements visqueux """
    r = 0.16
    coef = 6*pi*r
    K = coef*r
    Nair = 0.018 * 10** -13
    teta_rad = (teta_zero*pi)/180
    Ta = 2*pi*sqrt(l/g)*(1+(teta_rad**2/16))
    wa = (2*pi)/Ta
    Lambda =  (K*Ta)/(m*l**2)
    
    
    
    if abs(Lambda)<1 :
        t1 = np.linspace(0,720,720)
        axeX_Y = np.zeros_like(t1)
        print('Cas complexe Lambda = ',Lambda)
        Beta = wa*sqrt(1-Lambda**2)
        Alpha = -Lambda*wa
        C1 = teta_rad
        C2 = (Lambda*(teta_rad))/(sqrt(1-Lambda**2))
        PosAng = np.exp(Alpha*t1)*(C1*np.cos(Beta*t1)+C2*np.sin(Beta*t1))
        derPosAng = Alpha*np.exp(Alpha*t1)*(C1*np.cos(Beta*t1) + C2*np.sin(Beta*t1)) + Beta*np.exp(Alpha*t1)*(-C1*np.sin(Beta*t1)+C2*np.cos(Beta*t1))
        

        plt.figure('4')
        plt.subplot(3,1,1)
        plt.title('Vitesse angulaire avec amortissement (Cas delta complexe) Lambda = '+ str(Lambda))
        plt.plot(t1,PosAng, 'green' ,label = 'z')
        plt.xlabel("t en (s) ")
        plt.ylabel("Vitesse en (rad/s)")
        plt.legend()

        plt.subplot(3,1,2)
        plt.plot(t1, axeX_Y,'red', label = 'y')
        plt.xlabel("t en (s)")
        plt.ylabel("(rad/s) ")
        plt.legend()

        plt.subplot(3,1,3)
        plt.plot(t1,axeX_Y,'blue', label = 'z')
        plt.xlabel("t en (s)")
        plt.ylabel("(rad/s) ")
        plt.legend()

        plt.show()
        
    else:
        t1 = np.linspace(0,200,200)
        axeX_Y = np.zeros_like(t1)
        print('Cas réel Lambda = ',Lambda)
        Beta = wa*sqrt(Lambda**2-1)     
        r1 = wa*(-Lambda + sqrt(Lambda**2 - 1))
        r2 = wa*(-Lambda - sqrt(Lambda**2 -1))
        A = (r2/(r2-r1))*(teta_rad)
        B = (r1/(r1-r2))*(teta_rad)
        PosAng = A*np.exp(r1*t1) + B*np.exp(r2*t1)
        derPosAng = r1*A*np.exp(r1*t1) + r2*B*np.exp(r2*t1)
        

        plt.figure('4')
        plt.subplot(3,1,1)
        plt.title('Vitesse angulaire avec amortissement (cas delta réel) Lamnda = ' + str(Lambda))
        plt.plot(t1,PosAng , 'green' , label = 'z')
        plt.xlabel("t en (s) ")
        plt.ylabel("Vitesse en (rad/s)")

        plt.subplot(3,1,2)
        plt.plot(t1,axeX_Y,'red', label = 'y')
        plt.xlabel("t en (s)")
        plt.ylabel("(rad/s) ")
        plt.legend()

        plt.subplot(3,1,3)
        plt.plot(t1,axeX_Y,'blue', label = 'z')
        plt.xlabel("t en (s)")
        plt.ylabel("(rad/s) ")
        plt.legend()

        plt.show()
    
                                         
 # Fin des calculs et de l'affichage des figures
    

        
        
def delete(entry):
    entry.delete(0,END)


    
def display():
    if(a.get()==1): # Force de Coriolis est présente
         
        
        canvas.itemconfig(1, state='normal')
        canvas.itemconfig(2, state='normal')
        canvas.itemconfig(3, state='normal')
        canvas.itemconfig(4, state='hidden')
        canvas.itemconfig(5, state='hidden')
        canvas.itemconfig(6, state='hidden')
        canvas.itemconfig(7, state='hidden')
   
        
    else:   # Pas de force de Coriolis
        
      
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
    
MasseSmartphone = Label(window, text="Masse du smartphone (en moyenne 0.15 kg)", 
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
    
MessageAffich = Label(window, text="Les plots s'affichent dans l'environnement de développement \nou dans une autre fenêtre (si vous n'utilisez pas d'environnement de développement)", 
                    font =('Arial', 12),
                    fg = 'black', bg='white', 
                    relief = SUNKEN,
                    bd = 2,
                    padx = 0, pady = 0)
    
check_Coriol = Checkbutton(window, text = "Animation Pendule de Foucault",
                           variable = a, onvalue=1, offvalue= 2,
                            command = display)
    
check_Resist = Checkbutton(window, text = "Frottements")

# Menu Bar  .......................................................  

menubar = Menu(window)
window.config(menu = menubar)


simulMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Simulation", menu = simulMenu)
simulMenu.add_command(label ="Run Simulation", command = runSimulation)
simulMenu.add_command(label ="Run Animation", command = updateScreen)
simulMenu.add_command(label ="Clear Parameters", command = clearSimul)




# ................. Create entries for parameters ........................
# First parameter ......................
    
entryLong = Entry(window, font =("Arial",14))
deleteLong = Button(window, text ="Clear", command=lambda:   delete(entryLong))
    
# Second Parameter
    
entryMasse = Entry(window, font =("Arial",14))
deleteMasse = Button(window, text ="Clear", command= lambda: delete(entryMasse))
    
    
# Third Parameter
    
entryAngle = Entry(window, font =("Arial",14))
deleteAngle = Button(window, text ="Clear", command=lambda:   delete(entryAngle))
    
    
# Fourth Parameter
    
entryLatit = Entry(window, font =("Arial",14))
deleteLatit = Button(window, text ="Clear", command=lambda:   delete(entryLatit))
    

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
MessageAffich.place(x=5, y=670)

# Place buttons
check_Coriol.place(x=5, y=570)
check_Resist.place(x=210, y=570)

entryLong.place(x=5, y =200)
deleteLong.place(x=230, y=200)

entryMasse.place(x=5, y =300)
deleteMasse.place(x=230, y=300)

entryAngle.place(x=5, y =400)
deleteAngle.place(x=230, y=400)

entryLatit.place(x=5, y =500)
deleteLatit.place(x=230, y=500)



# .......................... Right Side Creation ..................




# ...............................................................

window.mainloop()