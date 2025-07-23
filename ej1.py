frase = input("Escribe una frase: ")

total_caracteres = len(frase)  # Cuenta todos los caracteres

espacios = frase.count(" ")  # Cuenta los espacios en blanco

print(f"La frase tiene {total_caracteres} caracteres en total.")
print(f"La frase tiene {espacios} espacios.")