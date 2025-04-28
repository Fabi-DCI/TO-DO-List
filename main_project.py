# My first version of my To-Do-List
# Author: Fabian-DCI
# Description: A simple terminal-based to-do list application to manage tasks.


tasks_by_day = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}

finished_tasks = []

def task_add():
    """
    Adds a new task to the list.
    If the task already exists for the same day, it notifies the user.
    """
    day = input("Enter the day for the task (e.g., Monday): ").capitalize()
    if day not in tasks_by_day:
        print("Invalid day! Please enter a valid day of the week.")
        return

    task_name = input("Enter your task: ")
    for task in tasks_by_day[day]:
        if task_name == task:
            print("Task already exists for this day!")
            return

    tasks_by_day[day].append(task_name)
    print(f"Task '{task_name}' added to {day}.")


def task_remove():
    """
    Removes a task from the list and marks it as finished.
    If the task is not found, it notifies the user.
    """
    day = input("Enter the day of the task to remove (e.g., Monday): ").capitalize()
    if day not in tasks_by_day:
        print("Invalid day! Please enter a valid day of the week.")
        return

    task_name = input("Enter the name of the task to remove: ")
    if task_name in tasks_by_day[day]:
        tasks_by_day[day].remove(task_name)
        finished_tasks.append(task_name)
        print(f"Task '{task_name}' removed and marked as finished!")
    else:
        print("Task not found!")

def view_tasks():
    """
    Displays all tasks organized by day.
    """
    print("\n--- All Tasks ---")
    for day, tasks in tasks_by_day.items():
        print(f"\n{day}:")
        if not tasks:
            print("  No tasks.")
        else:
            for task in tasks:
                print(f"  - {task}")
    print("-------------------")


def view_stats():
    """
    Displays stats about open and finished tasks.
    - Shows the count of open tasks.
    - Shows the count and list of finished tasks.
    """
    open_tasks_count = sum(len(tasks) for tasks in tasks_by_day.values())
    print("\n--- Task Statistics ---")
    print(f"Open Tasks: {open_tasks_count}")
    print(f"Finished Tasks: {len(finished_tasks)}")
    if len(finished_tasks) > 0:
        print("Finished Tasks List:", finished_tasks)
    print("------------------------")


while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. View Stats")
    print("5. Exit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        task_add()
    elif choice == "2":
        task_remove()
    elif choice == "3":
        view_tasks()
    elif choice == "4":
        view_stats()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
