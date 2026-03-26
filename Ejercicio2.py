import numpy as np

pares_1d = np.arange(0, 100, 2)

matriz_5x10 = pares_1d.reshape(5, 10)

print("=" * 55)
print(" 1. ARRAY ORIGINAL (Unidimensional de 50 elementos)")
print("=" * 55)
print(pares_1d)
print("\n")

print("=" * 55)
print(" 2. MATRIZ BIDIMENSIONAL RESULTANTE (5x10)")
print("=" * 55)

for fila in matriz_5x10:
    
    print("   " + "   ".join([f"{num:3}" for num in fila]))
print("=" * 55)