import argparse
import os
import json

def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list.")
    parser.add_argument("task", nargs='+', help="The task to add.")
    parser.add_argument("-c", "--complete", nargs='+', help="The task number to mark as complete.")
    parser.add_argument("--priority", choices=["High", "Medium", "Low"], default="Medium", help="The priority of the task (High, Medium, Low).")
    parser.add_argument("--priority_filter", choices=["High", "Medium", "Low"], help="Filter tasks by priority.")
    args = parser.parse_args()

    if not args.task:
        print("No tasks provided.")
        return

    # Load tasks from file
    try:
        if os.path.exists("todo.txt"):
            with open("todo.txt", "r") as f:
                tasks = json.load(f)
    except FileNotFoundError:
        tasks = []
    except json.JSONDecodeError:
        tasks = []

    # Add new tasks
    tasks.extend(args.task)

    # Mark tasks as complete
    if args.complete:
        for task_num in args.complete:
            try:
                task_index = int(task_num) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index] = {"task": tasks[task_index]["task"], "complete": True, "priority": tasks[task_index]["priority"]}
                else:
                    print(f"Invalid task number for completion.")
            except ValueError:
                print("Invalid task number for completion.")

    # Filter tasks by priority
    if args.priority_filter:
        tasks = [task for task in tasks if task["priority"] == args.priority_filter]

    # Save tasks to file
    with open("todo.txt", "w") as f:
        json.dump(tasks, f)

    # Display tasks
    print("Tasks:")
    for task in tasks:
        if task["complete"]:
            print(f"- [{task['priority']}] [{task['complete']}] {task['task']}")
        else:
            print(f"- {task['task']} (Priority: {task['priority']})")


if __name__ == "__main__":
    main()