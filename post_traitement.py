import os
from pre_traitement import nom_des_presidents
from pre_traitement import calculer_frequence_mots
from tf_idf import calculer_tf_idf

def mot_non_important(dico):
    """dico{str : float} -> list[str]
    Retourne le mot le moins important du corpus. """
    tab = []
    for clé,val in dico.items():
        if val == 0.0:
            tab.append(clé)
    return tab 
 
 
def TF_IDF_MAX(dico):
    """dico{str : float} -> tuple(str , float)
    Retourne le mot le plus important du corpus. """
    nom_du_president = ""
    valeur = 0
    print(dico.values())
    maxi = max(dico.values())
    for clé, val in dico.items():
        if val == maxi:
            nom_du_president = clé
            valeur = val
    return nom_du_president , valeur
            
    
    
def mot_le_plus_dit_president(name):
    """str -> tuple(str, float)
    Retourne le mot le plus dit dans l'ensemble des nominations."""
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
    """ str -> list[str]
        Retourne tout les président qui on dit un certains mot."""
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
    """ void : dico{str : int}
        Associe chaque président à leur date de début de mandat."""
    dico = {}
    date = [1995, 1974, 2012, 2017, 1981, 2007]
    tab = nom_des_presidents()
    for i in range(len(tab)):
        dico[tab[i]] = date[i]
    return sorted(dico.items(), key=lambda item: item[1])


def le_premier_sur_le_theme(theme):
    """str -> list[str]
    Quel président a parlé en premier sur un certains thème """
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
    """void -> list[str]
    Renvoie la liste des mots dit par tous les president et qui ne sont pas non importants."""
    mots_par_president = []
    noms_presidents = nom_des_presidents()
    l_mot_non_important = mot_non_important(calculer_tf_idf("cleaned"))
    if noms_presidents:
        premier_president = noms_presidents[0]
        liste = os.listdir("cleaned")
        for filename in liste:
            if premier_president in filename:
                with open(os.path.join("cleaned", filename), "r", encoding="utf-8") as f:
                    texte = f.read()
                mots_par_president = set(calculer_frequence_mots(texte).keys())
    for president in noms_presidents[1:]:
        liste = os.listdir("cleaned")
        mots_du_president = set()
        for filename in liste:
            if president in filename:
                with open(os.path.join("cleaned", filename), "r", encoding="utf-8") as f:
                    texte = f.read()
                mots_du_president.update(set(calculer_frequence_mots(texte).keys()))
                mots_par_president = mots_par_president.intersection(mots_du_president)
    mots_par_president = [mot for mot in mots_par_president if mot not in l_mot_non_important]
    return list(mots_par_president)
