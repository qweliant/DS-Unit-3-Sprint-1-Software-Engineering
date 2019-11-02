from random import randint, sample, uniform
from acme import Product


# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


"""
should return a list of product objects
"""


def generate_products(num_products=30):
    products = []
    for x in range(num_products):
        name = ' '.join(sample(ADJECTIVES, 1) + sample(NOUNS, 1))
        p1 = Product(name)
        p1.weight = randint(5, 101)
        p1.price = randint(5, 101)
        p1.flammability = uniform(0.0, 260)
        products.append(p1)
    return products


"""
returns count of unique elements
"""


def unique(elements):
    count = 0
    unique_list = []
    for i in elements:
        if i not in unique_list:
            unique_list.append(i)
            count + = 1
    # print (unique_list)
    return(count)


"""
returns average of elements in list
"""


def average(elements):
    return sum(elements)/len(elements)


"""
Prints a report of average values and unique items from the product factory
"""


def inventory_report(products):
    unique_names = []
    price = []
    weight = []
    flammability = []

    for obj in products:
        unique_names.append(obj.name)
        price.append(obj.price)
        weight.append(obj.weight)
        flammability.append(obj.flammability)

    unique_name_count = unique(unique_names)
    avg_price = average(price)
    avg_weight = average(weight)
    avg_flammability = average(flammability)

    print('\n')
    print(f'ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {unique_name_count}')
    print(f'Average price: {avg_price:.2f}')
    print(f'Average weight: {avg_weight:.2f}')
    print(f'Average flammability: {avg_flammability:.2f}')

    pass  # TODO - your code! Loop over the products to calculate the report.


if __name__ == '__main__':
    inventory_report(generate_products())
