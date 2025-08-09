tasks = []

def add_task():
    description = input("Enter task description(s) (separate multiple with commas): ")
    task_list = description.split(",")
    for desc in task_list:
        desc = desc.strip()
        if desc:
            task = {"description": desc, "status": "Pending"}
            tasks.append(task)
    print(f"{len(task_list)} task(s) added successfully!\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    print("\n- Task List -")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['description']} [{task['status']}]")
    print()

def mark_task_done():
    view_tasks()
    if not tasks:
        return
    task_numbers = input("Enter task number(s) to mark as Done (separate with commas): ")
    number_list = task_numbers.split(",")
    done_count = 0
    for num in number_list:
        num = num.strip()
        if num.isdigit():
            task_number = int(num)
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["status"] = "Done"
                done_count += 1
            else:
                print(f"Invalid task number: {num}")
        else:
            print(f"Invalid input: {num}")
    print(f"{done_count} task(s) marked as Done!\n")

def delete_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_number = int(input("Enter task number to delete: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Deleted task: {removed_task['description']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def show_menu():
    print("To-Do List Manager")
    print("1. Add Tasks")
    print("2. View Tasks")
    print("3. Mark Task as Done")
    print("4. Delete Tasks")
    print("5. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_task_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print("Thank you for using To-Do List Manager!")
        break
    else:
        print("Invalid choice, please try again.\n")
