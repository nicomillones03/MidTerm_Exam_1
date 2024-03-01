def find_un_an_words(text):
    """
    Counts the occurrences of words that start with 'un', have an unlimited number of letters, and end with 'an'.

    :param text: The text to search within.
    :return: The number of words matching the 'un...an' pattern.
    """
    # Initialize a counter for matches
    match_count = 0

    # Normalize the text to lowercase to make the search case-insensitive
    text = text.lower()

    # Split the text into words
    words = text.split()

    # Iterate through each word in the list
    for word in words:
        # Check if the word starts with 'un' and ends with 'an'
        if word.startswith("un") and word.endswith("an"):
            match_count += 1

    return match_count


# Example usage
sample_text = "Understanding the unknown is an unattainable dream for many, but not for an undaunted few. unffssan"
print(find_un_an_words(sample_text))
