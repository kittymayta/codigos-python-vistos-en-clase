# TODO 1: solicita la nota final y conviértela a float.
final_grade = float(input("Ingrese la nota final: "))

# TODO 2: solicita la asistencia y conviértela a float.
attendance = float(input("Ingrese la asistencia (%): "))

# TODO 3: solicita el código de modalidad.
modality_code = input("Ingrese el código de modalidad (P/V/H): ")

# TODO 4: crea una variable vacía para guardar el resultado.
result = ""

# TODO 5: usa if para comprobar si la nota es mayor o igual que 11
# y la asistencia es mayor o igual que 70.
if final_grade >= 11 and attendance >= 70:
    result = "Aprobado"
# TODO 6: usa elif para comprobar si la nota es mayor o igual que 11,
# pero la asistencia es menor que 70.
elif final_grade >= 11 and attendance < 70:
    result = "Desaprobado por Inasistencia"
# TODO 7: usa else para clasificar los demás casos como desaprobados.
else:
    result = "Desaprobado"

# TODO 8: crea una variable vacía para guardar el nombre de la modalidad.
modality_name = ""

# TODO 9: usa match con modality_code.upper().
# Para "P", guarda "Presencial".
# Para "V", guarda "Virtual".
# Para "H", guarda "Híbrida".
# Para cualquier otro código, guarda "Desconocida".
match modality_code.upper():
    case "P":
        modality_name = "Presencial"
    case "V":
        modality_name = "Virtual"
    case "H":
        modality_name = "Híbrida"
    case _:
        modality_name = "Desconocida"

# TODO 10: muestra el resultado.
print(f"Resultado: {result}")

# TODO 11: muestra el nombre de la modalidad.
print(f"Modalidad: {modality_name}")