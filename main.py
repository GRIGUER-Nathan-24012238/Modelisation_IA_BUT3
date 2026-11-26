import math
#import sympy as sp

"""
L = [[0,1,0,1,0,1,0,1,0],
     [0,0,1,0,1,1,1,0,0],
     [0,1,0,0,1,0,0,0,0],
     [1,1,1,1,0,0,0,1,0],
     [0,1,0,1,0,1,0,0,1]]

#L_cible = [8, 4, 8, 7, 8]

L_cible = [
    [0,0,0,0,0,0,0,0,1],   # 8
    [0,0,0,0,1,0,0,0,0],   # 4
    [0,0,0,0,0,0,0,0,1],   # 8
    [0,0,0,0,0,0,0,1,0],   # 7
    [0,0,0,0,0,0,0,0,1],   # 8
]
"""


def next_layer_numpy(A , W, B):
    """
    Calculate the next layer of a neural network using numpy

    Parameters:
        A (numpy array): Input of the last layer
        W (numpy array): Weights of the link
        B (numpy array): Biases for the neurons

    Returns:
        numpy array: the values of the neurons for the layer
    """

    Next_a = np.dot(W, A) + B
    Next_a = sigmoid(Next_a)
    return Next_a


print("L :", L)
print("W :", W)

def sigmoid(x):
    sig = 1 / (1 + math.exp(-x))
    return sig


def calcul_e(Z):
    somme_e=0
    for i in range(len(Z)):
        somme_e+=((L_cible[i]-Z[i])**2)
    return somme_e

if __name__ == '__main__' :
    #print(calcul_e(next_layer(L, W, B)))
    pass