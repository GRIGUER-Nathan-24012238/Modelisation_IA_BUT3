import math
import sympy as sp


L=[[0,1,0,1,0,1,0,1,0,1],
   [0,0,1,0,1,1,1,0,0,0],
   [0,1,0,0,1,0,0,0,0,1],
   [1,1,1,1,0,0,0,1,0,0],
   [0,1,0,1,0,1,0,0,1,1]]


L_cible = [5,
           4,
           3,
           5,
           5]

W=[0.5]*len(L[0])
Z=[]


def calcul_Z(Z):
    for current_list_index in range(len(L)):
        z=0
        for i in range(len(L[current_list_index])):
            z+=(L[current_list_index][i]*W[i])
        Z.append(z)
    return Z


def calcul_e(Z):
    somme_e=0
    for i in range(len(Z)):
        somme_e+=((L_cible[i]-Z[i])**2)
    return somme_e


print(calcul_Z(Z))
print(calcul_e(Z))