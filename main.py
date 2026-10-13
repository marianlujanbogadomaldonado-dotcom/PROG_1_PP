import funciones_validaciones
def main ():
    legajos = []
    nombres = []
    generos = []
    p1 = []
    p2 = []
    opcion = 0
    while opcion != 7:
        print("--- MENU---")
        print("1. Cargar datos")
        print("2. Mostrar todos los datos")
        print("3. Calcular promedios")
        print("4. Mostrar ordenados por promedio (DESC)")
        print("5. Mostrar estudiante con mayor promedio")
        print("6. Buscar estudiante por legajo")
        print("7. Salir")

        opcion = int(input("Ingrese una opción (1-7):"))
        match opcion:
            case 1: 
                funciones_validaciones.cargar_datos_(legajos, nombres, generos, p1, p2)
            case 2 | 3| 4| 5| 6:
                if len(legajos) == 0:
                    print("ERROR: Debe de cargar los datosprimero(Opción 1).")
                else:
                    if opcion == 2:
                        funciones_validaciones.mostrar_todos(legajos, nombres, generos, p1, p2)
                    elif opcion == 3:
                        promedios = funciones_validaciones.calcular_promedio(p1, p2)
                        print("¡Promedios calculados con exito!")
                    elif opcion == 4:
                        promedios = funciones_validaciones.calcular_promedio(p1,p2)
                        funciones_validaciones.ordenar_por_promedio( legajos, nombres, generos, p1, p2, promedios,  "DESC")
                        funciones_validaciones.mostrar_todos(legajos, nombres, generos, p1, p2)
                    elif opcion == 5:
                        promedios = funciones_validaciones.calcular_promedio(p1, p2)
                        funciones_validaciones.mostrar_mayor_promedio( legajos, nombres, generos, p1, p2,promedios )
                    elif opcion == 6:
                        funciones_validaciones.buscar_por_legajo(legajos, nombres,  generos, p1, p2)
            case 7:
                print("Saliendo del programa. ¡Haasta luego!")
            case _:
                print("ERROR: opción inválida. Ingrese un número del 1 al 7.")
main()


