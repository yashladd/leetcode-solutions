from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        res = []
        # Queue stores the path taken so far
        queue = deque([[0]])
        
        while queue:
            path = queue.popleft()
            curr_node = path[-1]
            
            # If we reach the target (n-1), add the path to results
            if curr_node == n - 1:
                res.append(path)
                continue
            
            # Explore all neighbors and add new paths to the queue
            for neighbor in graph[curr_node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
        
        return res