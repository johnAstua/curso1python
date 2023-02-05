# #da error si no existe 
# #tiene que estar en el mismo archivo

# #modo read
# file = open("demonfile.txt")

# #modo aappend
# #crea un archivo si no existe 
# #si el archivo eiste lo abre
# #escribe alfinal del archivo
# file2 = open("demonfile2.txt", "a")



# #modo write borra todo lo del archivo y escribe encima
# #nose puede en moso read
# file2.write ("hola archivo")
# file2 = open("demonfile2.txt", "w")

# #modo x crear el archivo especifico y si erxiste da error
# file3 = open("demonfile3.txt", "x")


# #preguntar si existe el archivo
# import os
# if (os.path.exists("demonfile.txt")) == False:

# #cambio de linea
# file2.write ("hola archivo /n")

# #cerrar archivos despues de usarse 
# file.close()
# file2.close()



# #leer archivos, va leer todo el contenido del archivo
# #si esta en otro directorio hay que poner la direccion, si esta en el mismo directorio solo con el nombre 
# file = open("demonfile.txt")
# prin(file.read())
# #leer algunos caracteres 
# prin(file.read(7))
# #leer por lineas
# prin(file.readline())


# for line in file:
#     print(line)