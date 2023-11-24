import os
import random

def nom_des_presidents():
    """void -> list[str]
        Retourne le nom de tout les présidents de "speeches"."""
    tab = []
    liste = os.listdir("speeches")
    for name in liste:
        if name[-3:] != "txt":
            liste.remove(name)
        else :
            name = name[11:]
            name = name.replace(".txt", "")
            if "1" in name:
                name = name.replace("1","")
            tab = [n for n in tab if '2' not in n]
            tab.append(name)       
    return tab
        

def prenom_des_presidents(tab):
    """list[str] -> dico{str : str}
    Retourne le prénom de tout les présidents de "speeches"."""
    dico = {}
    prenoms = ['Jacques', 'Valéry', 'François', 'Emmanuel', 'François', 'Nicolas']
    for i in range(len(tab)):
        dico[tab[i]] = prenoms[i]
    return dico
    
        

def minuscule():
    """void -> void
    Créé le dossier cleaned si il n'existe pas et y met une copie en minuscule des fichiers de "speeches"."""
    if not os.path.exists("cleaned"):
        os.mkdir("cleaned")
    liste = os.listdir("speeches")
    os.chdir("speeches")
    for name in liste:
        with open(name, "r", encoding="utf-8") as f:
            lignes = f.readlines()
        liste = [ligne.lower() for ligne in lignes]
        os.chdir("../cleaned")
        with open(name, "w", encoding="utf-8") as f2:
            for l in liste:
                f2.write(l)
        os.chdir("../speeches")
        

def enlever():
    """void -> void
    Enlèves chaque ponctuation et la remplace par un espace, sauf pour les apostrophes si il y a un "t" avant, on remplace aléatoirement " ' "
    par e ou par a, sinon on remplace par e. Tout les tiret sont remplacer par un espace si il sont entre 2 mot, sinon on les remplace par le vide"""
    liste = os.listdir("..\cleaned")
    for name in liste:
        with open("..\cleaned\\" + name, "r", encoding="utf-8") as f:
            ligne = f.read()
        mod = ""
        for i in range(len(ligne)):
            if ligne[i] == "-":
                if i > 0 and ligne[i - 1] == "\n":
                    mod += ""
                else:
                    mod += " "  
            elif ligne[i] == "'":
                if i + 1 < len(ligne) and ligne[i:i + 2] == "l'":
                    mod += random.choice(["a ", "e "])
                else:
                    mod += "e "              
            elif ligne[i] in "!#$%&()*+,./:;<=>?@[]^_`{|}~":
                mod += " "
            else:
                mod += ligne[i]
        with open("..\cleaned\\" + name, "w", encoding="utf-8") as f:
            f.write(mod)
            
            
def calculer_frequence_mots(chainee):
    """str -> Dico{str : int}
    Calcule la fréquence de chaque mot unique dans l'intégralité du texte."""
    frequence_mots = {}
    mots = chainee.split()
    for mot in mots:
        mot = mot.lower()
        frequence_mots[mot] = frequence_mots.get(mot, 0) + 1
    return frequence_mots