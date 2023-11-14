import os
import math
import random

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
            
            
def calculer_frequence_mots(chainee):
    frequence_mots = {}

    mots = chainee.split()
    for mot in mots:
        mot = mot.lower()
        frequence_mots[mot] = frequence_mots.get(mot, 0) + 1
    return frequence_mots

def TF_par_texte():
    analyse_textes = {}
    for texte in os.listdir("cleaned"):
        with open(f"cleaned/{texte}", "r", encoding="utf-8") as t:
            analyse_textes.update({texte: calculer_frequence_mots(t.readlines())})
    return analyse_textes
    
def calculer_idf(repertoire_corpus):
    nb_documents_contenant_mot = {}
    nb_doc = 0
    idf_scores = {}
    for fichier in os.listdir(repertoire_corpus):
        nb_doc += 1
        mots_dans_document = set()
        chemin_fichier = os.path.join(repertoire_corpus, fichier)
        with open(chemin_fichier, 'r', encoding='utf-8') as f:
            mots = f.read().split()
            mots_dans_document.update(set(mots))
        for mot in mots_dans_document:
            if mot in nb_documents_contenant_mot:
                nb_documents_contenant_mot[mot] += 1
            else:
                nb_documents_contenant_mot[mot] = 1
    for mot in nb_documents_contenant_mot:
        idf_scores[mot]= math.log(nb_doc / nb_documents_contenant_mot[mot])
    return idf_scores


def calculer_tf_idf(repertoire_corpus):
    idf_scores = calculer_idf(repertoire_corpus)

    # Parcourir les fichiers dans le répertoire
    for fichier in os.listdir(repertoire_corpus):
        if fichier.endswith(".txt"):
            chemin_fichier = os.path.join(repertoire_corpus, fichier)
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = f.read()
                # Calculer les scores TF pour chaque document
                tf_scores = calculer_frequence_mots(contenu)

                # Calculer les scores TF-IDF en multipliant les scores TF par les scores IDF
                tfidf_scores = {mot: tf_scores[mot] * idf_scores[mot] for mot in tf_scores}

    return tfidf_scores




def calculer_transposee(matrice):
    nb_lignes = len(matrice)
    nb_colonnes = len(matrice[0])
    transposee = [[matrice[j][i] for j in range(nb_lignes)] for i in range(nb_colonnes)]
    return transposee

def mot_non_important(matrice):
    liste_des_mot_non_important = []
    t = []
    liste = os.listdir("cleaned")  
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if matrice[i][j] == 0:
                tul = (i, j)
                t.append(tul)
    for indice in range(len(t)):
        with open("cleaned/" + liste[t[indice][0]], 'r', encoding='utf-8') as f:
                text = f.read()
                mots = text.split()
                liste_des_mot_non_important.append(mots[t[indice][1]])
    return set(liste_des_mot_non_important)


print(calculer_tf_idf("cleaned"))