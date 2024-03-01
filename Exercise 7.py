import random

# Initial list of random numbers
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# New list to store modified values
modified_numbers = []

# Iterate through the original list
for number in random_numbers:
    # Check if the number is even
    if number % 2 == 0:
        # If even, append double its value to the new list
        modified_numbers.append(number * 2)
    # If the number is odd, do nothing (effectively removing it)

# Print the modified list
print(modified_numbers)