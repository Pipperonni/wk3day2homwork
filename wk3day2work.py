
# Exercise #1
# Filter out all of the empty strings from the list below

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

print(list(filter(lambda place: place >= "," , places)))


# Exercise #2
# Write an anonymous function that sorts this list by the last name...
# Hint: Use the ".sort()" method and access the key"
# Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]

print(sorted(author, key = lambda x: x.split(), reverse=True))

# Exercise #3
# Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

# Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]

place, temp = map(list, zip(*places))

print(list(map(lambda temp, place: (place, (9/5)*float(temp) + float(32.0)), temp, place)))


# Exercise #4
# Write a recursion function to perform the fibonacci sequence up to the number passed in.

def factorial(number):
    if number <= 1: 
        return 1

    return (factorial(number-1) + factorial(number - 2))

print(factorial(5))

