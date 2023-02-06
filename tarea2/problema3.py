#strings intercaladas con 2 textos escritos por el usuario
""""
Primero debemos comprobar la cantidad de palabras de cada frase, cada frase representa una lista de 
palabras, buscamos la lista con mayor cantidad de palabras con la función “max_list”, 
"""

a =input("primera palabra:")
b =input("segunta palabra:")

max_list = max(len(a), len (b)) #comprobar la cantidad de letrass

if (len(a)== len(b)):   #si tienenla mmisma cantidad
    print(" ".join([item for sublist in zip(a, b) for item in sublist if item != ""]))

if (len(a) != len(b)): #si no tienen la misma cantidad imprimir error
    print("error")