#hacer un triangulo con el numero dado

n = int(input("numero:"))

for i in range(1, n + 1):
    for j in range(1, i + 1): #variable j desde 1 hasta i
        print(j, end=" ") #imprime j
    print("") #salto de linea 

if n < 0:            #si el numero es menor que cero dara error
    print("error")
    