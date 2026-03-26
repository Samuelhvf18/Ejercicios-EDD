import numpy as np

# 1. Array 5x5 de ceros
ventas = np.zeros((5,5), dtype=int)

ventas[0] = [120, 135, 110, 145, 130]
ventas[1] = [200, 215, 190, 225, 210]
ventas[2] = [ 80,  95,  70, 105,  90] 
ventas[3] = [150, 165, 140, 175, 160]
ventas[4] = [300, 315, 290, 325, 310]

total = np.sum(ventas, axis=0)

prom = np.mean(ventas, axis=1)

print("-" * 65)
print(f"{'':<12} | Día 1 | Día 2 | Día 3 | Día 4 | Día 5 | Promedio")
print("-" * 65)


for i in range(5):
   
    fila_str = " | ".join([f"{val:5}" for val in ventas[i]])
    print(f"Producto {i+1:<3} | {fila_str} | {prom[i]:8.1f}")

print("-" * 65)


total_str = " | ".join([f"{val:5}" for val in total])
print(f"{'Total / Día':<12} | {total_str} |")
print("-" * 65)