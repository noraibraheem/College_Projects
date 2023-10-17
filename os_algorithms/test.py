from tkinter import Tk, Label, Listbox, Entry, Button, END
from heapq import heappush, heappop
from EDF import Task, earliest_deadline_first
from MLF import Task_mlf,minimum_laxity_first


tasks = []

def add_task():
    name = name_entry.get()
    name=list(name.split())
    arrival_time_str = arrival_time_entry.get()
    arrival_time = list(map(int, arrival_time_str.split()))
    deadline_str = deadline_entry.get()
    deadline = list(map(int, deadline_str.split()))
    execution_time_str = execution_time_entry.get()
    excution_time=list(map(int, execution_time_str.split()))
    for i in range(3):
        tasks.append(Task(name[i], arrival_time[i], deadline[i], excution_time[i]))

def run_scheduler():
    total_time = int(total_time_entry.get())
    earliest_deadline_first(tasks, total_time)
    


#mlf
tasks_mlf = []

def add_task_mlf():
    name = name_entry_mlf.get()
    name=list(name.split())
    arrival_time_str = arrival_time_entry_mlf.get()
    arrival_time = list(map(int, arrival_time_str.split()))
    deadline_str = deadline_entry_mlf.get()
    deadline = list(map(int, deadline_str.split()))
    execution_time_str = execution_time_entry_mlf.get()
    excution_time=list(map(int, execution_time_str.split()))
    for i in range(3):
        tasks_mlf.append(Task_mlf(name[i], arrival_time[i], deadline[i], excution_time[i]))

def run_scheduler_mlf():
    total_time = int(total_time_entry_mlf.get())
    minimum_laxity_first(tasks_mlf, total_time)
    
window = Tk()
window.title("Earliest Deadline First Scheduler")
window.geometry("600x700")

name_label = Label(window, text="Task Name:")
name_label.grid(row=0, column=0)

name_entry = Entry(window)
name_entry.grid(row=0, column=1)

arrival_time_label = Label(window, text="Arrival Time:")
arrival_time_label.grid(row=1, column=0)

arrival_time_entry = Entry(window)
arrival_time_entry.grid(row=1, column=1)

deadline_label = Label(window, text="Deadline:")
deadline_label.grid(row=2, column=0)

deadline_entry = Entry(window)
deadline_entry.grid(row=2, column=1)

execution_time_label= Label(window, text="Execution Time:")
execution_time_label.grid(row=3, column=0)

execution_time_entry = Entry(window)
execution_time_entry.grid(row=3, column=1)



add_button = Button(window, text="Add Tasks", command=add_task)
add_button.grid(row=4, column=1)

total_time_label = Label(window, text="Total Time:")
total_time_label.grid(row=5, column=0)

total_time_entry = Entry(window)
total_time_entry.grid(row=5, column=1)

run_button = Button(window, text="Run Scheduler", command=run_scheduler)
run_button.grid(row=6, column=0)


name_label_mlf = Label(window, text="Task Name:")
name_label_mlf.grid(row=7, column=0)

name_entry_mlf = Entry(window)
name_entry_mlf.grid(row=7, column=1)

arrival_time_label = Label(window, text="Arrival Time:")
arrival_time_label.grid(row=8, column=0)

arrival_time_entry_mlf = Entry(window)
arrival_time_entry_mlf.grid(row=8, column=1)

deadline_label = Label(window, text="Deadline:")
deadline_label.grid(row=9, column=0)

deadline_entry_mlf = Entry(window)
deadline_entry_mlf.grid(row=9, column=1)

execution_time_label= Label(window, text="Execution Time:")
execution_time_label.grid(row=10, column=0)

execution_time_entry_mlf = Entry(window)
execution_time_entry_mlf.grid(row=10, column=1)



add_button = Button(window, text="Add Tasks", command=add_task_mlf)
add_button.grid(row=11, column=1)

total_time_label = Label(window, text="Total Time:")
total_time_label.grid(row=12, column=0)

total_time_entry_mlf = Entry(window)
total_time_entry_mlf.grid(row=12, column=1)

run_button = Button(window, text="Run Scheduler", command=run_scheduler_mlf)
run_button.grid(row=13, column=0)

window.mainloop()