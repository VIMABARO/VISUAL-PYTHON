edad = int(input("Ingresa tu edad: "))

if edad >= 120:
    print("Has superado la edad promedio, felicidades :)")
elif edad >= 18:
    print("Eres mayor de edad.")
elif edad <= 0 or edad == -0:
    print("Edad no válida.")
else:
    print("Eres menor de edad.")