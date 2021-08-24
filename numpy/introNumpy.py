import numpy as np


A = np.array([1,2,3])


B = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(B)
print(B[0,:])
print(B[1,1])
print(B[1:3,])
print(B[0:2,1:])


#zeros
#its type is float
Z=np.zeros((1,2))
#to convert its type to int
Z=np.zeros((1,2), dtype=int)
print(Z)


#onces
A=np.ones((2,2),dtype=int)

print(A)

A=np.array([[1,2],[4,5]])
B=np.array([[7,8],[9,10]])
print(np.concatenate((A,B),axis=1))

#fulll() ===> creation d'une matrice 3 ligne et 2 cols full of 5.3
print(np.full((3,2),5.3))

#dot() ===>  Multiplication de 2 matrices A et B
print(np.dot(A,B))

#pour creer une matrice identite
C=np.eye((3),dtype=int)
print(C)



import pandas as pd
#pour transformer le matrice en table
C=pd.DataFrame(C,index=['a','b','c'], columns=['e','f','g'])
print(C)
#pour transformer le table en une matrice
print(np.array(C))


