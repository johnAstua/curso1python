def main():
  numero = int(input("Dígame cuántas palabras tiene la lista: "))

  if numero < 1:
      print("¡Imposible!")
  else:
      lista = []
      for i in range(numero):
          palabra = input(f"Dígame la palabra {i + 1}: ")
          lista += [palabra]
      print(f"La lista creada es: {lista}")


if __name__ == "__main__":
  main()
