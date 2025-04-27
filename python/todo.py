import argparse
import os

TASK_FILE = ".tasks.txt"

def add_task(task):
    """Function: add_task
    
    Input - a task to add to the list
    Return - nothing
    """
    # Open file in append mode to add tasks on end 
    # If file doesn't exist, file will be created
    with open(TASK_FILE, "a", encoding="utf-8") as file:
        # Write the task with a newline character
        file.write(f"{task}\n")

def list_tasks():
    """Function: list_task
    
    Returns a formatted string of all tasks with indices
    """
    
    # Check if task file exists before trying to read
    if not os.path.exists(TASK_FILE):
        return ""
    
    try:
        # Open and read all tasks from the file
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
        
        # Format tasks with numbers
        counter = 1
        output_string = ""
        for task in tasks:
            # Remove trailing newlines 
            output_string = output_string + str(counter) + ". " + task.strip()
            if counter < len(tasks):     # Don't add newline after the last item
                output_string += "\n"
            counter = counter + 1
            
        return output_string
    except Exception:
        # Return empty string if any errors occur
        return ""
    

def remove_task(index):
    """Function: remove_task
    Input - Index (starting at 1) of the task to remove
    Return - nothing
    """
    
    # Check if task file exists before tying to remove task
    if not os.path.exists(TASK_FILE):
        return
    
    try:
        # Open and read tasks from file
        with open(TASK_FILE, "r", encoding="utf-8") as file:
            tasks = file.readlines()
            
        # Check if index is positive and within range
        if index <=0 or index >len(tasks):
            return
        
        # Remove task from list 
        # Convert from 1-based user index 0-based index
        tasks.pop(index - 1)
        
        # Write the updated task list back to file
        with open(TASK_FILE, "w", encoding="utf-8") as file:
            file.writelines(tasks)
            
    except Exception:
                # Return if errors occur
                return
    
    
def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument(
            "-a",
            "--add",
            help="Add a new task"
            )
    parser.add_argument(
            "-l",
            "--list",
            action="store_true",
            help="List all tasks")
    parser.add_argument(
            "-r",
            "--remove",
            help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()