bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

message = f"My first bicycle was a {bicycles[0].title()}"
print(message)

guitars = ['fender','gibson','rickenbacker']
guitars[0]='yamaha'
print(guitars[0])



guitars = ['fender','gibson','rickenbacker']
print(guitars)
guitars.append('yamaha')
print(guitars)

guitars = []
guitars.append('fender')
guitars.append('gibson')
guitars.append('rickenbacker')
guitars.append('yamaha')
print(guitars)

del guitars[0]
print(guitars)

guitars = ['fender','rickenbacker','epiphone','gibson']
print(guitars)
last_owned_guitar = guitars.pop()
print(guitars)
print(last_owned_guitar) 

print(f"The last guitar I bought was a {last_owned_guitar.title()}")


first_owned_guitar = guitars.pop(2)
print(guitars)
print(first_owned_guitar) 

print(f"The first guitar I bought was a {first_owned_guitar.title()}")
print(guitars)
guitars.remove('fender')
print(guitars)


guitars = ['fender','rickenbacker','epiphone','gibson']
print(guitars)
too_expensive = 'gibson'
guitars.remove(too_expensive)
print(guitars)
print(f"A {too_expensive} is too expensive for me.")

guitars = ['fender','rickenbacker','epiphone','gibson']
print(guitars)
guitars.insert(1, 'squire')
print(guitars)

guitars.sort()
print(guitars)

guitars.sort(reverse=True)
print(guitars)

guitars = ['fender','rickenbacker','epiphone','gibson']
print("\n Here is the original list:")
print(guitars)

print("\n Here is the sorted list:")
print(sorted(guitars))

print("\n Here is the original list again")
print(guitars)

guitars.reverse()
print("\n Here is the sorted list in reverse:")
print(guitars)
print(len(guitars))

# drums = []
# drums[-1]
