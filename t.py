def is_prime(number):
    """Return True if *number* is prime."""

    if number == 0:
        return False

    if number == 1:
        return False
    if number < 0:
        return False

    for element in range(2, number):
        if number % element == 0:
            return False
    return True
