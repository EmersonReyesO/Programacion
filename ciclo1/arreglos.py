n=int(input("Ingrese el tamaño del arreglo:"))
m=int(input("Ingrese el numero de multiplos:"))
#Crear arreglo

A=[]

for i in range(0,n):
    A.append(i*m)
    
print(A)    


#Imprimir en pantalla los numeros impares mayores a  3

# A=[1,5,8,9,30,9,13]
# B=[]

# for i in A:
#     if i > 3 and i%2!=0:
#         B.append(i)
        
# print(B)        


#Calcular 10 numeros aleatoriamente
#import random

# def vector_aleatorio(n):
#     vector=[0]*n
#     for i in range(n):
#         vector[i]=random.randint(0,10)#Devuleve numeros con base entera y solo numeros hasta 10
#     return vector

# print('Ingrese cuantos numeros aleatorios desea obtener: ')
# n=int(input())

# aleatorio=vector_aleatorio(n)
# print(aleatorio)


#numpy modulo que hace que trabaje de mejor manera con vectores y matrices
#Vectores y matrices

#import numpy as np#np simplifica el numpy para trabajarlo

# vector=np.array([6,7,1,2,3])#la palabra array identifica al vector
# print(vector)# muestran los datos que se almacenan en el vector.

# vector=np.array([6,7,1,2.3,3])# Se cambio un dato a flotante
# print(vector)# Si un elemento es diferente automaticamente va a influir en los demas

#Quiero convertir a mis elementos de un vector a un tipo
# vector=np.array([6,7,1,2.3,3])# Se cambio un dato a flotante
# print(vector.astype(str))
# print(vector.astype(float))

# a=np.array([6,7,1,2,3])
# b=np.array([6,7,1,5,11])
# print(a+b)

# print(a>b)

#Imprimir elementos
#vector=np.array([6,7,1,2,3])
# print(vector[3])

#Metodos

# print(vector.max())
# print(vector.min())
# print(vector.argmax())#Otorgar la posicion del maximo valor
# print(vector.argmin())#Otorgar la posicion del minimo valor
# print(vector.sum())
# print(vector.prod())

#Matriz
# vector=np.array([6,7,1,2,3])
# matriz=np.array([[1,2,3],[4,5,6],[7,8,9]])#matriz 3*3

# print("vector",vector)
# print(matriz)

# matriza=np.array([[1,2,3],[4,5,6],[7,8,9]])
# matrizb=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(matriza+matrizb)

#funcion size imprime la cantidad de elementos de mi vector

# vector=np.array([6,7,1,2,3])
# print('vector',vector.size)
# print('vector1',len(vector))


# matriza=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print('matriz',matriza.size)

#Recorrido de una matriz

# matriza=np.array([[1,2,3],[4,5,6],[7,8,9]])

# for i in range(3):
#     for j in range(3):
#         print(matriza[i][j], end=' ')
#     print()    
    