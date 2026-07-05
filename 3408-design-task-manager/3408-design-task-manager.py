class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_queue = []
        self.task_priority = {}
        self.task_user = {} 
        
        for u_id, t_id, priority in tasks:
            heappush(self.task_queue, (-priority, -t_id, u_id))
            self.task_priority[t_id] = priority
            self.task_user[t_id] = u_id 

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.task_queue, (-priority, -taskId, userId))
        self.task_priority[taskId] = priority
        self.task_user[taskId] = userId 

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_priority[taskId] = newPriority
        userId = self.task_user[taskId]
        heappush(self.task_queue, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        # Instead of a soft-delete set, just wipe it from our active dictionaries
        if taskId in self.task_priority:
            del self.task_priority[taskId]
            del self.task_user[taskId]

    def execTop(self) -> int:
        while self.task_queue:
            neg_priority, neg_taskId, userId = self.task_queue[0]
            taskId = -neg_taskId
            priority = -neg_priority
            
            # 1. Has the task been removed or executed already?
            if taskId not in self.task_priority:
                heappop(self.task_queue)
                continue
            
            # 2. Is this a stale heap entry? (e.g., Priority or User changed)
            if priority != self.task_priority[taskId] or userId != self.task_user[taskId]:
                heappop(self.task_queue)
                continue
                
            # If it passes both checks, it's our valid top task!
            heappop(self.task_queue)
            del self.task_priority[taskId]
            del self.task_user[taskId]
            
            return userId
            
        return -1