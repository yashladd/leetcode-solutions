class DisjointSet(object):
    def __init__(self, n) -> None:
        self.rank = [0] * (n+1)
        self.parent = []
        for i in range(n+1):
            self.parent.append(i)
        self.size = [1] * (n + 1)

    def findUParent(self, node):
        if node == self.parent[node]:
            return node
        self.parent[node] = self.findUParent(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ultp_u = self.findUParent(u)
        ultp_v = self.findUParent(v)
        if ultp_u == ultp_v:
            return

        if self.rank[ultp_u] < self.rank[ultp_v]:
            self.parent[ultp_u] = ultp_v 
        elif self.rank[ultp_v] < self.rank[ultp_u]:
            self.parent[ultp_v] = ultp_u
        # Equal ranks
        else: 
            self.parent[ultp_u] = ultp_v
            self.rank[ultp_u] += 1

    def unionBySize(self, u, v):
        ultp_u = self.findUParent(u)
        ultp_v = self.findUParent(v)
        if ultp_u == ultp_v:
            return

        if self.size[ultp_u] < self.size[ultp_v]:
            self.parent[ultp_u] = ultp_v
            self.size[ultp_v] += self.size[ultp_u]
        else:
            self.parent[ultp_v] = ultp_u
            self.size[ultp_u] += self.size[ultp_v]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        mailMap = {}
        ds = DisjointSet(n)
        for i in range(n):
            for mail in accounts[i][1:]:
                if mail not in mailMap:
                    mailMap[mail] = i
                else:
                    ds.unionBySize(i, mailMap[mail])
                    continue
        
        merged = [[] for _ in range(n)]
        print(mailMap)
        for mail, i in mailMap.items():
            par = ds.findUParent(i)
            merged[par].append(mail)
                
        ans = []
        for i, emails in enumerate(merged):
            if not len(emails):
                continue
            ans.append([accounts[i][0]] + sorted(emails))
            
        return ans
