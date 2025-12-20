class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        """

[

["E","E","E","E","E"],
["E","E","M","E","E"],
["E","E","E","E","E"],
["E","E","E","E","E"]], click = [3,0]


["B","1","E","1","B"],
["B","1","M","1","B"],
["B","1","1","1","B"],
["B","B","B","B","B"]

]
        """

        r, c = click
        N, M = len(board), len(board[0])

        if board[r][c] == "M":
            board[r][c] = "X"
            return board

        def inb(i, j):
            return i >= 0 and i < N and j >= 0 and j < M
        vis = set()

        def dfs(x, y):
            vis.add((x, y))
            cnt = 0
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                p, q = x + dx, y + dy
                if inb(p, q) and board[p][q] == "M":
                    cnt += 1
            board[x][y] = str(cnt) if cnt else "B"
            if cnt == 0:
                for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
                    p, q = x + dx, y + dy
                    if (inb(p, q)) and (p, q) not in vis:
                        dfs(p, q)

        # while queue:
        #     x, y = queue.popleft()
        #     c

        #     if cnt == 0:
        #         for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
        #             p, q = x + dx, y + dy
        #             if (inb(p, q)) and (p, q) not in vis:
        #                 queue.append((p, q))
        #                 vis.add((p, q))
        dfs(r, c)
        return board