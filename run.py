from app import Tdl
from app.models import Task

def run_tdl():
    print('Welcome to our To-Do List app!')
    tdl = Tdl()

    while True:
        print("1: Add Task\n2: View Tasks\n3: Edit Task\n4: Delete Task\n5: Quit")
        option = input("Which option would you like to do? ")
        while option not in {'1', '2', '3', '4', '5'}:
            option = input('Invalid option. Please enter 1, 2, 3, 4, or 5 ')
        if option == '5':
            break
        elif option =='1':
            tdl.create_new_task()
        elif option == '2':
            tdl.view_tasks()
        elif option == '3':
            tdl.edit_task()
        elif option == '4':
            tdl.delete_task()
    print('Thank you for using our app!\nHere is your final list.')
    for t in tdl.tasks:
        print(t)

    

run_tdl()