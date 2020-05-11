for value in range(1, 5):
    print(value)

for value in range(6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)


squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))


squares = [value ** 2 for value in range (1,11)]
print(squares)

million_sum = [value for value in range(1,1000001)]
print(sum(million_sum))



odd_numbers = list(range(1,11,2))
for odd_number in odd_numbers:
    print(odd_number)

threes = list(range(3,31,3))
for three in threes:
    print(three)

cubes = [value ** 3 for value in range (1,11)]
for cube in cubes:
    print(cube)

cubes = [value ** 3 for value in range (1,11)]
for cube in cubes:
    print(cube)


cubes = []
for value in range(1,11):
    cubes.append(value ** 3)
for cube in cubes:
    print(cube)
