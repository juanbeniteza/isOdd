# As an alias to remain backward compatible
def isOdd(number):
    return is_odd(number)

def is_odd(number: int) -> bool:
    return number & 1
