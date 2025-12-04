class Solution:
    def countCollisions(self, directions: str) -> int:

        """
        RRL -> 3
        RRLLLL
        """
        q = deque(directions)

        while q and q[0] == "L":
            q.popleft()
        while q and q[-1] == "R":
            q.pop()

        return len(q) - q.count('S')
        