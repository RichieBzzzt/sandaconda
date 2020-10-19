def get_pokemon_dict(pokemon_name, pokemon_type):
    """Returns information about a Pokemon"""
    pokemon = {'name': pokemon_name, 'type': pokemon_type}
    return pokemon


while True:
    print("\nPlease tell me your favourite Pokemon")
    print("(Press 'q' at any time to quit.)")

    pokemon = input("Pokemon name: ")
    if pokemon == 'q':
        break

    p_type = input("Pokemon type: ")
    if p_type == 'q':
        break

    pokemon_formatted = get_pokemon_dict(pokemon, p_type)
    print(pokemon_formatted)


def greet_pokemons(pokemons):
    """Print a simple greeting to each pokemon in a list"""
    for pokemon in pokemons:
        msg = f"Hello, {pokemon.title()}!"
        print(msg)


pkmns = ['sandaconda', 'serviper']
greet_pokemons(pkmns)
