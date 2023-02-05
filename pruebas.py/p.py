# def factoring(n): #descomposición en factores primos
#   text= str(n) + ' = '
#   i = 1
#   for i in range(1, int(n/2)+1, 2):      # recorre los impares
#     if i==1: i=2                         # salvo el 1 que será 2
#     counter = 0
#     while n % i == 0:
#       n /= i
#       counter += 1
#     if counter == 1:
#       text += str(i)+ ' × '
#     elif counter > 1:
#       text += str(i) + '^' + str (counter) + ' × '
#   if text[-2] == "=":       # si no hay divisores
#     text += str(n) + ' × '  # en ese caso el propio n será primo
#   text += '1'
#   return text

# if __name__ == "__main__":
#   while True:
#     try:
#       n = int(input('Introduzca el número a factorizar: ') or 202)
#       if 1 < n <= 1e10:
#         break
#       else:
#         print('Por favor, introduzca un número en el rango [2,10_000_000_000]')
#     except ValueError:
#       print('Por favor itroduzca un número entero positivo.')

#   print(factoring(n))
  
# numero = int(input("numero:"))
# factorial = 1
# if numero != 0:
#     for i in range(1, numero + 1):
#         factorial = factorial * i
# print("factorial:",factorial)






# #importa cosas como funciones creadas por nosotros de otros archivos 
# import modulos

# #arcortar(renombrar)

# import modulos as ma

# # el punto no permite accerder a lo que se creo en moduloss(archivo)
# print(modulos.syma(2, 2))

# #accerder a la constante 
# print(modulos.API_URL)

# #informacion del sistema donde estamos trabajando
# import platform
# print(platform.architecture)#ejemplo hay mas

# def suma (un, do):
#     return un + do
# print (suma(2, 5))

# def multiplicacion (a, b):
#     return a * b
# print (multiplicacion (45,55))
    
# cantidad = int (input("ingrese la cantidad de numero:"))
# suma = 0

# for i in range(1,cantidad+1):
#     num = int (input("digite el numero:"))
#     suma = suma + num
#     if num % 2 == 0:
#         print("la suma de todos los numeros es:",suma)


#funciones de la calculadora 
def restar(a, b):
    return a - b

def potencia(a, b):
     return a ** b


def division (a, b):
    return(a / b)

eleccion = 0
while eleccion != 7:
    print("""
    indique la operacion a realizar:

    1)suma
    2)resta
    3)multiplicaccion
    4)division
    5)factorial
    6)potencia
    7)salir

""")
    eleccion = int(input())
 
        #resta
    if eleccion == 2:
        numero1 = int(input("ingrese el primer numero:"))
        numero2= int(input("ingrese el sendo numero:"))
    
        print(f"{numero1} - {numero2} =", restar(numero1, numero2))
       
        #factorial
    if eleccion == 5:
        numero = int(input("numero:"))
        factorial = 1
        if numero !=0:
            for i in range(1, numero + 1):
                factorial = factorial * i
            
        if numero < 0: 
            print("error")

        if numero > 0:
            print("factorial:",factorial)

#potencia 
    if eleccion == 6:
        numero1 = int(input("numero:"))
        numero2= int(input("elevado a"))
    
        print(numero1,"elevado a", numero2,"=", potencia(numero1, numero2))

#division
    if eleccion == 4:
        numero1 = int(input("numero:"))
        numero2= int(input("dividido por:"))
    
        print(numero1,"/", numero2,"=", division(numero1, numero2))

       
         
    if eleccion ==1:
        cantidad_suma=int(input("ingrese la cantidad de numeros a sumar:"))
        suma =0
        for i in range(1,cantidad_suma+1):
            numero=int(input("digite el numero:"))
            suma = suma + numero
        print("resultado:",suma)


            


        #salir
    if eleccion == 7:
            print("adios")
       

            
     
            
    



