#ejercicio 1
edad= int(input("ingrese su edad por favor: "))
if edad>=18:
    print("es mayor de edad")
else:
    print("no es mayor de edad")

#ejercicio 2
nota= int(input("ingrese su nota por favor: "))
if nota>=6:
    print("aprobado")
else:
    print("desaprobado")

#ejercicio 3
numero_par= int(input("ingrese un numero par: "))
if numero_par %2==0:
    print("ha ingresado un numero par")
else:
    print("por favor, ingrese un numero par")

#ejercicio 4
edad_persona= int(input("por favor ingrese su edad: "))
if edad_persona<12:
    print("es niño/a")
elif edad_persona>=12 and edad_persona<18:
    print("es adolescente")
elif edad_persona>=18 and edad_persona<30:
    print("es un adulto/a joven")
else:
    print("es adulto/a")

#ejercicio 5
contraseña= input("por favor ingrese una contraseña de entre 8 y 14 caracteres: ")
if 8<= len(contraseña) <=14:
    print("ha ingresado una contraseña correcta")
else:
    print("contraseña incorrecta, por favor ingrese una contraseña entre 8 y 14 caracteres")

#ejercicio 6
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)

try:
    moda = mode(numeros_aleatorios)
except:
    moda = "No hay una sola moda"

print("Lista de números:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if isinstance(moda, (int, float)):
    if media > mediana > moda:
        print("La distribución tiene sesgo positivo (a la derecha)")
    elif media < mediana < moda:
        print("La distribución tiene sesgo negativo (a la izquierda)")
    elif media == mediana == moda:
        print("La distribución no tiene sesgo")
    else:
        print("La distribución no cumple exactamente con los criterios de sesgo")
else:
    print("No se puede determinar el sesgo porque no hay una moda única")

#ejercicio 7
texto = input("Ingrese una palabra o frase: ")
vocales = "aeiouAEIOU"
if texto[-1] in vocales:  
    texto += "!"
print("Resultado: ", texto)

#ejercicio 8
su_nombre= input("por favor ingrese su nombre: ")

print("seleccione una de las siguientes opciones por favor:")
print("1. su nombre en MAYUSCULAS")
print("2. su nombre en minusculas")
print("3. su nombre con la primer letras en mayuscula")

opcion= input("ingrese la opcion deseada 1, 2 o 3:")

if opcion == "1":
    print(su_nombre.upper())
elif opcion == "2":
    print(su_nombre.lower())
elif opcion == "3":
    print(su_nombre.title())
else:
    print("opcion no valida, vuelva a intentarlo")

#ejercicio 9
magnitud= int(input("por favor ingrese la magnitud del terremoto: "))

if magnitud <3:
    print("terremoto muy leve")
elif magnitud >=3 and magnitud <4:
    print("terremoto leve")
elif magnitud >=4 and magnitud <5:
    print("terremoto moderado")
elif magnitud >=5 and magnitud <6:
    print("terremoto fuerte")
elif magnitud >=6 and magnitud <7:
    print("terremoto muy fuerte")
else:
    magnitud >=7
    print("terremoto extremo")

#ejercicio 10
hemisferio= input("Ingrese el hemisferio (NORTE/SUR): ")
mes= int(input("Ingrese el mes (1-12): "))
dia= int(input("Ingrese el día (1-31): "))

estacion = ""
if hemisferio == "NORTE":
    if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or mes in (10, 11) or (mes == 12 and dia <= 20):
        estacion = "Otoño"

elif hemisferio == "SUR":
    if (mes == 12 and dia >= 21) or mes in (1, 2) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or mes in (4, 5) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or mes in (7, 8) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or mes in (10, 11) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
else:
    print("Hemisferio no válido (debe ser N o S)")

if estacion:
    print(f"En el hemisferio {hemisferio}, el {dia}/{mes} es {estacion}.")
