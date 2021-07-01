#Any
#Esta funcion retorna true si al menos un elemento de un iterable
#si almenos hay uno True

# print (any([1>0,1==0,1<0]))
# print (any([1<0,2<1,3<2]))
# print (any([]))


#All

#Esta funcion retorna true, si todos los elementos del iterable
#son iguales a true
# print (all(['a'<'b','b'<'c']))#lexicograficamente a es menor a b
# print (all(['a'<'b','c'<'b']))
# print (all([]))

#ejemplo Any

# numeros=list(range(1,11))#lista de uno hasta 10
# print(numeros)

# resultado=any([n<5 for n in numeros ])#de los numeros de la lista preguntamos si hay numeros menores de 5
# print(resultado)
#los primeros 4 numeros son menores a 5, si al menos hay un numero
#menor a 5 va a imprimir True

#Ejemplo All

# numeros=list(range(1,11))#lista de uno hasta 10
# print(numeros)

# resultado=all([n>0 for n in numeros ])#Todos los valores contenidos en numeros son mayores a 0
# print(resultado)# True


# numeros=list(range(1,11))#lista de uno hasta 10
# print(numeros)

# resultado=all([n>5 for n in numeros ])# No todos los valores contenidos en numeros son mayores a 5
# print(resultado)#False

#Ejercicio

#Nos dan un listado de numeros separados por espacio
#Si todos los numeros son positivos, se necesita verificar
#Si hay al menos un un entero que sea un entero palindromico
#Numeros que se leen lo mismo de izquierda a derecha como de derecha
#a izquierda (101, 1001, 212)
#Se va a imprimir True si todos lo planteamientos del problema 
#son satisfactorias en caso contrario imprime False

#All
#Todos los enteros de la lista son positivos

#Any
#5 es el unico numero palindromo


# n=int(input("Capturar: "))
# #12 9 61 5 14
# numeros=tuple(map(int, input("Captura2: ").split()))#Particionamos a partir del caracter de espacio
# print(n, numeros)

# #Verificar que todos los numeros son positivos
# resultado=all([n>0 for n in numeros])
# print(resultado)

# #Al menos un elemento es palindromo
# #Como comprobar si un numero es palindromo 
# #Convertimos a cadena ese n valor y preguntamos si el igual
# # a la representacion en cadena pero la lectura de derecha a izquierda
# #[::-1] con esto se invierte la cadena de caracteres 
# # and resultado se conjuga con lo que hay en resultado
# resultado=any([str(n)== str(n)[::-1] for n in numeros]) and resultado
# print(resultado)



# #all and any
# inf=['12', '9', '61', '5', '14']
# #inf=[int(input('12 9 61 5 14')), input().split('') ]
# print('True' if all(list(map(lambda x:x>0, list(map(int,inf[1]))))) and any(list(map(lambda x:x[0]==x[1] or x[0]=='5',list(zip(inf[1], list(map(lambda x:x[-1:(len(x)+1)*-1:-1], inf[1]))))))) else False )
 