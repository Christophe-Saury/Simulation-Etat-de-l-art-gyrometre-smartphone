# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 11:31:30 2022

@author: chris
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import cmath as c
from math import pi
import turtle



def pendule():

    
    
    """ Initialisation des variables"""
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
                m = float(1.5)
                l = float(1)       #définie par défaut à 1 mètre
                g = float(9.81)    #définie à défaut à 9.81
                teta =[]
                teta_zero = float(15)  #définit par défaut à 15
                L = float(48.52)       #Définie par défaut à la latitude de paris
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
    plt.title("Vitesse angulaire pendule foucault")
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
    plt.plot(X[sol],Z[sol])
    plt.title(" Trajectoire du pendule vue de face ")
    plt.xlabel("X")
    plt.ylabel("Z")
    plt.axis("equal")
    plt.show()


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
    plt.title("vitesse angulaire pendule simple")
    
    plt.subplot(3,1,1)
 
    plt.plot(t[sol],Vitesse_angX[sol],'yellow', label = 'x')
    plt.title("vitesse angulaire pendule simple")
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
    
                                         
    plt.plot(A[sol],B[sol],color = 'green')
    plt.title(" Trajectoire de Foucault vue de dessus")
    plt.xlabel(" axe Y")
    plt.ylabel("X")
    plt.axis("equal")

    plt.show()
    

        
pendule()    
        
    
    


    

    

    
