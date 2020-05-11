pokemons = ['bulbasaur', 'charmander', 'squirtle', 'pidgey', 'rattata','ekans']
print(pokemons[0:3])
print(pokemons[1:4])
print(pokemons[:4])
print(pokemons[2:])
print(pokemons[-3:])

print("Here are the first three Pokémon on my team:")
for pokemon in pokemons[:3]:
    print(pokemon)

#variables pointing to different list
rivals_pokemons = pokemons[:]

print("My Pokémons:")
pokemons.append("Flareon")
for pokemon in pokemons:
    print(pokemon)

print("\nMy rivals Pokémons:")
rivals_pokemons.append("Jolteon")
for rivals_pokemon in rivals_pokemons:
    print(rivals_pokemon)

#variables pointing to same list
bob = ['bulbasaur', 'charmander', 'squirtle', 'pidgey', 'rattata','ekans']
my_bob = bob
my_bob.append("Weezing")
bob.append("Arbok")
print(bob)
print(my_bob)