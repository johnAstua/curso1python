#problema 1 sacar factorial

#crear una variable, convertirla en entero
numero = int(input("numero:"))
factorial = 1         #guardar factorial del numero, iniciar en 1
if numero != 0:       #preguntar si el numero encontrado es diferente a 0
    for i in range(1, numero + 1): #va empezar desde 1 hasta el numero ingresado + 1 porque estaria por debajo
        factorial = factorial * i #factorial = a factorial pero multiplicado por i

if numero < 0:  #si el numero es menor que cero dara error
    print("error")

if numero > 0 :
    print("factorial:",factorial)

# imprime el factorial
