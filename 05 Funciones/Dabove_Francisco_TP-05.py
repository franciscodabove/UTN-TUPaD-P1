#trabajo practico 5 de Funciones
import random

#ejercicio 1

notas = [7, 5, 8, 9, 10, 4, 6, 7, 3, 8]
print("Notas de los estudiantes:")
for n in notas:
    print(n)

promedio = sum(notas) / len(notas)
print("Promedio:", promedio)
print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

#ejercicio 2

productos = []
for i in range(5):
    p = input(f"Ingrese el producto {i+1}: ")
    productos.append(p)

print("Lista ordenada alfabéticamente:")
for p in sorted(productos):
    print(p)

elimimar = input("Ingrese un producto a eliminar: ")
if elimimar in productos:
    productos.remove(elimimar)
print("Lista actualizada:", productos)

#ejercicio 3

numeros = [random.randint(1, 100) for _ in range(15)]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]

print("Lista completa:", numeros)
print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))

#ejercicio 4

lista = [1, 2, 2, 3, 4, 4, 5, 1, 6]
sin_repetidos = list(set(lista))
print("Lista sin repetidos: ", sin_repetidos)

#ejercicio 5

estudiantes = ["Ana", "Luis", "Juan", "Sofía", "Marcos", "Pedro", "Lucía", "Carla"]
op = input("¿Desea agregar (A) o eliminar (E) un estudiante?: ").upper()
if op == "A":
    nuevo = input("Ingrese el nombre del estudiante: ")
    estudiantes.append(nuevo)
elif op == "E":
    borrar = input("Ingrese el nombre a eliminar: ")
    if borrar in estudiantes:
        estudiantes.remove(borrar)
print("Lista final:", estudiantes)

#ejercicio 6

numeros = [1, 2, 3, 4, 5, 6, 7]
rotada = [numeros[-1]] + numeros[:-1]
print("Lista rotada: ", rotada)

#ejercicio 7

temperaturas = [
    [10, 22],
    [12, 25],
    [9, 20],
    [14, 27],
    [11, 21],
    [13, 24],
    [8, 19]
]

minimas = [fila[0] for fila in temperaturas]
maximas = [fila[1] for fila in temperaturas]

print("Promedio mínimas:", sum(minimas)/len(minimas))
print("Promedio máximas:", sum(maximas)/len(maximas))

amplitudes = [maximas[i] - minimas[i] for i in range(7)]
dia_max_amp = amplitudes.index(max(amplitudes)) + 1
print("Mayor amplitud térmica en el día:", dia_max_amp)

#ejercicio 8

notas = [
    [7, 6, 8],
    [5, 9, 7],
    [8, 8, 9],
    [6, 7, 5],
    [9, 10, 8]
]

print("Promedio por estudiante:")
for i, fila in enumerate(notas):
    print(f"Estudiante {i+1}: {sum(fila)/len(fila)}")

print("Promedio por materia:")
for j in range(3):
    materia = [notas[i][j] for i in range(5)]
    print(f"Materia {j+1}: {sum(materia)/len(materia)}")

#ejercicio 9

tablero = [["-"]*3 for _ in range(3)]

def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))

turno = "X"
for _ in range(5):  # hasta 5 jugadas de ejemplo
    print(f"Turno {turno}")
    fila = int(input("Fila (0-2): "))
    col = int(input("Columna (0-2): "))
    if tablero[fila][col] == "-":
        tablero[fila][col] = turno
        mostrar_tablero()
        turno = "O" if turno == "X" else "X"
    else:
        print("Casilla ocupada!")

#ejercicio 10

ventas = [
    [10, 12, 15, 20, 13, 17, 14],  #producto 1
    [5, 7, 8, 6, 9, 12, 10],      #producto 2
    [20, 22, 25, 23, 21, 19, 24], #producto 3
    [8, 10, 7, 6, 9, 11, 13]      #producto 4
]

print("Total vendido por producto: ")
for i, fila in enumerate(ventas):
    print(f"Producto {i+1}: {sum(fila)}")

totales_dia = [sum(ventas[i][j] for i in range(4)) for j in range(7)]
print("Día con mayores ventas:", totales_dia.index(max(totales_dia)) + 1)

totales_prod = [sum(fila) for fila in ventas]
print("Producto más vendido:", totales_prod.index(max(totales_prod)) + 1)
