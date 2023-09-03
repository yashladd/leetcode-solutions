#User function Template for python3

from typing import List
from queue import Queue
class Solution:
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V: int, adj: List[List[int]]) -> List[int]:
        # code here
        from collections import deque
        q = deque([0])
        vis = {}
        vis[0] = 1
        res= []
        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                res.append(node)
                for nei in adj[node]:
                    if nei not in vis:
                        q.append(nei)
                        vis[nei] = 1
        return res
                
        


#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends