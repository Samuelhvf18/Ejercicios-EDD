import numpy as np

np.random.seed(42) 

respuestas = np.random.randint(1, 6, 30)

matriz_6x5 = respuestas.reshape(6, 5)

print("=" * 55)
print(" 3. MATRIZ DE LA ENCUESTA (6 Personas x 5 Preguntas)")
print("=" * 55)
for fila in matriz_6x5:
    print("   " + "   ".join([f"{num:2}" for num in fila]))
print("\n")

matriz_5x6 = matriz_6x5.copy()
matriz_5x6.resize((5, 6))

print("=" * 55)
print(" 4. MATRIZ REDIMENSIONADA (5x6) - Usando resize()")
print("=" * 55)
for fila in matriz_5x6:
    print("   " + "   ".join([f"{num:2}" for num in fila]))
print("\n")

promedios = np.mean(matriz_6x5, axis=0)

print("=" * 55)
print(" 5. PROMEDIO DE RESPUESTAS POR PREGUNTA")
print("=" * 55)
for j, prom in enumerate(promedios):
    print(f"   Pregunta {j+1}: {prom:.2f}")
print("=" * 55)