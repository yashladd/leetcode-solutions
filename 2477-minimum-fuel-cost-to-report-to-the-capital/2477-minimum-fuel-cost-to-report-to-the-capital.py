class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        from collections import defaultdict
        
        # 1. Build the adjacency list
        graph = defaultdict(list)
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
            
        total_fuel = 0
        
        # 2. Define the post-order DFS
        def dfs(node, parent):
            nonlocal total_fuel
            passengers = 1  # Start with the representative of the current city
            
            for neighbor in graph[node]:
                if neighbor != parent:
                    # Get the total passengers from the child subtree
                    p = dfs(neighbor, node)
                    
                    # Calculate fuel for the edge connecting neighbor to node
                    # (p + seats - 1) // seats is a neat trick for ceiling division with integers
                    total_fuel += (p + seats - 1) // seats
                    
                    # Accumulate the passengers to pass up to the parent
                    passengers += p
                    
            return passengers
            
        # 3. Start traversal from the capital (0) with a dummy parent (-1)
        dfs(0, -1)
        
        return total_fuel