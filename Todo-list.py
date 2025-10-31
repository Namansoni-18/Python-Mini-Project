print("Hello World!")
def add_task(task_list, task):
    task_list.append(task)
    print(f'Task "{task}" added.')

def view_tasks(task_list):
    if not task_list:
        print("No tasks found.")
    else:
        print("Tasks:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")

def remove_task(task_list, task_number):
    if 0 < task_number <= len(task_list):
        removed_task = task_list.pop(task_number - 1)
        print(f'Task "{removed_task}" removed.')
    else:
        print("Invalid task number.")
def main():
    task_list = []
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            task = input("Enter the task: ")
            add_task(task_list, task)
        elif choice == '2':
            view_tasks(task_list)
        elif choice == '3':
            task_number = int(input("Enter the task number to remove: "))
            remove_task(task_list, task_number)
        elif choice == '4':
            print("Exiting the To-Do List application.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    