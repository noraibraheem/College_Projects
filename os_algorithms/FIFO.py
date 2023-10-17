import time
class Task:
    def __init__(self, description,ARV, EX,PR,DL):
        self.description = description
        self.ARV=ARV
        self.ex = EX
        self.pr=PR
        self.dl=DL

    def execute(self):
        start_time = time.time()
        final.append(f"Executing task: {self.description} at time {EX_time:.1f}")
        time.sleep(self.ex)
        end_time = time.time() 
        task_finish =  end_time - start_time
        return task_finish

# Example usage:
EX_time=0
tasks = []
rounds = []
final=[]
# Taking input from the user for adding tasks
def fifo_algorithm(tasks,Total):
    global EX_time
    for task in tasks:  
        ti=int(Total/task.pr)
        rounds.append(ti)

    I=0
    for _ in range(len(rounds)):
        ARVt=tasks[I].ARV
        for i in range(rounds[I]):
            descriptiont = tasks[I].description
            ARVt += tasks[I].pr
            EXt = tasks[I].ex
            PRt = tasks[I].pr
            DLt = tasks[I].dl
            tasks.append(Task(descriptiont,ARVt,EXt,PRt,DLt))
        I+=1
    Sorted_tasks=sorted(tasks, key=lambda x: x.ARV)

    # Displaying the tasks in the order they are executed
    for task in Sorted_tasks:

        # in the case of idel resource
        while(EX_time<task.ARV):
                time.sleep(1)
                EX_time+=1
                
        ex_time =task.execute()
        EX_time += ex_time
        if ((EX_time-task.ARV)>task.dl):
                broke=EX_time-(EX_time - (task.ARV+task.dl))
                final.append(f"Deadline broke for: {task.description} at time {broke:.1f}")

        final.append(f"Task: {task.description} finished at time {EX_time:.1f}")
        
    return final
    


        


    
    
