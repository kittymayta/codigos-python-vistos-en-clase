# TODO 1: crea el precio 12.5.
price = 12.5

# TODO 2: crea la cantidad 8.
quantity = 8

# TODO 3: crea el dinero disponible 120.
available_money = 120

# TODO 4: calcula el subtotal con el operador de multiplicación.
subtotal = price * quantity

# TODO 5: calcula el vuelto con el operador de resta.
change = available_money - subtotal

# TODO 6: calcula cuántas cajas completas de 3 unidades se pueden formar.
complete_boxes = quantity // 3

# TODO 7: calcula cuántas unidades sobran.
remaining_units = quantity % 3

# TODO 8: calcula 2 elevado a 3.
power = 2 ** 3

# TODO 9: comprueba si available_money es mayor o igual que subtotal.
has_enough_money = available_money >= subtotal

# TODO 10: comprueba si quantity es mayor que 5.
is_large_purchase = quantity > 5

# TODO 11: comprueba si available_money es igual a subtotal.
is_exact_payment = available_money == subtotal

# TODO 12: usa and para comprobar que hay dinero suficiente y quantity es mayor que 0.
is_approved = has_enough_money and (quantity > 0)

# TODO 13: usa not y or para comprobar si la compra no está aprobada o subtotal es mayor o igual que 500.
requires_review = not is_approved or subtotal >= 500

# TODO 14: crea el stock inicial con el valor 20.
stock = 20

# TODO 15: resta quantity de stock usando -=.
stock -= quantity

# TODO 16: agrega 2 unidades a stock usando +=.
stock += 2

# TODO 17: muestra el subtotal.
print(f"Subtotal: {subtotal}")

# TODO 18: muestra el vuelto.
print(f"Vuelto: {change}")

# TODO 19: muestra las cajas completas.
print(f"Cajas completas: {complete_boxes}")

# TODO 20: muestra las unidades sobrantes.
print(f"Unidades sobrantes: {remaining_units}")

# TODO 21: muestra la potencia.
print(f"Potencia: {power}")

# TODO 22: muestra has_enough_money.
print(f"Tiene suficiente dinero: {has_enough_money}")

# TODO 23: muestra is_large_purchase.
print(f"Es compra grande: {is_large_purchase}")

# TODO 24: muestra is_exact_payment.
print(f"Es pago exacto: {is_exact_payment}")

# TODO 25: muestra is_approved.
print(f"Compra aprobada: {is_approved}")

# TODO 26: muestra requires_review.
print(f"Requiere revisión: {requires_review}")

# TODO 27: muestra el stock final.
print(f"Stock final: {stock}")