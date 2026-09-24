def show_tasks(tasks):
    """Display every task with its number and completion status."""
    if not tasks:
        print("\nNo tasks yet. Add one to get started.")
        return

    print("\nYour tasks:")
    for number, task in enumerate(tasks, start=1):
        status = "x" if task["completed"] else " "
        print(f"{number}. [{status}] {task['title']}")


def choose_task(tasks, action):
    """Return a task selected by its displayed number."""
    if not tasks:
        print("There are no tasks to", action + ".")
        return None

    show_tasks(tasks)
    try:
        number = int(input(f"Enter the task number to {action}: "))
        if 1 <= number <= len(tasks):
            return tasks[number - 1]
    except ValueError:
        pass

    print("Invalid task number.")
    return None


def task():
    tasks = []
    print("---- WELCOME TO THE TO-DO LIST APP ----")

    while True:
        print("\n1. Add task")
        print("2. View tasks")
        print("3. Mark task complete")
        print("4. Update task")
        print("5. Delete task")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Enter the task: ").strip()
            if title:
                tasks.append({"title": title, "completed": False})
                print("Task added successfully.")
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            selected = choose_task(tasks, "complete")
            if selected:
                selected["completed"] = True
                print("Task marked as complete.")
        elif choice == "4":
            selected = choose_task(tasks, "update")
            if selected:
                title = input("Enter the new task text: ").strip()
                if title:
                    selected["title"] = title
                    print("Task updated successfully.")
                else:
                    print("Task cannot be empty.")
        elif choice == "5":
            selected = choose_task(tasks, "delete")
            if selected:
                tasks.remove(selected)
                print("Task deleted successfully.")
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    task()