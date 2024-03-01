def is_valid_url(url):
    """
    Checks whether the url is valid or not.
    :param url: uses a string url as parameter
    :return:
    """
    # Check if the URL starts with http:// or https://
    if not (url.startswith('http://') or url.startswith('https://')):
        return False

    # Check if there is at least one dot in the URL (for the domain part)
    if '.' not in url:
        return False

    # Check for spaces or other illegal characters
    # This is a simplified check and might not cover all cases
    illegal_chars = set(" <>\"#%{}|\\^~[]`")
    if any(char in illegal_chars for char in url):
        return False

    # If all checks passed, the URL is considered valid
    return True

# Example Usage
print(is_valid_url("http://example.com"))  # Expected: True
print(is_valid_url("https://example.com"))  # Expected: True
print(is_valid_url("example.com"))  # Expected: False
print(is_valid_url("http://example com"))  # Expected: False
