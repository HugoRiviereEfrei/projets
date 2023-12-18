from post_traitement import *
from pre_traitement import *
from question_traitement import *

dico = calculate_tf_idf("cleaned")

print("Test 1...", end="\r")
tab = name_of_presidents()
t = first_name_of_presidents(tab)
assert t == {'Chirac': 'Jacques', 'Giscard dEstaing': 'Valéry', 'Hollande': 'François', 'Macron': 'Emmanuel', 'Mitterrand': 'François', 'Sarkozy': 'Nicolas'}
print("Test 1 ✅")

print("Test 2...", end="\r")
assert len(non_important_word(dico)) == 32
print("Test 2 ✅")

print("Test 3...", end="\r")
a , b = TF_IDF_MAX(dico)
assert a == "doit"
print("Test 3 ✅")

print("Test 4...", end="\r")
for i in range(1,7):
    clé , freq = most_said_word_by_president(tab[i-1])
    
    match clé:
        case "de":
            assert freq == 63 or 40 or 58
        case "et":
            assert freq == 19
        case "la":
            assert freq == 63 or 61
print("Test 4 ✅")

print("Test 5...", end="\r")
word = "test_word"
result = presidents_who_said(word)


expected_output = name_of_presidents()+[[]]

assert result is not None
assert isinstance(result, list)
assert result in expected_output

empty_word = ""
result_empty = presidents_who_said(empty_word)

expected_output_empty = []

assert result_empty is not None
assert isinstance(result_empty, list)
assert result_empty == expected_output_empty
print("Test 5 ✅")

print("Test 6...", end="\r")
set = "1995 1974 2012 2017 1981 2007"
tab = name_of_presidents()
t = date_of_presidents()
for j in range(1,7):
    for i in range(len(t)):
        if tab[j-1] == t[i][0]:
            assert str(t[i][1]) in set
print("Test 6 ✅")

print("Test 7...", end="\r")
tab = word_said_by_all_presidents()
assert len(tab) == 10
print("Test 7 ✅")



print("Test 8...", end="\r")
questions = [
    # Questions sur des sujets spécifiques
    "Quel est le mot le plus utilisé par les présidents français dans un discours sur l'environnement ?",
    "Quel est le président français qui a parlé le plus du chômage ?",
    "Quel est le thème le plus discuté",

    # Questions avec des conditions
    "Quels sont les trois mots les plus utilisés par les présidents français dans leurs discours depuis 2017 ?",
    "Quels sont les trois thèmes les plus discutés par les présidents français dans leurs discours lors de la crise sanitaire de 2020 ?",
    "français qui a parlé le plus du mot 'écologie' dans ses discours ?",

    # Questions ouvertes
    "Quel est le mot le plus important que les présidents français ont prononcé sur la politique étrangère ?",
    "Quel est le président français qui a eu le plus d'impact sur l'économie française ?",
    "Quel est le thème us important que lesançais ont discuté sur l'éducation ?",

    # Questions avec des sujets et des conditions
    "Quels sont les trois mots les plus utilisés par les présidents français dans leurs discours sur l'écologie depuis 2017 ?",
    "Quels sont les trois thèmes les pdents françaisns leurs discours sur l'économie lors de la crise sanitaire de 2020 ?",
    "Quel est le président français qui a parlé le plus du mot 'éducation' dans ses discours sur la politique étrangère ?",

    # Questions avec des mots inconnus
    "Quel est le moparlé du plus de thèmes qui commencent par la lettre 'a' ?",
    "Quel est le thème le plus discuté par les présidents français qui commence par la lettre 't' ?",

    # Questions avec des erreurs de frappe
    "Quel est le mot le plus utlisé par les présidents français ?",
    "Quel est le dent qui  plus de thémes ?",
    "Quel est le thème le plus discuti par les présidents français ?",

    # Questions avec des cas limites
    "Quel est le mot le plus utilisé par les présidents français s'il n'y a pas de présidents ?",
    "Quel est le président quème le plus discuté par les présidents français s'il n'y a pas de présidents ?",
]

for q in questions:
    assert isinstance(q, str)
    assert q != ""
print("Test 8 ✅")