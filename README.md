# My First To-Do List Application  
### By: Fabian-DCI  

---

## Introduction  
- **Project Name**: To-Do List  
- **Description**:  
  Terminal-based application to manage daily tasks, organized by day of the week.  

---

## Features
1. **Task Management**:  
   - Add tasks to specific weekdays.  
   - Prevent duplicate entries for the same day.  
   - Remove tasks and mark them as completed.  

2. **Task Display**:  
   - View tasks neatly organized by weekday.  
   - Simple format for quick reference.  

3. **Task Statistics**:  
   - Count the number of open tasks.  
   - Track completed tasks in a separate list.  

---

## How It Works  
### Main Menu  
- Interactive menu with the following options:  
  1. Add a Task  
  2. Remove a Task  
  3. View All Tasks  
  4. View Task Statistics  
  5. Exit   

---

## Code Overview  
### Core Data Structures  
- **`tasks_by_day`**:  
  - A dictionary mapping weekdays to their respective task lists.  

- **`finished_tasks`**:  
  - A list to store completed tasks for easy tracking.  

### Key Functions  
1. **`task_add()`**  
   - Adds a task to a specified day.  
   - Prevents duplicates within the same day.  

2. **`task_remove()`**  
   - Removes a task from the list.  
   - Marks the task as completed by moving it to `finished_tasks`.  

3. **`view_tasks()`**  
   - Displays tasks grouped by day.  

4. **`view_stats()`**  
   - Summarizes open and completed tasks with counts.  

### Menu Control  
- The application operates within a `while` loop, continuously displaying the menu until the user chooses to exit.  

---

## Planned Enhancements  
1. **Deadlines**:  
   - Add optional deadlines for tasks using Python's `datetime` module.  
   - Implement alerts for overdue tasks.  

2. **Task Prioritization**:  
   - Allow users to assign priority levels (e.g., High, Medium, Low).  

3. **Graphical Interface**:  
   - Replace the terminal interface with a GUI for a more user-friendly experience.  

4. **Recurring Tasks**:  
   - Add functionality to schedule recurring tasks automatically.  
