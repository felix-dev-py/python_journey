tasks = ["купить хлеб", "выучить Python"]

tasks.append("сходить в зал")     # добавить в конец
tasks.insert(0, "проснуться")     # вставить по индексу
tasks.remove("купить хлеб")       # удалить по значению (первое совпадение)
last = tasks.pop()                # удалить и вернуть последний
first = tasks.pop(0)              # удалить и вернуть по индексу
tasks.sort()                      # сортировка на месте (меняет сам список)
tasks.sort(reverse=True)          # в обратном порядке
tasks.reverse()                   # перевернуть
length = len(tasks)               # длина
index = tasks.index("выучить Python")  # позиция элемента


numbers = [10, 20, 30, 40, 50]
numbers[0]       # 10
numbers[-1]      # 50 (с конца)
numbers[1:3]     # [20, 30] (с 1 включительно по 3 НЕ включительно)
numbers[:2]      # [10, 20] (с начала)
numbers[2:]      # [30, 40, 50] (до конца)
numbers[::-1]    # [50, 40, 30, 20, 10] (реверс — трюк!)

for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")    # нумерация с 1