def calcul_error(Z, L_cible):
    somme_e = 0
    for i in range(len(Z)):
        somme_e+=((L_cible[i]-Z[i])**2)
    return somme_e

def derive