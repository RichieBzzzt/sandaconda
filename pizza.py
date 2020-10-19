def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')

make_pizza('mushrooms', 'chicken', 'anchovies')


def build_pizza(first_topping, second_topping, **toppings):
    toppings['first_topping'] = first_topping
    toppings['second_topping'] = second_topping
    return toppings


toppings = build_pizza('cheese', 'tomato sauce',
                       third_topping='olives',
                       fourth_topping='pepperoni')

print(toppings)