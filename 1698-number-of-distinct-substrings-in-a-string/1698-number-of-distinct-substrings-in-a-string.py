class Node:
    def __init__(self):
        self.ch = {}

class Solution:
    def countDistinct(self, s: str) -> int:
        root = Node() # This stays as the anchor
        cnt = 0
        
        for i in range(len(s)):
            curr = root
            for j in range(i, len(s)):
                char = s[j]
                if char not in curr.ch:
                    curr.ch[char] = Node()
                    cnt += 1
                curr = curr.ch[char]
        return cnt
        