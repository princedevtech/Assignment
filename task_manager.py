import json

class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def __repr__(self):
        status = "Completed" if self.completed else "Pending"
        return f"[{self.id}] {self.title} - {status}"

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["title"], data["completed"])

tasks = []

def add_task(title):
    task_id = len(tasks) + 1
    task = Task(task_id, title)
    tasks.append(task)
    print(f"Task '{title}' added successfully.")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            print(task)

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task.id != task_id]
    print(f"Task with ID {task_id} deleted.")

def mark_task_complete(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            print(f"Task '{task.title}' marked as complete.")
            return
    print(f"No task found with ID {task_id}.")

def save_tasks():
    with open("tasks.json", "w") as file:
        json.dump([task.to_dict() for task in tasks], file)
    print("Tasks saved to tasks.json.")

def load_tasks():
    global tasks
    try:
        with open("tasks.json", "r") as file:
            task_dicts = json.load(file)
            tasks = [Task.from_dict(data) for data in task_dicts]
    except FileNotFoundError:
        tasks = []
    print("Tasks loaded from tasks.json.")

def main():
    load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Complete")
        print("5. Save Tasks")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Enter task title: ")
            add_task(title)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID to delete: "))
            delete_task(task_id)
        elif choice == "4":
            task_id = int(input("Enter task ID to mark as complete: "))
            mark_task_complete(task_id)
        elif choice == "5":
            save_tasks()
        elif choice == "6":
            save_tasks()
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
