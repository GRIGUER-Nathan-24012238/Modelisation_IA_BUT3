import csv
import itertools


def calculer_sortie(liste):
    if 1 not in liste:
        return 0  # Cas limite : aucun 1 dans la liste

    taille = len(liste)
    # Index du premier 1
    premier_index = liste.index(1)
    # Index du dernier 1
    dernier_index = taille - 1 - liste[::-1].index(1)

    x = taille - premier_index
    y = taille - dernier_index
    return x - y


# Génération des 256 combinaisons possibles de taille 8
dataset = []
for comb in itertools.product([0, 1], repeat=8):
    entree = list(comb)
    sortie = calculer_sortie(entree)
    dataset.append((entree, sortie))

# Exportation en fichier CSV
with open("dataset.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["entree", "sortie"])
    for entree, sortie in dataset:
        writer.writerow([entree, sortie])

print(f"Jeu de données généré avec succès : {len(dataset)} lignes.")