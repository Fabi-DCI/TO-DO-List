# My first version of my To-Do-List
# Author: Fabian-DCI
# Description: A simple terminal-based to-do list application to manage tasks.

# lists for tasks
Lst = ["Gym"]
finished_tasks = []

def task_add():
    """
    Adds a new task to the list.
    If the task already exists, it notifies the user.
    """
    Taskadd = input("Enter your task to add to the list: ").strip()
    if Taskadd in Lst:
        print("Task already exists!")
    else:
        Lst.append(Taskadd)
        print(f"Task '{Taskadd}' added!")
    
    print("Current Tasks:", Lst)

def task_remove():
    """
    Removes a task from the list and marks it as finished.
    If the task is not found, it notifies the user.
    """
    Taskdel = input("Enter your task to remove from the list: ").strip()
    if Taskdel in Lst:
        Lst.remove(Taskdel)
        finished_tasks.append(Taskdel)
        print(f"Task '{Taskdel}' removed and marked as finished!")
    else:
        print("Task not found!")
    print("Current Tasks: ", Lst)

def view_stats():
    """
    Displays statistics about open and finished tasks.
    - Shows the count of open tasks.
    - Shows the count and list of finished tasks.
    """
    print("\n--- Task Statistics ---")
    print(f"Open Tasks: {len(Lst)}")
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
        print("Your Tasks:", Lst)
    elif choice == "4":
        view_stats()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
