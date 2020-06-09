def isOdd(number):

    if not isinstance(number, int):
        raise ValueError('Expected an integer')

    return (abs(number) % 2 == 1)

