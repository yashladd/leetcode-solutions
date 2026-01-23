class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        # 1. DSU Implementation
        parent = list(range(max(nums) + 1))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x]) # Path compression
            return parent[x]
        
        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                parent[rootX] = rootY
        
        # 2. Iterate through numbers and union with prime factors
        for num in nums:
            temp = num
            d = 2
            # Prime factorization loop up to sqrt(num)
            while d * d <= temp:
                if temp % d == 0:
                    union(num, d) # Connect num to prime factor d
                    while temp % d == 0:
                        temp //= d # Remove this factor completely
                d += 1
            
            # If temp > 1, the remainder is a prime factor
            if temp > 1:
                union(num, temp)
        
        # 3. Count the size of components
        from collections import defaultdict
        group_count = defaultdict(int)
        max_size = 0
        
        for num in nums:
            root = find(num)
            group_count[root] += 1
            max_size = max(max_size, group_count[root])
            
        return max_size