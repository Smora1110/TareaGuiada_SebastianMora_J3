''''
Sebastian Mora
22 julio 2025
'''
palabra = input("Escribe una palabra: ").lower()  # Convierte a minúsculas para comparar bien
invertida = palabra[::-1]  # Invierte la palabra

if palabra == invertida:  # Compara original e invertida
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")