
from heapq import heappush, heappop
final= []
class Task_dma:
    def __init__(self, name, period, deadline, execution_time):
        self.name = name
        self.period = period
        self.deadline = deadline
        self.execution_time = execution_time
        self.priority = int(self.deadline)
    
    def __lt__(self, other):
        return self.priority > other.priority
    
    def execute(self, current_time):
        print(f"[{current_time}] Executing task {self.name}")
        final.append(f"[{current_time}] Executing task {self.name}")
    
    def next_deadline(self, current_time):
        return current_time + self.period

def deadline_monotonic_assignment(tasks, total_time):
    ready_queue = []
    executed_tasks=[]

    for task in tasks:
        heappush(ready_queue, (task.deadline, task))
    
    for current_time in range(total_time):
        if not ready_queue:
            return f"[{current_time}] No task available"
            
        
        _, current_task = heappop(ready_queue)
        current_task.execute(current_time)
        executed_tasks.append(current_task)
        
        heappush(ready_queue, (current_task.next_deadline(current_time), current_task))

        current_time+=1


    return [(current_time, task.name) for task in executed_tasks]



def DMA(input_gui,total_time):
    deadline_monotonic_assignment(input_gui,total_time)
    
    return final