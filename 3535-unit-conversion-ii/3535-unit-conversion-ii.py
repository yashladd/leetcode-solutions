class Solution:
    def queryConversions(self, conversions: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        
        # Helper for Modular Inverse using Fermat's Little Theorem
        # pow(a, b, m) computes (a^b) % m efficiently
        def get_inverse(n):
            return pow(n, MOD - 2, MOD)

        # 1. Build the Graph (Bidirectional)
        graph = defaultdict(list)
        for u, v, w in conversions:
            # u -> v with weight w
            graph[u].append((v, w))
            
            # v -> u with weight 1/w (modular inverse)
            w_inv = get_inverse(w)
            graph[v].append((u, w_inv))

        # 2. Precompute ratios from node 0 to all other nodes (BFS)
        # ratios[i] stores how many units of i equal 1 unit of 0
        ratios = {}
        ratios[0] = 1
        
        queue = deque([0])
        
        # Standard BFS to fill `ratios`
        # Since it's a tree with n nodes and n-1 edges, 
        # visiting every node once is sufficient.
        while queue:
            curr = queue.popleft()
            current_val = ratios[curr]
            
            for neighbor, weight in graph[curr]:
                if neighbor not in ratios:
                    # The value at neighbor is (value at curr) * (conversion weight)
                    ratios[neighbor] = (current_val * weight) % MOD
                    queue.append(neighbor)

        # 3. Answer Queries
        results = []
        for unitA, unitB in queries:
            if unitA not in ratios or unitB not in ratios:
                # This case shouldn't happen based on constraints, 
                # but good for safety.
                results.append(-1) 
                continue
                
            # We want: ratios[B] / ratios[A]
            # Which is: ratios[B] * inverse(ratios[A])
            valA = ratios[unitA]
            valB = ratios[unitB]
            
            ans = (valB * get_inverse(valA)) % MOD
            results.append(ans)
            
        return results