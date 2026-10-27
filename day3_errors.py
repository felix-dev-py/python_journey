try:
    number = int(input("Enter the number: "))
    print(number * 2)
except ValueError:
    print("This is not a number")
