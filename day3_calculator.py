def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero")
    return a / b

def main():
    while True:
        symbol = input("Enter +, -, *, / or q for quit: ")
        if symbol == 'q':
            break
        try:
            number_1 = int(input("Enter first number: "))
            number_2 = int(input("Enter second number: "))
  
            if symbol == '+':
                print(f"{number_1} {symbol} {number_2} = {add(number_1, number_2)}")
            elif symbol == '-':
                print(f"{number_1} {symbol} {number_2} = {subtract(number_1, number_2)}")
            elif symbol == '*':
                print(f"{number_1} {symbol} {number_2} = {multiply(number_1, number_2)}")
            elif symbol == '/':
                try:
                    print(f"{number_1} {symbol} {number_2} = {divide(number_1, number_2)}")
                except ZeroDivisionError:
                    print("Division by zero!")
            else:
                print('You should enter +, -, *, / or q!')
        except ValueError:
            print('You should enter a number!')
       
if __name__ == "__main__":
    main()