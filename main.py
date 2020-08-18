#000000#000000import sys
#Opciones De Inicio
print("Options")
print("Para Salir Del Programa Escriba 0")
print("Para Comenzar Escribir 1")
user_input = input(": ")
if user_input == "0":
  sys.exit()
if user_input == "1": 
  ...
print("Escriba 2 Diferenciador Para Inciarla")
print("Escriba 3 Calculadora Para Iniciarlo")
user_input = input(": ")
if user_input == "2": 
    ...
#Diferenciar Numeros Comandos
    print("Bienvenido Al Diferenciador De Numeros En Python")
    num1 = (input("Por Favor Introduzca Un Numero: "))
    num2 = (input("Por Favor Introduzca Otro Numero: "))
    if num1 == num2:
     result = num1 == num2
     print("El Numero "  + str(num1) + " " + "Es Igual Al Numero" + " " + str(num2))
    if num1 < num2:
     result = num1 < num2
     print("El Numero "  + str(num1) + " " + "Es Menor Al Numero" + " " + str(num2))
    if num1 > num2:
     result = num1 > num2
     print("El Numero "  + str(num1) + " " + "Es Mayor Al Numero" + " " + str(num2))
     exit()

elif user_input == "3":

 import sys
#Calculadora
print("Bienvenido A La Calculadora En Python")
print("Para Comenzar Presione 4")
print("Para Salir Presione 5") 
user_input = input(": ")
if user_input == "0":
  sys.exit()
if user_input == "4": 
  ...
  print("Presione S Para Suma")
  print("Presione R Para Resta")
  print("Presione M Multipliacion")
  print("Presione D Para Division")
  user_input = input(": ")
#SUMA
if user_input == "S": 
  ...
a=(input("Ingrese Numero "))
b=(input("Ingrese Otro Numero "))
print (int (b) +int (a))
sys.exit()

#RESTA
if user_input == "R": 
  ...
a=(input("Ingrese Numero "))
b=(input("Ingrese Otro Numero "))
print (int (b) - int (a))
sys.exit()

#MULTIPLICACION
if user_input == "M":
  ... 
a=(input("Ingrese Numero "))
b=(input("Ingrese Otro Numero "))
print (int (b) *int (a))
sys.exit()

#DIVISION
if user_input == "D": 
  ...
a=(input("Ingrese Numero "))
b=(input("Ingrese Otro Numero "))
print (int (b) /int (a))
sys.exit()
