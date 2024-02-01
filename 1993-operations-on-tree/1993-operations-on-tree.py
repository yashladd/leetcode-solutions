class Node:
    def __init__(self, val, user=None, lock=False):
        self.val = val
        self.user = user
        self.lock = lock

class LockingTree:

    def __init__(self, parent: List[int]):
        state = [Node(i) for i in range(len(parent))]
        g = defaultdict(list)
        
        for i, v in enumerate(parent):
            if i != 0:
                g[state[v]].append(state[i]) 
        self.g = g
        self.state = state
        self.parent = parent
        
    def lock(self, num: int, user: int) -> bool:
        node = self.state[num]
        if node.lock == False:
            node.lock = True
            node.user = user
            return True
        else:
            return False
    
    def unlock(self, num: int, user: int) -> bool:
        node = self.state[num]
        if node.lock and node.user == user:
            node.lock = False
            node.user = None
            return True
        else:
            return False
        
    def upgrade(self, num: int, user: int) -> bool:
        if self.state[num].lock:
            return False
        
        def checkAnc(num):
            anc = self.parent[num]
            while anc != -1:
                currNode = self.state[anc]
                if currNode.lock:
                    return False
                anc = self.parent[anc]
            return True
        
        def dfs(node):
            for nei in self.g[node]:
                if nei.lock:
                    return True
                if dfs(nei):
                    return True
            return False
        
        def unlock(node):
            for nei in self.g[node]:
                nei.lock = False
                nei.user = None
                unlock(nei)
        
        if checkAnc(num) and dfs(self.state[num]):
            currNode = self.state[num]
            currNode.lock = True
            currNode.user = user
            unlock(currNode)
            return True
        else:
            return False
            
                
                    
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)