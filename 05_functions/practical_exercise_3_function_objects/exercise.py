# TODO 1: define add(a, b) y devuelve la suma.
def add(a, b):
    return a + b

# TODO 2: define multiply(a, b) y devuelve la multiplicación.
def multiply(a, b):
    return a * b

# TODO 3: define apply_operation(a, b, operation).
# Debe devolver el resultado de llamar a operation con a y b.
def apply_operation(a, b, operation):
    return operation(a, b)

# TODO 4: define create_multiplier(multiplier).
def create_multiplier(multiplier):
    # TODO 5: dentro de create_multiplier, define multiply_value(value).
    # Debe devolver value multiplicado por multiplier.
    def multiply_value(value):
        return value * multiplier
    # TODO 6: retorna multiply_value desde create_multiplier.
    return multiply_value

# TODO 7: define la función pura calculate_discount(price, discount).
# Debe devolver price menos price multiplicado por discount.
def calculate_discount(price, discount):
    return price - (price * discount)

# TODO 8: define la función impura add_to_log(message, log).
# Debe agregar message a log usando append().
def add_to_log(message, log):
    log.append(message)

# TODO 9: usa apply_operation para sumar 3 y 4.
sum_result = apply_operation(3, 4, add)

# TODO 10: usa apply_operation para multiplicar 3 y 4.
multiplication_result = apply_operation(3, 4, multiply)

# TODO 11: usa create_multiplier para crear double.
double = create_multiplier(2)

# TODO 12: llama a double con 5.
double_result = double(5)

# TODO 13: llama a calculate_discount con 100 y 0.10.
discounted_price = calculate_discount(100, 0.10)

# TODO 14: crea una lista vacía llamada operation_log.
operation_log = []

# TODO 15: llama a add_to_log con "Operación completada" y operation_log.
add_to_log("Operación completada", operation_log)

# TODO 16: asigna a add el atributo description con "Suma dos números".
add.description = "Suma dos números"

# TODO 17: muestra todos los resultados y el atributo.
print(f"Suma: {sum_result}")
print(f"Multiplicación: {multiplication_result}")
print(f"Doble de 5: {double_result}")
print(f"Precio con descuento: {discounted_price}")
print(f"Log de operaciones: {operation_log}")
print(f"Descripción de la función add: {add.description}")