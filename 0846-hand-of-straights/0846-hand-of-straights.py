class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize: return False
        h = defaultdict(int)
        for i in hand:
            h[i] += 1
        q = list(h.keys())
        heapq.heapify(q)
        while q:
            nex = q[0]
            for i in range(groupSize):
                if h[nex] == 0:
                    return False
                h[nex] -= 1
                if h[nex] == 0:
                    if nex != q[0]:
                        return False
                    heappop(q)
                nex += 1
        return True
        
        
        
        