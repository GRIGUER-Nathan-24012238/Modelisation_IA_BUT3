import math
import numpy as np


class Neurone:
    def __init__(self,X,W,B,Z=np.array([])):
        self.X=X
        self.W=W
        self.B=B
        self.Z=Z

    def sigmoid(self,z):
        return (1 / (1 + math.exp(-z)))

    def calcul_z(self):
        for i in range(len(self.X)):
            print(self.X[i],self.W)
            z=(self.X[i].dot(self.W)+self.B)
            #z=self.sigmoid(z)
            self.Z=np.append(self.Z,z)

    def print(self):
        return self.Z

if __name__=="__main__":

    L = np.array(
    [[0,1,0,1,0,1,0,1,0],
     [0,0,1,0,1,1,1,0,0],
     [0,1,0,0,1,0,0,0,0],
     [1,1,1,1,0,0,0,1,0],
     [0,1,0,1,0,1,0,0,1]])


    L_cible = np.array([8,4,0,7,8])

    W = np.array([0.5] * len(L[0]))
    W=np.transpose(W)


    B=0
    n1 = Neurone(L,W,B)
    print(n1.calcul_z())
    print(n1.print())