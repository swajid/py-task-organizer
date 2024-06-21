class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)

    def get_all_tasks(self):
        return self.tasks

    def number_of_tasks(self):
        return len(self.tasks)

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.is_completed]

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.is_completed]