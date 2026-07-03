# TODO 1: crea total con el valor inicial 0.0.
total = 0.0

# TODO 2: crea valid_count con el valor inicial 0.
valid_count = 0

# TODO 3: crea attempt_count con el valor inicial 0.
attempt_count = 0

# TODO 4: crea un while True.
while True:
    # TODO 5: dentro del while, solicita un número o la palabra "salir".
    entry = input("Ingrese un número o la palabra 'salir': ")

    # TODO 6: si la entrada en minúsculas es "salir", termina con break.
    if entry.lower() == "salir":
        break

    # TODO 7: aumenta attempt_count en 1 usando +=.
    attempt_count += 1

    # TODO 8: crea un bloque try que convierta la entrada a float,
    # sume el número a total y aumente valid_count.
    try:
        number = float(entry)
        total += number
        valid_count += 1
    # TODO 9: agrega except ValueError y muestra "Entrada inválida.".
    except ValueError:
        print("Entrada inválida.")
    # TODO 10: agrega finally y muestra "Intento procesado.".
    finally:
        print("Intento procesado.")

# TODO 11: después del while, intenta calcular total / valid_count.
try:
    average = total / valid_count
# TODO 12: captura ZeroDivisionError y muestra "No se ingresaron números válidos.".
except ZeroDivisionError:
    print("No se ingresaron números válidos.")
# TODO 13: usa else para mostrar el promedio.
else:
    print(f"El promedio es: {average}")
# TODO 14: usa finally para mostrar "Proceso de promedio terminado.".
finally:
    print("Proceso de promedio terminado.")

# TODO 15: muestra total, valid_count y attempt_count.
print(f"Total: {total}, Válidos: {valid_count}, Intentos: {attempt_count}")