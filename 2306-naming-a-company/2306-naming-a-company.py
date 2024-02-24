class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        h = defaultdict(set)
        for i in ideas:
            h[i[0]].add(i[1:])
        groups = list(h.items())
        # print(groups, type(groups))
        # print(groups[0][1], type(groups))
        res = 0
        for i in range(len(groups)-1):
            for j in range(i+1, len(groups)):
                set1, set2 = groups[i][1], groups[j][1]
                interection = len(set1 & set2)
                distinct1 = len(set1) - (interection)
                distinct2 = len(set2) - interection
                res += (2 * distinct1 * distinct2)
        return res


