class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (u, v), val in zip(equations, values):
            graph[u][v] = val
            graph[v][u] = 1.0 / val
        
        # Step 2: Define the DFS function
        def dfs(curr, target, visited):
            # If the variable isn't in our graph, it's undefined
            if curr not in graph or target not in graph:
                return -1.0
            
            # Found the destination
            if curr == target:
                return 1.0
            
            visited.add(curr)
            
            # Explore neighbors
            for neighbor, weight in graph[curr].items():
                if neighbor not in visited:
                    product = dfs(neighbor, target, visited)
                    if product != -1.0:
                        return weight * product
            
            return -1.0

        # Step 3: Process each query
        results = []
        for start, end in queries:
            results.append(dfs(start, end, set()))
            
        return results