class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        q = deque(["0000"])
        steps = 0
        def generate(l):
            res = []
            for i, v in enumerate(l):
                if v == "0":
                    res.append(l[:i] + str(9) + l[i+1:])
                    res.append(l[:i] + str(1) + l[i+1:])
                elif v=="9":
                    res.append(l[:i] + str(0) + l[i+1:])
                    res.append(l[:i] + str(8) + l[i+1:])
                else:
                    res.append(l[:i] + str((int(v))+1) + l[i+1:])
                    res.append(l[:i] + str(int(v)-1) + l[i+1:])
            return res
        vis = set(deadends)
        vis.add("0000")
        while q:
            sz = len(q)
            for _ in range(sz):
                l = q.popleft()
                if l == target:
                    return steps
                nextSequences = generate(l)
                for seq in nextSequences:
                    if seq not in vis:
                        vis.add(seq)
                        q.append(seq)
            steps += 1
        return -1      
                    
                    
                    

        
        