class Solution:
    def frequencySort(self, s: str) -> str:
        f = Counter(s)
        n = len(s)
        bucket = [[]for _ in range(n+1)]
        for ch, cnt in f.items():
            bucket[cnt].append(ch)

        res = ""
        for i in range(n, -1, -1):
            for ch in bucket[i]:
                res += (ch * i)
        return res
        