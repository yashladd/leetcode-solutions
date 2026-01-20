class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(graph)
        def f(node, cur):
            nonlocal res, n
            # print(node, cur)
            if node == n-1:
                tmp = cur + [n-1]
                res.append(tmp)
                return 

            for nei in graph[node]:
                f(nei, cur + [node])

        f(0, [])
        return res



        