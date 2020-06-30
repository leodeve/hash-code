import sys
from tqdm import tqdm
import random
import copy

# POUR LIRE UNE LIGNE DU FICHIER TEXTE
def lire_livre(ligne): #retourne une liste pour chaque ligne
    liste = ligne.strip().split(" ") #strip empêche le retour à la ligne en lisant tous les caractères sauf le \n
    return liste

# POUR LIRE TOUT LE FICHIER
fichier="C:/Users/Android/Documents/Travail/Programmation/Python/Hash/f_libraries_of_the_world.txt"
def lire_tout(nom_fichier):
    with open(nom_fichier,'r') as f :
        livres = []
        for ligne in f:
            livres.append(lire_livre(ligne))
    return livres

resultat=lire_tout(fichier)


## POUR RECUPERER LES DONNEES
nbr_livres_tot = int(resultat[0][0])
nbr_lib = int(resultat[0][1])
nbr_jours_tot = int(resultat[0][2])
scores_livres = resultat[1]
for i in range(len(scores_livres)):
    scores_livres[i] = int(scores_livres[i])

def infos_lib(resultat):
  infos_lib = []
  liste_livres = []
  nbr_livres_lib = []
  tmps_signup = []
  livres_par_jour = []
  for i in range(2, nbr_lib*2+2, 2): #on veut les infos de chaque librairies. Il faut faire nbr_lib tours de boucle
    infos_lib.append(resultat[i])              #liste d'infos pour chaque librairie (liste de listes)
    liste_livres.append(resultat[i+1])         #liste de livres pour chaque librairie (liste de listes)
  for i in range(nbr_lib):
    nbr_livres_lib.append(infos_lib[i][0])      #nbr livres dans une librairie (liste de nb)
    tmps_signup.append(infos_lib[i][1])          #teps de sign up par lib
    livres_par_jour.append(infos_lib[i][2])        #nbr de livre scanable par jours
  ret = [liste_livres , nbr_livres_lib , tmps_signup , livres_par_jour]
  return ret

liste_livres = infos_lib(resultat)[0]
nbr_livres_lib = infos_lib(resultat)[1]
tmps_signup = infos_lib(resultat)[2]
livres_par_jour = infos_lib(resultat)[3]

#LIVRES A SCANNER
livres_scannes = nbr_livres_tot*[False]

#Toutes les librairies donnent le même nombre de points. Commencer par celles qui ont un temps de signup plus long.
#LISTE ORDRE LIBRAIRIES EN FONCTION DU TEMPS DE SIGNUP
def ordre_librairies():
    liste_ordre_librairie = []
    tmps_signup_temp = [int(tmps_signup[k]) for k in range(nbr_lib)]
    for i in range(nbr_lib):
        print("i = ",i)
        min = sys.maxsize
        for j in range(nbr_lib):
            if(tmps_signup_temp[j] < min):
                min = tmps_signup_temp[j]
                position_min = j
        tmps_signup_temp[position_min] = sys.maxsize
        liste_ordre_librairie.append(position_min)
    return liste_ordre_librairie

liste_ordre_librairie = ordre_librairies()


#LISTE DES LIVRES EN FONCTION DES POINTS QU'ILS RAPPORTENT (ORDRE DECROISSANT)
def ordre_livres(num_librairie): #Attention, chaque librairie a certains livres précis
    taille = len(liste_livres[num_librairie])
    liste_livres_ordonnee = []
    scores_livres_temp = copy.copy(scores_livres) #obligatoire pour ne pas réécrire sur scores_livres
    for i in range (taille):
        max = -2 #certains livres valent 0 points
        for j in range(taille): #on parcourt tous les livres de la librairie
            livre_temp = int(liste_livres[num_librairie][j])
            if(scores_livres_temp[livre_temp]>max):
                    max = scores_livres_temp[livre_temp]
                    position_max = livre_temp
        scores_livres_temp[position_max] = -2
        liste_livres_ordonnee.append(position_max)
        livres_scannes[position_max] = True
        scores_livres[position_max] = -1
    return liste_livres_ordonnee


# POUR CREER LE FICHIER TEXTE A ENVOYER
def submission():
        with open("C:/Users/Android/Documents/Travail/Programmation/Python/Hash/submission6.txt",'w') as f2 :
            f2.write(str(nbr_lib)+'\n')
            for i in tqdm(range(nbr_lib)): #pour chaque librairie
                num_librairie = liste_ordre_librairie[i] #amélioration : on prend dans l'ordre croissant des signup
                liste_livres_ordonnee = ordre_livres(num_librairie) #amélioration : on prend dans l'ordre décroissant des scores
                taille = len(liste_livres[num_librairie])
                f2.write(str(num_librairie) + " ") 
                f2.write(str(taille)+'\n') #nb de livres de la librairie
                for j in range(taille):
                    f2.write(str(liste_livres_ordonnee[j]) + " ")
                f2.write('\n')

submission()
