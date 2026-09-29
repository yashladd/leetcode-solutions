class Ds:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.sz = [1] * n

    def find(self, u):
        if self.par[u] == u:
            return self.par[u]
        self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self, u, v):
        u_p, v_p = self.find(u), self.find(v)

        if u_p == v_p:
            return False

        if self.sz[u_p] > self.sz[v_p]:
            u_p, v_p = v_p, u_p

        self.par[v_p] = u_p
        self.sz[u_p] += self.sz[v_p]

        return True



class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:

        mail_index = {}

        N = len(accounts)

        ds = Ds(N)

        for i in range(N):
            for email in accounts[i][1:]:
                if email not in mail_index:
                    mail_index[email] = i
                else:
                    ds.union(i, mail_index[email])


        index_to_emails = defaultdict(set)
        for i in range(N):
            p_i = ds.find(i)
            name = accounts[p_i][0]
            for email in accounts[i][1:]:
                index_to_emails[p_i].add(email)

        res = []
        for index, emails in index_to_emails.items():
            row = [accounts[index][0]]
            row.extend(sorted(emails))
            res.append(row)

        return res

        