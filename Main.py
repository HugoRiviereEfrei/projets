import os
import math
import time
from pre_traitement import *
from post_traitement import *
from tf_idf import *





    
    
            
def main():
    """void -> void
    Interface d'utilisation du programme """
    Boucle = True
    while Boucle :
        minuscule()
        enlever()
        os.chdir("..")
        dico = calculer_tf_idf("cleaned")
        demande = int(input("Quelle est votre demande ?" + "\n" +\
                            "1- Liste des President" + "\n" +\
                            "2- Liste des mots non imporants" + "\n" +\
                            "3- Le mot le plus dit par les president" + "\n" +\
                            "4- Mot le plus dit par " + "\n"+\
                            "5- Qui a dit le mot " + "\n"+\
                            "6- Quelle est l'anner des premier election des president" + "\n" +\
                            "7- Premier President a avoir parler d'un theme" +"\n"+\
                            "8- Liste des mot dit par tout les president" + "\n"+\
                            "9- Sortie" + "\n"))
        
        while demande not in [1,2,3,4,5,6,7,8,9]:
            demande = int(input("Quelle est votre demande ?" + "\n" +\
                            "1- Liste des President" + "\n" +\
                            "2- Liste des mot nom imporant" + "\n" +\
                            "3- Le mot le plus dit par les president" + "\n" +\
                            "4- Mot le plus dit par " + "\n" +\
                            "5- Qui a dit le mot " + "\n" +\
                            "6- Quelle est l'anner des premier election des president" + "\n"+\
                            "7- Premier President a avoir parler d'un theme" +"\n"+\
                            "8- Liste des mot dit par tout les president" + "\n"+\
                            "9- Sortie" +"\n"))
        if demande == 1:
            print("\n" +\
                  "Liste des president: ")
            tab = nom_des_presidents()
            t = prenom_des_presidents(tab)
            cpt = 1
            for cle, valeur in t.items():
               print(str(cpt) + "-" + valeur + " " + cle)
               cpt +=1
                        
        if demande == 2:
            tab = mot_non_important(dico)
            print("Il y a " + str(len(tab)) + " mots non importants :")
            print(tab)
        
        if demande == 3:
            a , b = TF_IDF_MAX(dico)
            print("\n" +\
                  "Le mot le plus dit par les president est '" + a + "' avec un TF-IDF de " + str(b))
            
        if demande == 4:
            name = int(input("\n" +\
                          "Chosiser un president :" + "\n" +\
                          "1- Chirac" + "\n" +\
                          "2- Giscard dEstaing " + "\n" +\
                          "3- Hollande" + "\n" +\
                          "4- Macron" + "\n" +\
                          "5- Mitterrand" + "\n" +\
                          "6- Sarkozy" + "\n"))
            while name not in [1,2,3,4,5,6]:
                name = int(input("\n" +\
                             "Chosiser un president :" + "\n" +\
                              "1- Chirac" + "\n" +\
                              "2- Giscard dEstaing " + "\n" +\
                              "3- Hollande" + "\n" +\
                              "4- Macron" + "\n" +\
                              "5- Mitterrand" + "\n" +\
                              "6- Sarkozy" + "\n"))
            tab = nom_des_presidents()
            clé , freq = mot_le_plus_dit_president(tab[name-1])
            print("le mot le plus dit par " + tab[name-1] + " est '" + clé + "' a une frequence de " + str(freq))
            
        if demande == 5:
            mot = str(input("\n" +\
                "Ecriver le mot que vous souhaiter chercher : "))
            tab = presidents_qui_ont_dit(mot)
            i = 0
            print("\n" +\
                  "Les president ayant dit '" + mot + "' sont :")
            while i < len(tab):
                print(str(i+1) + "- " + tab[i])
                i += 1 
            print("Le president ayant dit le plus de fois le mot '" + mot + "' est " + tab[0])
            
            
        if demande == 6:
            name = int(input("\n" +\
                          "Chosiser un president :" + "\n" +\
                          "1- Chirac" + "\n" +\
                          "2- Giscard dEstaing " + "\n" +\
                          "3- Hollande" + "\n" +\
                          "4- Macron" + "\n" +\
                          "5- Mitterrand" + "\n" +\
                          "6- Sarkozy" + "\n"))
            
            while name not in [1,2,3,4,5,6]:
                name = int(input("\n" +\
                              "Chosiser un president :" + "\n" +\
                              "1- Chirac" + "\n" +\
                              "2- Giscard dEstaing " + "\n" +\
                              "3- Hollande" + "\n" +\
                              "4- Macron" + "\n" +\
                              "5- Mitterrand" + "\n" +\
                              "6- Sarkozy" + "\n"))
            tab = nom_des_presidents()
            t = date_des_president()
            for i in range(len(t)):
                if tab[name-1] == t[i][0]:
                    print("\n" + tab[name-1] + " a été elu la premiere fois en " + str(t[i][1]))
                    
            
        if demande == 7:
            theme = str(input("\n" + "Entrer le theme que vous voulez chercher : "))
            tab = le_premier_sur_le_theme(theme)
            if len(tab) == 0:
                print("le mot ne ce trouve pas dans les Nomination")
            else :
                print("n\" + Les présidents ayant parlé du theme sont :" + "\n")
                for i in range(len(tab)):
                    print(str(i+1) + "- " + tab[i])
                    i += 1
                print("Le President qui en a parle en premier est " + tab[-1])
        
        if demande == 8:
            tab = mots_dits_par_tous_les_presidents()
            print("Il y a " + str(len(tab)) + " mots dit par tout les president  :")
            print(tab)
        if demande == 9:
            Boucle = False
        print("" + "\n")
        time.sleep(5) #Attendre 5s avant de relance le menu
        os.system("clear") #clear la console
    
    
main()

