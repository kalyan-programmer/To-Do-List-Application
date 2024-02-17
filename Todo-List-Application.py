tasks = []

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as f:
            for line in f:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass

def show_tasks():
    print("Tasks:")
    for index, task in enumerate(tasks):
        print(f"{index + 1}. {task}")

def add_task(task):
    tasks.append(task)
    save_tasks()

def remove_task(index):
    if index <= len(tasks):
        tasks.pop( (index-1) )
        save_tasks()
    else:
        print("Invalid index")

load_tasks()
while True:
    print("\n1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '3':
        index = int(input("Enter task index to remove: "))
        remove_task(index)
    elif choice == '4':
        break
    else:
        print("Invalid choice")
