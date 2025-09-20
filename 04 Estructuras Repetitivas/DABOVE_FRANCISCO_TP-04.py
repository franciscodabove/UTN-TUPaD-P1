#ejercicio 1
cont = 0
for cont in range(0,101):
    print(cont)

#ejercicio 2
numero = int(input("ingrese un numero entero: "))
cant_digitos = len(str(numero))    
#con str convierto un numero a un string
#con la funcion LEN detecto la cantidad de digitos del tring
print(f"el numero {numero} tiene {cant_digitos} digitos")

#ejercicio 3
num1 = int(input("ingrese el primer numero entero: "))
num2 = int(input("ingrese el segundo numero entero: "))
suma = 0
for i in range(num1, num2 +1):
    suma += i
print(f"la suma de los numeros comprendidos entre los dos valores es {suma}")

#ejercicio 4
suma = 0
numeros = "n"
print("ingrese numeros enteros para sumarlos. Para terminar ingrese 0(cero)")
while numeros != 0:
    numeros = int(input("ingrese los numeros: "))
    suma += numeros
    if numeros == 0:
        break
print(f"la suma de los numeros es {suma}")

#ejercicio 5
import random

numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False
print("Juego de adivinanza: adivina el número entre 0 y 9")

while not adivinado:
    intento = int(input("Ingresa tu número: "))
    intentos += 1

    if intento == numero_secreto:
        adivinado = True
    else:
        print("No es correcto, intenta de nuevo.")

print(f"Felicidades, el número era {numero_secreto}")
print(f"Lo lograste en {intentos} intento(s)")

#ejercicio 6
print("A continuacion se mostraran todos los numeros pares entre 0 y 100 en orden decreciente")
for i in range(100, -1, -2):
    print(i)

#ejercicio 7
num_entero = int(input("ingrese un numero entero mayor que 0: "))
suma = 0
for i in range(0, num_entero +1):
    suma+= i
print(f"la suma entre los valores de 0 y {num_entero} es {suma}")

#ejercicio 8
CANTIDAD = 100 

pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese {CANTIDAD} numeros enteros:")

for i in range(CANTIDAD):
    numero = int(input(f"Numero {i+1}: "))
#defino pares e impares
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
#defino positivos y negativos
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

#muestro resultados

print("Resultados:")
print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")

#ejercicio 9
cantidad = 100
suma = 0

print(f"ingrese por favor {cantidad} numeros enteros: ")

for i in range(cantidad):
    numero = int(input(f"numero {i+1}: "))
    suma += numero
    promedio = suma / cantidad

print(f"El promedio de los {cantidad} numeros ingresados es {promedio}")

#ejercicio 10
numero = input("Ingrese un número entero: ")
#utilizo una funcion para invertir el numero ingresado
invertido = numero[::-1]

print(f"El número invertido es: {invertido}")