class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        vocab = set(wordDict)
        
        # dp[i] will store a list of valid starting indices that can form a word ending at i
        dp = [[] for _ in range(N + 1)]
        
        # Base case: to show that index 0 is a valid starting point
        dp[0] = [-1] 

        # 1. Forward DP to build the parent pointers
        for end_idx in range(1, N + 1):
            for start_idx in range(end_idx):
                # If start_idx is reachable AND the substring is a valid word
                if dp[start_idx] and s[start_idx:end_idx] in vocab:
                    dp[end_idx].append(start_idx)
        
        # If the end of the string is completely unreachable, bail out early
        if not dp[N]:
            return []
            
        res = []
        
        # 2. Backtrack from the end using our stored pointers
        def backtrack(end_idx, current_path):
            if end_idx == 0:
                # We reached the start! Reverse the path and join it
                res.append(" ".join(current_path[::-1]))
                return
            
            for start_idx in dp[end_idx]:
                word = s[start_idx:end_idx]
                current_path.append(word)       # Choose
                backtrack(start_idx, current_path) # Explore
                current_path.pop()              # Un-choose (backtrack)
        
        backtrack(N, [])
        return res