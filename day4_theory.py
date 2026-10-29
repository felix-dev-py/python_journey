tasks = ["Buy bread", "Learn Python"]

tasks.append("Go to gym")
print(tasks)
tasks.insert(0, "Awake")
print(tasks)
tasks.remove("Buy bread")
print(tasks)
last = tasks.pop()
print(last)
first = tasks.pop(0)
print(first)
tasks.append("New task 1")
tasks.append("New task 3")
tasks.append("New task 2")
tasks.sort()
print(tasks)
tasks.sort(reverse=True)
print(tasks)
tasks.reverse()
print(tasks)
length = len(tasks)
print(length)
index = tasks.index("Learn Python")
print(index)


numbers = [10, 20, 30, 40, 50]

print(numbers[0])
print(numbers[-1])
print(numbers[1:3])
print(numbers[:2])
print(numbers[2:])
print(numbers[::-1])

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")