class RangeModule:
    def __init__(self):
        self.iv = SortedList()                      # sorted by (start, end)

    def addRange(self, left, right):
        lo = self.iv.bisect_left((left, -1))        # first interval with start >= left
        # walk left while it overlaps/touches
        while lo > 0 and self.iv[lo-1][1] >= left:
            lo -= 1
        # walk right while it overlaps/touches
        hi = lo
        new_l, new_r = left, right
        while hi < len(self.iv) and self.iv[hi][0] <= right:
            new_l = min(new_l, self.iv[hi][0])
            new_r = max(new_r, self.iv[hi][1])
            hi += 1
        del self.iv[lo:hi]
        self.iv.add((new_l, new_r))                 # O(√n) insert

    def removeRange(self, left, right):
        lo = self.iv.bisect_left((left, -1))
        while lo > 0 and self.iv[lo-1][1] > left:
            lo -= 1
        residues = []
        hi = lo
        while hi < len(self.iv) and self.iv[hi][0] < right:
            a, b = self.iv[hi]
            if a < left:  residues.append((a, left))
            if b > right: residues.append((right, b))
            hi += 1
        del self.iv[lo:hi]
        for r in residues: self.iv.add(r)           # O(√n) each

    def queryRange(self, left, right):
        i = self.iv.bisect_left((left, float('inf'))) - 1
        return i >= 0 and self.iv[i][0] <= left and self.iv[i][1] >= right