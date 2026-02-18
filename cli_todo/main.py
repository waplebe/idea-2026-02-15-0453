import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="A simple command-line todo list.")
    parser.add_argument("task", nargs='+', help="The task to add.")
    parser.add_argument("-c", "--complete", nargs='+', help="The task number to mark as complete.")
    args = parser.parse_args()

    if not args.task:
        print("No tasks provided.")
        return

    print("Tasks:")
    for i, task in enumerate(args.task):
        if args.complete and i + 1 in [int(x) for x in args.complete]:
            print(f"- [{args.complete[0]}] {task}")
        else:
            print(f"- {task}")

    # Add persistence using a simple file
    with open("todo.txt", "a") as f:
        for task in args.task:
            f.write(f"{task}\n")

    # Load tasks from file on startup
    try:
        if os.path.exists("todo.txt"):
            with open("todo.txt", "r") as f:
                tasks = [line.strip() for line in f.readlines()]
                print("\nLoaded tasks from file:")
                for task in tasks:
                    if task.startswith("["):
                        print(f"- [{task}]")
                    else:
                        print(f"- {task}")
    except FileNotFoundError:
        pass

    # Clear the todo list when the script is run without arguments
    if len(args.task) == 0:
        try:
            with open("todo.txt", "w") as f:
                f.write("")
            print("\nTodo list cleared.")
        except FileNotFoundError:
            pass

    # Mark tasks as complete
    if args.complete:
        try:
            with open("todo.txt", "r") as f:
                tasks = [line.strip() for line in f.readlines()]
            
            for task_num in args.complete:
                task_index = int(task_num) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index] = "[X] " + tasks[task_index]
            
            with open("todo.txt", "w") as f:
                for task in tasks:
                    f.write(task + "\n")
            print("\nTasks marked as complete.")
        except FileNotFoundError:
            pass
        except ValueError:
            print("Invalid task number for completion.")


if __name__ == "__main__":
    main()