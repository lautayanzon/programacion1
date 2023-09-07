#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

word = input("Ingrese una palabra: ")
for i in range(0, 10, 1):
    print(f"{word}")


#Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

age = int(input("Ingrese su edad: "))
for i in range(1, age):
    print("Años: ", i)
    
#Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos
#los números impares desde 1 hasta ese número separados por comas.

num = int(input("Ingrese un numero entero positivo: "))

while num < 0:
    num = int(input("El numero ingresado es negativo, por favor ingrese uno positivo: "))


impar = []
for i in range(num+1):
    if (i % 2 != 0):
        impar.append(i)
impar_str = ', '.join(map(str, impar))
print("Los numeros impares son: ", impar_str)


#Escribir un programa que pida al usuario un número entero positivo y
#muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

num = int(input("Ingrese un numero entero positivo: "))

while num < 0:
    num = int(input("El numero ingresado es negativo, por favor ingrese uno positivo: "))

count = []
for i in range(num, 0, -1):
    count.append(i)
count_str = ', '.join(map(str, count))
print(count_str)


#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y 
#muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

cantidad_invertida = float(input("Ingres la cantidad a invertir: "))
int_anual = float(input("Ingrese el interes anual(0,1 = 10% de interes): " ))
num_years = int(input("Ingrese la cantidad de años: "))
capital_obtenido = cantidad_invertida
for i in range(num_years):
    capital_obtenido = (capital_obtenido * int_anual) + capital_obtenido
    print(capital_obtenido)


#Escribir un programa que pida al usuario un número entero y muestre por 
#pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

num = int(input("Ingrese un numero entero positivo: "))

while num < 0:
    num = int(input("El numero ingresado es negativo, por favor ingrese uno positivo: "))

for i in range(num + 1):
    print("*" * i)


#Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.

for i in range(1,11):
    print(f"Tabla del {i}")
    for j in range(1, 11):
        print(f"{i} x {j} = " , i*j)

#Escribir un programa que pida al usuario un número entero y 
#muestre por pantalla un triángulo rectángulo como el de más abajo.

num = int(input("Ingrese un numero entero positivo: "))

while num < 0:
    num = int(input("El numero ingresado es negativo, por favor ingrese uno positivo: "))

nums = []
if num % 2 == 0:
    num -= 1
    for i in range(1, num + 1, 2):
        nums.append(i)
else:
    for i in range(1, num + 1, 2):
        nums.append(i)

for i in range(1, len(nums) + 1):
    inicio = 2 * i - 1
    for j in range(inicio, 0, -2):
        print(j, ' ')
    print("")
    
#Escribir un programa que almacene la cadena de caracteres contraseña en 
#una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

password = "contraseña"
password_input = input("Ingrese la contraseña: ")

while password_input != password:
    password_input = input("Contraseña incorrecta, intente nuevamente: ")

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.


number = int(input("Ingrese un número entero: "))
if number <= 1:
    print("El número no es primo.")
else:
    es_primo = False
    for i in range(2, number):
        if number % i == 0:
            print("El número es primo.")
            break
        else:
            print("El número no es primo.")
            break

#Escribir un programa que pida al usuario una palabra
#y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

word = input("Ingrese una palabra: ")
for i in range(len(word) - 1, -1, -1):
    print(word[i])


#Escribir un programa en el que se pregunte al usuario por una frase y una 
#letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

phrase = input("Ingrese la frase: ")
letter = input("Ingrese la letra: ")
count = frase.count(letter)
print(f"La letra {letter} se repite un total de: {count}")


#Escribir un programa que muestre el eco de todo lo que el
#usuario introduzca hasta que el usuario escriba “salir” que terminará.

phrase = input("Ingrese una frase: ").lower()

while phrase != 'salir':
    phrase = input("Ingrese otra").lower()

#Escriba un programa que pida dos números enteros y escriba qué
#números son pares y cuáles impares desde el primero hasta el segundo.

first = int(input("Ingrese el primer numero entero: "))
second = int(input("Ingrese el segundo numero entero: "))
even = []
odd = []

for i in range(first, second, 1):
    if (i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)

print(f"Los numeros pares son: {even} y los numeros impares son: {odd}")

#Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.

num = int(input("Ingrese un numero mayor que 0: "))
if num <= 0:
    print("El numero ingresado es incorrecto o menor que 0.")
else:
    divisores = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisores.append(i)
    print(f"Los divisores son: {divisores}")

#Escriba un programa que pregunte cuántos números se van
#a introducir, pida esos números y escriba cuántos negativos ha introducido.

rep = int(input("Ingrese cuantos numeros quiere introducir: "))
contador = 0
for i in range(rep):
    num = int(input("Ingrese el numero: "))
    
    if num<0:
        contador = contador + 1
print(f"Se introdujeron {contador} numeros negativos")


#Solicitar al usuario que ingrese una frase y luego
#imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas).

phrase = input("Ingrese una frase: ")
vowels = 'aeiou'
vowels_select = set()

for i in phrase:
    if i.lower() in vowels and i.lower() not in vowels_select:
        vowels_select.add(i.lower())
print(f"Las vocales en la frase son {vowels_select}")

#Crear un algoritmo que muestre los primeros 10 números de la sucesión de Fibonacci. La 
#sucesión comienza con los números 0 y 1 y, a partir de éstos, 
#cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

fib = [0, 1]
for i in range(2,10):
    next_number = fib[i-1] + fib[i-2]
    fib.append(next_number)
for num in fib:
    print(num)

#Escriba un programa que simule una alcancía. El programa solicitará primero una cantidad, que
#será la cantidad de dinero que queremos ahorrar. A continuación, el programa solicitará una y
#otra vez las cantidades que se irán ahorrando, hasta que el total ahorrado iguale o supere al objetivo.
#El programa deberá comprobar que las cantidades ingresadas sean positivas.

tope = int(input("Ingrese la cantidad que quiere lograr ahorrar: "))
fondo = 0
while fondo < tope:
    deposito = int(input("Ingrese la cantidad que quiere depositar: "))
    if deposito < 0:
        print("El monto ingresado debe ser positivo.")
    else:
        fondo = fondo + deposito
print(f"Los fondos depositados fueron de: {fondo}")

#Leer números enteros de teclado, hasta que el usuario 
#ingrese el 0. Finalmente, mostrar la sumatoria de todos los números ingresados.

num = 1
count = 0
while num != 0:
    num = int(input("Ingrese un numero entero: "))
    count =  num + count
print(f"La sumatoria de los numeros es: {count}")

#Solicitar al usuario que ingrese números enteros positivos y, por cada uno, imprimir 
#la suma de los dígitos que lo componen. La condición de corte es que se ingrese 
#el número -1. Al finalizar, mostrar cuántos de los números ingresados por el usuario fueron números pares.

max = 0
num = 1
while num != 0:
    num = int(input("Ingrese un numero positivo: "))
    if num<0:
        print("El numero ingresado no es positivo")
    else:
        if num>max:
            max = num
print(f"El numero mayor ingresado es: {max}")

#Crear un programa que permita al usuario ingresar los montos de las compras 
#de un cliente (se desconoce la cantidad de datos que cargará, 
#la cual puede cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingrese el monto 0.

even_numbers = 0
while True:
    number = int(input("Ingrese un numero entero positivo(-1 para finalizar el programa): "))
    if number == -1:
        break
    if number<=0:
        print("Por favor ingrese un numero positivo")
        continue
    sum = 0
    numtemp = number
    while numtemp>0:
        sum += numtemp%10
        numtemp //= 10
    print(f"La sumatoria de los digitos del numero {number} es: {sum}")
    if number%2 == 0:
        even_numbers += 1
print(f"La cantidad de numeros pares ingresados es de: {even_numbers}")


#Ej 23 y 24
total = 0
while True:
    monto = float(input("Ingrese el monto de la compra(0 para salir)"))
    if monto == 0:
        break
    if monto<=0:
        print("Por favor ingrese un monto positivo")
        continue
    total = total + monto
if total > 1000:
    total = total - (total * 0.1)
print(f"El total del monto de las compras es de: {total}")

#Ej 25
facto = int(input("Ingrese el numero que quiere obtener su factorial: "))
factorial=0
if facto == 0:
    factorial = 1
elif facto< 0:
    print("Ingrese un numero positivo")
else:
    factorial = 1
    for i in range(1, facto+1):
        factorial *= i
print(f"El resultado es: {factorial}")


