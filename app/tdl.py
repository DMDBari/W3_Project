from app.models import Task

class Tdl:
    def __init__(self):
        self.tasks = []

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