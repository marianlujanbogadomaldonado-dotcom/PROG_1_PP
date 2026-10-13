def pedir_edad():
    """
    Solicita al usuario una edad por consola, valida
    que se encuentre en el rando de 1 al 120, y la retorna como numero enetero.
     """
    edad = int(input("Ingrese su edad(entre 1 y 120):" ))
# Crear un bucle infinito de validación
    while edad < 1 or edad > 120:
       print("ERROR: ingrese un numero entre 1 y 120")
       edad = int(input("ingrese un numero valido (entre 1 y 120):"))
    return edad 
# pedir_edad()

def es_par(numero):
    """
    Recibe un número entero y retorna True si es par y en caso que sea impar  
    retorna False.
    """
    if numero % 2 == 0:
       return True
    else: 
        return False
# print(es_par(7))


# EJERCICIO 3: Menu de opcioes 
def mostrar_menu():
    """
    Muestra un menu de opciones, valida que la respuesta del usuario sea 
    1,2 o 3, y retorna la opción correcta.
    """
    print("---MENÚ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    opcion = int(input("Elija una opción (1, 2 o 3):"))
    while opcion < 1 or opcion > 3:
        print("Error: debe ingresar la opción (1, 2 o 3):")
        opcion = int(input("Elija una opcion valida (1, 2 o 3):"))
    return opcion
#mostrar_menu()


#EJERCICIO 4: validación de Nota de Parcial
def pedir_nota():
    """
    Solicita al usuario una nota por consola, valida
    que se encuentre en el rango de 1 al 10, y la retorna como número entero.
    """
    nota = int(input("Ingrese su nota del parcial, debe de ser del (1 al 10):"))

    while nota < 1 or nota > 10:
        print("ERROR: la nota que ingreso es invalida.")
        nota = int(input("Reingrese la nota, debe de ser entre (1 al 10):"))
    return nota 
# pedir_nota()

#EJERCICIO 5: Mayor de Tres Números
def obtener_mayor(num1, num2, num3):
    """
    Recibe tres número, compara los valores y retorna el número mayor.
    """

    if num1 > num2 and num1 > num3:
       return num1
    elif num2 > num3:
       return num2
    else:
        return num3


    # Ejercicio 6:  Calculadora de Descuento
def calcular_descuento(precio, porcentaje):
    """
    Recibe el precio de un producto y el porcentaje de descuento,
    calcula el precio final aplicando el descuento y lo retorna.
    """ 
    monto_descuento = (precio * porcentaje) / 100
    precio_final = precio - monto_descuento
    return precio_final


# EJERCICIO 7: Validación de DNI o Rango numerico 
def pedir_dni():
    """
    Solicitar al usuario su número de dni, valida si se encuentra en el rango de
    1.000.000 a 100.000.000 y finalmente retorna el número validado como entero.
    """
    dni = int(input("Ingrese su número de DNI:"))
    while dni < 1000000 or dni > 100000000:
        print("Error, numero ingresado no es valido.")
        dni = int(input("Ingrese su número de DNI nuevamente:"))
    return dni 
# pedir_dni()


# EJERCICIO 8: Clasificador de Edades.
def clasificar_edad(edad):
    """
    Recube una edad como parametro y retorna un texto según corresponda.
    """
    if edad < 18:
        return "Menor de edad"
    elif edad > 18 and edad < 64:
        return "Adulto"
    
    else:
        return "Adulto mayor"


# EJERCICIO 9: Calcukadora de Envio según el peso
def calcular_costo_envio(peso):
    """
    Recibe el peso en kilogramos como número  y retorna
    el costo del envio.
    """
    if peso <= 1:
        return 1500
    elif peso <= 5:
        return 3000
    else:
        return 5000


# EJERCICIO 10: Descuento por Categoria de Socio
def calcular_descuento_socio(monto, categoria):
    """
    Recibe el monto de una compra y la categoria del socio y
    retorna el monto final con el descuento aplicado.
    """
    if categoria == "A":
        return monto - (monto * 0.20)
    elif categoria == "B":
        return monto - (monto * 0.10)
    else:
        return monto


# EJERCICIO 11: Validador de rando de temperatura
def pedir_temperatura():
    """
    Solicita al usiario ingresar una temperatura, que debe de estar en el rango de -10 y 40
    valida el dato y luego retorna la temperatura validada como entero.
    """
    temperatura = int(input("Ingrese una temperatura:"))
    while temperatura < -10 or temperatura > 40:
        print("ERROR: la temperatura que ingreso no es invalida.")
        temperatura = int(input("Reingrese la temperatura nuevamente:"))
    return temperatura 
# pedir_temperatura()


# Validación de generos:
def validar_genero():
    """
    Valida que el genero ingresado sea F, M o X de forma estricta
    """
    genero = input("Ingrese género (F / M / X):")
    while genero != 'F' and genero != 'M' and genero != 'X':
        print("Error: Genero invalido. Debe incresar exactamente F,M o X.")
        genero = input("Ingrese genero (F / M / X)")
    return genero


# Validación de legajos
def validacion_legajos():
    """
    Valida y solicita por consola el ingreso de un número de legajo.
    Controla que sea un número entero positivo mayor a 0.
    """
    legajo = int(input("Ingrese su numero de legajo(entero positivo):"))
    while legajo <= 0:
        print(" Error: El legajo debe ser un número mayor a 0.")
        legajo = int(input("Ingrese número de legajo (entero positivo):"))
    return legajo

# busqueda por legajo:
def buscar_por_legajo(legajos, nombres, genero, p1, p2):
    """
    Busca un estudiante por su número de legajo y muestra sus datos
    utilizando las funciones de visualización
    """
    print("---BUSCAR ESTUDIANTE POR LEGAJO---")
    legajo_buscado = validacion_legajos()
    encontrado = False
    for i in range(len(legajos)):
        if legajos[i] == legajo_buscado:
           mostrar_un_estudiante(i, legajos, nombres, genero, p1, p2)
           encontrado = True
           break
    if not encontrado:
        print(f"AVISO: No se encontró ningún estudiante con el legajo{legajo_buscado}")

# Validacion de nombre y apellino (alfabetico )
def validar_nombre():
    """
    Valida que el apellido y nombre contenga solo letras y espacios de forma manual.
    """
    valido = False
    while not valido:
        nombre = input("Ingrese apellido y nombre:")
        if nombre == "":
            print("Error: el campo no puede estar vacío.")
        else:
            valido = True
            i = 0
            while i < len(nombre):
                caracter = nombre [i]
                es_minuscula = ('a' <= caracter <= 'z')
                es_mayuscula = ('A' <= caracter <= 'Z')
                es_espacio = (caracter == ' ')
                if not (es_minuscula or es_mayuscula or es_espacio):
                    valido = False 
                i += 1 
            if not valido :
                print("Error: El nombre solo debe contener letras y espacios.")
    return nombre 


# cargar datos:
def cargar_datos_(legajos, nombres, generos, p1, p2):
    """
    Realiza la carga masiva de los 30 estudiantes validando cada dato.
    """
    for i in range(30):
        print(f"\nEstudiante N° {i + 1}:")
       
        legajos.append(validacion_legajos())
        nombres.append(validar_nombre ())
        generos.append(validar_genero ())
        p1.append(pedir_nota())
        p2.append(pedir_nota())


    # Mostrar un estidiante
def mostrar_un_estudiante (i,legajos,nombres,generos,p1,p2):
    """
    Muestra por pantalla los datos de un único estudiante
    utilizando el indice i de las listas paralelas.
    """
    print(f"Legajo:{legajos[i]} | Nombre: {nombres [i]} | Genero: {generos[i]} | Parcial1: {p1[i]} | Parcial2 : {p2[i]} ")


# Mostrar todos los estudiantes.
def mostrar_todos (legajos, nombres, generos, p1, p2):
    """
    Recorre todas las posiciones de las listas paralela
    y llama a la función mostrar_un_estudiante para cada registro.
    """
    print("---LISTADO DE ESTUDIANTES---")
    print(f"Largos -> legajos:{len(legajos)}, nombres: {len(nombres)}, generos: {len(generos)}, p1: {len(p1)}, p2: {len(p2)}")
    

    for i in range(len(legajos)):
        mostrar_un_estudiante(i, legajos, nombres, generos, p1, p2, )


# Calcular Promedio:
def calcular_promedio(p1, p2):
    """
Calcula el promedio de cada estudiante y los guarda en una nueva lista.
    """
    lista_promedios = []
    for i in range(len(p1)):
        promedio = round((p1[i] + p2[i]) / 2, 2)
        lista_promedios.append(promedio)

    return lista_promedios


# Ordenanar por promedio
def ordenar_por_promedio( legajos, nombres, generos, parcial1, parcial2, promedios, orden):
    """
    Ordena las listas paralelas según los promedios usando el método burbuja.
    Recibe el parámetro 'orden' ("ASC" o "DESC").
    """
    n = len(promedios)
    
    for i in range(n - 1):
        for j in range(n  - 1):
            
            # Definimos la condición según el sentido del ordenamiento
            if orden == "ASC":
                condicion = promedios[j] > promedios[j + 1]
            else: # Por defecto DESC
                condicion = promedios[j] < promedios[j + 1]
                
            if condicion:
                # Intercambiamos el promedio
                promedios[j], promedios[j + 1] = promedios[j + 1], promedios[j]
                
                # Intercambiamos en TODAS las listas paralelas para que no pierdan sincronía
                legajos[j], legajos[j + 1] = legajos[j + 1], legajos[j]
                nombres[j], nombres[j + 1] = nombres[j + 1], nombres[j]
                generos[j], generos[j + 1] = generos[j + 1], generos[j]
                parcial1[j], parcial1[j + 1] = parcial1[j + 1], parcial1[j]
                parcial2[j], parcial2[j + 1] = parcial2[j + 1], parcial2[j]
# Mostrar Mayor Promedio:
def mostrar_mayor_promedio( legajos, nombres, generos, p1, p2, promedios):
    """
    Busca el mayor promedio y  mouestra al estudiante o estudiantes que lo tengan.
    """
    if len(promedios) == 0:
        print("No hay promedios calculados.")
        return

    mayor = promedios[0]
    for p in promedios:
        if p > mayor:
            mayor = p

    print(f"--- ESTUDIANTE/S CON MAYOR PROMEDIO ({mayor:.2f}) ---")
    
    
    for i in range(len(promedios)):
        if promedios[i] == mayor:
            
            mostrar_un_estudiante( i,legajos, nombres, generos, p1, p2)