# projet python 
Equipe : Hugo Riviere et Valentin Belougne  
Ce projet a pour but de calculer la matrice tf-idf et de pouvoir en tirer des informations importante pour notre chat bot.

[Dépot git](https://github.com/HugoRiviereEfrei/projets.git)
### pre_traitement.py : 
Dans ce fichier python sont regrouper tout les fonctions permettant le prétraitement du texte a savoir :  
->  Extrait les nom des presidents depuis le nom des fichiers du corpus "speeches", les doublons sont supprimer.   
->  Associe les nom des presidents extrait précédement avec leurs prenoms.  
->  Vérifier que "cleaned" existe au même niveau que les fichiers python et si il n'existe pas on le crée.    
->  Ajoute a "cleaned" une copie des fichier de speeches mit en minuscule.    
->  Supprime les ponctuation de tout les texte contenue dans "cleaned".       
  
### Tf_idf : 
Dans ce fichier sont regrouper tout les méthode permettant que calcule le TF-IDF et les associe a leurs mot :  
->  Calcule de la frequence des mot dans les texte.  
->  Calcule l'inverse de la frequence des document.  
->  Crée la matrice TF-IDF.

### post_traitement.py :  
Dans ce fichier sont regrouper les fonctionalité qui nous fallait dévelloper pour le chat bot :  
->  Défini la liste des mot_nom_important (Mot ayant un TF-IDF = 0)  
->  Défini le mot le plus dit par tout les president.  
->  Défini le mot le plus dit par un président.  
->  Rechercher les président qui ont dit un certain mot.  
->  Défini la date de premiere election des president.  
->  Défini la liste des president ayant parlé d'un theme.  
->  Défini la liste des mot dit par tout les president.

### question_traitement.py:
-> Standardise la question posé par l'utilisateur  
-> Tokenise la questions  
-> Trouve le document le plus similaire au mot le plus important de la question  
-> Renvoie la réponse tiré du texte le plus similaire dont la phrase contient le mot  
-> On ajoute des formules de politesse à la reponse et un "."  
-> On renvoie la réponse à l'utilisateur  


### Main()
Dans ce fichier est présent le menue ainsi que l'appel des fonction des pre traitements minimun et enlever.

### Utilisation 
Il faut vérifier qu'il n'y est pas autre que des .txt dans les fichier "cleaned" et "speeches"
Il vous suffit de run le fichier main.  
Afin de garantire la meilleur utilisation du menue il est a noté que lorsque le code vous propose plusieur option il faut rentre le chiffre   
correspondant voulu.

# Warning
Les mots comme climat et climatique ne peuvent pas être confondus de ce fait il ne faut pas espérer avoir la phrase désigné dans l'exemple
