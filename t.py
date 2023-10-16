def is_prime(number):
    """Return True if *number* is prime."""

    if number == 0:
        return False

    if number == 1:
        return False
    if number < 0:
        return False

    for element in range(2, number // 2):
        if number % element == 0:
            return False
    return True


from math import sqrt


def get_all_factors(number):
    factors = []
    for i in range(sqrt(number)):
        if number % i == 0:
            factors.append(i)
        if i != number // i:
            factors.append(number // i)

    return factors


print(get_all_factors(100))
