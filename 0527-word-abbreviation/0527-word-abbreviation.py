class Node:
    def __init__(self):
        self.edges = {}
        self.count = 0

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:

        root = defaultdict(lambda : Node())
        for word in words:
            curr = root[len(word)]
            for c in word[-1] + word[:-1]:
                if c not in curr.edges:
                    curr.edges[c] = Node()
                curr = curr.edges[c]
                curr.count += 1


        res = []
        for word in words:
            curr = root[len(word)]

            currRes = []
            curr = curr.edges[word[-1]]
            curr = curr.edges[word[0]]
            currRes.append(word[0])

            i = 1
            while curr.count > 1:
                curr = curr.edges[word[i]]
                currRes.append(word[i])
                i += 1

            remainingChars = len(word) - i - 1
            # // interval internal
            # // 8 - 5 - 1
            if remainingChars == 1:
                currRes.append(word[i])
            elif remainingChars > 1:
                currRes.append(str(remainingChars))
            currRes.append(word[-1])
            res.append("".join(currRes))

        return res