
#****************************************************************************************************
#Titre :                 Jeu de la vie
#Ressources utilisées :  Python, Tkinter, Random
#Auteurs :               MOHAMED Ahamed, MULLIER Léo
#Date de mise à jour :   23/12/21
#****************************************************************************************************

#****************************************************************************************************
# DECLARATION DES MODULES
#****************************************************************************************************

from tkinter import *
from random import Random, randrange

#****************************************************************************************************
# DECLARATION DES FONCTIONS
#****************************************************************************************************

#========== INITIALISATION D'UNE MATRICE ALEATOIRE ==========#
def init(ncases):
    for i in range(0,ncases):
        for j in range(0,ncases):
            m[i,j]=randrange(0,2)
    return m

#========== AFFICHAGE D'UNE MATRICE ==========#
def printer(ncases):
    for i in range(0,ncases):
        for j in range(0,ncases):
            print(" ",tab[i,j], end='')
        print("\n")

#========== CREATION DE LA GENERATION SUIVANTE ==========#        
def jeu(m,ncases):
    voisins_vivants=0
    voisins_morts=0
    ncases=ncases-1
    for i in range(0,ncases+1):
        for j in range(0,ncases+1):
            voisins_vivants=0
            voisins_morts=0
            #voisin de dessous
            if(m[(i+1+ncases)%ncases,(j+ncases)%ncases]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin du dessus
            if(m[(i-1+ncases)%ncases,(j+ncases)%ncases]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin de droite
            if(m[(i+ncases)%ncases,(j+1+ncases)%ncases]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin de gauche
            if(m[(i+ncases)%ncases,(j-1+ncases)%ncases]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin de diago
            if(m[(i+1+ncases)%ncases,(j+1+ncases)%ncases]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin du diago
            if(m[(i-1+ncases)%ncases,(j+1+ncases)%ncases]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin de diago
            if(m[(i-1+ncases)%ncases,(j-1+ncases)%ncases]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin de diago
            if(m[(i+1+ncases)%ncases,(j-1)%ncases]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
                
            #print("voisin vivants=",voisins_vivants)   
            if m[i,j]==1:
                if voisins_vivants==2 or voisins_vivants==3:
                    n[i,j]=1
                elif voisins_vivants>=4:
                    n[i,j]=0
                elif voisins_vivants<=1:
                    n[i,j]=0
            else:
                if voisins_vivants==3:
                    n[i,j]=1
                else:
                    n[i,j]=0
    return n




#****************************************************************************************************
# MISE EN PLACE DU PROGRAMME
#**************************************************************************************************** 

#========== INITIALISATION DU PROGRAMME ==========#
print("\n          | Le jeu de la vie\n          | MOHAMED Ahamed, MULLIER Leo\n")

#========== PREPARATION DES MATRICES ==========#
m={}
n={}
m=init(10)
tab=m
printer(10)
#print(tab[1,2])
#print(tab[1,3])
times=1

tab=jeu(m,10)
printer(10)
while(times<=10):
    print("tours ",times)
    tab=jeu(tab,10)
    printer(10)
    
    times+=1
#print(tab[1,2])
#print(tab[1,3])
#
#

def tester (taille_tab):
    
    taille_tab = scaletaille.get()
    print ('heee')
    print(scaletaille.get())

fenetre = Tk()
fenetre.title("SR01 - Devoir 3")
fenetre.geometry("657x512")
fenetre.resizable(width=False, height=False)

fgauche = Frame(fenetre)
fgauche.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=5, pady=5)

fdroite = Frame(fenetre, height=500, width=18, padx=5, pady=5)
fdroite.pack(side = RIGHT, fill = Y)

menubar = Menu(fenetre)  
file = Menu(menubar, tearoff=0)  
file.add_command(label="Nouveau")  
file.add_command(label="Demarrer la simulation")  
file.add_command(label="Arreter la simulation")
file.add_separator() 
file.add_command(label="Quitter", command=fenetre.quit)  
menubar.add_cascade(label="Fichier", menu=file) 
 
help = Menu(menubar, tearoff=0)  
help.add_command(label="A propos du projet")  
menubar.add_cascade(label="Aide", menu=help)  

fenetre.config(menu=menubar)  

btnlancer = Button(fdroite, text="Demarrer la simulation", relief=RAISED, height=2, width=18)  
btnlancer.pack(anchor=CENTER, side=TOP) 

btnarreter = Button(fdroite, text="Arreter la simulation", relief=RAISED, height=2, width=18)  
btnarreter.pack(anchor=CENTER, side=TOP) 
def changer_couleur (event,i,j):
    ["rec",i,"_",j].configure(fill="red")

def changer_taille (event):
    taille_tab = scaletaille.get()
    print ('heee')
    print(scaletaille.get())
    largeur = 500/taille_tab
    canvas = Canvas(fgauche, bg="white")
    canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)

    for i in range(taille_tab):
        y = i * largeur
        for j in range(taille_tab):
            x = j * largeur
            globals()['rec',i,'_',j]=canvas.create_rectangle(x, y, x+largeur, y+largeur, fill="white")
            ['rec',i,'_',j].bind('<ButtonRelease>', changer_couleur(i,j))

btnreset = Button(fdroite, text="Initialiser la grille", relief=RAISED, height=2, width=18)
btnreset.pack(anchor=CENTER, side=TOP) 
btnreset.bind('<ButtonRelease>', changer_taille)

txtvide = Label(fdroite, text="  ")
txtvide.pack(anchor=CENTER, side=TOP)

txttaille = Label(fdroite, text="Taille de la grille")
txttaille.pack(anchor=CENTER, side=TOP)

taille = DoubleVar()
scaletaille = Scale(fdroite, variable = taille, from_ = 1, to = 100, orient = HORIZONTAL)  
scaletaille.pack(anchor=CENTER, side=TOP) 

txtvie = Label(fdroite, text="Pourcentage de vie")
txtvie.pack(anchor=CENTER, side=TOP)

vie = DoubleVar()  
scalevie = Scale(fdroite, variable = vie, from_ = 0, to = 100, orient = HORIZONTAL)  
scalevie.pack(anchor=CENTER, side=TOP)  

txtvitesse = Label(fdroite, text="Vitesse d'evolution")
txtvitesse.pack(anchor=CENTER, side=TOP)

vitesse = DoubleVar()  
scalevitesse = Scale(fdroite, variable = vitesse, from_ = 1, to = 10, orient = HORIZONTAL)  
scalevitesse.pack(anchor=CENTER, side=TOP)  

btnquitter = Button(fdroite, text="Quitter le programme", fg="red", relief=RAISED, height=2, width=18)
btnquitter.pack(anchor=CENTER, side=BOTTOM) 

#taille_tab = 10
#largeur = 500/taille_tab

#canvas = Canvas(fgauche, bg="white")
#canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)

#for i in range(taille_tab):
#    y = i * largeur
#    for j in range(taille_tab):
#        x = j * largeur
#        canvas.create_rectangle(x, y, x+largeur, y+largeur, fill="white")



fenetre.mainloop()