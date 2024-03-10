from app.models import Task

class Tdl:
    def __init__(self):
        self.tasks = []

    def __get_task_from_id(self):
        task_id = input('What task would you like to view? ')
        while not task_id.isdigit():
            task_id = input('Invalid option. Please select task by number: ')
        for t in self.tasks:
            if t.id == int(task_id):
                return t
        print(f"Task number {task_id} does not exist")


    def create_new_task(self):
        task = input('What new task would you like to add? ')
        new_task = Task(task)
        self.tasks.append(new_task)
        print('Your new task has been added.')

    def view_tasks(self):
        if self.tasks:
            for t in self.tasks:
                print(t)
        else:
            print('There are currently no tasks in your list.')

    def edit_task(self):
        task = self.__get_task_from_id()
        if task:
            option = input('Did you finish this task? yes or no? ')
            while option.lower() not in {'yes', 'no'}:
                option = input("Please use 'yes' or 'no'.  Did you finish this task? ")
            if option.lower() == 'yes':
                task.status = True
                print('Congrats on finishing this task! We updated the task to reflect that it is complete.')
            else:
                task.status = False
                print("We updated the task to reflect that it is not complete.  You've got this!")

    def delete_task(self):
        task = self.__get_task_from_id()
        if task:
            confirmation = input("Are you sure you would like to delete this task? Enter 'yes' to delete ")
            if confirmation.lower() == 'yes':
                self.tasks.remove(task)
                print('This task has been removed\nHere is your current list')
                for t in self.tasks:
                    print(t)
            else:
                print('We did not delete this task\nHere is your current list')
                for t in self.tasks:
                    print(t)
