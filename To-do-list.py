def toDoList():
    tasks = []
    while True:
        # Adding a newline for better readability
        print("\n--- To-Do List Menu ---")
        print("1. Add New Task")
        print("2. Delete Task")
        print("3. Show All Tasks")
        print("4. Exit")

        choice = input("Enter Your Choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            tasks.append(task)
            print(f"✅ Task '{task}' added!")

        elif choice == '2':
            task_to_remove = input("Enter the task to remove: ")
            if task_to_remove in tasks:
                tasks.remove(task_to_remove)
                print(f"🗑️ Task '{task_to_remove}' removed.")
            else:
                print("❌ Task not found.")

        elif choice == '3':
            print("\n--- Your Tasks ---")
            if not tasks:
                print("Your to-do list is empty.")
            else:
                # The corrected loop to display tasks
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")

        elif choice == '4':
            print("Goodbye! 👋")
            break

        else:
            print("Invalid Choice! Please enter a number between 1 and 4.")

# Run the to-do list
toDoList()