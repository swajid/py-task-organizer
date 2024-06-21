import os
import pandas as pd
import task
from ToDoList import ToDoList

if __name__ == "__main__":
    task_list = pd.read_csv('files/todo-list-simple.csv')
    task_list = task_list.sort_values(by=['priority'], ascending=False)

    #planned, started, not_started, done = ([] for i in range(4))

    planned = ToDoList()
    started = ToDoList()
    not_started = ToDoList()
    done = ToDoList()

    num_tasks = task_list.shape[0]
    print("There are", num_tasks, "total tasks.")

    for index, row in task_list.iterrows():
        task_status = row['status']
        task = row['task']
        priority = row['priority']
        
        if task_status == "p":
            planned.add_task(task)
        elif task_status == "s":
            started.add_task(task)
        elif task_status == "n":
            not_started.add_task(task)
        elif task_status == "d":
            done.add_task(task)

    print("There are", planned.number_of_tasks(), "planned task(s) and they are:")
    for planned_list in planned.get_all_tasks():
        print("- [ ]", planned_list)

    print("There are", started.number_of_tasks(), "task(s) that have been started and they are:")
    for started_list in started.get_all_tasks():
        print("- [ ]", started_list)

    print("There are", not_started.number_of_tasks(), "task(s) that have not been started and they are:")
    for not_started_list in not_started.get_all_tasks():
        print("- [ ]", not_started_list)

    print("There are", done.number_of_tasks(), "task(s) that are done and they are:")
    for done_list in done.get_all_tasks():
        print("- [x]", done_list)



