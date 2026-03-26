import numpy as np

# 1. Generación de códigos secuenciales
# Creamos una lista de 20 números que representan "códigos de producto"
# Van desde 1001 hasta 1020 (el 1021 es el límite exclusivo)
codigos = np.arange(1001, 1021)

# 2. Uso de reshape()
# Cambiamos la forma de los 20 elementos a una matriz de 4 filas x 5 columnas
# Importante: reshape() NO cambia el array original, crea una "vista" nueva
matriz_4x5 = codigos.reshape(4, 5)

print("=" * 50)
print(" 2. MATRIZ ORIGINAL (4x5) - Usando reshape()")
print("=" * 50)
for fila in matriz_4x5:
    # Formateamos la salida para que cada código ocupe 4 espacios
    print("   " + "   ".join([f"{num:4}" for num in fila]))
print("\n")

# 3. Copia y Redimensionamiento
# Hacemos una copia profunda para no afectar a la matriz anterior
matriz_inventario = matriz_4x5.copy()

# 4. Uso de resize()
# A diferencia de reshape, resize() modifica la estructura del array directamente
# Aquí reorganizamos los mismos 20 elementos en 5 filas x 4 columnas
matriz_inventario.resize((5, 4))

print("=" * 50)
print(" 4. MATRIZ REDIMENSIONADA (5x4) - Usando resize() in-place")
print("=" * 50)
for fila in matriz_inventario:
    print("   " + "   ".join([f"{num:4}" for num in fila]))
print("=" * 50)

# Explicación de la diferencia fundamental:
print("\nNota teórica: reshape() devuelve una vista del array original,")
print("mientras que resize() modifica el array in-place.")
