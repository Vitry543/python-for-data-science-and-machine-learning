# command line task manager

import os

# file to store to task
task_file = "tasks.txt"

# load task from files
def load_task():
    task={}
    # check if the file exists
    if os.path.exists(task_file):
        with open(task_file, 'r') as f:
            for line in f:
                task_id, title, status = line.strip().split(" | ")
                task[int(task_id)] = {
                    "title": title,
                    "status": status
                }
    return task

# save task to files
def save_task(task):
    with open(task_file, 'w') as f:
        for task_id, task_info in task.items():
            f.write(f"{task_id} | {task_info['title']} | {task_info['status']}\n")
    

# add a new task
def add_task(task):
    title = input("Enter the task title: ")
    task_id = max(task.keys(), default=0) + 1
    task[task_id] = {
        "title": title,
        "status": "pending"
    }
    save_task(task)
    print(f"Task {title} added successfully with ID: {task_id}")

# view all tasks
def view_task(task):
    if not task:
        print("No task found")
    else:
        for task_id, task_info in task.items():
            print(f"Task ID: {task_id}")
            print(f"Title: {task_info['title']}")
            print(f"Status: {task_info['status']}")
            print("-"*20)

            print(f"[{task_id}] {task_info['title']} {task_info['status']}")

# mark task as complete
def mark_task_complete(task):
    task_id = int(input("Enter the task ID to mark as complete: "))
    if task_id in task:
        task[task_id]['status'] = "completed"
        save_task(task)
        print(f"Task {task_id} marked as completed")
    else:
        print(f"Task {task_id} not found")

# delete task
def delete_task(task):
    task_id = int(input("Enter the task ID to delete: "))
    if task_id in task:
        del task[task_id]
        save_task(task)
        print(f"Task {task_id} deleted successfully")
    else:
        print(f"Task {task_id} not found")

# main function
def main():
    task = load_task()
    while True:
        print("\nTask Manager Menu")
        print("1. Add Task")
        print("2. View Task")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(task)
        elif choice == "2":
            view_task(task)
        elif choice == "3":
            mark_task_complete(task)
        elif choice == "4":
            delete_task(task)
        elif choice == "5":
            save_task(task)
            print("goodbye")
            break
        else:
            print("Invalid choice, please try again")

if __name__ == "__main__":
    main()
