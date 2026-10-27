# Function 1
def greet(name):
    """Returns greeting with name"""
    return f"Hello, {name}"

print(greet('Lucia'))

# Function 2
def power(base, exp=2):
    """Returns the given number raised to the second power"""
    return base ** exp

print(power(7))

# Function 3
def is_even(number):
    """Returns True if the number is even or False"""
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(8))