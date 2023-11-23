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
        with open(os.path.join(f"cleaned", file_name), 'r', encoding='utf-8') as file:
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
    a = ""
    b = 0
    maxi = max(dico.values())
    for clé, val in dico.items():
        if val == maxi:
            a = clé
            b = val
    return a,b
            
    
    
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
    presidents_ajoutes = set()
    for filename in liste:
        with open(os.path.join("cleaned", filename), "r", encoding="utf-8") as f:
            texte = f.read()
        freq = calculer_frequence_mots(texte)
        if mot.lower() in freq:
            for president in noms_presidents:
                if president.lower() in filename.lower() and president not in presidents_ajoutes:
                    dit.append((president, freq[mot.lower()]))
                    presidents_ajoutes.add(president)
    dit = sorted(dit, key=lambda x: (x[1], x[0]), reverse=True)
    dit = list({item[0] for item in dit})
    return dit


def date_des_president():
    dico = {}
    date = [1995, 1974, 2012, 2017, 1981, 2007]
    tab = nom_des_presidents()
    for i in range(len(tab)):
        dico[tab[i]] = date[i]
    return sorted(dico.items(), key=lambda item: item[1])


def le_premier_sur_le_theme(theme):
    tab = []
    liste = os.listdir("cleaned")
    t = dict(date_des_president())
    for i in range(len(liste)):
        with open(os.path.join("cleaned", liste[i]), "r", encoding="utf-8") as f:
            texte = f.read()
        if theme.lower() in texte:
            president = liste[i][11:-4]  
            tab.append(president)
    return sorted(tab, key=lambda x: t.get(x, 0), reverse=True)
    
            
    
def mots_dits_par_tous_les_presidents():
    mots_dits = set()
    noms_presidents = nom_des_presidents()
    l_mot_non_important = mot_non_important(calculer_tf_idf("cleaned"))
    for president in noms_presidents:
        liste = os.listdir("cleaned")
        for filename in liste:
            if president in filename:
                with open(os.path.join("cleaned", filename), "r", encoding="utf-8") as f:
                    texte = f.read()
                mots_du_president = set(calculer_frequence_mots(texte).keys())
                mots_dits.update(mots_du_president)

    mots_dits = [mot for mot in mots_dits if mot not in l_mot_non_important]
    return list(mots_dits)

    
    
            
def main():
    dico = calculer_tf_idf("cleaned")
    demande = int(input("Quelle est votre demande ?" + "\n" +\
                        "1- Liste des President" + "\n" +\
                        "2- Liste des mots non imporants" + "\n" +\
                        "3- Le mot le plus dit par les president" + "\n" +\
                        "4- Mot le plus dit par " + "\n"+\
                        "5- Qui a dit le mot " + "\n"+\
                        "6- Quelle est l'anner des premier election des president" + "\n" +\
                        "7- Premier President a avoir parler d'un theme" +"\n"+\
                        "8- Liste des mot dit par tout les president" + "\n"))
    
    while demande not in [1,2,3,4,5,6,7,8]:
        demande = int(input("Quelle est votre demande ?" + "\n" +\
                        "1- Liste des President" + "\n" +\
                        "2- Liste des mot nom imporant" + "\n" +\
                        "3- Le mot le plus dit par les president" + "\n" +\
                        "4- Mot le plus dit par " + "\n" +\
                        "5- Qui a dit le mot " + "\n" +\
                        "6- Quelle est l'anner des premier election des president" + "\n"+\
                        "7- Premier President a avoir parler d'un theme" +"\n"+\
                        "8- Liste des mot dit par tout les president" + "\n"))
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
        a , b = TD_IDF_MAX(dico)
        print("\n" +\
              "Le mot le plus dit par les president est '" + a + "' avec un TF-IDF de " + str(b))
        
    if demande == 4:
        a = int(input("\n" +\
                      "Chosiser un president :" + "\n" +\
                      "1- Chirac" + "\n" +\
                      "2- Giscard dEstaing " + "\n" +\
                      "3- Hollande" + "\n" +\
                      "4- Macron" + "\n" +\
                      "5- Mitterrand" + "\n" +\
                      "6- Sarkozy" + "\n"))
        while a not in [1,2,3,4,5,6]:
            a = int(input("\n" +\
                         "Chosiser un president :" + "\n" +\
                          "1- Chirac" + "\n" +\
                          "2- Giscard dEstaing " + "\n" +\
                          "3- Hollande" + "\n" +\
                          "4- Macron" + "\n" +\
                          "5- Mitterrand" + "\n" +\
                          "6- Sarkozy" + "\n"))
        tab = nom_des_presidents()
        clé , freq = mot_le_plus_dit_president(tab[a-1])
        print("le mot le plus dit par " + tab[a-1] + " est '" + clé + "' a une frequence de " + str(freq))
        
    if demande == 5:
        a = str(input("\n" +\
            "Ecriver le mot que vous souhaiter chercher : "))
        tab = presidents_qui_ont_dit(a)
        i = 0
        print("\n" +\
              "Les president ayant dit '" + a + "' sont :")
        while i < len(tab):
            print(str(i+1) + "- " + tab[i])
            i += 1 
        print("Le president l'ayant le plus dit est " + tab[0])
        
        
    if demande == 6:
        a = int(input("\n" +\
                      "Chosiser un president :" + "\n" +\
                      "1- Chirac" + "\n" +\
                      "2- Giscard dEstaing " + "\n" +\
                      "3- Hollande" + "\n" +\
                      "4- Macron" + "\n" +\
                      "5- Mitterrand" + "\n" +\
                      "6- Sarkozy" + "\n"))
        
        while a not in [1,2,3,4,5,6]:
            a = int(input("\n" +\
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
            if tab[a-1] == t[i][0]:
                print("\n" + tab[a-1] + " a été elu la premiere fois en " + str(t[i][1]))
                
        
    if demande == 7:
        a = str(input("\n" + "Entrer le theme que vous voulez chercher : "))
        tab = le_premier_sur_le_theme(a)
        print("n\" + Les présidents ayant parlé du theme sont :" + "\n")
        for i in range(len(tab)):
            print(str(i+1) + "- " + tab[i])
            i += 1
        print("Le President qui en a parle en premier est " + tab[-1])
    
    if demande == 8:
        tab = mots_dits_par_tous_les_presidents()
        print("Il y a " + str(len(tab)) + " mots dit par tout les president  :")
        print(tab)
    
    
main()

