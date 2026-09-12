"""Reto de Clase 04: Control de Flujo: Bucles (for / while)."""
# Escribe un programa que imprima la tabla de multiplicar de un número del 1 al 10.

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
print("=" * 60)
print(f"Tabla de multiplicar del {numero}:")
print("=" * 60)
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")      
    
