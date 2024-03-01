a = 6
a = a - 2
print(a*2)
a = a * 2
print(a+1)
a = a // 3
print(a)

print((2+3)*6/12 and 18.0)

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)


def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome("2704702208931031198668911301398022074072"))
print(palindrome("7798338247658278460338648728567428338977"))
print(palindrome("4257304920394478392772938744930294037524"))
print(palindrome("0974101607733149676776769413377061014790"))

# Initialize a counter for matches
pattern_count = 0

# Assuming 'text' is the text you want to process
punctuation = ".,!?;:\n-()"


# Assume 'text' is defined or read from somewhere else, for example, a file

# Function to clean and process the text
def pattern(filename):
    global pattern  # Use the global counter

    # Remove punctuation
    for p in punctuation:
        text = text.replace(p, "")

    # Split the text into words
    words = text.split()

    # Process each word
    for word in words:
        word = word.lower()  # Convert to lowercase to ensure consistent matching
        # Check if the word starts with 'un', ends with 'an', and has more than just 'un' and 'an'
        if word.startswith("un") and word.endswith("an"):
            pattern += 1


# Assuming you have a file named "book.txt" with your text
with open("text.txt") as file:
    for line in file:
        pattern(line)

# The result is the count of words matching the pattern
print(f"Number of words matching the pattern: {pattern_count}")



list = [1, 2, 3, 4]
list[0] = 10  # Changing the first element
print(list)  # Prints [10, 2, 3, 4], showing the list has been modified

list.append(5)  # Adding a new element
print(list)  # Prints [10, 2, 3, 4, 5], showing the list has been modified

del list[2]  # Deleting the third element
print(list)  # Prints [10, 2, 4, 5], showing the list has been modified


def url():
    """
    Checks whether the url is valid or not
    :return:
    """

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
