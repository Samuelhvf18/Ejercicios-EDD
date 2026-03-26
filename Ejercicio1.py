import numpy as np

# 1. Creación de la matriz base
# Creamos un array de 5 filas y 5 columnas lleno de ceros (tipo entero)
# Esto reserva el espacio en memoria para nuestros datos de ventas
ventas = np.zeros((5,5), dtype=int)

# 2. Carga manual de datos
# Asignamos una lista de valores a cada fila (representando un producto diferente)
# Cada valor dentro de la lista representa la venta de un día (Día 1 al Día 5)
ventas[0] = [120, 135, 110, 145, 130] # Producto 1
ventas[1] = [200, 215, 190, 225, 210] # Producto 2
ventas[2] = [ 80,  95,  70, 105,  90] # Producto 3
ventas[3] = [150, 165, 140, 175, 160] # Producto 4
ventas[4] = [300, 315, 290, 325, 310] # Producto 5

# 3. Cálculos estadísticos con NumPy
# Sumamos las ventas por columnas (axis=0) para obtener el total vendido por cada día
total = np.sum(ventas, axis=0)

# Calculamos el promedio por filas (axis=1) para saber cuánto se vende de cada producto en promedio
prom = np.mean(ventas, axis=1)

# 4. Diseño de la interfaz de salida (Encabezado)
print("-" * 65)
# Usamos f-strings con alineación (:<12) para que la tabla se vea derecha
print(f"{'':<12} | Día 1 | Día 2 | Día 3 | Día 4 | Día 5 | Promedio")
print("-" * 65)

# 5. Bucle para imprimir cada fila de la tabla
for i in range(5):
    # Creamos una cadena de texto uniendo los valores de la fila con "|"
    # {val:5} asegura que cada número ocupe 5 espacios de ancho
    fila_str = " | ".join([f"{val:5}" for val in ventas[i]])
    
    # Imprimimos: Nombre del producto + ventas diarias + el promedio calculado anteriormente
    # {prom[i]:8.1f} muestra el promedio con 8 espacios de ancho y 1 decimal
    print(f"Producto {i+1:<3} | {fila_str} | {prom[i]:8.1f}")

print("-" * 65)

# 6. Fila de totales por día
# Generamos la cadena de texto para la fila final de sumas
total_str = " | ".join([f"{val:5}" for val in total])
print(f"{'Total / Día':<12} | {total_str} |")
print("-" * 65)
