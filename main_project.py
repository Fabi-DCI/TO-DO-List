Lst = ["Gym"]

def task_add():
    Taskadd = input("Enter your task to add to the list: ")
    if Taskadd in Lst:
        print("Task already exists!")
    else:
        Lst.append(Taskadd)
        print(f"Task '{Taskadd}' added!")
    print("Current Tasks:", Lst)

def task_remove():
    Taskdel = input("Enter your task to remove from the list: ")
    if Taskdel in Lst:
        Lst.remove(Taskdel)
        print(f"Task '{Taskdel}' removed!")
    print("Current Tasks: ", Lst)

while True:
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        task_add()
    elif choice == "2":
        task_remove()
    elif choice == "3":
        print("Your Tasks:", Lst)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")