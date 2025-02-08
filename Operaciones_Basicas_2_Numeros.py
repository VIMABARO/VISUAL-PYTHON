# Programa para realizar operaciones matemáticas básicas en Python

# Diferentes formas de manejar valores numéricos en Python:
# 1. int -> Números enteros (ejemplo: 5, -3, 100)
# 2. float -> Números decimales (ejemplo: 5.5, -3.2, 100.0)
# 3. complex -> Números complejos (ejemplo: 3+5j, -2+7j)
# 4. Decimal -> Más precisión en cálculos decimales (requiere importar decimal)
# 5. Fraction -> Manejo de fracciones exactas (requiere importar fractions)

# Solicitar al usuario que ingrese dos números
num1 = float(input("Ingrese el primer número: "))  # Convertimos la entrada a float para admitir decimales
num2 = float(input("Ingrese el segundo número: "))

# Operaciones básicas
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

division = num1 / num2 if num2 != 0 else "No se puede dividir entre cero"

# Mostrar resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
