nombre = input("Escribe tu nombre completo: ")

if nombre.replace(" ", "").isalpha():  # Verifica que solo haya letras (sin contar espacios)
    if nombre.istitle():  # Verifica que cada palabra comience con mayúscula
        print("El nombre es válido.")
    else:
        print("El nombre debe comenzar con mayúscula.")
else:
    print("El nombre solo debe contener letras.")