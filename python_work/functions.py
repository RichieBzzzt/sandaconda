def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user("richie")


def describe_pokemon(pokemon_name, pokemon_type='poison'):
    """Describes information about a Pokemon"""
    print(f"I have a {pokemon_type} type.")
    print(f"My {pokemon_type} type Pokemon is a {pokemon_name.title()}.")


describe_pokemon('ekans')

describe_pokemon(pokemon_name='sandaconda', pokemon_type='ground')


describe_pokemon('serviper')
describe_pokemon(pokemon_name='serviper')

describe_pokemon(pokemon_type='psychic', pokemon_name='necrozma')
describe_pokemon(pokemon_name='necrozma', pokemon_type='psychic')
describe_pokemon('necrozma', 'psychic')


def get_pokemon_description(pokemon_name, pokemon_type='poison'):
    """Returns information about a Pokemon"""
    pokemon = (f"My {pokemon_type} \
                 type Pokemon is called {pokemon_name.title()}.")
    return pokemon


pkmn = get_pokemon_description(pokemon_type='water', pokemon_name='sobble')
print(pkmn)
pkmn = get_pokemon_description(pokemon_name='scorbunny', pokemon_type='fire')
print(pkmn)
pkmn = get_pokemon_description('banette', 'ghost')
print(pkmn)


def get_pokemon_description(pokemon_name, pokemon_primary_type,
                            pokemon_secondary_type=''):
    """Returns information about a Pokemon"""
    pokemon = (f"My {pokemon_primary_type} {pokemon_secondary_type} \
type Pokemon is called {pokemon_name.title()}.")
    return pokemon


pkmn = get_pokemon_description(pokemon_primary_type='ghost',
                               pokemon_secondary_type='fairy',
                               pokemon_name='mimikyu')
print(pkmn)
pkmn = get_pokemon_description(pokemon_name='scorbunny',
                               pokemon_primary_type='fire')
print(pkmn)
pkmn = get_pokemon_description('banette', 'ghost')
print(pkmn)


def get_pokemon_dict(pokemon_name, pokemon_type='poison', natdex_number=None):
    """Returns information about a Pokemon"""
    pokemon = {'name': pokemon_name, 'type': pokemon_type}
    if natdex_number:
        pokemon['natdex_number'] = natdex_number
    return pokemon


pkmn = get_pokemon_dict(pokemon_name='arbok', pokemon_type='poison')
print(pkmn)


pkmn = get_pokemon_dict(pokemon_name='zacian', pokemon_type='fairy',
                        natdex_number=888)
print(pkmn)


