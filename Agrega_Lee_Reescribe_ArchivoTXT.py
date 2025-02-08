# ✅ open() se usa para abrir archivos.
# ✅ "w" escribe un archivo (borra lo anterior).
# ✅ "r" lee un archivo.
# ✅ "a" añade sin borrar.
# ✅ with asegura que el archivo se cierre correctamente.

# Escribir en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("\nHola, este es un texto escrito que se borra cuando se vuelve a usar, usa *a* para agregar un nuevo dato sin borrar este.")

# Leer un archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)

# Ejemplo de añadir contenido en lugar de sobrescribir
# Si quieres agregar texto sin borrar el anterior, usa "a" (append):

#    with open("archivo.txt", "a") as archivo:
#   archivo.write("\nEste es un nuevo texto agregado.")