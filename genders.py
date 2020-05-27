# coding : utf-8

import csv, spacy
from collections import Counter

fichier = "top_200_daily.csv"

f1 = open(fichier)
lignes = csv.reader(f1)

# print(lignes)

artists = []

for ligne in lignes :
    # print(ligne[2])
    artists.append(ligne[2])

# print(artists)
freq = Counter(artists)
# print(freq.most_common(300))
freq2 = freq.most_common(300)
# print(freq2)

fichierFinal = "top300.csv"

for resultat in freq2:
    nom = resultat[0]
    nbr = resultat[1]
    top300 = [nom, nbr]
    print(top300)
    
    dead = open(fichierFinal, "a")
    obies = csv.writer(dead)
    obies.writerow(top300)
