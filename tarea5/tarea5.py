'1:tarea 2 problema 4:'
numeros = [1, 2, 3, 4, 5] #creamos 1 lista 

numeros= [1, 2**3, 3**3, 4**3, 5**3] #elevamos 1 lista al cubo 

#print(numeros) #se imprime la lista al cubo

'creo que esete lo tuve malo en su dia en la tarea XD'

"paradigma de programación funcional:"

#imprime una lista de 7 numeros al cubo, pruebas:

# print((lambda a,b,c,d,e,f,g: (a**3,b**3,c**3,d**3,e**3,f**3,g**3))(23, 45, 32, 76, 4, 3, 23))

# print((lambda a,b,c,d,e,f,g: (a**3,b**3,c**3,d**3,e**3,f**3,g**3))(233, 72, 34, 78,34, 333, 88))

# print((lambda a,b,c,d,e,f,g: (a**3,b**3,c**3,d**3,e**3,f**3,g**3))(1, 2, 12, 68,25, 54, 998))

'tarea 2 ejercicio 4:'
#pruebas
# lista = [1, 2, 3, 4, 5, 2, 6, 7, 2,2,2,2,2,2,2,2,2,2,] 
# lista = ["perro","perro","gato"]
# elemento_para_borrar = "perro"

# if elemento_para_borrar in lista: #si el elemento que se quiere borrar esta en la lista
#     while elemento_para_borrar in lista: #mientras el elemnto que se quiere borrar este en lista se va a borrar
#         lista.remove(elemento_para_borrar) #borrar elemento 

#     print(lista)    #imprimir la lista nueva
# else:
#   print(elemento_para_borrar, "no esta en la lista") #si el elemnto no esta en la lista 

"paradigma de programación funcional:"
"cambiado"
#pruebas:
mi_lista = [2, 3, 4, 5, 6]
mi_lista = ["perro","perro","gato"]

remove_element = "gato" #lo que se quiere remover
nueva_lista = list(filter(lambda x: x != remove_element, mi_lista)) #eliminina lo seleccionado
#print(nueva_lista)  #imprime la nueva lista 





"tarea 2 ejercicio 3"

# a =input("primera palabra:") #primera palabra ingresada por el usuario 
# b =input("segunta palabra:")#segunda palabra ingresada por el usuario 

# max_list = max(len(a), len (b)) #comprobar la cantidad de letras

# if (len(a)== len(b)):   #si tienenla mmisma cantidad
#     print(" ".join([item for sublist in zip(a, b) for item in sublist if item != ""]))#intercla las palabras 

# if (len(a) != len(b)): #si no tienen la misma cantidad imprimir error
#     print("error")


"paradigma de programación funcional:"
"cambiado"

# palabra1 = input("Ingresa la primera palabra: ")#primera palabra ingresada por el usuario

# palabra2 = input("Ingresa la segunda palabra: ")#segunda palabra ingresada por el usuario 

# intercaladas = ''.join(list(map(lambda x, y: x + y, palabra1, palabra2)))#intercla las palabras

# if (len(palabra1)== len(palabra2)): #si las 2 palabras del mismo largo

#     print(intercaladas)#imprime las 2 palabras intercaladas 

# if (len(palabra1) != len(palabra2)): #si no tienen la misma cantidad imprimir error

#     print("error, las palabras no tienen la misma cantidad de letras")

"tarea 3 calculadora funcion para restar 2 numeros"

# def restar(a, b):  #funcion para poder restar 2 numeros ingresados por el usuario(a y b)

#     return a - b

# if eleccion == 2: #si el usuario ingresa un 2 entrara en la resta

#         numero1 = int(input("ingrese el primer numero:"))  #el usuario ingresa el primer numero

#         numero2= int(input("ingrese el segundo numero:"))   #el usuario ingresa el segundo numero
    
#         print(f"{numero1} - {numero2} =", restar(numero1, numero2)) #esto hace que la operacion con los numeros ingresados aparezcan junto con el resultado(se usa la funcion restar creada)

"paradigma de programación funcional:"
"cambiado"
#numero_resta1= int(input("ingrese el primer numero:"))#el usuario ingresa el primer numero

#numero_resta2= int(input("ingrese el segundo numero:"))#el usuario ingresa el segundo numero

#restar = (lambda x,y: x-y)( numero_resta1, numero_resta2) #restar los 2 numeros ingresados 

#print(restar)#imprime los 2 numeros restados 