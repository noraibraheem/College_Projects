from heapq import heappush, heappop

class Task:
    def __init__(self, name, arrival_time, deadline, execution_time):
        self.name = name
        self.arrival_time = arrival_time
        self.deadline = deadline
        self.execution_time = execution_time
        self.priority = self.deadline
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def execute(self, current_time):
        print(f"[{current_time}] Executing task {self.name}")
    
    def is_deadline_missed(self, current_time):
        return current_time > self.deadline

def earliest_deadline_first(tasks, total_time):
    ready_queue = []
    current_time = 0
    executed_tasks=[]
    while current_time < total_time:
        for task in tasks:
            if task.arrival_time == current_time:
                heappush(ready_queue, task)
        
        if not ready_queue:
            print(f"[{current_time}] No task available")
            current_time += 1
            continue
        
        current_task = heappop(ready_queue)
        current_task.execute(current_time)
        executed_tasks.append(current_task)
        
        if current_task.is_deadline_missed(current_time):
            return None
        else:
            current_task.deadline += current_task.execution_time
            current_task.priority = int(current_task.deadline)
            heappush(ready_queue, current_task)
        
        current_time += 1
    return executed_tasks,total_time


