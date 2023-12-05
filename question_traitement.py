

import random

from tf_idf import *


def question_spliting(texte):
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

def trouve_question_dans_texte(texte):
    t = []
    tab = question_spliting(texte)
    dico = calculer_tf_idf("cleaned")
    for i in range(len(tab)):
        for cle in dico.keys():
            if tab[i] == cle:
                t.append(cle)
    return t 
        

def TF_question(texte):
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

def IDF_question(texte):
    dico = {}
    d = calculer_idf("cleaned")
    tab = trouve_question_dans_texte(texte)
    for i in range(len(tab)):
        for cle, valeur in d.items():
            if cle == tab[i]:
                dico[cle] = valeur
    return dico


def TFIDF_question(texte):
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

def len_modif(texte):
    dico = {}
    d1 = TFIDF_question(texte)
    d2 = calculer_tf_idf("cleaned")
    for cle in d1.keys():
        for key, value in d2.items():
            if cle == key :
                dico[key] = value
    return 


def produit_scalaire(A, B):
    return sum(A.get(word, 0) * B.get(word, 0) for word in set(A.keys()) & set(B.keys()))

def norme_vecteur(A):
    return math.sqrt(sum(val**2 for val in A.values()))

def similarite_cosinus(A, B):
    produit = produit_scalaire(A, B)
    norme_A = norme_vecteur(A)
    norme_B = norme_vecteur(B)

    if norme_A == 0 or norme_B == 0:
        return 0

    return produit / (norme_A * norme_B)


def doc_similaire(texte):
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

def sim_max(texte):
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

a = doc_similaire("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?")
b= find_max_key_value(TFIDF_question("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"))


def reponse(text:str):
    a = doc_similaire(text)
    b= find_max_key_value(TFIDF_question(text))

    for line in open(f"cleaned/{a}", "r", encoding="utf-8").readlines():
        if "climat" in line:
            return line

print(reponse("Peux-tu me dire comment une nation peut-elle prendre soin du climat ?"))