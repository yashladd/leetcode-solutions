class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        tf = defaultdict(int)
        for ch in s1:
            tf[ch] += 1
        sf = defaultdict(int)
        l  = 0
        def check(tf, sf):
            for k, v in tf.items():
                if k not in sf or sf[k] != v:
                    return False
            return True
        for r in range(len(s2)):
            sf[s2[r]] += 1
            print(sf)
            if r >= len(s1):
                sf[s2[l]] -= 1
                if not sf[s2[l]]:
                    del sf[s2[l]]
                l += 1
            if check(tf, sf):
                return True

        return False

        