# Task data stored in a list of tuples
tasks = [
    ("Task 1", "2023-02-20", False),
    ("Task 2", "2023-02-25", False),
    ("Task 3", "2023-03-01", False),
    ("Task 4", "2023-03-05", False),
    ("Task 5", "2023-03-10", False)
]

# Dictionary to store tasks by status
task_status = {"completed": [], "incomplete": []}

def add_task(task_name, due_date):
    """Add a new task"""
    tasks.append((task_name, due_date, False))
    task_status["incomplete"].append((task_name, due_date))

def complete_task(task_name):
    """Mark a task as completed"""
    for i, task in enumerate(tasks):
        if task[0] == task_name:
            tasks[i] = (task[0], task[1], True)
            task_status["incomplete"].remove((task[0], task[1]))
            task_status["completed"].append((task[0], task[1]))
            print(f"Task '{task_name}' marked as completed.")
            return
    print(f"Task '{task_name}' not found.")

def remove_task(task_name):
    """Remove a task"""
    for i, task in enumerate(tasks):
        if task[0] == task_name:
            tasks.pop(i)
            if task in task_status["incomplete"]:
                task_status["incomplete"].remove(task)
            elif task in task_status["completed"]:
                task_status["completed"].remove(task)
            print(f"Task '{task_name}' removed.")
            return
    print(f"Task '{task_name}' not found.")

def display_tasks():
    """Display tasks by status"""
    print("Completed Tasks:")
    for task in task_status["completed"]:
        print(f"- {task[0]} (Due: {task[1]})")
    print("\nIncomplete Tasks:")
    for task in task_status["incomplete"]:
        print(f"- {task[0]} (Due: {task[1]})")

def task_manager():
    while True:
        print("\n Task Manager ")
        print("\n 1. Add a task ")
        print("\n 2. Mark a task as completed ")
        print("\n 3. Remove a task ")
        print("\n 4. Display tasks ")
        print("\n 5. Quit the program ")

        choice = input("Enter your choice: ")

        if choice == "1":
            task_name = input("Enter task name: ")
            due_date = input("Enter due date: ")
            add_task(task_name, due_date)
        elif choice == "2":
            task_name = input("Enter task name: ")
            complete_task(task_name)
        elif choice == "3":
            task_name = input("Enter task name: ")
            remove_task(task_name)
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            break
        else:
            print("Oops! It's invalid. Please choose again.")

task_manager()