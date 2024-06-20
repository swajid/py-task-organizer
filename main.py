import os
import pandas as pd

#def grep(l, s):
#    return [i for i in l if s in i]

task_list = pd.read_csv('files/todo-list-simple.csv')
task_list = task_list.sort_values(by=['priority'], ascending=False)

planned, started, not_started, done = ([] for i in range(4))

num_tasks = task_list.shape[0]
print("There are", num_tasks, "total tasks.")

for index, row in task_list.iterrows():
    task_status = row['status']
    task = row['task']
    priority = row['priority']
    
    if task_status == "p":
        planned.append(task)
    elif task_status == "s":
        started.append(task)
    elif task_status == "n":
        not_started.append(task)
    elif task_status == "d":
        done.append(task)

print("There are", len(planned), "planned task(s) and they are:")
for planned_list in planned:
    print("- [ ]", planned_list)

print("There are", len(started), "task(s) that have been started and they are:")
for started_list in started:
    print("- [ ]", started_list)

print("There are", len(not_started), "task(s) that have not been started and they are:")
for not_started_list in not_started:
    print("- [ ]", not_started_list)

print("There are", len(done), "task(s) that are done and they are:")
for done_list in done:
    print("- [x]", done_list)



