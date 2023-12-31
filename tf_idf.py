"""
Projet Python:
-----
Riviere Hugo
Belougne Valentin
-----
Implémentation principal de TF-IDF
"""

import math
import os

def calculer_frequence_mots(chainee):
    """str -> Dico{str : int}
    Calcule la fréquence de chaque mot unique dans l'intégralité du texte."""
    frequence_mots = {}
    mots = chainee.split()
    for mot in mots:
        mot = mot.lower()
        frequence_mots[mot] = frequence_mots.get(mot, 0) + 1
    return frequence_mots

def TF_per_texte():
    """void -> dico{str : int}
    Retourne un dictionnaire des occurences des mot de chaque texte du "cleaned"."""
    analyse_textes = {}
    for texte in os.listdir("cleaned"):
        with open(f"cleaned/{texte}", "r", encoding="utf-8") as t:
            analyse_textes.update({texte: calculer_frequence_mots(t.readlines())})
    return analyse_textes

    
def calculate_idf(repertoire_corpus):
    """str -> dico{str : float}
    Calcul l'idf de chaque mot du texte."""
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


def calculate_tf_idf(repertoire_corpus):
    """str -> dico{str : float}
    Calcul le nombre tf-idf pour chaque mot unique. """
    tfidf_dict = {}
    files_names = [file for file in os.listdir(repertoire_corpus) if file.endswith(".txt")]
    for file_name in files_names:
        with open(os.path.join(f"cleaned", file_name), 'r', encoding='utf-8') as file:
            text = file.read()
        tf_dict = calculer_frequence_mots(text)
        idf_dict = calculate_idf(repertoire_corpus)
        for word in tf_dict:
            if word not in tfidf_dict:
                tfidf_dict[word] = tf_dict[word] * idf_dict.get(word, 0)
            else:
                tfidf_dict[word] += tf_dict[word] * idf_dict.get(word, 0)
    return tfidf_dict
