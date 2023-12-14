import string
import random
from tf_idf import *
import os
import math 
from post_traitement import *


def question_spliting(texte:str):
    """str -> list[str]
       Enleve les ponctuation d'un texte et renvoie un tableau ayant pour valeur les mot de la question en minuscule"""
    t = []
    for i in range(len(texte)):
        if texte[i] == "-":
            texte = texte[:i] + " " + texte[i + 1:]
        elif texte[i] == "'":
            if texte[i - 1] == "l":
                texte = texte[:i] + random.choice(["a ", "e "]) + texte[i + 1:]
            else:
                texte = texte[:i] + "e" + texte[i + 1:]
        elif texte[i] in "!#$%&()*+,./:;<=>?@[]^_`{|}~?":
            texte = texte[:i] + " " + texte[i + 1:]
        
    for val in texte.split():
        t.append(val.lower())

    return t

def trouve_question_dans_texte(texte:str):
    """str -> list[str]
       prend une question en valeur et supprime du tableau de question_spliting(texte) les mot qui ne sont pas dans les Nomination")"""
    t = []
    tab = question_spliting(texte)
    dico = calculer_tf_idf("cleaned")
    for i in range(len(tab)):
        for cle in dico.keys():
            if tab[i] == cle:
                t.append(cle)
    return t 
        

def TF_question(texte:str):
    """str -> dico[str] : float
    Calcule la frequence des mot dans la question a savoir (mot dans la question et dans le texte)/taille de la question"""
    dico = {}
    tab = trouve_question_dans_texte(texte)
    for val in tab:
        if val in dico.keys():
            dico[val] += 1
        else :
            dico[val] = 1
            
    for cle, valeur in dico.items():
        dico[cle] = valeur/len(tab)
    
    return dico

def IDF_question(texte:str):
    """str -> dico[str] : float
    Recuperer l'idf des mot present dans les nomination et la question (recuperer grace a calculer_idf de la parti 1)"""
    dico = {}
    d = calculer_idf("cleaned")
    tab = trouve_question_dans_texte(texte)
    for i in range(len(tab)):
        for cle, valeur in d.items():
            if cle == tab[i]:
                dico[cle] = valeur
    return dico


def TFIDF_question(texte:str):
    """str -> dico[str] : float
       renvoie un dico avec en valeur la multiplication des TF de la question et des idf des mot contenue dans les nomination"""
    dico = {}
    TF = TF_question(texte)
    IDF = IDF_question(texte)
    for key, value in TF.items():
        for cle, valeur in IDF.items():
            if cle == key:
                if key not in dico.keys():
                    dico[key] = TF[key] * IDF.get(key, 0)
                else :
                    dico[key] += TF[key] * IDF.get(key, 0)
    return dico

def len_modif(texte:str):
    """texte -> dico[str] : float
    ressort un dico des TF-IDF des nomination mais que les mot qui sont aussi présent dans la question"""
    dico = {}
    d1 = TFIDF_question(texte)
    d2 = calculer_tf_idf("cleaned")
    for cle in d1.keys():
        for key, value in d2.items():
            if cle == key :
                dico[key] = value
    return 


def produit_scalaire(A:dict, B:dict):
    """dico[str] : float, dico[str] : float -> dico[str] : float
       renvoie le produit sacalaire des 2 TFIDF par mot"""
    return sum(A.get(word, 0) * B.get(word, 0) for word in set(A.keys()) & set(B.keys()))  #Recupere les clé des 2 dico puis fait le produit des valeur des mot en commun (0 si le mot n'est pas dans les clé), fait la somme de tout les produit afin d'obtenir le produit scalaire" 

def norme_vecteur(A:dict):
    """dico[str] : float -> dico[str] : float
       renvoie la norme des vecteurs contenue en valeur du dico dans un dico ayant en clé les mot et la norme en valeur"""
    return math.sqrt(sum(val**2 for val in A.values()))

def similarite_cosinus(A:dict, B:dict):
    produit = produit_scalaire(A, B)
    norme_A = norme_vecteur(A)
    norme_B = norme_vecteur(B)

    if norme_A == 0 or norme_B == 0:
        return 0

    return produit / (norme_A * norme_B)


def doc_similaire(texte:str):
    A = TFIDF_question(texte)
    B = []
    tab = os.listdir("cleaned")
    for text in os.listdir("cleaned"):
        document_text = open(f"cleaned/{text}", "r", encoding="utf-8").read()
        document_tfidf = TFIDF_question(document_text)
        B.append(document_tfidf)
    similarites = [similarite_cosinus(A, doc) for doc in B]
    index_document_similaire = similarites.index(max(similarites))
    return tab[index_document_similaire]

def sim_max(texte:str):
    A = TFIDF_question(texte)
    B = []
    tab = os.listdir("cleaned")
    for text in os.listdir("cleaned"):
        document_text = open(f"cleaned/{text}", "r", encoding="utf-8").read()
        document_tfidf = TFIDF_question(document_text)
        B.append(document_tfidf)
    similarites = [similarite_cosinus(A, doc) for doc in B]
    return max(similarites)

def find_max_key_value(dictionary:dict):
    max_key = max(dictionary, key=lambda k: dictionary[k])
    max_value = dictionary[max_key]
    return max_key, max_value


def reperage(texte:str):
    index = []
    value = []
    res = ""
    file = doc_similaire(texte)
    val = TF_IDF_MAX(TFIDF_question(texte))
    with open(os.path.join("Duplicate", file), encoding="utf-8") as f:
        ligne = f.read()
        mot = ligne.split()
    for i in range(len(mot)):
        if mot[i][-1] in ".?!":
            index.append(i)
        if mot[i] == val[0]:
            value.append(i)
    with open(os.path.join("Duplicate", file), encoding="utf-8") as f:
        ligne = f.read()
        mot = ligne.split()
    for j in range(1,len(index)):
        if  value !=[]:
            if index[j-1] < value[0] and index[j] > value[0]:
                res += ' '.join(mot[index[j-1]+1:index[j]]) + "."
        else:
            res = "Je suis incapable de répondre à votre question"
    return res



def espacement():
    duplicate_folder = "Duplicate"
    if not os.path.exists(duplicate_folder):
        os.makedirs(duplicate_folder)
    liste = os.listdir("speeches")
    for name in liste:
        with open(os.path.join("speeches", name), "r", encoding="utf-8") as f:
            ligne = f.read()
        mod = ""
        for caractere in ligne:
            if caractere in string.punctuation:
                mod += " " + caractere
            else:
                mod += caractere
        with open(os.path.join(duplicate_folder, name), "w", encoding="utf-8") as f:
            f.write(mod)

def beautifier(texte:str):

    question_starters = {
        "Comment": "Après une étude approfondie, ",
        "Pourquoi": "En raison de divers facteurs, ",
        "Peux-tu": "Bien entendu, c'est tout à fait faisable! ",
        "Qu'est-ce que": "Permettez-moi de vous expliquer que ",
        "Quand": "À ce moment précis, ",
        "Où": "À cet endroit précis, ",
        "Est-ce que": "Absolument, oui! ",
        "Quel est": "Permettez-moi de détailler que ",
        "Combien": "En quantité, cela se traduit par ",
        "Quelle est": "Il est intéressant de noter que ",
        "Pouvez-vous": "Je vous assure que vous pouvez! ",
        "Connaissez-vous": "En effet, je suis bien informé sur ",
        "Que pensez-vous de": "Ma perspective sur cela est que ",
        "Avez-vous": "Bien sûr, j'ai ",
        "Seriez-vous capable de": "Assurément, je pourrais ",
    }
    
    rep = reperage(texte)
    
    for key, value in question_starters.items():
        if key in texte:
            rep = value + rep
    if rep[-1] != ".":
        rep+"."
    return rep
