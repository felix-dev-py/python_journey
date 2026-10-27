# Function 1
def greet(name):
    return f"Hello, {name}"

print(greet('Lucia'))

# Function 2
def power(base, exp=2):
    return base ** exp

print(power(7))

# Function 3
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(8))