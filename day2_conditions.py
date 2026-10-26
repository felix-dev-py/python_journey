age = int(input("Print your age: "))
if age >= 26:
    print("Worker")
elif age >= 18:
    print("Student")
elif age > 0 & age < 18:
    print("Schoolchild")
else:
    print("non‑existent age")