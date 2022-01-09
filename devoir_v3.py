
#****************************************************************************************************
#Titre :                 Jeu de la vie
#Ressources utilises :   Python, Tkinter, Random
#Auteurs :               MOHAMED Ahamed, MULLIER Léo
#Date de mise jour :     09/01/22
#****************************************************************************************************

#****************************************************************************************************
# DECLARATION DES MODULES
#****************************************************************************************************

from tkinter import *
from math import *
from random import Random, randrange
import time

#****************************************************************************************************
# DECLARATION DES FONCTIONS
#****************************************************************************************************

#========== INITIALISATION D'UNE MATRICE ALEATOIRE ==========#
def init():
    global ncases
    global largeur
    global tab
    global varvie
    #print(vie.get())
    varvie=vie.get()
    ncases = scaletaille.get()
    #print ('heee')
    print(scaletaille.get())
    largeur = 500/ncases
    for i in range(0,ncases):
        for j in range(0,ncases):
            rando=randrange(1,101)
            #m[i,j]=randrange(0,2)
            if(rando<=varvie):
                tab[i,j]=1
            else:
                tab[i,j]=0
    dessiner()

#========== AFFICHAGE D'UNE MATRICE GRAPHIQUE ==========#
def dessiner():
    global canvas
    global ncases
    canvas.delete(ALL)
    canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
    canvas.bind("<Button-1>", clic_case)
    for i in range(ncases):
        x = i * largeur
        for j in range(ncases):
            y = j * largeur
            if tab[i,j]==0:
                canvas.create_rectangle(x, y, x+largeur, y+largeur, fill='white') 
            else:
                canvas.create_rectangle(x, y, x+largeur, y+largeur, fill='red')

#========== AFFICHAGE D'UNE MATRICE NUMERIQUE CONSOLE ==========#
def printer(ncases):
    for i in range(0,ncases):
        for j in range(0,ncases):
            print(" ",tab[i,j], end='')
        print("\n")

#========== CREATION DE LA GENERATION SUIVANTE ==========#        
def jeu():
    global ncases
    global largeur
    global tab
    ncases = scaletaille.get()
    #print ('heee')
    #print(scaletaille.get())
    largeur = 500/ncases
    global flag
    #while flag>0:
    voisins_vivants=0
    voisins_morts=0
    nb=ncases-1
    m=tab
    new={}
    #print("0**************************************************")
    for i in range(0,nb+1):
        for j in range(0,nb+1):
            voisins_vivants=0
            voisins_morts=0
            #voisin de dessous
            if(m[(i+1+nb)%nb,(j+nb)%nb]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin du dessus
            if(m[(i-1+nb)%nb,(j+nb)%nb]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin de droite
            if(m[(i+nb)%nb,(j+1+nb)%nb]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin de gauche
            if(m[(i+nb)%nb,(j-1+nb)%nb]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin de diago
            if(m[(i+1+nb)%nb,(j+1+nb)%nb]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin du diago
            if(m[(i-1+nb)%nb,(j+1+nb)%nb]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin de diago
            if(m[(i-1+nb)%nb,(j-1+nb)%nb]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #voisin de diago
            if(m[(i+1+nb)%nb,(j-1)%nb]==0):
                voisins_morts+=1
            else:
                voisins_vivants+=1
            #print("voisin vivants=",voisins_vivants)   
            if m[i,j]==1:
                if voisins_vivants==2 or voisins_vivants==3:
                    new[i,j]=1
                elif voisins_vivants>=4:
                    new[i,j]=0
                elif voisins_vivants<=1:
                    new[i,j]=0
            else:
                if voisins_vivants==3:
                    new[i,j]=1
                else:
                    new[i,j]=0
    tab=new
    #print("nbvivants",voisins_vivants)
    dessiner()
    #print("5**************************************************")
    global vitesse
    vitess=vitesse.get()
    if flag >0: 
        fgauche.after(vitess,jeu)

#========== AFFICHAGE DU A PROPOS ==========#
def credits():
    global canvas
    canvas.delete(ALL)
    canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
    canvas.create_text(250,75,text="Titre : Jeu de la vie\nRessources utilises : Python, Tkinter, Random\nAuteurs : MOHAMED Ahamed, MULLIER Leo\nDate de mise jour : 09/01/22\nIl s'agit du troisieme devoir propose dans le cadre de l'UV SR01 dispensee a l'UTC.\nOn utilise ici l'interface graphique proposee par Tkinter et le langage de\nprogrammation Python pour mettre en place les mecanismes du jeu de la vie.") 
           
#========== LANCER SIMULATION ==========#
def lancer():
    global flag
    print ("Demarrage de la simulation")
    if flag ==0:
        flag =1
        jeu()

#========== STOPPER SIMULATION ==========#
def arret():
    print("Arret de la simulation")
    global flag    
    flag =0

#========== MODIFIER LA VALEUR D'UNE CASE MANUELLEMENT ==========#
def clic_case(event): #fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au dico_case
    global tab
    global ncases
    global largeur
    global canvas
    largeur = 500/ncases
    case_x = event.x // largeur
    case_y = event.y // largeur
    #z="n="+str(ncases)+" l="+str(largeur)+" x="+str(case_x)+" et y="+str(case_y)+"\n"
    #print(z)
    x=case_x
    y=case_y
    if tab[x,y]==1:
        canvas.create_rectangle(x*largeur, y*largeur, x*largeur+largeur, y*largeur+largeur, fill='white')
        tab[x,y]=0
    else:
        canvas.create_rectangle(x*largeur, y*largeur, x*largeur+largeur, y*largeur+largeur, fill='red')
        tab[x,y]=1

#****************************************************************************************************
# MISE EN PLACE DU PROGRAMME
#**************************************************************************************************** 

#========== INITIALISATION DU PROGRAMME ==========#
print("\n          | Le jeu de la vie\n          | MOHAMED Ahamed, MULLIER Leo\n")
vitesse=50
tab={}
ncases=1
flag=0

#========== PREPARATION DES MATRICES ==========#
fenetre = Tk()
fenetre.title("SR01 - Devoir 3")
fenetre.geometry("657x512")
fenetre.resizable(width=False, height=False)

#========== CREATION DU MENU ==========#
menubar = Menu(fenetre)  

file = Menu(menubar, tearoff=0)
file.add_command(label="Demarrer la simulation", command =lancer)  
file.add_command(label="Arreter la simulation", command=arret)
file.add_command(label="Initialiser la grille", command=init)
file.add_separator() 
file.add_command(label="Quitter", command=fenetre.quit)  
menubar.add_cascade(label="Fichier", menu=file) 

help = Menu(menubar, tearoff=0)  
help.add_command(label="A propos du projet", command=credits)  
menubar.add_cascade(label="Aide", menu=help)  

#========== DISPOSITION DE LA FENETRE ==========#
fenetre.config(menu=menubar)  

fgauche = Frame(fenetre)
fgauche.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=5, pady=5)

fdroite = Frame(fenetre, height=500, width=30, padx=5, pady=2)
fdroite.pack(side = RIGHT, fill = Y)

#========== CREATION DES BOUTONS/CURESEURS DE DROITE ==========#
btnlancer = Button(fdroite, text="Demarrer la simulation", relief=RAISED, height=2, width=18, command =lancer)  
btnlancer.pack(anchor=CENTER, side=TOP) 

btnarreter = Button(fdroite, text="Arreter la simulation", relief=RAISED, height=2, width=18, command=arret)  
btnarreter.pack(anchor=CENTER, side=TOP) 

btnreset = Button(fdroite, text="Initialiser la grille", relief=RAISED, height=2, width=18, command=init)
btnreset.pack(anchor=CENTER, side=TOP) 

txtvide = Label(fdroite, text="  ")
txtvide.pack(anchor=CENTER, side=TOP)

txttaille = Label(fdroite, text="Taille de la grille")
txttaille.pack(anchor=CENTER, side=TOP)

taille = DoubleVar()
scaletaille = Scale(fdroite, variable = taille, from_ = 1, to = 100, orient = HORIZONTAL)  
scaletaille.pack(anchor=CENTER, side=TOP) 

txtvie = Label(fdroite, text="Pourcentage de vie")
txtvie.pack(anchor=CENTER, side=TOP)

vie = IntVar() 
scalevie = Scale(fdroite, variable = vie, from_ = 0, to = 100, orient = HORIZONTAL)  
scalevie.pack(anchor=CENTER, side=TOP)  
varvie=vie.get()
txtvitesse = Label(fdroite, text="Vitesse d'evolution(ms)")
txtvitesse.pack(anchor=CENTER, side=TOP)

vitesse = IntVar()  
scalevitesse = Scale(fdroite, variable = vitesse, from_ = 1, to = 10000, orient = HORIZONTAL)  
scalevitesse.pack(anchor=CENTER, side=TOP)  

btnquitter = Button(fdroite, text="Quitter le programme", fg="red", relief=RAISED, height=2, width=18, command=fenetre.destroy)
btnquitter.pack(anchor=CENTER, side=BOTTOM) 

#========== CREATION DU CANVAS GAUCHE ==========#
largeur = 500/ncases
canvas = Canvas(fgauche, bg="white")
canvas.bind("<Button-1>", clic_case)
canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)

#========== EXECUTION PRINCIPALE ==========#
fenetre.mainloop()
