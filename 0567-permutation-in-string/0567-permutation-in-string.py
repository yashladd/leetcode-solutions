class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1f = Counter(s1)

        s1_len = len(s1)

        matches = 0
        required = len(s1f)
        state = defaultdict(int)
        for r, ch in enumerate(s2):
            
            state[ch] += 1

            if ch in s1f and state[ch] == s1f[ch]:
                matches += 1

            

            if r >= s1_len:
                prev_char = s2[r-s1_len]
                state[prev_char] -= 1
                if prev_char in s1f and state[prev_char]== s1f[prev_char] - 1:
                    matches -= 1

            if matches == required:
                return True


        return True if required == matches else False



 
        