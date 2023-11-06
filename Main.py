import os

def nom_des_presidents():
    liste = os.listdir("speeches")
    tab = []
    for name in liste:
        name = name[11:]
        name = name.replace(".txt", "")
        if "1" in name:
            name = name.replace("1","")
        tab = [n for n in tab if '2' not in n]
        tab.append(name)       
    return tab
        

def prenom_des_presidents(tab):
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
    print(liste)
    for name in liste:
        with open(name,"r") as f:
            lignes = f.readlines()
        liste = [str(ligne.strip().lower()) for ligne in lignes]
        os.chdir("../cleaned")
        with open(name,"w") as f2:
            for l in liste:
                f2.write(l)
        os.chdir("..\speeches")
                
        

        




            
            
tab_nom_president = nom_des_presidents()
nom_prenom_presiedent = prenom_des_presidents

minuscule()
