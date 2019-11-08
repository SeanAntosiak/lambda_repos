from acme import Product
from acme import BoxingGlove
from acme_report import generate_products, inventory_report

prod = Product('A Cool Toy')

glove = BoxingGlove('a glove')

print(prod.name)

print(prod.price)

print(prod.weight)

print(prod.flammability)

print(prod.identifier)

print(prod.stealability())

print(prod.explode())

print(glove.price)

print(glove.weight)

print(glove.punch())

print(glove.explode())

print(inventory_report(generate_products()))
