import numpy as np


def derive_sigmoid(x):
    """
    Calculate the derivative of the sigmoid function.

    Parameters:
        x (float): The input value for which to calculate the derivative.
    """
    # return np.exp(x) / ((1 + np.exp(x)) ** 2)
    return x * (1 - x)

def calcul_error_each_neuron_of_layer(Z, L_cible):
    """
    Calculate the error between the predicted output and the target output for each neuron in a layer.
    
    Parameters:
        Z (numpy): List of exemple represented as a List. The predicted output values from the network.
        L_cible (numpy): List of result represented as a List. Each element represents the target output value for the corresponding neuron.
    """
    # somme_e = 0
    # for i in range(len(Z)):
    #     somme_e+=((L_cible[i]-Z[i])**2)
    # return somme_e

    error = []
    for i in range(len(Z)):
        error.append((L_cible[i] - Z[i]) * derive_sigmoid(Z[i]))
    return error



def calcul_error_reseau(Z_full, L_cible_full, W) :
    """
    Calculate the error of the network in each layer.

    Parameters:
        Z_full (numpy): The predicted output values from the network of all examples.
        L_cible_full (numpy): The target output values of the network with all exemples and with the hidden layers.
        W (numpy): The weights of the network.
         """

    error = []
    for i in range(len(Z_full)):
        error.append(calcul_error_each_neuron_of_layer(Z_full[][i], L_cible_full[][i]))
    return error
