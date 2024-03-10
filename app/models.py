class Task:
    id_counter = 1
    status = False

    def __init__(self, task):
        self.id = Task.id_counter
        Task.id_counter += 1
        self.status = Task.status
        self.task = task

    def __str__(self):
        while self.status == False:
            return f"[ ] {self.id}: {self.task}"
        else:
            return f"[X] {self.id}: {self.task}"