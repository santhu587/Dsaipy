# Create a list
numbers = [1, 2, 3, 4, 5]

# Access elements
print(numbers[0])   # First element
print(numbers[-1])  # Last element

# Add items
numbers.append(6)

# Insert at position
numbers.insert(1, 10)

# Remove item
numbers.remove(3)

# Pop item (last by default)
numbers.pop()

# Change value
numbers[0] = 100

# Length of list
print(len(numbers))
