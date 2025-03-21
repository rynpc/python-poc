from datetime import datetime
from task_manager import TaskManager

def print_task(task):
    status = "✓" if task.completed else " "
    due_date = task.due_date.strftime("%Y-%m-%d") if task.due_date else "No due date"
    print(f"[{status}] Task {task.id}: {task.title}")
    print(f"    Description: {task.description}")
    print(f"    Due date: {due_date}")
    print()

def main():
    manager = TaskManager()
    
    while True:
        print("\nTask Manager Menu:")
        print("1. Add task")
        print("2. List tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date_str = input("Enter due date (YYYY-MM-DD) or press Enter for no due date: ")
            
            due_date = None
            if due_date_str:
                try:
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d")
                except ValueError:
                    print("Invalid date format. Task will be created without due date.")
            
            task = manager.add_task(title, description, due_date)
            print("\nTask created successfully!")
            print_task(task)
            
        elif choice == "2":
            tasks = manager.list_tasks()
            if not tasks:
                print("\nNo tasks found.")
            else:
                print("\nTask List:")
                for task in tasks:
                    print_task(task)
                    
        elif choice == "3":
            task_id = input("Enter task ID to mark as completed: ")
            try:
                task_id = int(task_id)
                if manager.mark_completed(task_id):
                    print("Task marked as completed!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid task ID.")
                
        elif choice == "4":
            task_id = input("Enter task ID to delete: ")
            try:
                task_id = int(task_id)
                if manager.delete_task(task_id):
                    print("Task deleted successfully!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid task ID.")
                
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 