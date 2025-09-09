
# Daily to-do list
# Ask the user to enter their daily tasks.
# Allow them to add tasks, 
# mark a task as completed,
# and display the updated list.

def display_task(Tasks) :
     for index, task in enumerate(Tasks):
        num = index + 1  # start at 1 wihile index in the list start at 0
        task_name = task["task"]
        status = "completed " if task["completed"] else "not completed"
        
        print(f"{num}. {task_name} - {status}")

def add():
    Tasks = []

    while True: 
        task_input = input("enter your task or stop to exit: ")
        if task_input == "stop":
            break

        completed_task = input("is it completed : y for yes or n for no: ")
        completed_task = True if completed_task == "y" else False

        # add to the list
        Tasks.append({"task": task_input, "completed": completed_task})

    # display the al the task
    print("\nyour tasks:")
    #call the function who display all the task
    display_task(Tasks)

    mark_completed = input("do you want to mark a task as completed: ")
    if mark_completed == "no" :
        print("thank you")
    else:
        selected_task = input("select the num you want to mark as complete: ")
        #verfified if the input is a valid number
        if selected_task.isdigit() :
            #transform into a int 
            task_num = int(selected_task)
            #associate the right index with the index in the list
            task_index = task_num -1

            #verified if the index exist in the list
            if task_index >= 0 and task_index < len(Tasks):
                #associaate the task inedex to the variable selected_task_disc
                selected_task_disc = Tasks[task_index]
       
                if selected_task_disc ["completed"] == False :
                    selected_task_disc["completed"] = True
                    print(f"Task {task_num} marked as completed! ")
                    
                    print('your tasks')
                    display_task(Tasks)
                else:
                    print("your task is already completed")
            else: 
                print(f"invalid number please choose betwwen 1 and {len(Tasks)}")
        else: 
            print("please enter a valid number! ")


add()