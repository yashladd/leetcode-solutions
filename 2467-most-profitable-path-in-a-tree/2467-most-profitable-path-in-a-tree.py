import collections

class Solution:
    def mostProfitablePath(self, edges: list[list[int]], bob: int, amount: list[int]) -> int:
        n = len(amount)
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        # Step 1: DFS on Bob to find the time he reaches each node on the path to 0
        bob_map = {}
        visited = [False] * n

        def dfs_bob(curr, t):
            visited[curr] = True
            bob_map[curr] = t
            if curr == 0:
                return True
            
            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    if dfs_bob(neighbor, t + 1):
                        return True
            
            del bob_map[curr]
            return False

        dfs_bob(bob, 0)

        # Step 2: DFS on Alice to find the maximum net income to a leaf node
        self.alice_income = float('-inf')
        visited = [False] * n

        def dfs_alice(curr, t, income):
            visited[curr] = True
            
            # Logic for income at the current node based on Bob's arrival time
            if curr not in bob_map or t < bob_map[curr]:
                income += amount[curr]
            elif t == bob_map[curr]:
                income += amount[curr] // 2
            # if t > bob_map[curr], Alice gets nothing (income += 0)

            # Check if current node is a leaf (only one neighbor and not the root)
            if len(adj[curr]) == 1 and curr != 0:
                self.alice_income = max(self.alice_income, income)

            for neighbor in adj[curr]:
                if not visited[neighbor]:
                    dfs_alice(neighbor, t + 1, income)

        dfs_alice(0, 0, 0)

        return self.alice_income