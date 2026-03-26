import numpy as np

codigos = np.arange(1001, 1021)

matriz_4x5 = codigos.reshape(4, 5)

print("=" * 50)
print(" 2. MATRIZ ORIGINAL (4x5) - Usando reshape()")
print("=" * 50)
for fila in matriz_4x5:
    print("   " + "   ".join([f"{num:4}" for num in fila]))
print("\n")

matriz_inventario = matriz_4x5.copy()
matriz_inventario.resize((5, 4))

print("=" * 50)
print(" 4. MATRIZ REDIMENSIONADA (5x4) - Usando resize() in-place")
print("=" * 50)
for fila in matriz_inventario:
    print("   " + "   ".join([f"{num:4}" for num in fila]))
print("=" * 50)

print("\nNota teórica: reshape() devuelve una vista del array original,")
print("mientras que resize() modifica el array in-place.")