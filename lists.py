# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list
numbers = [1,2,3,4,5,6,7]
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

# Use the constructor
# numbers2 = list((1,2,3,4,5,6,7))

# Get a value
print(fruits[0])

# Get the length
print(len(fruits))

# Append
fruits.append('Mangos')
print(fruits)

# Remove from list
fruits.remove('Grapes')
print(fruits)

# Insert into position
fruits.insert(2, 'Strawberries')
print(fruits)

# Remove from specific position
fruits.pop(2)
print(fruits)

# Reverse
fruits.reverse()
print(fruits)

# Sort list in alphabetic order
fruits.sort()
print(fruits)

# Sort list in reverse alphabetic order
fruits.sort(reverse=True)
print(fruits)

# Replace a value
fruits[0] = 'Bananas'
print(fruits)
