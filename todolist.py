tasks = []
   
def add_task():
    description = input("Enter your task's description: ") 
    priority = input("Enter your task's priority (High/Medium/Low)")
    task = {'description': description, 'status':'incomplete', 'priority':priority}
    tasks.append(task)
    print("Task has been added")

def view_task():
    if not tasks:
        print("Task does not exist")
    else:
        print("Your task is available")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task['description']} | Status: {task['status']} | Priority: {task['priority']}")
    

def edit_task():
    # if not tasks:
    #     print("Task does not exist")
    # else:
        user_input =int(input("What task number would you like to edit: "))
        if 1 <= user_input <= len(tasks):
            new_description = input("Enter your new description")
            tasks[user_input - 1]['description'] = new_description
            print("Yout task has been updated ")
        else:
            print("Invalid task number.")

def mark_as_completed():
    # if not tasks:
    #     print("Task does not exist")
    # else:
        task_to_complete = int(input("Enter task number to mark as completed")) 
        if 1 <= task_to_complete <= len(tasks):
            tasks[task_to_complete - 1] = 'completed'
            print(f"The task {task_to_complete} has been completed ")
        else:
            print("Invalid task number.")
    
def delete_task():
    task_to_delete = int(input("Enter task number to delete"))
    if 1 <= task_to_delete <= len(tasks):
        deleted_task = tasks.pop(task_to_delete - 1)
        print(f"Task number{task_to_delete} has been deleted sucessfully")
    else:
         print("Invalid task number")

def search_task():
    keyword = input("Enter a keyword to search for (or press Enter to skip): ")
    priority = input("Enter priority to filter by (High/Medium/Low, or press Enter to skip): ").capitalize()

    found_tasks = [task for task in tasks if (keyword.lower() in task['description'].lower() if keyword else True) and
                   (task['priority'].lower() == priority.lower() if priority else True)]

    if found_tasks:
        print("\nSearch Results:")
        for i, task in enumerate(found_tasks, 1):
            print(f"{i}. {task['description']} | Status: {task['status']} | Priority: {task['priority']}")
    else:
        print("No matching tasks found.")
                
def exit():
    exit_confirmed = input("Are you sure you want to exit?")
    return exit_confirmed

def main():
    while True:
        print("To-Do LIST MANAGER")
        print("1.ADD TASK")
        print("2.EDIT TASK")
        print("3.VIEW TASK")
        print("4.DELETE TASK")
        print("5.MARK AS COMPLETED")
        print("6.SEARCH TASK")
        print("7.EXIT")
        choice = int(input("Enter your choice between (1-7)"))

        if choice == 1:
            add_task()
        if choice == 2:
            edit_task()
        if choice == 3:
            view_task()
        if choice == 4:
            delete_task()
        if choice == 5:
            mark_as_completed()
        if choice == 6:
            search_task()
        if choice == 7:   
            exit()
            print("Goodbye!!")

main()                                


