tasks = []

def display_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"'{task}' has been added.")

def remove_task():
    display_tasks()
    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        removed_task = tasks.pop(task_num - 1)
        print(f"'{removed_task}' has been marked as complete and removed.")
    except (IndexError, ValueError):
        print("Invalid task number.")

while True:
    print("\nTo-Do List Manager")
    print("1. View Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Exiting To-Do List Manager.")
        break
    else:
        print("Invalid choice. Please choose a valid option.")
