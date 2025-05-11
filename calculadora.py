'''
Desarrollo de una calculadora de promedios escolares en Python 
utilizando variables, operadores, estructuras de control y funciones básicas.

Escuela de postgrado Newman
Autor: Daniel Chavez
Maestria en Big Data
'''
def ingreso_estudiantes():
    # Solicitar al usuario el número de estudiantes
    while True:
        try:
            num_estudiantes = int(input("Ingrese el número de estudiantes: "))
            if num_estudiantes <= 0:
                print("El número de estudiantes debe ser mayor que cero.")
                continue
            return num_estudiantes
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def ingreso_materias():
    # Solicitar al usuario el número de materias
    while True:
        try:
            num_materias = int(input("Ingrese el número de materias: "))
            if num_materias <= 0:
                print("El número de materias debe ser mayor que cero.")
                continue
            
            # Solicitar los nombres de cada materia
            nombres_materias = []
            num_evaluaciones = []
            for i in range(num_materias):
                nombre_materia = input(f"Ingrese el nombre de la materia {i + 1}: ")
                nombres_materias.append(nombre_materia)
                
                # Solicitar el número de evaluaciones para esta materia
                while True:
                    try:
                        n_eval = int(input(f"¿Cuántas evaluaciones tuvo en {nombre_materia}? "))
                        if n_eval <= 0:
                            print("El número de evaluaciones debe ser mayor que cero.")
                            continue
                        num_evaluaciones.append(n_eval)
                        break
                    except ValueError:
                        print("Por favor, ingrese un número entero válido.")
                
            return num_materias, nombres_materias, num_evaluaciones
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

def ingreso_notas(num_materias, nombres_materias, num_evaluaciones, nombre_estudiante):
    # Solicitar al usuario las notas de cada materia para un estudiante
    notas_por_materia = []
    for i in range(num_materias):
        materia = nombres_materias[i]
        evaluaciones = num_evaluaciones[i]
        notas_materia = []
        
        print(f"\nIngresando notas de {materia} para {nombre_estudiante}:")
        for j in range(evaluaciones):
            while True:
                try:
                    nota = float(input(f"Ingrese la nota {j+1} de {evaluaciones}: "))
                    if nota < 0 or nota > 10:
                        print("La nota debe estar entre 0 y 10.")
                        continue
                    notas_materia.append(nota)
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")
        
        # Calcular promedio de la materia
        promedio_materia = sum(notas_materia) / len(notas_materia)
        notas_por_materia.append(promedio_materia)
        
    return notas_por_materia

def calcular_promedio(notas):
    # Calcular el promedio de las notas
    suma = sum(notas)
    promedio = suma / len(notas)
    return promedio

def mostrar_resultado_individual(nombre_estudiante, nombres_materias, notas):
    # Mostrar resultados individuales por materia
    print(f"\nCalificaciones de {nombre_estudiante}:")
    for i in range(len(nombres_materias)):
        materia = nombres_materias[i]
        nota = notas[i]
        estado = "Aprobado" if nota >= 7 else "Reprobado"
        print(f"- {materia}: {nota:.2f} ({estado})")

def mostrar_resultado_general(nombre_estudiante, promedio):
    # Mostrar el resultado general al usuario
    if promedio >= 7:
        print(f"Promedio general de {nombre_estudiante}: {promedio:.2f}. ¡Felicidades, has aprobado!")
    else:
        print(f"Promedio general de {nombre_estudiante}: {promedio:.2f}. Lo siento, has reprobado.")

def main():
    # Función principal para ejecutar la calculadora
    print("Bienvenido a la calculadora de promedios escolares.")
    
    num_estudiantes = ingreso_estudiantes()
    num_materias, nombres_materias, num_evaluaciones = ingreso_materias()
    
    # Procesar cada estudiante
    for i in range(num_estudiantes):
        nombre_estudiante = input(f"\nIngrese el nombre del estudiante {i + 1}: ")
        notas = ingreso_notas(num_materias, nombres_materias, num_evaluaciones, nombre_estudiante)
        promedio = calcular_promedio(notas)
        
        # Mostrar resultados del estudiante
        mostrar_resultado_individual(nombre_estudiante, nombres_materias, notas)
        mostrar_resultado_general(nombre_estudiante, promedio)
    
if __name__ == "__main__":
    main()