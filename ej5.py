''''
Sebastian Mora
22 julio 2025
'''
frase = input("Escribe una frase: ")

a = frase.count("a") + frase.count("A")  # Cuenta 'a' y 'A'
e = frase.count("e") + frase.count("E")  # Cuenta 'e' y 'E'
i = frase.count("i") + frase.count("I")  # Cuenta 'i' y 'I'
o = frase.count("o") + frase.count("O")  # Cuenta 'o' y 'O'
u = frase.count("u") + frase.count("U")  # Cuenta 'u' y 'U'

total_vocales = a + e + i + o + u  # Suma total de vocales

print(f"La frase tiene {total_vocales} vocales.")