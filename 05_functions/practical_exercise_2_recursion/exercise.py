# TODO 1: define la función recursiva countdown(number).
def countdown(number):
    # TODO 2: crea el caso base.
    # Si number es menor o igual que 0, muestra "Fin" y usa return.
    if number <= 0:
        print("Fin")
        return
    # TODO 3: crea el caso recursivo.
    # Muestra number y llama a countdown con number - 1.
    else:
        print(number)
        countdown(number - 1)

# TODO 4: define la función recursiva sum_to(number).
def sum_to(number):
    # TODO 5: crea el caso base.
    # Si number es menor o igual que 0, devuelve 0.
    if number <= 0:
        return 0
    # TODO 6: crea el caso recursivo.
    # Devuelve number más el resultado de sum_to(number - 1).
    else:
        return number + sum_to(number - 1)

# TODO 7: llama a countdown con 5.
countdown(5)

# TODO 8: llama a sum_to con 5 y guarda el resultado.
total = sum_to(5)

# TODO 9: muestra "Suma de 1 a 5:" y total.
print(f"Suma de 1 a 5: {total}")