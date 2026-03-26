import numpy as np

cuadricula = np.zeros((8, 8), dtype=int)

cuadricula[2, 3:6] = 1

turnos = np.arange(1, 11)

print("=" * 50)
print(" 4. CUADRÍCULA DEL JUEGO (8x8) - 1=Barco, 0=Vacío")
print("=" * 50)
for fila in cuadricula:
    # Imprimimos cada fila alineando los números
    print("   " + "   ".join([f"{num:1}" for num in fila]))
print("\n")

print("=" * 50)
print(" 5. SECUENCIA DE TURNOS (10 jugadas)")
print("=" * 50)
print("  ", turnos)
print("=" * 50)