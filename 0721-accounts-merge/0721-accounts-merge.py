class DS:
    def __init__(self, n):
        self.par = [0] * (n + 1)
        for i in range(n + 1):
            self.par[i] = i
        self.size = [1] * (n + 1)
    
    def find(self, node):
        if node == self.par[node]:
            return node
        self.par[node] = self.find(self.par[node])
        return self.par[node]
    
    def union(self, u, v):
        up_u, up_v = self.find(u), self.find(v)
        if up_u == up_v:
            return 
        if self.size[up_u] < self.size[up_v]:
            self.par[up_u] = up_v
            self.size[up_v] += self.size[up_u]
        else:
            self.par[up_v] = up_u
            self.size[up_u] += self.size[up_v]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        ds = DS(n)
        
        mailToIdx = {}
        for i in range(n):
            for mail in accounts[i][1:]:
                if mail not in mailToIdx:
                    mailToIdx[mail]  = i
                else:
                    ds.union(i, mailToIdx[mail])
                    
        mergedMails = [[] for _ in range(n)]
        
        for mail, idx in mailToIdx.items():
            i = ds.find(idx)
            mergedMails[i].append(mail)
            
            
        res = []
        for idx, mails in enumerate(mergedMails):
            if not len(mails):
                continue
            res.append([accounts[idx][0]] + sorted(mergedMails[idx]))
        
        return res