"""Cree una función que cuente e imprima en pantalla todos los números,
 letras y caracteres especiales presentes en una string. Debe recibir esta
 string por parámetro"""

def contar_caracteres_de_una_palabra(texto): #creo una funcion para contar los caracteres de la palabra 
     
     letras = 0  #comienza desde 0 a contar 
     
     digitos = 0 #comienza desde 0 a contar
     
     especial = 0 #comienza desde 0 a contar 
     
     for i in texto:    
       
        if i.isdigit():  #esto es si hay numeros 
             digitos += 1 #esto contara desde el 0 al untimo numero del texto ingresado 
        elif i.isalpha(): # #esto es si hay letras 
             letras += 1 #esto contara desde el 0 a la ultima letra ingresada 
        else:  #si no son letras y numeros 
             especial += 1  #esto contara desde el 0 al ultimo caracter especial 
        
     print("Letras: ", letras) #imprimira la cantidad de letras 
     print("Números: ", digitos)#imprimira la cantidad de numeros 
     print("Caracteres especiales: ", especial)#imprimira la cantidad de caracteres especiales 

#pruebas 
texto = "Hola, esta es una frase de ejemplo 123!@#$"
texto = "alsdladslaldaldsladl#$$#@#12434 "
texto = "2323232323#$%$$$#$%^%))#sgsgsgsgsgsgsgsgjgjg2325386885485838548568387387HAFSAGJSGJSG@$@$@$$@$$@$$@$$@"
texto = ""
#contar_caracteres_de_una_palabra(texto) #esto hace que el texto sea analizado 






"""Cree una función que cuente todas las apariciones de cada caracter en una
string; esta string debe recibirse como parámetro. El resultado debe ser un
diccionario y debe ser impreso en pantalla"""


def contar_aparicion_de_un_caracteres(texto): #defino mi funcion para contar la aparicion de un caracter 
    contar_aparicion_de_un_caracteres = {} #meto el texto en un diccionario 
    for i in texto: #por cada letra
        if i in contar_aparicion_de_un_caracteres: #comprueeba si cada letra esta en el diccionario 
            contar_aparicion_de_un_caracteres[i] += 1 #si esta en el diccionario se aumenta 1 por cada vez que se repita 
        else:
            contar_aparicion_de_un_caracteres[i] = 1 #si no esta en el diccionario se agrega 
    return contar_aparicion_de_un_caracteres #vuelve a repitir todo con todas las letras 
#pruebas
texto = "Esta es la cadena que quieres contar."
texto = " esto es una prueba ooaaslslflfgllfafaf23323232323$@$#@#@!#@$"

texto_caracteres_contados = contar_aparicion_de_un_caracteres(texto)#defino una funcio de caracteres contados 
#print("El número de apariciones de cada carácter es:") #imprime el resultado 
#print(texto_caracteres_contados)#imprime todas las apariciones de caa digito 






"""Escriba una función que elimine todas las apariciones de un elemento en una
lista. Tanto la lista como el valor que se quiere eliminar deben ser parámetros
de la función"""
#pruebas
lista = [1, 2, 3, 4, 5, 2, 6, 7, 2,2,2,2,2,2,2,2,2,2,] 
lista = ["perro","perro","gato"]
elemento_para_borrar = "perro"

if elemento_para_borrar in lista: #si el elemento que se quiere borrar esta en la lista
    while elemento_para_borrar in lista: #mientras el elemnto que se quiere borrar este en lista se va a borrar
        lista.remove(elemento_para_borrar) #borrar elemento 

    print(lista)    #imprimir la lista nueva
else:
  print(elemento_para_borrar, "no esta en la lista") #si el elemnto no esta en la lista 



  """. Cree una función que reciba una secuencia de números separados por coma
por parte del usuario e imprima una lista y una tupla que contengan dichos
valores. El usuario debe ingresar un único input con los valores separados
por comas."""



#pruebas
numeros = 2,3,4,34,4343,43434,3.4334,3434
numeros = 23333.2323,233233453,34434,44.4444
numeros = 1,2,3,4,5,6


numeros_resultados_lista = list(numeros) #los mete en una lista 
numeros_resultados_tupla = tuple(numeros) #los mete en una tupla
print(numeros_resultados_lista) #imprime la lista
print(numeros_resultados_tupla) #imprime la tupla 

"""estuve un rato investigando y no se porque pero no logre que si no eran numeros imprimiera algo perdon :(  )"""








