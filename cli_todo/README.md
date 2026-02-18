# Simple CLI Todo List

This is a command-line tool for managing a todo list. It now includes the ability to mark tasks as complete, persistent storage, and basic error handling.

## Usage

To add tasks, run the script with the tasks as arguments:

```bash
python main.py task1 task2 task3
```

This will print the list of tasks to the console. The tasks are also saved to a file named `todo.txt` in the project directory.

To mark a task as complete, use the `-c` flag followed by the task number (starting from 1).

```bash
python main.py -c 1 task1
```

This will mark the first task as complete and update the `todo.txt` file.

## Persistence

The todo list is now persisted to a file named `todo.txt`. Each task is written on a new line. To view the list, run the script again. To clear the list, delete the `todo.txt` file.

## Startup

The script now loads existing tasks from `todo.txt` when it starts, displaying them before accepting new tasks. Completed tasks are marked with a `[X]` prefix.

## Clearing the List

The script can now clear the todo list. If you run the script without any arguments, it will delete the `todo.txt` file, effectively clearing the list.

## Error Handling

The script now handles the following errors:

*   **No tasks provided:** If no tasks are provided, it prints a message and exits.
*   **Invalid task number:** If an invalid task number is provided for marking as complete, it prints an error message and continues.
*   **File not found:** If `todo.txt` is not found, it creates it.

## Example

```bash
# Add some tasks
python main.py task1 task2 task3

# View the tasks
python main.py

# Mark task 1 as complete
python main.py -c 1 task1

# View the tasks again
python main.py

# Clear the list
python main.py
```

## New Features

*   **Task Completion:**  Tasks can now be marked as complete using the `-c` flag. Completed tasks are indicated with a `[X]` prefix in the output and saved to the `todo.txt` file.
*   **Robust Error Handling:**  The script now handles cases where the task number provided for completion is invalid or out of range, and when the `todo.txt` file is not found.
*   **Comprehensive Testing:**  A suite of unit tests has been added to ensure the functionality of the script, including adding tasks, completing tasks, loading tasks, clearing the list, and handling invalid input.