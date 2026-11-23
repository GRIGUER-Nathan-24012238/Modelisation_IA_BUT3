import math
import numpy as np

def next_layer(A , W, B):
    """
    Calculate the next layer of a neural network

    Parameters:
        A (list): Input of the last layer
        W (list): Weights of the link
        B (list): Biases for the neurons

    Returns:
        list: the values of the neurons for the layer
    """
    Next_a = []
    for i in range(len(W)):
        z = 0
        for j in range(len(A)):
            z += A[j] * W[i][j]
        z += B[i]
        z = (1+math.exp(-z))**-1
        Next_a.append(z)
    return Next_a


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
    Next_a = (1+np.exp(-Next_a))**-1
    return Next_a