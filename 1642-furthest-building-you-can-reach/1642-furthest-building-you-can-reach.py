class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        h = []
        def push(x):
            heappush(h, -x)
        def pop():
            return -heappop(h)
        for i in range(1, n):
            if heights[i] > heights[i-1]:
                reqBricks = heights[i] - heights[i-1]
                # Use these many bricks
                push(reqBricks)
                bricks -= reqBricks
                # Dont have enough! -> go back (including this index) 
                # and replace bricks -> ladders
                while ladders > 0 and len(h) and bricks < 0:
                    bricks += pop()
                    ladders -= 1
                if bricks < 0:
                    # we can reach only previous index range(1, n)
                    return i-1

        return n-1



                