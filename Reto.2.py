"""Reto de Clase 01: Primer Vistazo Práctico (print, variables, if, for)."""
# Crea un script que defina una lista de 3 alumnos con sus notas, use un for para recorrerlos y un if/else para imprimir si cada uno aprobó (nota >= 60) o reprobó.

print("Alumnos del Colegio Normal Superior")

Alumno_1 = "Robinson"
Nota_1 = 100

Alumno_2 = "Rosa"
Nota_2 = 40

Alumno_3 = "juanito"
Nota_3 = 60




if Nota_1 >= 60:
    print(f"Estudiante: {Alumno_1} | Nota: {Nota_1} | Aprobado")
else:
    print(f"Estudiante: {Alumno_1} | Nota: {Nota_1} | Reprobado")

if Nota_2 >= 60:
    print(f"Estudiante: {Alumno_2} | Nota: {Nota_2} | Aprobado")
else:
    print(f"Estudiante: {Alumno_2} | Nota: {Nota_2} | Reprobado")

if Nota_3 >= 60:
    print(f"Estudiante: {Alumno_3} | Nota: {Nota_3} | Aprobado")
else:
    print(f"Estudiante: {Alumno_3} | Nota: {Nota_3} | Reprobado")
