#nos piden que que {nombre : nota} solo hay que calcular el promedio y anotar el nombre
#calcular el rpomedio del estudiante
nombre_estudiante = (input("nombre del estudiante:"))
#notas
n1 = float(input("ingrese la nota de historia:"))
n2 = float(input("ingrese la nota de matematicas:"))
n3 = float(input("ingrese la nota de fisica:"))
#operacion
promedio = (n1 + n2 + n3) / 3

#diccionario
promedio_estudiantes ={
 nombre_estudiante : promedio

}
#imprimir los datos del estudiante 
print (promedio_estudiantes)