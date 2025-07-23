telefono = input("Escribe un número de teléfono de 10 dígitos: ")

if len(telefono) == 10 and telefono.isdigit():  # Verifica longitud y que sean solo dígitos
    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"  # Da formato al número
    print(f"El número formateado es: {telefono_formateado}")
else:
    print("El número debe tener exactamente 10 dígitos.")