from heapq import heappush, heappop

class Task_mlf:
    def __init__(self, name, arrival_time, deadline, execution_time):
        self.name = name
        self.arrival_time = arrival_time
        self.deadline = deadline
        self.execution_time = execution_time
        self.period = deadline - arrival_time
        self.slack_time = self.period - self.execution_time
        self.priority = self.slack_time
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def execute(self, current_time):
        print(f"[{current_time}] Executing task {self.name}")
    
    def is_deadline_missed(self, current_time):
        return current_time > self.deadline

def minimum_laxity_first(tasks, total_time):
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
        executed_tasks.append(current_task.execute(current_time))
        
        if current_task.is_deadline_missed(current_time):
            return f"[{current_time}] Deadline missed for task {current_task.name}"
        else:
            current_task.slack_time = current_task.period - (current_time + current_task.execution_time - current_task.arrival_time)
            current_task.priority = current_task.slack_time
            heappush(ready_queue, current_task)
        
        current_time += 1
    return executed_tasks, total_time



