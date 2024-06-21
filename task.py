from datetime import datetime

class Task:
    def __init__(self, status, task, priority=0):
        self.status = status
        self.task = task
        self.priority = priority
        self.is_completed = False
        
    def mark_completed(self):
        self.is_completed = True

    def mark_incomplete(self):
        self.is_completed = False