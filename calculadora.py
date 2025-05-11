'''
Desarrollo de una calculadora de promedios escolares en Python 
utilizando variables, operadores, estructuras de control y funciones básicas.

Escuela de postgrado Newman
Autor: Daniel Chavez
Maestria en Big Data
'''

def ingresar_calificaciones():
    """
    Función para ingresar los nombres de materias y sus calificaciones.
    Retorna dos listas separadas: materias y calificaciones.
    """
    materias = []
    calificaciones = []
    
    # Solicitar al usuario el número de materias
    while True:
        try:
            num_materias = int(input("Ingrese el número de materias: "))
            if num_materias <= 0:
                print("El número de materias debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número entero válido.")
    
    # Solicitar los nombres y calificaciones de cada materia
    for i in range(num_materias):
        nombre_materia = input(f"Ingrese el nombre de la materia {i + 1}: ")
        materias.append(nombre_materia)
        
        # Solicitar la calificación para esta materia
        while True:
            try:
                calificacion = float(input(f"Ingrese la calificación para {nombre_materia} (0-10): "))
                if calificacion < 0 or calificacion > 10:
                    print("La calificación debe estar entre 0 y 10.")
                    continue
                calificaciones.append(calificacion)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    
    return materias, calificaciones

def determinar_estado(calificaciones):
    """
    Determina el estado (aprobado/reprobado) de cada materia.
    Recibe una lista de calificaciones y retorna una lista de estados.
    """
    estados = []
    for calificacion in calificaciones:
        if calificacion >= 5.0:  # Umbral de aprobación es 5.0
            estados.append("Aprobado")
        else:
            estados.append("Reprobado")
    return estados

def encontrar_extremos(calificaciones):
    """
    Encuentra los índices de la calificación más alta y más baja.
    Retorna una tupla (índice_máximo, índice_mínimo).
    """
    if not calificaciones:
        return None, None
    
    max_indice = 0
    min_indice = 0
    max_valor = calificaciones[0]
    min_valor = calificaciones[0]
    
    for i in range(len(calificaciones)):
        if calificaciones[i] > max_valor:
            max_valor = calificaciones[i]
            max_indice = i
        if calificaciones[i] < min_valor:
            min_valor = calificaciones[i]
            min_indice = i
    
    return max_indice, min_indice

def calcular_promedio(calificaciones):
    """
    Calcula el promedio de las calificaciones.
    """
    if not calificaciones:
        return 0
    return sum(calificaciones) / len(calificaciones)

def mostrar_resultados(materias, calificaciones, estados, mejor_i, peor_i, promedio):
    """
    Muestra los resultados detallados de las calificaciones.
    """
    print("\n=== RESULTADOS ===")
    
    # Mostrar resultados por materia
    print("\nCalificaciones por materia:")
    for i in range(len(materias)):
        materia = materias[i]
        calificacion = calificaciones[i]
        estado = estados[i]
        print(f"- {materia}: {calificacion:.2f} ({estado})")
    
    # Mostrar mejor y peor materia
    if mejor_i is not None and peor_i is not None:
        print(f"\nMejor materia: {materias[mejor_i]} con {calificaciones[mejor_i]:.2f}")
        print(f"Peor materia: {materias[peor_i]} con {calificaciones[peor_i]:.2f}")
    
    # Mostrar promedio general
    print(f"\nPromedio general: {promedio:.2f}")
    
    # Mostrar resultado general
    if promedio >= 5.0:
        print("¡Felicidades! Has aprobado con un promedio satisfactorio.")
    else:
        print("Lo sentimos, no has alcanzado el promedio mínimo para aprobar.")

def main():
    """
    Función principal para ejecutar la calculadora de promedios escolares.
    """
    print("Bienvenido a la calculadora de promedios escolares.")
    
    # Ingresar materias y calificaciones
    materias, calificaciones = ingresar_calificaciones()
    
    # Determinar estados (aprobado/reprobado)
    estados = determinar_estado(calificaciones)
    
    # Encontrar materias con mayor y menor calificación
    mejor_i, peor_i = encontrar_extremos(calificaciones)
    
    # Calcular promedio general
    promedio = calcular_promedio(calificaciones)
    
    # Mostrar resultados
    mostrar_resultados(materias, calificaciones, estados, mejor_i, peor_i, promedio)

if __name__ == "__main__":
    main()