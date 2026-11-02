import json

TASKS_FILE = "tasks2.json"

#---------------Work with file----------------------

def load_tasks():
    """Читает tasks.json. Если файла нет - возвращает []"""
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Сохраняет список задач в файл."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

#--------------Work with array--------------------

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})

def show_tasks(tasks):
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task["done"] else "[ ]"
        print(f"{index}. {status} {task['title']}")

def mark_done(tasks, index):
    if not (1 <= index <= len(tasks)):
            raise IndexError("This task is not valid")
    tasks[index-1]["done"] = True

def delete_task(tasks, index):
    if not (1 <= index <= len(tasks)):
        raise IndexError("This task is not valid")
    tasks.pop(index-1)

#------------------MAIN FUNCTION--------------------

def main():
    tasks = load_tasks()
    while True:
        try:
            user_number = int(input("" \
            "--------------------------\n" \
            "1. Показать задачи;\n" \
            "2. Добавить задачу;\n" \
            "3. Отметить выполненной;\n" \
            "4. Удалить задачу;\n" \
            "5. Выход.\n"
            "--------------------------\n" \
            "Ввод: "))
        except ValueError:
            print("You should input only numbers by 1 to 5.\n")
            continue
        if user_number == 1:
            if not tasks: 
                print("Список пуст")
            else:
                show_tasks(tasks)
        elif user_number == 2:
            user_title = input("Input the title of task: ")
            while user_title == "":
                user_title = input("Input not empty title of the task!: ")
            add_task(tasks, user_title)
            save_tasks(tasks)
        elif user_number == 3:
            try:
                user_index = int(input("Which task in list is done? : "))
                mark_done(tasks, user_index)
                save_tasks(tasks)
            except IndexError:
                print("You can only input numbers from tasks!")
            except ValueError:
                print("You can only input numbers from tasks!")
        elif user_number == 4:
            try:
                user_delete_index = int(input("What is the index of the task being deleted?: "))
                delete_task(tasks, user_delete_index)
                save_tasks(tasks)
            except IndexError:
                print("You can only input numbers from tasks!")
            except ValueError:
                print("You can only input numbers from tasks!")
        elif user_number == 5:
            break
        else:
            print("You should input only numbers by 1 to 5!\n")

if __name__ == "__main__": 
    main()