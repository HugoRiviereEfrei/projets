import os
import math

def nom_des_presidents():
    """Recupere le Nom des president dans les titre et les ressort dans un tableau"""
    liste = os.listdir("speeches")
    liste = [fichier for fichier in liste if fichier.endswith(".txt")]
    tab = []
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
        liste = [ligne.lower() for ligne in lignes]
        os.chdir("../cleaned")
        with open(name, "w", encoding="utf-8") as f2:
            for l in liste:
                f2.write(l)
        os.chdir("../speeches")
        

def enlever():
    liste = os.listdir("..\cleaned")
    for name in liste:
        with open(name, "r", encoding="utf-8") as f:
            ligne = f.read()
        mod = ""
        for i in range(len(ligne)):
            if ligne[i] == "-":
                if i > 0 and ligne[i - 1] == "\n":
                    mod += ""
                else:
                    mod += " "
            if ligne[i] == "'":
                if ligne[i] == "l'":
                    mod = random.choice(["a","b"])
                else :
                    mod = "e"
            elif ligne[i] in "!#$%&()*+,./:;<=>?@[]^_`{|}~":
                mod += " "
            else:
                mod += ligne[i]
        with open(name, "w", encoding="utf-8") as f:
            f.write(mod)
            
"""
def word_occ_pres(text):
    pres =[[]*len(text)]
    for file in text:
        word_counts = {}
        if "Chirac" in file:
            with open(file, "r", encoding="utf-8") as f:
                ligne = f.read()

            words = ligne.split()
            

            for word in words:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1
            pres[0].append(word_counts)
        
        elif "Giscard" in file:
            with open(file, "r", encoding="utf-8") as f:
                ligne = f.read()

            words = ligne.split()
            

            for word in words:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1
            pres[1].append(word_counts)
        
        elif "Hollande" in file:
            with open(file, "r", encoding="utf-8") as f:
                ligne = f.read()

            words = ligne.split()
            

            for word in words:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1
            pres[2].append(word_counts)
        
        elif "Macron" in file:
            with open(file, "r", encoding="utf-8") as f:
                ligne = f.read()

            words = ligne.split()
            

            for word in words:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1
            pres[3].append(word_counts)
        
        elif "Mitterrand" in file:
            with open(file, "r", encoding="utf-8") as f:
                ligne = f.read()

            words = ligne.split()
            

            for word in words:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1
            pres[4].append(word_counts)
        
        elif "Sarkozy" in file:
            with open(file, "r", encoding="utf-8") as f:
                ligne = f.read()

            words = ligne.split()
            

            for word in words:
                if word not in word_counts:
                    word_counts[word] = 1
                else:
                    word_counts[word] += 1
            pres[5].append(word_counts)
    res = [pre for pre in pres if pre != []]
    return res


def idf():
    os.chdir("..\cleaned")
    doc_len = len(os.listdir())
    
    idfs = word_occ(os.listdir())

    for word, score in idfs.items():
        idfs[word] = math.log(doc_len / (score + 1))

    return idfs
        

def mot_non_important(dico):
    tab = []
    for cle, valeur in dico.items():
        if valeur == 0:
            tab.append(cle)
    return tab
        

def mot_plus_important(dico):
    tab = []
    val = max(dico.values())
    for cle, valeur in dico.items():
        if valeur == val:
            tab.append(cle)
    return tab
""" 
#Tout a refaire
            
            
tab_nom_president = nom_des_presidents()
nom_prenom_presiedent = prenom_des_presidents
minuscule()
enlever()

