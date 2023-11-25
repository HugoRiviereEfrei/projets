# projet python
Equipe : Hugo Riviere et Valentin Belougne
Ce projet a pour but de calculer la matrice tf-idf et de pouvoir en tirer des informations importante pour notre chat bot.

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


### Main()
Dans ce fichier est présent le menue ainsi que l'appel des fonction des pre traitements minimun et enlever.

### Utilisation 
Il vous suffit de run le fichier main. Afin de garantire la fonctionnalite du menue il faut que si vous noté

