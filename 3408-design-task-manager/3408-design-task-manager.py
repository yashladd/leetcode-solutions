class TaskManager:
    def __init__(self, tasks: List[List[int]]):
        self.task_queue = []
        self.task_info = {} # Maps taskId -> (priority, userId)
        
        for u_id, t_id, priority in tasks:
            heappush(self.task_queue, (-priority, -t_id, u_id))
            self.task_info[t_id] = (priority, u_id)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heappush(self.task_queue, (-priority, -taskId, userId))
        self.task_info[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        # Fetch the existing userId
        _, userId = self.task_info[taskId]
        
        # Overwrite the dictionary key with a brand new tuple
        self.task_info[taskId] = (newPriority, userId)
        heappush(self.task_queue, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_info:
            del self.task_info[taskId]

    def execTop(self) -> int:
        while self.task_queue:
            neg_priority, neg_taskId, userId = self.task_queue[0]
            taskId = -neg_taskId
            priority = -neg_priority
            
            # 1. Does the task still exist?
            if taskId not in self.task_info:
                heappop(self.task_queue)
                continue
            
            # Unpack the current active state from our single dictionary
            active_priority, active_userId = self.task_info[taskId]
            
            # 2. Is this a stale heap entry?
            if priority != active_priority or userId != active_userId:
                heappop(self.task_queue)
                continue
                
            # Valid top task!
            heappop(self.task_queue)
            del self.task_info[taskId]
            
            return userId
            
        return -1