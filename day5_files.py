with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("Привет!\n")
    f.write("My name is Felix\n")
    f.write("What is your name?/Как тебя зовут?\n")

with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)