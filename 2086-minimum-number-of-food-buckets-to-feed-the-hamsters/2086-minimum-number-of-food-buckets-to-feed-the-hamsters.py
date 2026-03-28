class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        n = len(hamsters)
        hamsters = list(hamsters) # Convert to list to "place" buckets
        buckets = 0
        
        for i in range(n):
            if hamsters[i] == 'H':
                # 1. Check if already fed by a bucket at i-1
                if i > 0 and hamsters[i-1] == 'B':
                    continue
                
                # 2. Try placing a bucket at i+1 (Greedy choice)
                if i + 1 < n and hamsters[i+1] == '.':
                    buckets += 1
                    hamsters[i+1] = 'B' # Mark as bucket
                # 3. Try placing a bucket at i-1
                elif i > 0 and hamsters[i-1] == '.':
                    buckets += 1
                    # No need to mark hamsters[i-1] as 'B' since we already passed it
                # 4. No possible placement
                else:
                    return -1
                    
        return buckets