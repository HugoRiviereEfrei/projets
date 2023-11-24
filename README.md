# projet python
Ce projet a pour but de calculer la matrice tf-idf et de pouvoir en tirer des informations importante pour notre chat bot.
## Fonctions
Entrer -> Renvoie  
Description

### nom_des_présidents:
void -> list[str]  
Retourne le nom de tout les présidents de "speeches".

### prénom_des_présidents:
list[str] -> dico{str : str}  
Retourne le prénom de tout les présidents de "speeches".

### minuscule:
void -> void  
Créé le dossier cleaned si il n'existe pas et y met une copie en minuscule des fichiers de "speeches".

### enlever:
void -> void  
Enlèves chaque ponctuation et la remplace par un espace, sauf pour les apostrophes si il y a un "t" avant, on remplace aléatoirement " ' " par e ou par a, sinon on remplace par e.

### calculer_frequence_mot:
str -> Dico{str : int}  
Calcule la fréquence de chaque mot unique dans l'intégralité du texte.

### TF_par_texte:
void -> dico{str : int}  
Retourne un dictionnaire des occurences des mot de chaque texte du "cleaned".

### calculer_idf:
str -> dico{str : float}  
Calcul l'idf de chaque mot du texte.

### calculer_tf_idf:
str -> dico{str : float}  
Calcul le nombre tf-idf pour chaque mot unique.

### mot_non_important:
dico{str : float} -> list[str]  
Retourne le mot le moins important du corpus.

### TF_IDF_MAX:  
dico{str : float} -> tuple(str , float)
Retourne le mot le plus important du corpus.

### mot_le_plus_dit_president:
str -> tuple(str, float)  
Retourne le mot le plus dit dans l'ensemble des nominations.

### president_qui_on_dit:
str -> list[str]  
Retourne tout les président qui on dit un certains mot.

### date_president:
void : dico{str : int}  
Associe chaque président à leur date de début de mandat.

### le_premier_sur_le_theme:
str -> list[str]  
Quel président a parlé en premier sur un certains thème

### mots_dits_par_tous_les_presidents:
void ->  list[str]  
Renvoie la liste des mots dit par tout les president et qui ne sont pas non important.

### main:
Interface d'utilisation du programme

## Utilisation
Prérequis Assurez-vous d'avoir les discours des présidents stockés dans un dossier appelé "speeches" à côté du script Python. 

### Instructions  
1. Mise en Minuscules des Discours Le programme commence par convertir tous les discours en minuscules et les stocke dans un dossier "cleaned". ``` python minuscule()
2. 
