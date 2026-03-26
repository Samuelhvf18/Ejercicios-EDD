import numpy as np

# 1. Creación del tablero (Mundo del juego)
# Generamos una matriz de 8x8 llena de ceros.
# En este contexto, el 0 representa el "agua" o espacio vacío.
cuadricula = np.zeros((8, 8), dtype=int)

# 2. Posicionamiento de un objeto (El Barco)
# Usamos "Slicing" para colocar un barco de tamaño 3.
# [2, 3:6] significa: Fila índice 2, y Columnas desde el índice 3 hasta el 5 (el 6 no se incluye).
cuadricula[2, 3:6] = 1

# 3. Generación de secuencia de turnos
# Creamos un array que va del 1 al 10 para llevar el control de las jugadas.
turnos = np.arange(1, 11)

# 4. Visualización del tablero
print("=" * 50)
print(" 4. CUADRÍCULA DEL JUEGO (8x8) - 1=Barco, 0=Vacío")
print("=" * 50)

# Recorremos cada fila de la cuadrícula para imprimirla
for fila in cuadricula:
    # Imprimimos cada celda con un espacio de separación (f"{num:1}")
    # .join une los números de la fila con espacios para que se vea como una red.
    print("   " + "   ".join([f"{num:1}" for num in fila]))
print("\n")

# 5. Visualización de turnos
print("=" * 50)
print(" 5. SECUENCIA DE TURNOS (10 jugadas)")
print("=" * 50)
# Mostramos el array de turnos generado anteriormente
print("  ", turnos)
print("=" * 50)
