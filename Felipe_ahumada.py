from os import system
system("cls")
from random import randint
from statistics import geometric_mean

def asignar_sueldos():
    global lista_trabajadores
    global total_sueldos
    global todos_sueldos 
    trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", 
                "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]
    lista_trabajadores = []
    total_sueldos = 0
    todos_sueldos = []
    for i in range(len(trabajadores)):
        sueldo = randint(300000, 2500000)
        lista_trabajadores.insert(i, [])
        lista_trabajadores[i].insert(i,trabajadores[i])
        lista_trabajadores[i].append(sueldo)

    for i in range(len(lista_trabajadores)):
        total_sueldos += lista_trabajadores[i][1]

    #Lista para media
    for i in range(len(lista_trabajadores)):
        todos_sueldos.append(lista_trabajadores[i][1])

def mostrar_empleados():
    total_sueldos_menos = 0
    trabajadores_menos = []
    sueldos_menos = []
    total_sueldos_entre = 0
    trabajadores_entre = []
    sueldos_entre = []
    total_sueldos_superior = 0
    trabajadores_superior = []
    sueldos_superior = []

    ############### Trabajadores con sueldo menor a $800.000 #######################

    for i in range(len(lista_trabajadores)):
        if lista_trabajadores[i][1] < 800000:
            trabajadores_menos.append(lista_trabajadores[i][0])
            sueldos_menos.append(lista_trabajadores[i][1])
            total_sueldos_menos += 1

    print(f"""          Sueldos menores a $800.000 TOTAL: {total_sueldos_menos}\n
                  Nombre empleado       Sueldo      """)
    for i in range(len(trabajadores_menos)):
        print(f"""
                  {trabajadores_menos[i]}           ${sueldos_menos[i]}             """)
        
    ############### Trabajadores con sueldo entre $800.000 y $2.000.000 #######################
    
    for i in range(len(lista_trabajadores)):
        if lista_trabajadores[i][1] >= 800000 and lista_trabajadores[i][1] <= 2000000:
            trabajadores_entre.append(lista_trabajadores[i][0])
            sueldos_entre.append(lista_trabajadores[i][1])
            total_sueldos_entre += 1

    print(f"""\n          Sueldos entre $800.000 y $2.000.000 
          TOTAL: {total_sueldos_entre} \n
                  Nombre empleado       Sueldo      """)
    for i in range(len(trabajadores_entre)):
        print(f"""
                  {trabajadores_entre[i]}           ${sueldos_entre[i]}             """)
    
    ############### Trabajadores con sueldo superior a $2.000.000 #######################

    for i in range(len(lista_trabajadores)):
        if lista_trabajadores[i][1] > 2000000:
            trabajadores_superior.append(lista_trabajadores[i][0])
            sueldos_superior.append(lista_trabajadores[i][1])
            total_sueldos_superior += 1

    print(f"""\n          Sueldos superiores a $2.000.000 
          TOTAL: {total_sueldos_superior} \n
                  Nombre empleado       Sueldo      """)
    for i in range(len(trabajadores_superior)):
        print(f"""
                  {trabajadores_superior[i]}           ${sueldos_superior[i]}             """)
    print(f"""
                  TOTAL SUELDOS: ${total_sueldos}""")

def ver_estadisticas():
    sueldo_mayor = 0
    sueldo_menor = 999999999
    for i in range(len(lista_trabajadores)):
        if sueldo_mayor < lista_trabajadores[i][1]:
            sueldo_mayor = lista_trabajadores[i][1]
        if sueldo_menor > lista_trabajadores[i][1]:
            sueldo_menor = lista_trabajadores[i][1]

    promedio = total_sueldos/len(lista_trabajadores)
    promedio = round(promedio)
    media = geometric_mean(todos_sueldos)
    media = round(media)
    print(f""" Estos son sus estadísticas
          
            Sueldo más alto:     ${sueldo_mayor}
            Sueldo más bajo:     ${sueldo_menor}
            Primedio de sueldos: ${promedio}
            Media geométrica:    ${media} """)
    
def reporte_sueldos():

    print(f"""\n                Nombre empleado       Sueldo base           Descuento Salud             Descuento AFP               Sueldo líquido      """)
    for i in range(len(lista_trabajadores)):
        salud = todos_sueldos[i] * 0.07
        salud = round(salud)
        afp = todos_sueldos[i] * 0.12
        afp = round(afp)
        liquido = todos_sueldos[i] - salud - afp
        print(f"""
                  {lista_trabajadores[i][0]}           ${lista_trabajadores[i][1]}              ${salud}                        {afp}               {liquido}             """)
    for i in range(len(lista_trabajadores)):
            with open("Datos.csv", "w") as archivo:
                archivo.write(f"""
                  {lista_trabajadores[i][0]}           ${lista_trabajadores[i][1]}              ${salud}                        {afp}               {liquido}             """)

print("""
1. Asignar sueldos aleatorios
2. Clasificar sueldos
3. Ver estadísticas
4. Reporte de sueldos
5. Salir del programa \n""")
while True:
    op = input("Ingrese opción deseada: ")
    match op:
        case "1":
            asignar_sueldos()
        case "2":
            mostrar_empleados()
            #Si no existen empleados, crear funcion que diga que no existen empleados
        case "3":
            ver_estadisticas()
        case "4":
            reporte_sueldos()
        case "5":
            break

#https://github.com/fesilva12/ahumada_felipe_pgy1121-003d.git