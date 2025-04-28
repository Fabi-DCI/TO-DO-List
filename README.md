My First To-Do List Application

Author: Fabian-DCI
Description

This is a simple terminal-based To-Do List application built as my first-ever project using Python. The application allows users to manage their tasks for each day of the week, providing functionalities to add, remove, and view tasks. Users can also see task statistics, including the number of tasks completed and still open.
Features

    Add Task: Add a task to a specific day of the week.

    Remove Task: Remove a task from a day and mark it as finished.

    View Tasks: View all tasks organized by day of the week.

    View Stats: See the number of open and finished tasks.

    Task Duplication Check: Prevent adding duplicate tasks for the same day.

How to Run
Prerequisites

    Python 3.x: Ensure that Python is installed on your machine.

Installation Steps

    Clone the Repository:

git clone git@github.com:Fabi-DCI/TO-DO-List.git

Navigate to the project directory:

cd TO-DO-List

Run the script:

    python todo_list.py

Usage

Once the application is running, you will be presented with a menu of options:

    Add Task: Add a new task to the specified day.

    Remove Task: Remove a task and mark it as finished.

    View Tasks: View all tasks for the week.

    View Stats: View the total number of open tasks and completed tasks.

    Exit: Exit the application.

Example Interaction:

--- To-Do List Menu ---
1. Add Task
2. Remove Task
3. View Tasks
4. View Stats
5. Exit
Choose an option (1-5): 1
Enter the day for the task (e.g., Monday): Monday
Enter your task: Go to the gym
Task 'Go to the gym' added to Monday.

--- To-Do List Menu ---
1. Add Task
2. Remove Task
3. View Tasks
4. View Stats
5. Exit
Choose an option (1-5): 3

--- All Tasks ---
Monday:
  - Go to the gym
-------------------

Code Structure

    tasks_by_day: A dictionary that stores tasks categorized by days of the week.

    finished_tasks: A list that keeps track of tasks that have been removed and marked as finished.

    task_add(): Adds a new task to the list for the specified day.

    task_remove(): Removes a task and marks it as finished.

    view_tasks(): Displays all tasks organized by day of the week.

    view_stats(): Displays statistics about open and finished tasks.

This was my first Python project! If you'd like to improve the project, feel free.