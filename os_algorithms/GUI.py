from tkinter import *
from tkinter import Tk, Label, Listbox, Entry, Button,ttk,StringVar, END
import tkinter as tk
from heapq import heappush, heappop
from SSTF import shortest_seek_time_first
from FCFS import FCFS
from SCAN import SCAN
from LOCK import LOCK
from C_LOCK import c_lock
from C_SCAN import c_scan
from EDF import earliest_deadline_first,Task
from MLF import Task_mlf,minimum_laxity_first
from DMA import Task_dma,deadline_monotonic_assignment
from rma import Task_rma,rate_monotonic_assignment
from FIFO import Task,fifo_algorithm
from algorithms.ProducerConsumer import ProducerThread,ConsumerThread,result3
window = Tk()
window.title("Advanced OS Algorithms")
window.geometry("1000x800")
background_image = PhotoImage(file="img.png")

# Create a label widget and set the image as the background
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


def shortest_seek_time_first_algorithm():
    requests_str = requests_entry.get()
    head_str = head_entry.get()
    disk_size_str = disk_size_entry.get()
    requests = list(map(int, requests_str.split()))
    head = int(head_str)
    disk_size = int(disk_size_str)
    seek_count, sequence= shortest_seek_time_first(requests, head, disk_size)
    result_label.config(text="Total Access Time: {}\nSeek Sequence: {}".format(seek_count, sequence),fg="blue")
    
def FCFS_algorithm():
    requests_str = requests_entry.get()
    head_str = head_entry.get()
    requests = list(map(int, requests_str.split()))
    head = int(head_str)
    seek_count, sequence= FCFS(requests, head)
    result_label.config(text="Total Access Time: {}\nSeek Sequence: {}".format(seek_count, sequence),fg="blue")
    

def SCAN_algorithm():
    requests_str = requests_entry.get()
    head_str = head_entry.get()
    disk_size_str = disk_size_entry.get()
    requests = list(map(int, requests_str.split()))
    head = int(head_str)
    disk_size = int(disk_size_str)
    direction=direction_entry.get()
    seek_count, sequence= SCAN(requests, head, disk_size,direction)
    result_label.config(text="Total Access Time: {}\nSeek Sequence: {}".format(seek_count, sequence),fg="blue")
    
def LOCK_algorithm():
    requests_str = requests_entry.get()
    head_str = head_entry.get()
    requests = list(map(int, requests_str.split()))
    head = int(head_str)
    direction=direction_entry.get()
    seek_count, sequence= LOCK(requests, head,direction)
    result_label.config(text="Total Access Time: {}\nSeek Sequence: {}".format(seek_count, sequence),fg="blue")

def C_LOCK_algorithm():
    requests_str = requests_entry.get()
    head_str = head_entry.get()
    requests = list(map(int, requests_str.split()))
    head = int(head_str)
    seek_count, sequence= c_lock(requests, head)
    result_label.config(text="Total Access Time: {}\nSeek Sequence: {}".format(seek_count, sequence),fg="blue")
    
def C_SCAN_algorithm():
    requests_str = requests_entry.get()
    head_str = head_entry.get()
    disk_size_str = disk_size_entry.get()
    disk_size = int(disk_size_str)
    requests = list(map(int, requests_str.split()))
    head = int(head_str)
    seek_count, sequence= c_scan(requests, head,disk_size)
    result_label.config(text="Total Access Time: {}\nSeek Sequence: {}".format(seek_count, sequence),fg="blue")
    
###############chapter4###################
tasks = []

def run_scheduler():
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
    total_time = int(total_time_entry.get())
    executed_tasks, total_execution_time=earliest_deadline_first(tasks, total_time)
    edf_label.config(text="Scheduling: " + " -> ".join([task.name for task in executed_tasks]),fg="blue")
    
#mlf
tasks_mlf = []
def run_scheduler_mlf():
    name = name_entry.get()
    name=list(name.split())
    arrival_time_str = arrival_time_entry.get()
    arrival_time = list(map(int, arrival_time_str.split()))
    deadline_str = deadline_entry.get()
    deadline = list(map(int, deadline_str.split()))
    execution_time_str = execution_time_entry.get()
    excution_time=list(map(int, execution_time_str.split()))
    for i in range(3):
        tasks_mlf.append(Task_mlf(name[i], arrival_time[i], deadline[i], excution_time[i]))

    total_time = int(total_time_entry.get())
    executed_tasks, total_execution_time=minimum_laxity_first(tasks_mlf, total_time)
    mlf_label.config(text="Scheduling: " + " -> ".join([task.name for task in executed_tasks]),fg="blue")
#dma
tasks_dma=[]
def run_scheduler_dma():
    name = name_entry.get()
    name=list(name.split())
    period_str = period.get()
    period = list(map(int, period_str.split()))
    deadline_str = deadline_entry.get()
    deadline = list(map(int, deadline_str.split()))
    execution_time_str = execution_time_entry.get()
    excution_time=list(map(int, execution_time_str.split()))
    for i in range(3):
        tasks_dma.append(Task_dma(name[i], period[i], deadline[i], excution_time[i]))
    total_time_str = total_time_entry.get()
    total_time=int(total_time_str)
    deadline_monotonic_assignment(tasks_dma, total_time)
    
##rma 
tasks_rma = []
total_time = 0
def run_scheduler_rma():
    global tasks_rma, total_time
    name_str = name_entry.get()
    name = list(name_str.split())

    period_str = period_entry.get()
    period = list(map(int, period_str.split()))

    exec_time_str = execution_time_entry.get()
    execution_time = list(map(int, exec_time_str.split()))

    for i in range(len(tasks_rma)):
        tasks_rma.append(Task_rma(name[i], period[i], execution_time[i]))

    total_time = int(total_time_entry.get())
    executed_tasks = rate_monotonic_assignment(tasks_rma, total_time)

    if not executed_tasks:
        edf_label.config(text="No task available",fg='blue')
    else:
        result = [f"[{task.next_deadline}] Executing task {task.name}" for task in executed_tasks]
        edf_label.config(text="\n".join(result),fg='blue')



# FIFO algorithm
tasks_fifo = []
def run_scheduler_fifo():
    name = name_entry.get()
    name=list(name.split())
    arrival_time_str = arrival_time_entry.get()
    arrival_time = list(map(int, arrival_time_str.split()))
    deadline_str = deadline_entry.get()
    deadline = list(map(int, deadline_str.split()))
    execution_time_str = execution_time_entry.get()
    excution_time=list(map(int, execution_time_str.split()))
    period_str = period_entry.get()
    period_time=list(map(int, period_str.split()))
    for i in range(len(tasks_fifo)):
        tasks_fifo.append(Task(name[i], arrival_time[i],excution_time[i],period_time[i],deadline[i]))
    total_time = int(total_time_entry.get())
    final=fifo_algorithm(tasks, total_time)
    edf_label.config(text='\n'.join(final), fg="blue")

    


# Create a new button for the FIFO algorithm
run_button_fifo = Button(window, text="Run FIFO", command=run_scheduler_fifo, font=("Times New Roman", 12))
run_button_fifo.grid(row=13, column=2)

# Create a label to display the FIFO results
result2_label = Label(window, text="Result:", font=("Times New Roman", 18, "bold"))
result2_label.grid(row=14, column=2)

    
#####################chapter 1 ###########################3
#ProducerConsumer(Semaphores)
def producer_consumer():
    producer_thread = ProducerThread()
    consumer_thread = ConsumerThread()
    producer_thread.start()
    consumer_thread.start()

    # Wait for both threads to finish executing
    producer_thread.join()
    consumer_thread.join()

    # Update the GUI label with the results
    result3_label.config(text="\n".join(result3), fg="blue")
    


#labels and entry
ch2_label=Label(window, text="Disk scheduling Algorithms", font=("Arial", 20, "bold"))
ch2_label.grid(row=0,column=2)
requests_label = Label(window, text="Enter the requests (separated by space):",font=("Times New Roman", 12))
requests_label.grid(row=1,column=0)
requests_entry = Entry(window)
requests_entry.grid(row=1,column=1)

head_label = Label(window, text="Enter the current head position:",font=("Times New Roman", 12))
head_label.grid(row=1,column=2)
head_entry = Entry(window)
head_entry.grid(row=1,column=3)

disk_size_label = Label(window, text="Enter the disk size:",font=("Times New Roman", 12))
disk_size_label.grid(row=2,column=0)
disk_size_entry = Entry(window)
disk_size_entry.grid(row=2,column=1)

direction_label = Label(window, text="Enter the direction:",font=("Times New Roman", 12))
direction_label.grid(row=2,column=2)
direction_entry = Entry(window)
direction_entry.grid(row=2,column=3)


#Algorithms Buttons
# create a Combobox with some choices
choices = ["FCFS", "SSTF", "SCAN","LOCK","C_SCAN","C_LOCK"]
choice_var = StringVar()
choice_combobox = ttk.Combobox(window, textvariable=choice_var, values=choices)
choice_combobox.grid(row=4,column=2)

# define a function to perform the action
def perform_action():
    selected_choice = choice_var.get()
    if selected_choice == "FCFS":
        FCFS_algorithm()
    elif selected_choice == "SSTF":
        shortest_seek_time_first_algorithm()
    elif selected_choice == "SCAN":
        SCAN_algorithm()
    elif selected_choice == "LOCK":
        LOCK_algorithm()
    elif selected_choice == "C_SCAN":
        C_SCAN_algorithm()
    elif selected_choice == "C_LOCK":
        C_LOCK_algorithm()

# create a button to trigger the action
action_button = Button(window, text="Run Scheduler", command=perform_action)
action_button.grid(row=5,column=2)
# pack the widgets into the window
#result_label
result_label = Label(window, text="Result:",font=("Times New Roman", 18,"bold"))
result_label.grid(row=6,column=2)

###scheduling labels########
ch3_label=Label(window, text="RTOS scheduling Algorithms", font=("Arial", 20, "bold"))
ch3_label.grid(row=7,column=2)


name_label = Label(window, text="Task Name:",font=("Times New Roman", 12))
name_label.grid(row=9,column=0)

name_entry = Entry(window,font=("Times New Roman", 12))
name_entry.grid(row=9,column=1)

arrival_time_label = Label(window, text="Arrival Time:",font=("Times New Roman", 12))
arrival_time_label.grid(row=10,column=0)

arrival_time_entry = Entry(window,font=("Times New Roman", 12))
arrival_time_entry.grid(row=10,column=1)

deadline_label = Label(window, text="Deadline:",font=("Times New Roman", 12))
deadline_label.grid(row=11,column=0)

deadline_entry = Entry(window,font=("Times New Roman", 12))
deadline_entry.grid(row=11,column=1)

execution_time_label= Label(window, text="Execution Time:",font=("Times New Roman", 12))
execution_time_label.grid(row=12,column=0)

execution_time_entry = Entry(window,font=("Times New Roman", 12))
execution_time_entry.grid(row=12,column=1)


total_time_label = Label(window, text="Total Time:",font=("Times New Roman", 12))
total_time_label.grid(row=14,column=0)

total_time_entry = Entry(window)
total_time_entry.grid(row=14,column=1)

period_label = Label(window, text="period:",font=("Times New Roman", 12))
period_label.grid(row=13,column=0)

period_entry = Entry(window, font=("Times New Roman", 12))
period_entry.grid(row=13,column=1)

#Algorithms Buttons
# create a Combobox with some choices
choices2 = ["FIFO", "RR", "EDF","MFA","RMA","DMA"]
choice_var2 = StringVar()
choice_combobox2 = ttk.Combobox(window, textvariable=choice_var2, values=choices2)
choice_combobox2.grid(row=12,column=2)

# define a function to perform the action
def perform_action2():
    selected_choice = choice_var2.get()
    if selected_choice == "FIFO":
        run_scheduler_fifo()
    elif selected_choice == "RR":
        run_scheduler_rr()
    elif selected_choice == "EDF":
        run_scheduler()
    elif selected_choice == "MLF":
        run_scheduler_mlf()
    elif selected_choice == "RMA":
        run_scheduler_rma()
    elif selected_choice == "DMA":
        run_scheduler_dma()

run_button2 = Button(window, text="Run Scheduler", command=perform_action2,font=("Times New Roman", 12))
run_button2.grid(row=13,column=2)

#EDF
result2_label=Label(window, text="Result",font=("Times New Roman", 18,"bold"))
result2_label.grid(row=14, column=2)


edf_label = Label(window, text="")
edf_label.grid(row=15, column=2, columnspan=4)


#MLF

mlf_label = Label(window, text="")
mlf_label.grid(row=15, column=2, columnspan=4)

## dma

dma_label = Label(window, text="")
dma_label.grid(row=15, column=2, columnspan=4)


### rma

rma_label = Label(window, text="")
rma_label.grid(row=15, column=2, columnspan=4)

#############################chapter 1###########################

ch1_label=Label(window, text="Locking Mechanisms", font=("Arial", 20, "bold"))
ch1_label.grid(row=0,column=25)

# create a Combobox with some choices
choices3 = ["Test and Set", "Wait and signal", "Semaphores"]
choice_var3 = StringVar()
choice_combobox3 = ttk.Combobox(window, textvariable=choice_var3, values=choices3)
choice_combobox3.grid(row=4,column=25)

# define a function to perform the action
def perform_action3():
    selected_choice = choice_var3.get()
    if selected_choice == "Test and Set":
        test_set()
    elif selected_choice == "Wait and signal":
        wait_signal()
    elif selected_choice == "Semaphores":
        producer_consumer()

run_button3 = Button(window, text="Run Scheduler", command=perform_action3,font=("Times New Roman", 12))
run_button3.grid(row=5,column=25)

result3_label = Label(window, text="", font=("Times New Roman", 12))
result3_label.grid(row=6, column=25, columnspan=4)


window.mainloop()
