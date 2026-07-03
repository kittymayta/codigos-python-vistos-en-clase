# TODO 1: define calculate_subtotal con los parámetros price y quantity.
# Debe devolver price multiplicado por quantity.
def calculate_subtotal(price, quantity):
    return price * quantity

# TODO 2: define calculate_tax con los parámetros subtotal y tax_rate.
# tax_rate debe tener 0.18 como valor por defecto.
# Debe devolver subtotal multiplicado por tax_rate.
def calculate_tax(subtotal, tax_rate=0.18):
    return subtotal * tax_rate

# TODO 3: define calculate_total con los parámetros subtotal y tax.
# Debe devolver la suma de subtotal y tax.
def calculate_total(subtotal, tax):
    return subtotal + tax

# TODO 4: define show_receipt con product, subtotal, tax y total.
# Debe mostrar los cuatro valores.
def show_receipt(product, subtotal, tax, total):
    print(f"Producto: {product}")
    print(f"Subtotal: {subtotal}")
    print(f"Impuesto: {tax}")
    print(f"Total: {total}")

# TODO 5: crea el producto "Cuaderno".
product = "Cuaderno"

# TODO 6: llama a calculate_subtotal con 7.5 y 4.
subtotal = calculate_subtotal(7.5, 4)

# TODO 7: llama a calculate_tax usando su porcentaje por defecto.
tax = calculate_tax(subtotal)

# TODO 8: llama a calculate_total.
total = calculate_total(subtotal, tax)

# TODO 9: llama a show_receipt.
show_receipt(product, subtotal, tax, total)

# TODO 10: llama a calculate_tax con subtotal y 0.10.
custom_tax = calculate_tax(subtotal, 0.10)

# TODO 11: muestra el impuesto personalizado.
print(f"Impuesto personalizado: {custom_tax}")