import sqlite3

DB_FILE = "todo.db"

def get_db_connection():
    return sqlite3.connect(DB_FILE)

def init_db():
    conn = get_db_connection()
    try:
        with conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    done INTEGER DEFAULT 0
                )
            """)
    finally:
        conn.close()

def add_task(title):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()

def show_tasks():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, done FROM tasks")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("List is empty")
        return

    for row in rows:
        task_id, title, done = row
        status = "[x]" if done else "[ ]"
        print(f"{task_id}. {status} {title}")

def mark_done(task_id):
    conn = get_db_connection()
    try: 
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            raise ValueError("The task was not found")
        conn.commit()
    finally:
        conn.close()

def delete_task(task_id):
    conn = get_db_connection()
    try: 
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        if cursor.rowcount == 0:
            raise ValueError("The task was not found")
        conn.commit()
    finally:
        conn.close()

def main():
    init_db()
    while True:
        try:
            user_number = int(input("" \
            "--------------------------\n" \
            "1. Show tasks;\n" \
            "2. Add task;\n" \
            "3. Mark done task;\n" \
            "4. Delete task;\n" \
            "5. Exit.\n"
            "--------------------------\n" \
            "Input: "))
        except ValueError:
            print("You should input only numbers by 1 to 5.\n")
            continue
        if user_number == 1:
            show_tasks()
        elif user_number == 2:
            user_title = input("Input the title of task: ")
            while user_title == "":
                user_title = input("Input not empty title of the task!: ")
            add_task(user_title)
        elif user_number == 3:
            try:
                user_index = int(input("Which task in list is done? : "))
                mark_done(user_index)
            except ValueError:
                print("You can only input numbers from tasks!")
        elif user_number == 4:
            try:
                user_delete_index = int(input("What is the index of the task being deleted?: "))
                delete_task(user_delete_index)
            except ValueError:
                print("You can only input numbers from tasks!")
        elif user_number == 5:
            break
        else:
            print("You should input only numbers by 1 to 5!\n")

if __name__ == "__main__": 
    main()