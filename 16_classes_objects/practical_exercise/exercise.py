class Product:
    # TODO 1: crea un metodo __init__ que reciba name, price y stock.
    # Dentro de __init__, guarda esos valores en self.name, self.price y self.stock.
    # Luego usa la clase en los siguientes TODOs.
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    # TODO 2: crea un metodo de instancia llamado subtotal.
    # Debe recibir quantity y retornar self.price * quantity.
    # Luego usa este metodo en el TODO 10.
    def subtotal(self, quantity):
        return self.price * quantity

    # TODO 3: crea un metodo de instancia llamado is_available.
    # Debe retornar True si self.stock es mayor que 0, o False si no.
    # Luego usa este metodo en el TODO 11.
    def is_available(self):
        return self.stock > 0

    # TODO 4: crea un metodo de clase llamado from_tuple.
    # Debe recibir product_data y retornar cls(product_data[0], product_data[1], product_data[2]).
    # Luego usa este metodo en el TODO 12.
    @classmethod
    def from_tuple(cls, product_data):
        return cls(product_data[0], product_data[1], product_data[2])

    # TODO 5: crea un metodo estatico llamado apply_discount.
    # Debe recibir price y discount, y retornar price * (1 - discount).
    # Luego usa este metodo en el TODO 13.
    @staticmethod
    def apply_discount(price, discount):
        return price * (1 - discount)

    # TODO 6: crea un metodo __eq__.
    # Debe retornar True si other tambien es Product y tiene el mismo name.
    # Luego usa este metodo en el TODO 14.
    def __eq__(self, other):
        if isinstance(other, Product):
            return self.name == other.name
        return False


# TODO 7: crea un objeto product_a de la clase Product con "lapiz", 2.5 y 30.
# Luego revisa sus atributos en el siguiente TODO para ver el objeto creado.
product_a = Product("lapiz", 2.5, 30)

# TODO 8: obtiene el nombre, precio y stock de product_a.
# Luego revisa el valor de product_name, product_price y product_stock.
product_name = product_a.name
product_price = product_a.price
product_stock = product_a.stock

# TODO 9: cambia el stock de product_a a 25.
# Luego revisa el valor de product_a.stock para ver el atributo modificado.
product_a.stock = 25

# TODO 10: llama product_a.subtotal(4) y guarda el resultado en subtotal_value.
# Luego revisa el valor de subtotal_value.
subtotal_value = product_a.subtotal(4)

# TODO 11: llama product_a.is_available() y guarda el resultado en available.
# Luego revisa el valor de available.
available = product_a.is_available()

# TODO 12: crea product_b usando Product.from_tuple(("cuaderno", 8.0, 12)).
# Luego revisa el valor de product_b.name, product_b.price y product_b.stock.
product_b = Product.from_tuple(("cuaderno", 8.0, 12))

# TODO 13: llama Product.apply_discount(100, 0.1) y guarda el resultado en discounted_price.
# Luego revisa el valor de discounted_price.
discounted_price = Product.apply_discount(100, 0.1)

# TODO 14: crea product_c con "lapiz", 3.0 y 10.
# Luego compara product_a == product_c y guarda el resultado en same_product.
# Luego revisa los atributos de product_c y el valor de same_product.
product_c = Product("lapiz", 3.0, 10)
same_product = (product_a == product_c)

# TODO 15: crea una lista products con product_a, product_b y product_c.
# Luego usa products en los siguientes TODOs.
products = [product_a, product_b, product_c]

# TODO 16: crea una lista vacia product_summaries.
# Luego revisa el valor de product_summaries para ver que empieza vacia.
product_summaries = []

# TODO 17: recorre products.
# Dentro del for, crea product_summary con el formato "lapiz: 2.5 (25)".
# Agrega product_summary a product_summaries.
# Luego revisa el valor de product_summary en cada vuelta y product_summaries al final.
for product in products:
    product_summary = f"{product.name}: {product.price} ({product.stock})"
    product_summaries.append(product_summary)