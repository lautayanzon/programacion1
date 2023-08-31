import math

# Crear un programa que reciba el número de años que tiene nuestra computadora y muestre en la consola que el computador es nuevo si es menor o igual a 2 años y que el computador es viejo si es mayor a 2 años.
# Hacer que el programa anterior muestre un mensaje de error si el usuario digita un número negativo.
#Ejercicio 1 y 2

anios = int(input("Ingrese la cantidad de años del ordenador: \n"))
if (anios < 0):
        print("Los años ingresados deben ser positivos")
elif(anios >= 0 and anios<=2):
        print("El ordenador es nuevo")
elif(anios > 2):
        print("El ordenador es viejo")

#Ejercicio 3
# Solicitar al usuario que ingrese los nombres de dos personas, los cuales se almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ si ambos nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.

nombre1 = input("Ingrese el nombre de la primer persona")
nombre2 = input("Ingrese el nombre de la segunda persona")
if (nombre1[0] == nombre2[0]):
        print("Coinciden")
else:
        print("No coinciden")

# Crear un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verde, candidato C por el partido azul.
# Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado por el partido [color del candidato elegido].
# Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar ‘Opción errónea.’
#Ejercicio 4
candidatos = {
        "A": "Rojo",
        "B": "Verde",
        "C": "Azul"
}

print("Elección de candidato:")
for clave, valor in candidatos.items():
        print(f"{clave} - Candidato por el partido {valor}")

opcion = input("Ingrese la letra del candidato por el cual desea votar: ").upper()

if (opcion in candidatos):
        print(f"Usted ha votado por el partido {candidatos[opcion]}.")
else:
        print("Opción errónea.")

# Escribir un programa que solicite al usuario una letra, si es una vocal, mostrar el mensaje ‘Es vocal’.
# Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string de más de un carácter, informarle que no se puede procesar el dato.
#Ejercicio 5

vocales = 'aeiou'

vocal = input("Ingrese una letra: ").lower()

if (len(vocal) != 1):
        print("No se puede procesar el dato.")
elif (vocal in vocales):
        print("Es vocal.")
else:
        print("No es vocal")

# Hacer un programa que permita saber si un año es bisiesto. Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.
#Ejercicio 6

anio = int(input("Ingrese el año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        print("Es bisiesto")
else:
        print("No es bisiesto")

        
# Escribí un programa para solicitar al usuario tres números y mostrar en pantalla al menor de los tres.
#Ejercicio 7
print("Ingrese 3 numeros: ")
numeros = [int(input("Primero: ")), int(input( "Segundo: ")),int(input("Tercero: "))]

menor = numeros[0]

for num in numeros:
    if (num < menor):
           menor = num

print(f"El menor de los 3 es {menor}")

# Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla “Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o la contraseña no coinciden, mostrar “Acceso denegado”.
#Ejercicio 8

usuario = "gwenevere"
contrasena = "excalibur"
usuario_in = input("Ingrese el usuario: ")
contrasena_in = input("Ingrese la contraseña: ")

if (usuario == usuario_in.lower() and contrasena == contrasena_in.lower()):
        print("Usuario y contraseña correctos. Puede ingresar a Camelot.")
else:
        print("Acceso denegado.")


# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
#Ejercicio 9

nombre = input("Ingrese el nombre: ").lower()
sexo = input("Ingrese el sexo F/M: ").lower()

if(sexo == 'f' and nombre[0].lower() < 'm') or (sexo == 'm' and nombre[0].lower() > 'n'):
        grupo = "A"
        print("Corresponde grupo A.")
else:
        print("Corresponde grupo B.")


# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $500 y si es mayor de 18 años, $1000.
#Ejercicio 10



edad = int(input("Ingrese su edad: "))
if (edad < 4):
        print("Puede entrar gratis.")
elif(edad > 4 and edad < 18):
        print("Debe pagar $500.")
else:
        print("Debe pagar $1000.")


# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# Ingredientes vegetarianos: Pimiento y tofu.
# Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
#Ejercicio 11
print("Bienvenido a la pizzería Bella Napoli!")
print("Opciones de pizza:")
print("1. Vegetariana")
print("2. No vegetariana")

opcion = int(input("Seleccione el tipo de pizza (1/2): "))

if opcion == 1:
        pizza = "Vegetariana"
        print("Usted a elegido la pizza Vegetariana")
        ingredientes_disponibles = ["Pimiento", "Tofu"]
elif opcion == 2:
        pizza = "No vegetariana"
        print("Usted a elegido la pizza No Vegetariana")
        ingredientes_disponibles = ["Peperoni", "Jamón", "Salmón"]
else:
        print ("Opcion mal")
print(f"Excelente elección: Pizza {pizza}!\nIngredientes disponibles:")
for i, ingrediente in enumerate(ingredientes_disponibles, start=1):
        print(f"{i}. {ingrediente}")
seleccion = int(input(f"Seleccione un ingrediente: "))
if seleccion < 1 or seleccion > len(ingredientes_disponibles):
        print("Selección inválida.")
ingrediente_elegido = ingredientes_disponibles[seleccion - 1]
print(f"Usted ha elegido una pizza {pizza} con los siguientes ingredientes:")
print("Mozzarella, Tomate,", ingrediente_elegido)

# Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde ese año o cuántos años faltan para llegar a ese año.
#Ejercicio 12

anio_actual_igresado = int(input("Ingrese el año actual: "))
anio_cualquiera = int(input("Ingrese el año cualqueria: "))
if(anio_actual_igresado > anio_cualquiera):
        diferencia = anio_actual_igresado - anio_cualquiera
        print(f"La cantidad de años que han pasado son: {diferencia}")
else:
        diferencia = anio_cualquiera - anio_actual_igresado
        print(f"La cantidad de año que faltan son: {diferencia}" )



# Escriba un programa que pida dos números enteros y que escriba si el mayor es múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos o nulos.
#Ejercicio 13
num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

if num1 <= 0 or num2 <= 0:
        print("Por favor ingrese valores positivos y no nulos.")
else:
        if num1 > num2:
                mayor = num1
                menor = num2
        else:
                mayor = num2
                menor = num1

if mayor % menor == 0:
        print(f"El mayor número ({mayor}) es múltiplo del menor número ({menor}).")
else:
        print(f"El mayor número ({mayor}) no es múltiplo del menor número ({menor}).")



# Escriba un programa que pida los coeficientes de una ecuación de primer grado (a x + b = 0) y escriba la solución.
# Se recuerda que una ecuación de primer grado puede no tener solución, tener una solución única, o que todos los números sean solución. Se recuerda que la fórmula de las soluciones es 
# x = -b / a
#Ejercicio 14
a = float(input("Ingrese el primer valor: "))
b = float(input("Ingrese el segundo valor: "))

if (a == 0):
        if (b == 0):
                print("La ecuacion tiene infinitas soluciones")
        else:
                print("La ecuacion no tiene solucion")
else:
        resultado = ((-b)/a)
        if (resultado == -0.0):
                print("El resultado es: 0")
        else:
                print(f"El resultado es: {resultado}")



# Escriba un programa que pregunte primero si se quiere calcular el área de un triángulo o la de un círculo. Si se contesta que se quiere calcular el área de un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base y la altura y escribir el área. Si se contesta que se quiere calcular el área de un círculo (escribiendo C o c), el programa tiene que pedir entonces el radio y escribir el área.
#Ejercicio 15

calcular = input("Que area desea calcular, la de un triangulo o un circulo (T/A): ")
calcular = calcular.upper()
if calcular == "T":
        base = float(input("Ingrese la base: "))
        altura = float(input("Ingrese la altura: "))
        area = (base*altura)/2
        print(f"El area del triangulo es: {area}")
elif calcular == "A":
        radio = float(input("Ingrese el radio del circulo: "))
        area = math.pi * radio ** 2
        print(f"El area del circulo es: {area}")
else:
        print("Ingrese una opcion correcta")




# Haz una calculadora básica pida al usuario dos valores, a y b.
# Según la opción que desean, realizar la operación:
# Si operación es 1 entonces debemos ver el resultado de a + b
# Si operación es 2 entonces debemos ver el resultado de a * b
# Si operación es 3 entonces debemos ver el resultado de a - b
# Si operación es 4 entonces debemos ver el resultado de a / b
#Ejercicio 16

a = float(input("Ingrese el primer valor"))
b = float(input("Ingrese el segundo valor"))
print("Eligue la operacion a realizar")
print("1. Suma")
print("2. Multiplicacion")
print("3. Resta")
print("4. Division")
operacion= float(input("Ingrese el numero de la operacion a realizar: "))
if(operacion>1 and operacion<4):
        if operacion == 1:
                resultado = a + b
        elif operacion == 2:
                resultado = a * b
        elif operacion == 3:
                resultado = a - b
        elif operacion == 4:
                resultado = a / b
else:
        print("Ingrese una opcion correcta")
print(f"El resultado de la operacion es: {resultado}")



# Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.

#Ejercicio 17

dia = str(input("Ingrese el dia: "))
dia = dia.lower()

if dia == "lunes":
        print("El dia es Lunes")
elif dia == "viernes":
        print("El dia es Viernes")
elif dia == "sabado" or dia == "domingo":
        print("El dia es Sabado o Domingo")
else:
        print("El dia es Martes, Miercoles o Jueves")




# Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
# La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, si trabajó horas extras y mostrar esta cantidad.
# Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas un 10% más que las horas laborales comunes.
#Ejercicio 18

horas = int(input("Ingrese la cantidad de horas trabajadas: "))
salario_hora = float(input("Ingrese su salario por hora: "))

if horas > 48:
        horas_extras = horas - 48
        horas = horas - horas_extras
        print(f"Usted trabajo un total de {horas_extras} hs extras")
        salario = horas * salario_hora + (((salario_hora*0.10)+salario_hora)*horas_extras)
        print(f"Su salario es de: {salario}")
else:
        salario = horas * salario_hora
        print(f"Su salario es de: {salario}")



# Determinar cuánto se debe pagar por una cantidad de lápices considerando que si son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz es de $60; de lo contrario no hay descuento.
#Ejercicio 19
cant_lapiz = int(input("Ingrese la cantidad de lapices a comprar: "))
if cant_lapiz >= 1000:
        descuento = 60-(60*0.07)
        total = cant_lapiz * descuento
        print(f"El total a pagar con el descuento por la compra de mas de 1000 lapices es de: {total}")
else:
        total = cant_lapiz * 60
        print(f"El total a pagar es de: {total}")



# Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario saldrá desaprobado.
#Ejercicio 20
nota = 0
cantidad = 0
for i in range(4):
        nota_i = int(input("Ingrese la nota del alumno: "))
        nota = nota + nota_i
        cantidad = cantidad + 1
promedio = nota / (cantidad)
print(f"El promedio de notas es de: {promedio}")

if promedio<6:
        print("Desaprobado")
else:
        print("Aprobado")