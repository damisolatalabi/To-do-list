##simple to do list

tasks = [] #list to store tasks

def displayMenu():
    """Display the menu options."""
    print("\n===== To-Do List Menu =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Mark Task as Done")
    print("5. Exit")

def viewTasks():
    """view all tasks."""
    if not tasks:
        print("Your To-Do List is empty!\n")
    else:
        print("\nYour To-Do List ----> ")
        for idx, task in enumerate(tasks, start = 1):
            status = "[done]" if task["done"] else "[NOT done]"
            print("{}. {} {}".format(idx, task["title"], status))
        print()

def addTask():
    """Add a new task."""
    title = input ("Enter the ask: ")
    tasks.append({"title" : title,"Done": False})
    print("Task",title , " added to the list!" )

def removeTask():
    """Remove a task by its index ."""
    viewTasks()
    try:
        task_num = int(input("Enter the number of the task you what to remove: "))
        if 1 <= task_num <= len(tasks):  #checks whether the provided task number (task_num) is within a valid range
            removed_task = tasks.pop(task_num -1) #pop removed item from list an returns it
            print("Task '" + removed_task['title'] + "' removed!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def markAsDone():
    """Mark a task as done ."""
    viewTasks()
    try:
        task_num = int(input("Enter the number of the task to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["done"] = True
            print("Task '" + tasks[task_num - 1]['title'] + "' marked as done!")
        else:
            print("Invalid task number!")
    except ValueError:
        print("Please enter a valid number!")

def validateTasks():
    ##to ensure  tasks have the done key.
    for tasks in tasks:
        if "done" not in task:
            task["done"] = False   

def main():
    """Main loop for the to-do list application."""
    validateTasks()
    while True:
        displayMenu()
        try:
            choice = input("Choose an option (1-5): ")
            if choice == "1":
                viewTasks()
            elif choice == "2":
                addTask()
            elif choice == "3":
                removeTask()
            elif choice == "4":
                markAsDone()
            elif choice == "5":
                print("Goodbye!")
                break
            else:
                print("Invalid option! Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

# Run the application
