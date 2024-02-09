def is_prime(number: int) -> bool:
    """Check if a number is prime
    number: An integer.
    Returns: True if number is prime, False otherwise
    """

    """ Special case 0 and 1, which are not prime.
    """

    if number <= 1:
        return False

    for i in range(2, int(number * 0.5)):
        if number % i == 0:
            return False
    return True

