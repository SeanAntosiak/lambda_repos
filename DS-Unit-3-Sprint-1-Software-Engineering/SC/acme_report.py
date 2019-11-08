import random as rnd
from acme import Product


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num=30):
    '''
    Generates a list of products
    '''

    products = []

    for prod in range(num):

        adj = rnd.sample(ADJECTIVES, k=1)[0]
        noun = rnd.sample(NOUNS, k=1)[0]
        name = f'{adj} {noun}'
        price = rnd.randint(5, 100)
        weight = rnd.randint(5, 100)
        flammability = rnd.uniform(0.0, 2.5)

        prod = Product(name,
                       price=price,
                       weight=weight,
                       flammability=flammability
                       )

        products.append(prod)

    return(products)


def inventory_report(products):
    '''
    creates and returns an invintory report
    '''

    names = []
    weights = []
    prices = []
    flams = []

    for i in range(len(products)):
        names.append(products[i].name)
        weights.append(products[i].weight)
        prices.append(products[i].price)
        flams.append(products[i].flammability)

    uniqueNames = len(set(names))
    avgWeight = sum(weights)/len(weights)
    avgPrice = sum(prices)/len(prices)
    avgFlam = sum(flams)/len(prices)

    return(f''' There are {uniqueNames} Products. They have an average weight \
of {avgWeight}, an average price of {avgPrice},and an average flammability \
of {avgFlam}.'''
           )


if __name__ == '__main__':
    inventory_report(generate_products())
