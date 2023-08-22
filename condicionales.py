
fechaIngresada = str(input("Ingrese la fecha de hoy: ")) #lunes, 22/8

fecha = [str(fechaIngresada[:fechaIngresada.index(",")]), int(fechaIngresada[fechaIngresada.index(",") + 1:fechaIngresada.index("/")]), int(fechaIngresada[fechaIngresada.index("/") + 1:])]

dias = ["lunes", "martes", "miercoles", "jueves", "viernes"]

if (fecha[1] > 31 or fecha[2] > 12 or not(fecha[0].lower() in dias)) :
    print("Se produjo un error. ")

# Una vez indicada la fecha el usuario necesita poder indicar si ese día se tomaron los
# exámenes, pero eso solo si se trata de los niveles inicial, intermedio o avanzado, ya
# que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo
# exámenes, el usuario ingresará cuántos alumnos aprobaron y cuantos no, y el
# programa le mostrará el porcentaje de aprobados.
# Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el
# porcentaje de asistencia a clase y el programa le indicará ‘asistió la mayoría’ en caso de
# que la asistencia sea mayor al 50% o ‘no asistió la mayoría’ si no es así.

diasExamen = ["lunes", "martes", "miercoles"]

if(fecha[0].lower() in diasExamen):
    isExamen = input("Se tomaron examenes? Si/No. ")
    if(isExamen.lower() == "si"):
        aprobados = int(input("Cuantos alumnos aprobaron? "))
        desaprobados = int(input("Cuantos alumnos no aprobaron? "))
        total = aprobados + desaprobados
        porcentaje_aprobados = (aprobados/total)*100
        print(f"El porcentaje de aprobados es: {porcentaje_aprobados}%")

if(fecha[0] == dias[3]):
    asistencia = float(input("Ingrese el porcentaje de asistencia a clases: "))
    if(asistencia > 50.0):
        print("Asistio la mayoria.")
    else:
        print("No asistio la mayoria.")  


# Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o del
# mes 7, se deberá imprimir ‘Comienzo de nuevo ciclo’ y solicitar al usuario que ingrese
# la cantidad de alumnos del nuevo ciclo y el arancel en $ por cada alumno, para luego
# imprimir el ingreso total en $.

if(fecha[0] == dias[4]): 
   if(fecha[1] == 1 and (fecha[2] == 1 or fecha[2] == 7)):  
        print("Comienzo de nuevo ciclo.")
        cant_alumnos = int(input("Ingrese la cantidad de alumnos: "))
        arancel = float(input("Ingrese el arancel por alumno: "))
        ingreso_total = cant_alumnos * arancel
        print(f"El ingreso total es {ingreso_total}$")

        