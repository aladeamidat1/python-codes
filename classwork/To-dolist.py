task = []
def display_menu():

	print("1. Add a task")
	print("2. View all task")
	print("3. Mark a task as complete")
	print("4. Delete a task")
	print("5. Exit")

while True:
	choice = input("Enter your choice: ")

	if choice == "1":
		task = input("Enter add task: ")
		add_task() 
	elif choice == "2":
		view_all_task()
	elif choice =="3":
		task_index = int(input("Enter task number to mark completed"))
		Mark_task()
	elif choice  == "4":
		delete_task() 
	elif choice == "5":
		print("Exist")
		break
	
	else:
		print("invalid choice. pls try again.")


       		
 
    def view_tasks(task):
        if not tasks:
            print("No tasks available.")
        else:
            for index, task in enumerate(task, start=1):
                 = "[X]" if task['completed'] else "[ ]"
                print(f"{index}. {status} {task['task']}")
    
    def mark_complete(task_index):
        if 0 < task_index <= len(self.tasks):
            tasks[task_index - 1]['completed'] = True
            print("Task marked as complete!")
        else:
            print("Invalid task number.")
    
    def delete_task(task_index):
        if 0 < task_index <= len(self.tasks):
            tasks[task_index - 1]
            print("Task deleted successfully!")
        else:
            print("Invalid task number.")
    

