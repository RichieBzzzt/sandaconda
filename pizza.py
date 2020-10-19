def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')

make_pizza('mushrooms', 'chicken', 'anchovies')
