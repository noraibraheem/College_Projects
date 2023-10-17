from heapq import heappush, heappop

final = []

class Task_rma:
    def __init__(self, name, period, execution_time):
        self.name = name
        self.period = period
        self.execution_time = execution_time
        self.next_deadline = period
        self.priority = int(1 / period)

    def __lt__(self, other):
        return self.priority > other.priority

    def execute(self, current_time):
        final.append(f"[{current_time}] Executing task {self.name}")
        self.next_deadline += self.period


def rate_monotonic_assignment(tasks, total_time):
    ready_queue = []
    executed_tasks = []
    for task in tasks:
        heappush(ready_queue, (task.next_deadline, task))
    
    for current_time in range(total_time):
        if not ready_queue:
            return [(current_time, "No task available")]
        
        _, current_task = heappop(ready_queue)
        current_task.execute(current_time)
        executed_tasks.append(current_task)

        heappush(ready_queue, (current_task.next_deadline, current_task))

    return executed_tasks