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

def veiwTasks():
    """view all tasks."""
    if not tasks:
        print("Your To-Do List is empty!\n")
    else:
        print("\nYour To-Do List ----> ")
        for idx, task in enumerate(tasks, start = 1):
            status = "[DONE]" if task["Done"] else "[NOT DONE]"
            print("{}. {} {}".format(idx, task["title"], status))
        print()

def addTask():
    """Add a new task."""
    title = input ("Enter the ask: ")
    tasks.append({"title" : title,"Done": False})
    print("Task",title , " added to the list!" )

    
