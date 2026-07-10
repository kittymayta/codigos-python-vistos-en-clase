# TODO 1: crea una lista de numeros del 1 al 10.
# Luego revisa el valor de numbers para ver la lista inicial.
numbers = list(range(1, 11))

# TODO 2: crea una lista con los cuadrados de numbers usando list comprehension.
# Luego revisa el valor de squares para ver los cuadrados.
squares = [numero ** 2 for numero in numbers]

# TODO 3: crea una lista solo con los numeros pares.
# Luego revisa el valor de evens para ver los numeros pares.
evens = [numero for numero in numbers if numero % 2 == 0]

# TODO 4: crea una lista solo con los numeros mayores que 5.
# Luego revisa el valor de greater_than_five para ver los numeros filtrados.
greater_than_five = [numero for numero in numbers if numero > 5]

# TODO 5: crea una lista de etiquetas "Par" o "Impar".
# Luego revisa el valor de labels para ver las etiquetas creadas.
labels = ["Par" if numero % 2 == 0 else "Impar" for numero in numbers]

# TODO 6: crea una lista donde los pares se dupliquen y los impares se conviertan en 0.
# Luego revisa el valor de modified_numbers para ver los numeros modificados.
modified_numbers = [numero * 2 if numero % 2 == 0 else 0 for numero in numbers]

# TODO 7: crea una lista de nombres.
# Luego revisa el valor de names para ver la lista de nombres.
names = ["Ana", "Luis", "Marcela", "Jose"]

# TODO 8: crea una lista con los nombres en mayusculas.
# Luego revisa el valor de uppercase_names para ver los nombres transformados.
uppercase_names = [nombre.upper() for nombre in names]

# TODO 9: crea una lista solo con los nombres que tengan mas de 4 caracteres.
# Luego revisa el valor de long_names para ver los nombres filtrados.
long_names = [nombre for nombre in names if len(nombre) > 4]

# TODO 10: crea una lista de numeros pequeños y una lista de letras.
# Luego revisa el valor de small_numbers y letters para ver las listas base.
small_numbers = [1, 2, 3]
letters = ["a", "b"]

# TODO 11: crea pares (numero, letra) combinando small_numbers y letters con varios for.
# Luego revisa el valor de number_letter_pairs para ver las combinaciones.
number_letter_pairs = [(numero, letra) for numero in small_numbers for letra in letters]

# TODO 12: crea una lista de numeros y una lista de vocales.
# Luego revisa el valor de more_numbers y vowels para ver las listas base.
more_numbers = [1, 2, 3, 4]
vowels = ["a", "e", "i"]

# TODO 13: crea pares solo con numeros pares y vocales "a" y "e".
# Luego revisa el valor de filtered_pairs para ver las combinaciones filtradas.
filtered_pairs = [(numero, vocal) for numero in more_numbers if numero % 2 == 0 for vocal in vowels if vocal in ("a", "e")]
