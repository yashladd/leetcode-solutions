class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
    Time Complexity: O(N * 2^N)
        - In a Directed Acyclic Graph (DAG) with N nodes, the number of distinct paths
          from the source to the destination can be exponential.
        - In the worst-case scenario (where every node i connects to all nodes j > i),
          there are roughly 2^(N-2) paths.
        - For each valid path found, we take O(N) time to copy the path into the results list.
        - Therefore, the total time complexity is bounded by O(N * 2^N).
        - Note: Standard DFS is O(V+E) because it visits each node once. Here, we must
          re-visit nodes to discover all unique paths, leading to exponential behavior.

    Space Complexity: O(N * 2^N)
        - O(N) for the recursion stack (depth of the graph).
        - O(N * 2^N) to store the result list of all paths in the worst case.
        - If we use backtracking (mutating a single list), auxiliary space is O(N).
          If we create new lists at each step (cur + [node]), auxiliary space increases to O(N^2).
    """
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



        