#  Append Method
numbers = [10, 20, 30, 40]

numbers.append(50)

print(numbers)

#  Extend Method

numbers.extend([50,60])

# Insert Method
numbers.insert(1, 11)

print(numbers)

# Remove Method
numbers.remove(20)

print(numbers)

# POP Method 
numbers.pop()

print(numbers)

# You can also specify an index
numbers.pop(1)

# Clear Method

numbers.clear()

# Index Method
# Returns the index of an item
numbers = [10,20,30,40,50]

print(numbers.index(20))


# Count Method

numbers = [10,20,30,40,30,60,50,30]

print(numbers.count(30))


# Sort Method

numbers = [50,40,30,10,20,70,60]


numbers.sort()

print(numbers)


numbers.sort(reverse=True)

print(numbers)

# Reverse Method

numbers = [10,20,30,40,50]

numbers.reverse()

print(numbers)


# Copy Method

numbers = [10,20,30,40,50]

new_number = numbers.copy()

print(new_number)