# projet python
Ce projet a pour but de calculer la matrice tf-idf et de pouvoir en tirer des informations importante pour notre chat bot.
## Fonctions

### nom_des_présidents:
Retourne le nom de tout les présidents du corpus.
### prénom_des_présidents:
Retourne le prénom de tout les présidents du corpus.
### minuscule:
Créé le dossier cleaned si il n'existe pas et y met une copie en minuscule des fichiers du corpus.
### enlever:
Enlèves chaque ponctuation et la remplace par un espace, sauf pour les apostrophes si il y a un "t" avant, on remplace aléatoirement " ' " par e ou par a, sinon on remplace par e.
### calculer_frequence_mot:
Calcule la fréquence de chaque mot unique dans l'intégralité du texte.
### TF_par_texte:
Retourne un dictionnaire des occurences des mot de chaque texte du corpus.
### calculer_idf:
Calcul l'idf de chaque mot du texte.
### calculer_tf_idf:
Calcul le nombre tf-idf pour chaque mot unique.
### mot_non_important:
Retourne le mot le moins important du corpus.
### TF_IDF_MAX:
Retourne le mot le plus important du corpus.
### mot_le_plus_dit_president:
Retourne le mot le plus dit dans l'ensemble des nominations.
### president_qui_on_dit:
Retourne tout les président qui on dit un certains mot.
### date_president:
Associe chaque président à leur date de début de mandat.
### le_premier_sur_le_theme:
Quel président a parlé en premier sur un certains thème
### mots_dits_par_tous_les_presidents:
Les mot dit pas tout les présidents
### main:
Interface d'utilisation du programme

## Utilisation
Prérequis Assurez-vous d'avoir les discours des présidents stockés dans un dossier appelé "speeches" à côté du script Python. 
### Instructions  
1. Mise en Minuscules des Discours Le programme commence par convertir tous les discours en minuscules et les stocke dans un dossier "cleaned". ```python minuscule()
