import os
import math
import random

def nom_des_presidents():
    liste = os.listdir("speeches")
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
        with open(os.path.join(repertoire_corpus, fichier), 'r', encoding='utf-8') as f:
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
    tfidf_dict = {}
    files_names = [file for file in os.listdir(repertoire_corpus) if file.endswith(".txt")]
    for file_name in files_names:
        with open(os.path.join(f"cleaned", file_name), 'r') as file:
            text = file.read()
        tf_dict = calculer_frequence_mots(text)
        idf_dict = calculer_idf(repertoire_corpus)
        for word in tf_dict:
            if word not in tfidf_dict:
                tfidf_dict[word] = tf_dict[word] * idf_dict.get(word, 0)
            else:
                tfidf_dict[word] += tf_dict[word] * idf_dict.get(word, 0)
    return tfidf_dict


def mot_non_important(dico):
    tab = []
    for clé,val in dico.items():
        if val == 0.0:
            tab.append(clé)
    return tab 
 
 
def TD_IDF_MAX(dico):
    tab = []
    maxi = max(dico.values())
    print(maxi)
    for clé, val in dico.items():
        if val == maxi:
            tab.append(clé)
    return tab
    
    
def mot_le_plus_dit_president(name):
    dico = {}
    liste = os.listdir("cleaned")
    for filename in liste:
        if name in filename:
            with open(os.path.join("cleaned", filename), "r", encoding="utf-8") as f:
                texte = f.read()
            d = calculer_frequence_mots(texte)
            dico.update(d)
    clé = max(dico, key=lambda i: dico[i])
    freq = dico[clé]
    return clé, freq  
            
        

def presidents_qui_ont_dit(mot):
    dit = []
    liste = os.listdir("cleaned")
    noms_presidents = nom_des_presidents()
    for filename in liste:
        with open(os.path.join("cleaned", filename), "r", encoding="utf-8") as f:
            texte = f.read()
        freq = calculer_frequence_mots(texte)
        if mot.lower() in freq:
            president = filename[11:-4]  
            if president and president in noms_presidents:
                dit.append((president, freq[mot.lower()]))
    dit = sorted(dit, key=lambda x: x[1], reverse=True)
    presidents_tries = [item[0] for item in dit]
    return presidents_tries



       
def premier_president(theme):
    liste = os.listdir("cleaned")
    n_president = nom_des_presidents()
    dico_presidents = {}

    for i in range(len(liste)):
        with open(os.path.join("cleaned", liste[i]), "r", encoding="utf-8") as f:
            ligne = f.readline()
            mots = ligne.split()
            if any(word.lower() in theme.lower() for word in mots):
                if n_president[i] not in dico_presidents:
                    dico_presidents[n_president[i]] = i

    return dico_presidents



print(nom_des_presidents())
dico = calculer_tf_idf("cleaned")
print(mot_le_plus_dit_president("Chirac"))
print(presidents_qui_ont_dit("Nation"))
print(premier_president("Ecologie"))
