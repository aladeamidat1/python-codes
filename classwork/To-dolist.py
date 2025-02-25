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


def view_tasks():
	if no tasks:
		return("No tasks available.")
	else:
		for index, tasks in enumerate(tasks, start=1):
			result = if tasks['compelete']
				return ['x']
	else: 
			return []
	

def mark_complete():
	if task < 0 

















 
       

