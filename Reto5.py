class person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

person = [
    person("Juan", 33, 1000),
    person("Maria", 22, 1500),
    person("Pedro", 95, 800),
]

#Sacar el valor de las peresonas, y el incremento del salario de cada una de ellas un 10%

nomina = 0
for p in person:
    print(f"Nombre: {p.name}, Edad: {p.age}, Salario: {p.salary:.2f}")
    p.salary *= 1.1  # Incremento del salario en un 10%
    print(f"Nuevo Salario después del incremento: {p.salary:.2f}\n")
    nomina += p.salary
print(*"=" * 40)
print(f"Total de la nómina antes del incremento: {nomina / 1.1:.2f} ")
print(f"Total de la nómina después del incremento: {nomina:.2f}")
print(*"=" * 40)
