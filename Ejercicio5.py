import numpy as np

# 1. Control de aleatoriedad
# La "semilla" (seed) asegura que los números "aleatorios" sean los mismos 
# cada vez que corras el código. Esto es vital para depurar errores.
np.random.seed(42) 

# 2. Generación de datos de la encuesta
# Creamos 30 respuestas aleatorias entre 1 y 5 (el 6 no se incluye).
# Esto simula una escala de satisfacción (ej. 1: Muy malo, 5: Excelente).
respuestas = np.random.randint(1, 6, 30)

# 3. Organización de los datos (Reshape)
# Convertimos los 30 datos en una matriz donde:
# Filas (6) = Personas encuestadas | Columnas (5) = Preguntas realizadas
matriz_6x5 = respuestas.reshape(6, 5)

print("=" * 55)
print(" 3. MATRIZ DE LA ENCUESTA (6 Personas x 5 Preguntas)")
print("=" * 55)
for fila in matriz_6x5:
    # Imprimimos los resultados de cada persona
    print("   " + "   ".join([f"{num:2}" for num in fila]))
print("\n")

# 4. Redimensionamiento (Resize)
# Creamos una copia para reorganizar los datos en una nueva estructura de 5x6
matriz_5x6 = matriz_6x5.copy()
matriz_5x6.resize((5, 6))

print("=" * 55)
print(" 4. MATRIZ REDIMENSIONADA (5x6) - Usando resize()")
print("=" * 55)
for fila in matriz_5x6:
    print("   " + "   ".join([f"{num:2}" for num in fila]))
print("\n")

# 5. Análisis Estadístico (Promedio por pregunta)
# Calculamos el promedio de cada COLUMNA (axis=0).
# Esto nos dice cuál es la calificación media de cada una de las 5 preguntas.
promedios = np.mean(matriz_6x5, axis=0)

print("=" * 55)
print(" 5. PROMEDIO DE RESPUESTAS POR PREGUNTA")
print("=" * 55)

# 6. Impresión con enumeración
# enumerate() nos da el índice (j) y el valor (prom) al mismo tiempo
for j, prom in enumerate(promedios):
    # j+1 es para que el usuario vea "Pregunta 1" en vez de "Pregunta 0"
    print(f"   Pregunta {j+1}: {prom:.2f}")
print("=" * 55)
