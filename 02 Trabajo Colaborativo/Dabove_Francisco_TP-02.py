#ejercicio 1
print ("Hola Mundo!")

#ejercicio 2
nombre= input ("por favor ingrese su nombre: ")
print (f"Hola {nombre}")

#ejercicio 3
nombre= input ("ingrese su nombre: ")
apellido= input ("ingrese su apellido: ")
edad= input ("ingrese su edad: ")
residencia= input ("ingrese su lugar de residendia: ")
print (f"Hola soy {nombre} {apellido}, tengo {edad} anos y soy de {residencia}")

#ejercicio 4
radio= float(input ("ingrese el radio del circulo: "))
area=math.pi*radio**2
perimetro= 2*math.pi*radio
print (f"el area del circulo es {area} y su perimetro es {perimetro}")

#ejercicio 5
segundos= int(input("ingrese la cantidad de segundos: "))
horas= segundos/3600
print(f"{segundos} segundos equivalen a {horas} horas")

#ejercicio 6
numero = int(input("ingrese un numero: "))
print(f"Tabla de multiplicar del {numero}:\n")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero}*{i} = {resultado}")

#ejercicio 7
num1= float(input("ingrese un numero entero mayor a 0: "))
num2= float(input("ingrese un segundo numero entero mayor a 0: "))
suma= num1+num2
division= num1/num2
multiplicacion= num1*num2
resta= num1-num2
print(f"la suma de ambos numeros es {suma}, su division es {division}, su multiplicacion es {multiplicacion} y su resta es {resta}")

#ejercicio 8
altura= float(input("ingrese su altura: "))
peso= float(input("ingrese su peso corporal: "))
imc= peso/(altura**2)
print(f"su indice de masa corporal es: {imc}")

#ejercicio 9
grados_celsius= float(input("ingrese la temperatura en grados celsius: "))
grados_fahrenheit= Fraction(9, 5)*(grados_celsius)+32
print(f"los {grados_celsius} grados celsius equivalen a {grados_fahrenheit} grados fahrenheit")

#ejercicio 10
numero1= float(input("ingrese el primer numero: "))
numero2= float(input("ingrese el segundo numero: "))
numero3= float(input("ingrese el tercer numero: "))
promedio= (numero1+numero2+numero3)/3
print(f"el promedio de los tres numeros es {promedio}")