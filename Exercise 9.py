def days_since_birthday(birthday_str):
    """

    :param birthday_str: takes birthday as a string
    :return:
    """
    # Split the birthday string into day, month, and year
    day, month, year = birthday_str.split('-')

    # Convert the year to an integer
    birth_year = int(year)

    # Get the current year.
    # Since we're not allowed to import or use current date directly,
    # you need to manually enter the current year or find another way to get it.
    current_year = 2024  # Example, replace with the actual current year

    # Calculate the full years passed since the birth year
    full_years_passed = current_year - birth_year - 1

    # Calculate the days passed in full years
    days_passed = full_years_passed * 365

    return days_passed


# Example usage
print(days_since_birthday("01-01-1990"))
