from dataclasses import dataclass
from typing import List
from heapq import heappush, heappop

@dataclass(frozen=True)
class TaskInfo:
    priority: int
    taskId: int
    userId: int

    # Custom comparison to force heapq to act like a Max-Heap
    def __lt__(self, other):
        # 1. Highest priority comes first
        if self.priority != other.priority:
            return self.priority > other.priority
        # 2. If priorities tie, highest taskId comes first
        return self.taskId > other.taskId

class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_queue = []
        self.task_info = {} 
        
        for u_id, t_id, priority in tasks:
            task = TaskInfo(priority=priority, taskId=t_id, userId=u_id)
            heappush(self.task_queue, task)
            self.task_info[t_id] = task

    def add(self, userId: int, taskId: int, priority: int) -> None:
        task = TaskInfo(priority=priority, taskId=taskId, userId=userId)
        heappush(self.task_queue, task)
        self.task_info[taskId] = task

    def edit(self, taskId: int, newPriority: int) -> None:
        old_task = self.task_info[taskId]
        
        # Create a new frozen instance with updated priority
        new_task = TaskInfo(priority=newPriority, taskId=taskId, userId=old_task.userId)
        
        self.task_info[taskId] = new_task
        heappush(self.task_queue, new_task)

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self) -> int:
        while self.task_queue:
            # We now just grab the entire object from the top of the heap
            top_task = self.task_queue[0]
            
            # 1. Does the task still exist in our active records?
            if top_task.taskId not in self.task_info:
                heappop(self.task_queue)
                continue
            
            # 2. Is this a stale heap entry? 
            # Because frozen dataclasses check equality by comparing all their fields,
            # we can just use `!=` to see if the heap task perfectly matches the active task.
            active_task = self.task_info[top_task.taskId]
            if top_task != active_task:
                heappop(self.task_queue)
                continue
                
            # Valid top task!
            heappop(self.task_queue)
            del self.task_info[top_task.taskId]
            
            return top_task.userId
            
        return -1