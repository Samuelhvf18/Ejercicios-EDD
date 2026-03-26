import numpy as np

# 1. Generación de datos secuenciales
# np.arange(inicio, fin, paso) genera números desde 0 hasta 99 (el 100 es exclusivo)
# saltando de 2 en 2. Esto nos da exactamente 50 números pares.
pares_1d = np.arange(0, 100, 2)

# 2. Cambio de dimensión (Reshape)
# Convertimos el array de una sola fila (1D) en una estructura de 5 filas y 10 columnas (2D).
# Nota: Esto solo funciona porque 5 * 10 = 50 (el número total de elementos).
matriz_5x10 = pares_1d.reshape(5, 10)

# 3. Impresión del Array Original
print("=" * 55)
print(" 1. ARRAY ORIGINAL (Unidimensional de 50 elementos)")
print("=" * 55)
print(pares_1d) # Muestra los datos en una sola línea larga
print("\n")

# 4. Impresión de la Matriz Formateada
print("=" * 55)
print(" 2. MATRIZ BIDIMENSIONAL RESULTANTE (5x10)")
print("=" * 55)

# Iteramos sobre cada fila de la matriz para mostrarla de forma organizada
for fila in matriz_5x10:
    # f"{num:3}" reserva 3 espacios para cada número, manteniendo las columnas alineadas.
    # .join une esos números con espacios adicionales para que la tabla sea legible.
    print("    " + "    ".join([f"{num:3}" for num in fila]))

print("=" * 55)
