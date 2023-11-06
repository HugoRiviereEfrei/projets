import os

def nom_des_presidents():
    """Recupere le Nom des president dans les titre et les ressort dans un tableau"""
    liste = os.listdir("speeches")
    tab = []
    for name in liste:
        name = name[11:]
        name = name.replace(".txt", "")
        if "1" in name:
            name = name.replace("1","")
        tab = [n for n in tab if '2' not in n]
        tab.append(name)       
    return tab
        

def prenom_des_presidents(tab):
    """Associe les nom des president et les prenom dans un dico"""
    dico = {}
    prenoms = ['Jacques', 'Valéry', 'François', 'Emmanuel', 'François', 'Nicolas']
    for i in range(len(tab)):
        dico[tab[i]] = prenoms[i]
    return dico
    
        

def minuscule():
    """Convertir les textes des 8 fichiers en minuscules et stocker les contenus dans de nouveaux fichiers. Les
nouveaux fichiers doivent être stockés dans un nouveau dossier appelé « cleaned ». Ce dossier doit se
situer dans le répertoire principal où se trouve le programme main.py et au même niveau que le répertoire
« speeches »"""
    if not os.path.exists("cleaned"):
        os.mkdir("cleaned")
    liste = os.listdir("speeches")
    os.chdir("speeches")
    print(liste)
    for name in liste:
        with open(name, "r", encoding="utf-8") as f:
            lignes = f.readlines()
        liste = [ligne.strip().lower() for ligne in lignes]
        os.chdir("../cleaned")
        with open(name, "w", encoding="utf-8") as f2:
            for l in liste:
                f2.write(l)
        os.chdir("../speeches")
                
        

        




            
            
tab_nom_president = nom_des_presidents()
nom_prenom_presiedent = prenom_des_presidents

minuscule()
