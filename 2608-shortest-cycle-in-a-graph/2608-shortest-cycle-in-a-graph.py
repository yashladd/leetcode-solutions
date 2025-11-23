from collections import deque

class Solution:
    def findShortestCycle(self, n: int, edges: list[list[int]]) -> int:
        # 1. Build Adjacency List
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        min_cycle = float('inf')
        
        # 2. Run BFS from every node
        for start_node in range(n):
            # Initialize distance array for this BFS run
            dist = [-1] * n
            dist[start_node] = 0
            
            # Queue for BFS: (current_node, parent_node)
            # We track parent to ensure we don't just go back up the edge we came from
            queue = deque([(start_node, -1)])
            
            while queue:
                u, parent = queue.popleft()
                
                for v in adj[u]:
                    if dist[v] == -1:
                        # Neighbor not visited: record distance and push to queue
                        dist[v] = dist[u] + 1
                        queue.append((v, u))
                    elif v != parent:
                        # Neighbor visited and NOT parent: Cycle detected!
                        # Calculate cycle length and update minimum
                        cycle_len = dist[u] + dist[v] + 1
                        min_cycle = min(min_cycle, cycle_len)
        
        return min_cycle if min_cycle != float('inf') else -1