number = 7
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

import random
secret = random.randint(1, 11)
user_number = 0
print("Hi, guess what number I’m thinking of")
while secret != user_number:
    user_number = int(input("Print the number: "))
    if secret == user_number:
        print('Congradulations!')
        break
    elif secret < user_number:
        print(f"My number is less then {user_number}")
    elif secret > user_number:
        print(f"My number is greater then {user_number}")
    else:
        print('Unknown error')