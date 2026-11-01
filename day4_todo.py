tasks = []

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})

def show_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{index}. {status} {task['title']}")

def mark_done(tasks, index):
    tasks[index-1]["done"] = True

def delete_task(tasks, index):
    tasks.pop(index)

def main():
    try:
        while True:
            user_number = int(input("" \
            "--------------------------\n" \
            "1. Показать задачи;\n" \
            "2. Добавить задачу;\n" \
            "3. Отметить выполненной;\n" \
            "4. Удалить задачу;\n" \
            "5. Выход.\n"
            "--------------------------\n" \
            "Ввод: "))
            if user_number == 1:
                show_tasks(tasks)
            elif user_number == 2:
                user_title = input("Input the title of task: ")
                while user_title == "":
                    user_title = input("Input not empty title of the task!: ")
                add_task(tasks, user_title)
            elif user_number == 3:
                try:
                    user_index = int(input("Which task in list is done?: "))
                    mark_done(tasks, user_index)
                except IndexError:
                    print("You can only input numbers from tasks!")
            elif user_number == 4:
                try:
                    user_delete_index = int(input("What is the index of the task being deleted?: "))
                    delete_task(tasks, user_delete_index)
                except IndexError:
                    print("You can only input numbers from tasks!")
            elif user_number == 5:
                break
            else:
                print("You should input only numbers by 1 to 5!\n")
    except TypeError:
        print("You should input only numbers by 1 to 5.\n")

if __name__ == "__main__": main()