# Sebastián Andrés Mora Valenzuela

22 marzo 2025

## ❇**Taller Guiado: Trabajando con Cadenas de Caracteres en Python**

Este taller está diseñado para practicar el uso de cadenas de caracteres en Python. Cada ejercicio tiene instrucciones claras y una explicación de cómo resolverlo.

------

### **Objetivo del taller**

- Aprender a manipular, validar y formatear cadenas de caracteres.
- Usar los métodos básicos de las cadenas para resolver problemas prácticos.

------

### **Ejercicio 1: Contando caracteres**

#### **Instrucción:**

Escribe un programa que solicite al usuario una frase y muestre:

1. La cantidad total de caracteres en la frase.
2. La cantidad de espacios en la frase.

#### **Código base:**

```python
frase = input("Escribe una frase: ")
total_caracteres = len(frase)
espacios = frase.count(" ")

print(f"La frase tiene {total_caracteres} caracteres en total.")
print(f"La frase tiene {espacios} espacios.")
```

####  Explicación:

Este programa pide una frase y cuenta cuántos caracteres tiene en total (incluyendo espacios y signos), y cuántos espacios hay usando `.count(" ")`. Sirve para practicar cómo contar cosas dentro de un texto.

------

### **Ejercicio 2: Validando nombres**

#### **Instrucción:**

Crea un programa que solicite al usuario su nombre completo y verifique:

1. Que solo contenga letras.
2. Que comience con mayúscula.

#### **Código base:**

```python
nombre = input("Escribe tu nombre completo: ")

if nombre.replace(" ", "").isalpha():
    if nombre.istitle():
        print("El nombre es válido.")
    else:
        print("El nombre debe comenzar con mayúscula.")
else:
    print("El nombre solo debe contener letras.")
```

####  Explicación:

Se verifica que el nombre solo tenga letras (sin números ni símbolos) y que cada palabra empiece con mayúscula. Es como una validación para asegurarse de que el nombre esté bien escrito.

------

### **Ejercicio 3: Invirtiendo palabras**

#### **Instrucción:**

Escribe un programa que pida al usuario una palabra y muestre la palabra invertida.

#### **Código base:**

```python
palabra = input("Escribe una palabra: ")
invertida = palabra[::-1]
print(f"La palabra invertida es: {invertida}")
```

####  Explicación:

Usa `[::-1]` para invertir la palabra, como si la leyéramos al revés. Es una forma rápida de invertir cualquier texto.

------

### **Ejercicio 4: Cifrando texto**

#### **Instrucción:**

Crea un programa que solicite al usuario una frase y reemplace todas las vocales por un carácter especial (*).

#### **Código base:**

```python
frase = input("Escribe una frase: ")

frase_cifrada = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")
frase_cifrada = frase_cifrada.replace("A", "*").replace("E", "*").replace("I", "*").replace("O", "*").replace("U", "*")

print(f"La frase cifrada es: {frase_cifrada}")
```

####  Explicación:

Se reemplazan todas las vocales (mayúsculas y minúsculas) por `*` usando `replace()` varias veces.

------

### **Ejercicio 5: Contador de vocales**

#### **Instrucción:**

Escribe un programa que cuente cuántas vocales hay en una frase ingresada por el usuario.

#### **Código base:**

```python
frase = input("Escribe una frase: ")

a = frase.count("a") + frase.count("A")
e = frase.count("e") + frase.count("E")
i = frase.count("i") + frase.count("I")
o = frase.count("o") + frase.count("O")
u = frase.count("u") + frase.count("U")

total_vocales = a + e + i + o + u

print(f"La frase tiene {total_vocales} vocales.")
```

####  Explicación:

Cuenta cuántas veces aparece cada vocal, tanto en minúscula como en mayúscula, y luego suma todo para dar el total. 

------

### **Ejercicio 6: Formateando cadenas**

#### **Instrucción:**

Escribe un programa que tome un número de teléfono ingresado por el usuario (10 dígitos) y lo formatee como `(XXX) XXX-XXXX`.

#### **Código base:**

```python
telefono = input("Escribe un número de teléfono de 10 dígitos: ")
if len(telefono) == 10 and telefono.isdigit():
    telefono_formateado = f"({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}"
    print(f"El número formateado es: {telefono_formateado}")
else:
    print("El número debe tener exactamente 10 dígitos.")
```

####  Explicación:

Verifica que el número tenga 10 dígitos y que sean solo números. Luego se separa en partes y lo muestra bonito con paréntesis y guión.

------

### **Ejercicio 7: Detectando palíndromos**

#### **Instrucción:**

Escribe un programa que determine si una palabra ingresada por el usuario es un palíndromo (se lee igual al derecho y al revés).

#### **Código base:**

```python
palabra = input("Escribe una palabra: ").lower()
invertida = palabra[::-1]

if palabra == invertida:
    print("La palabra es un palíndromo.")
else:
    print("La palabra no es un palíndromo.")
```

####  Explicación:

Convierte la palabra a minúsculas para que no importe si está en mayúsculas. Luego la invierte y la compara con la original. Si son iguales, es un palíndromo