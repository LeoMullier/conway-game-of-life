ttt
#****************************************************************************************************
#Titre :                 Jeu de la vie
#Ressources utilis�es :  Python, Tkinter, Random
#Auteurs :               MOHAMED Ahamed, MULLIER L�o
#Date de mise � jour :   23/12/21
#****************************************************************************************************

#****************************************************************************************************
# DECLARATION DES MODULES
#****************************************************************************************************

from tkinter import *
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
    ncases = scaletaille.get()
    print ('heee')
    print(scaletaille.get())
    largeur = 500/ncases
    for i in range(0,ncases):
        for j in range(0,ncases):
            #m[i,j]=randrange(0,2)
            tab[i,j]=0
    dessiner()

#========== AFFICHAGE D'UNE MATRICE ==========#
def dessiner():
    global canvas
    global ncases
    canvas.delete(ALL)
    canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
    canvas.bind("<Button-1>", clic_case)
    for i in range(ncases):
        y = i * largeur
        for j in range(ncases):
            x = j * largeur
            if tab[i,j]==0:
                canvas.create_rectangle(x, y, x+largeur, y+largeur, fill='white') 
            else:
                canvas.create_rectangle(x, y, x+largeur, y+largeur, fill='green')

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
    print ('heee')
    print(scaletaille.get())
    largeur = 500/ncases
    global flag
    #while flag>0:
    voisins_vivants=0
    voisins_morts=0
    nb=ncases-1
    m=tab
    new={}
    print("0**************************************************")
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
    print(tab)
    dessiner()
    print("5**************************************************")
    if flag >0: 
        fgauche.after(1000,jeu)

def lancer():
    global flag
    print ("Demarrage de la simulation")
    if flag ==0:
        flag =1
        jeu()

def arret():
    print("Arret de la simulation")
    global flag    
    flag =0

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
        canvas.create_rectangle(x*largeur, y*largeur, x*largeur+largeur, y*largeur+largeur, fill='green')
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

menubar = Menu(fenetre)  
file = Menu(menubar, tearoff=0)  
file.add_command(label="Nouveau")  
file.add_command(label="Demarrer la simulation", command =lancer)  
file.add_command(label="Arreter la simulation", command=arret)
file.add_command(label="Initialiser la grille", command=init)
file.add_separator() 
file.add_command(label="Quitter", command=fenetre.quit)  
menubar.add_cascade(label="Fichier", menu=file) 
 
help = Menu(menubar, tearoff=0)  
help.add_command(label="A propos du projet")  
menubar.add_cascade(label="Aide", menu=help)  

fenetre.config(menu=menubar)  

fgauche = Frame(fenetre)
fgauche.pack(side=LEFT, fill=BOTH, expand=TRUE, padx=5, pady=5)

fdroite = Frame(fenetre, height=500, width=18, padx=5, pady=5)
fdroite.pack(side = RIGHT, fill = Y)

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

vie = DoubleVar()  
scalevie = Scale(fdroite, variable = vie, from_ = 0, to = 100, orient = HORIZONTAL)  
scalevie.pack(anchor=CENTER, side=TOP)  

txtvitesse = Label(fdroite, text="Vitesse d'evolution")
txtvitesse.pack(anchor=CENTER, side=TOP)

vitesse = DoubleVar()  
scalevitesse = Scale(fdroite, variable = vitesse, from_ = 1, to = 10, orient = HORIZONTAL)  
scalevitesse.pack(anchor=CENTER, side=TOP)  

btnquitter = Button(fdroite, text="Quitter le programme", fg="red", relief=RAISED, height=2, width=18, command=fenetre.quit)
btnquitter.pack(anchor=CENTER, side=BOTTOM) 
largeur = 500/ncases
canvas = Canvas(fgauche, bg="white")
canvas.bind("<Button-1>", clic_case)
canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)


#can1 = Canvas(fen1, width =width, height =height, bg ='white')
#can1.bind("<Button-1>", click_gauche)
#can1.bind("<Button-3>", click_droit)
#can1.pack(side =TOP, padx =5, pady =5)

#m={}
#n={}
#m=init(10)

#def clic(event, c): #fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au dico_case
#    x = event.x -(event.x%c)
#    y = event.y -(event.y%c)
#    canvas.create_rectangle(x, y, x+c, y+c, fill='red')
#    dico_case[x,y]=1


#def affichage_mat (event):
#    taille_tab = scaletaille.get()
#    print ('heee')
#    print(scaletaille.get())
#    largeur = 500/taille_tab
#    canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
#    canvas.bind("<Button-1>", clic(largeur))
#    for i in range(taille_tab):
#        y = i * largeur
#        for j in range(taille_tab):
#            x = j * largeur
#            if m[i,j]==0:
#                canvas.create_rectangle(x, y, x+largeur, y+largeur, fill='white')         
#            else:
#                canvas.create_rectangle(x, y, x+largeur, y+largeur, fill='red')    

#tab=m
#printer(10)
##print(tab[1,2])
##print(tab[1,3])
#times=1

#tab=jeu(m,10)
#printer(10)
#while(times<=10):
#    print("tours ",times)
#    tab=jeu(tab,10)
#    printer(10)
    
#    times+=1
##print(tab[1,2])
##print(tab[1,3])
##
##

#def tester (taille_tab):
    
#    taille_tab = scaletaille.get()
#    print ('heee')
#    print(scaletaille.get())



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
















#from tkinter import *

#def damier(): #fonction dessinant le tableau
#    ligne_vert()
#    ligne_hor()
        
#def ligne_vert():
#    c_x = 0
#    while c_x != width:
#        can1.create_line(c_x,0,c_x,height,width=1,fill='black')
#        c_x+=c
        
#def ligne_hor():
#    c_y = 0
#    while c_y != height:
#        can1.create_line(0,c_y,width,c_y,width=1,fill='black')
#        c_y+=c

#def click_gauche(event): #fonction rendant vivante la cellule cliquée donc met la valeur 1 pour la cellule cliquée au dico_case
#    x = event.x -(event.x%c)
#    y = event.y -(event.y%c)
#    can1.create_rectangle(x, y, x+c, y+c, fill='black')
#    dico_case[x,y]=1

#def click_droit(event): #fonction tuant la cellule cliquée donc met la valeur 0 pour la cellule cliquée au dico_case
#    x = event.x -(event.x%c)
#    y = event.y -(event.y%c)
#    can1.create_rectangle(x, y, x+c, y+c, fill='white')
#    dico_case[x,y]=0

#def change_vit(event): #fonction pour changer la vitesse(l'attente entre chaque étape)
#    global vitesse
#    vitesse = int(eval(entree.get()))
#    print(vitesse)

#def canon(): #fonction dessinant le célèbre canon à planeur de Bill Gosper
#    dico_case[0*c,5*c]=1
#    dico_case[0*c,6*c]=1
#    dico_case[1*c,5*c]=1
#    dico_case[1*c,6*c]=1
#    dico_case[10*c,5*c]=1
#    dico_case[10*c,6*c]=1
#    dico_case[10*c,7*c]=1
#    dico_case[11*c,4*c]=1
#    dico_case[11*c,8*c]=1
#    dico_case[12*c,3*c]=1
#    dico_case[12*c,9*c]=1
#    dico_case[13*c,3*c]=1
#    dico_case[13*c,9*c]=1
#    dico_case[14*c,6*c]=1
#    dico_case[15*c,4*c]=1
#    dico_case[15*c,8*c]=1
#    dico_case[16*c,5*c]=1
#    dico_case[16*c,6*c]=1
#    dico_case[16*c,7*c]=1
#    dico_case[17*c,6*c]=1
#    dico_case[20*c,3*c]=1
#    dico_case[20*c,4*c]=1
#    dico_case[20*c,5*c]=1
#    dico_case[21*c,3*c]=1
#    dico_case[21*c,4*c]=1
#    dico_case[21*c,5*c]=1
#    dico_case[22*c,2*c]=1
#    dico_case[22*c,6*c]=1
#    dico_case[24*c,1*c]=1
#    dico_case[24*c,2*c]=1
#    dico_case[24*c,6*c]=1
#    dico_case[24*c,7*c]=1
#    dico_case[34*c,3*c]=1
#    dico_case[34*c,4*c]=1
#    dico_case[35*c,3*c]=1
#    dico_case[35*c,4*c]=1    
#    go()

#def go():
#    "démarrage de l'animation"
#    global flag
#    if flag ==0:
#        flag =1
#        play()
        
#def stop():
#    "arrêt de l'animation"
#    global flag    
#    flag =0
    
#def play(): #fonction comptant le nombre de cellules vivantes autour de chaque cellule
#    global flag, vitesse
#    v=0
#    while v!= width/c:
#        w=0
#        while w!= height/c:
#            x=v*c
#            y=w*c
            
#            # cas spéciaux:
#            # les coins
#            if x==0 and y==0: #coin en haut à gauche
#                compt_viv=0
#                if dico_case[x, y+c]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y+c]==1:
#                    compt_viv+=1
#                dico_etat[x, y]=compt_viv
#            elif x==0 and y==int(height-c): #coin en bas à gauche
#                compt_viv=0
#                if dico_case[x, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y]==1:
#                    compt_viv+=1
#                dico_etat[x, y]=compt_viv
#            elif x==int(width-c) and y==0: #coin en haut à droite
#                compt_viv=0
#                if dico_case[x-c, y]==1:
#                    compt_viv+=1
#                if dico_case[x-c, y+c]==1:
#                    compt_viv+=1
#                if dico_case[x, y+c]==1:
#                    compt_viv+=1
#                dico_etat[x, y]=compt_viv
#            elif x==int(width-c) and y==int(height-c): #coin en bas à droite
#                compt_viv=0
#                if dico_case[x-c, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x-c, y]==1:
#                    compt_viv+=1
#                if dico_case[x, y-c]==1:
#                    compt_viv+=1
#                dico_etat[x, y]=compt_viv
                
#            # cas spéciaux:
#            # les bords du tableau (sans les coins)    
#            elif x==0 and 0<y<int(height-c): # bord de gauche
#                compt_viv=0
#                if dico_case[x, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x, y+c]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y+c]==1:
#                    compt_viv+=1
#                dico_etat[x, y]=compt_viv
#            elif x==int(width-c) and 0<y<int(height-c): # bord de droite
#                compt_viv=0
#                if dico_case[x-c, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x-c, y]==1:
#                    compt_viv+=1
#                if dico_case[x-c, y+c]==1:
#                    compt_viv+=1
#                if dico_case[x, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x, y+c]==1:
#                    compt_viv+=1
#                dico_etat[x, y]=compt_viv
#            elif 0<x<int(width-c) and y==0: # bord du haut
#                compt_viv=0
#                if dico_case[x-c, y]==1:
#                    compt_viv+=1
#                if dico_case[x-c, y+c]==1:
#                    compt_viv+=1
#                if dico_case[x, y+c]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y+c]==1:
#                    compt_viv+=1
#                dico_etat[x, y]=compt_viv
#            elif 0<x<int(width-c) and y==int(height-c): # bord du bas
#                compt_viv=0
#                if dico_case[x-c, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x-c, y]==1:
#                    compt_viv+=1
#                if dico_case[x, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y]==1:
#                    compt_viv+=1
#                dico_etat[x, y]=compt_viv

#            #cas généraux
#            #les cellules qui ne sont pas dans les bords du tableau
#            else:
#                compt_viv=0
#                if dico_case[x-c, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x-c, y]==1:
#                    compt_viv+=1
#                if dico_case[x-c, y+c]==1:
#                    compt_viv+=1
#                if dico_case[x, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x, y+c]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y-c]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y]==1:
#                    compt_viv+=1
#                if dico_case[x+c, y+c]==1:
#                    compt_viv+=1
#                dico_etat[x, y]=compt_viv
                
#            w+=1
#        v+=1
#    redessiner()
#    if flag >0: 
#        fen1.after(vitesse,play)

        

#def redessiner(): #fonction redessinant le tableau à partir de dico_etat
#    can1.delete(ALL)
#    damier()
#    t=0
#    while t!= width/c:
#        u=0
#        while u!= height/c:
#            x=t*c
#            y=u*c
#            if dico_etat[x,y]==3:
#                dico_case[x,y]=1
#                can1.create_rectangle(x, y, x+c, y+c, fill='black')
#            elif dico_etat[x,y]==2:
#                if dico_case[x,y]==1:
#                    can1.create_rectangle(x, y, x+c, y+c, fill='black')
#                else:
#                    can1.create_rectangle(x, y, x+c, y+c, fill='white')
#            elif dico_etat[x,y]<2 or dico_etat[x,y]>3:
#                dico_case[x,y]=0
#                can1.create_rectangle(x, y, x+c, y+c, fill='white')
#            u+=1
#        t+=1
        
    
##les différentes variables:

## taille de la grille
#height = 400
#width = 400

##taille des cellules
#c = 10

##vitesse de l'animation (en réalité c'est l'attente entre chaque étapes en ms)
#vitesse=50

#flag=0
#dico_etat = {} #dictionnaire contenant le nombre de cellules vivantes autour de chaque cellule
#dico_case = {} #dictionnaire contenant les coordonnées de chaques cellules et une valeur 0 ou 1 si elles sont respectivement mortes ou vivantes
#i=0
#while i!= width/c: #assigne une valeur 0(morte) a chaque coordonnées(cellules) (valeur par défault en quelque sorte ^^)
#    j=0
#    while j!= height/c:
#        x=i*c
#        y=j*c
#        dico_case[x,y]=0
#        j+=1
#    i+=1

##programme "principal" 
#fen1 = Tk()

#can1 = Canvas(fen1, width =width, height =height, bg ='white')
#can1.bind("<Button-1>", click_gauche)
#can1.bind("<Button-3>", click_droit)
#can1.pack(side =TOP, padx =5, pady =5)

#damier()

#b1 = Button(fen1, text ='Go!', command =go)
#b2 = Button(fen1, text ='Stop', command =stop)
#b1.pack(side =LEFT, padx =3, pady =3)
#b2.pack(side =LEFT, padx =3, pady =3)
#b3 = Button(fen1, text ='Canon planeur', command =canon)
#b3.pack(side =LEFT, padx =3, pady =3)

#entree = Entry(fen1)
#entree.bind("<Return>", change_vit)
#entree.pack(side =RIGHT)
#chaine = Label(fen1)
#chaine.configure(text = "Attente entre chaque étape (ms) :")
#chaine.pack(side =RIGHT)

#fen1.mainloop()
