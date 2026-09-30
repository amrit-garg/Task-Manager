# Task Manager – CLI Application

A simple and user-friendly **Command Line Task Manager** developed using Python. This application helps users create, view, update, complete, and delete tasks directly from the terminal.

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Update existing tasks
* Delete tasks
* Input validation
* Simple menu-driven command-line interface
* Displays completion status of each task

## Technologies Used

* **Programming Language:** Python
* **Application Type:** Command Line Interface (CLI)
* **Data Structure:** List and Dictionary
* **Libraries:** No external libraries required

## Project Structure

```text
Task-Manager/
│
└── vityarthi.py
```

## How to Run

### Step 1: Install Python

Make sure Python is installed on your computer.

You can check it using:

```bash
python --version
```

### Step 2: Clone the Repository

```bash
git clone https://github.com/amrit-garg/Task-Manager.git
```

### Step 3: Open the Project Folder

```bash
cd Task-Manager
```

### Step 4: Run the Application

```bash
python vityarthi.py
```

## How to Use

After running the program, the following menu is displayed:

```text
---- WELCOME TO THE TO-DO LIST APP ----

1. Add task
2. View tasks
3. Mark task complete
4. Update task
5. Delete task
6. Exit
```

### Add Task

Select option `1` and enter the task you want to add.

Example:

```text
Choose an option: 1
Enter the task: Complete Python assignment
Task added successfully.
```

### View Tasks

Select option `2` to display all tasks.

Example:

```text
Your tasks:
1. [ ] Complete Python assignment
2. [x] Study Python
```

`[ ]` means the task is incomplete.

`[x]` means the task is completed.

### Mark Task Complete

Select option `3`, choose the task number, and the selected task will be marked as completed.

### Update Task

Select option `4` and choose the task that needs to be updated. Enter the new task text.

### Delete Task

Select option `5`, choose the task number, and the selected task will be removed.

### Exit

Select option `6` to close the application.

## Input Validation

The application handles several invalid inputs, including:

* Empty task names
* Invalid menu choices
* Invalid task numbers
* Non-numeric task selections

For example:

```text
Invalid option. Please choose a number from 1 to 6.
```

## Working of the Application

The application stores tasks in a Python list. Each task is represented using a dictionary containing:

```python
{
    "title": "Task name",
    "completed": False
}
```

The program continuously displays the menu and waits for the user's choice. According to the selected option, the program performs the required operation.

## Learning Outcomes

Through this project, the following Python concepts were practiced:

* Variables
* Lists
* Dictionaries
* Functions
* Conditional statements
* Loops
* User input
* Exception handling
* String methods
* Basic CRUD operations
* Command-line application development

## Future Enhancements

The project can be improved further by adding:

* Permanent task storage using files
* SQLite database integration
* Task priorities
* Due dates
* Task categories
* Search and filtering
* Separate completed and pending task views
* Graphical User Interface (GUI)
* User accounts and authentication

## Author

**Amrit Garg**

GitHub Repository:

https://github.com/amrit-garg/Task-Manager

## License

This project is created for educational and learning purposes.
