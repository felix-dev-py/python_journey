# Function 1
def greet(name):
    """Returns greeting with name"""
    return f"Hello, {name}"

print(greet('Lucia'))

# Function 2
def power(base, exp=2):
    """Returns base raised to exp (default 2)."""
    return base ** exp

print(power(7))

# Function 3
def is_even(number):
    """Returns True if the number is even or False"""
    return number % 2 == 0

print(is_even(8))