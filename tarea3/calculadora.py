""" #Debe crear una aplicación que funcione como una calculadora. Debe tomar en
 cuenta las siguientes consideraciones:
 ● La aplicación debe ser capaz de ejecutar las siguientes operaciones:
 ○ Suma: entre n números
 ○ Resta: entre 2 números
 ○ Multiplicación: entre n números
 ○ División: entre 2 número
 ○ Factorial: de 1 número
 ○ Potencia: 1 número elevado al otro"""

#primero hay que crear una interfaz para que el usuario navege en las diferentes opciones



 #funciones de la calculadora 
#resta
def restar(a, b):  #funcion para poder restar 2 numeros ingresados por el usuario(a y b)
    return a - b

#potencia
def potencia(a, b):  #funcion para elevar un numero ingresado por el usuario(a elevado a b)
     return a ** b

#division
def division (a, b): #funcion para dividir 2  numeros ingresados por el usuario
    return(a / b)



eleccion = 0 #significa que la eleccion no se a realizado
#preguntar la opereracion que quiere realizar    
while eleccion != 7: #el usuario debe poner un numero menor o igual a 7 para elegir una opcion de la calculadora 
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
    eleccion = int(input())  #convierte el numero ingresado por el usuario  en un entero para elegir una de la opciones

#1 suma
    if eleccion ==1: #si ingresa un 1 el usuario entrara en la suma
        cantidad_suma=int(input("ingrese la cantidad de numeros que quiere sumar:")) #el usuario ingresa la cantidad de numeros que quiere sumar 
        suma =0   #esto significa que la suma no se a realizado, es para sumar todos lo elemento ingresados
        for i in range(1,cantidad_suma+1):  #esto hace que ingrese la cantidad de numeros que eligio
            numeros=int(input("digite el numero:"))#el usuario ingresa los numeros que quiere sumar y se guarda en la variable numeros
            suma = suma + numeros  #se suma todos los numeros ingresados por el usuario 
        print("resultado de la suma:",suma) #imprime el resultado de la suma



 
#2 resta                 
    if eleccion == 2: #si el usuario ingresa un 2 entrara en la resta
        numero1 = int(input("ingrese el primer numero:"))  #el usuario ingresa el primer numero
        numero2= int(input("ingrese el segundo numero:"))   #el usuario ingresa el segundo numero
    
        print(f"{numero1} - {numero2} =", restar(numero1, numero2)) #esto hace que la operacion con los numeros ingresados aparezcan junto con el resultado(se usa la funcion restar creada)


#3 multiplicacion
    if eleccion == 3: #si el usuario ingresa un 3 entrara en la multiplicacion
        cantidad_multiplicacion=int(input("ingrese la cantidad de numeros que quiere multiplicar:")) #se ingresa la cantidad de numeros que se quiere multiplicar 
        multiplicacion =1 #inicia en 1
        for i in range(1,cantidad_multiplicacion+1): #esto hace que se repita la variable numero la cantidad de numeros que quiere multiplicar 
            numeros=int(input("digite el numero:")) #ingresa los numeros que quiere multiplicar y se guardan en la variable numeros
            multiplicacion = multiplicacion * numeros #se multiplica los numeros que ingreso el usuario 
        print("resultado:",multiplicacion)   #imprime el resultado de la multiplicacion






#4 division
    if eleccion == 4: #si el numero ingresado por el usuario es 4 entrara en la division
        numero1 = int(input("numero:")) #el usuario ingresa el primer numero
        numero2= int(input("dividido por:")) #el usuario ingresa el segundo numero
    
        print(numero1,"/", numero2,"=", division(numero1, numero2)) #esto hace que la operacion con los numeros ingresados aparezcan junto con el resultado(se usa la funcion de division creada)
       







#5 factorial
    if eleccion == 5: #si el numero ingresado por el usuario entrara en el factorial 
        numero = int(input("numero:")) #el usuario ingresa un numero y se guarda en la variable numero
        factorial = 1 #inicia en 1
        if numero !=0: #si el numero  no es igual a 0 
            for i in range(1, numero + 1):#del 1 hasta el numero ingresado
                factorial = factorial * i#de 1 se multiplica hasta el numero ingresado
            
        if numero < 0:  #si el numero es menor a 0 va a impimir error
            print("error")

        if numero > 0: #si el numero es mayor a 0 va a imprimir el resultado del numero ingresado
            print("factorial:",factorial)




 #6 potencia
    if eleccion == 6: #si el usuario ingresa un 6 entrara en la potencia
        numero1 = int(input("numero:")) #el usuario ingresa un numero 
        numero2= int(input("elevado a:"))#el usuario ingresa a que numero lo quiere elevar 
    
        print(numero1,"elevado a", numero2,"=", potencia(numero1, numero2)) #esto hace que la operacion con los numeros ingresados aparescan junto con el resultado(se usa la funcion potencia creada)

          
          
          #salir
    if eleccion == 7: #si el usuario ingresa 7 saldra de la calculadora 
        print("apagada")

        #final