class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        N = len(cars)
        stk = []
        res = [-1] * N
        # Store indixes in stack
       
        for i in range(N-1, -1, -1):
            # First we need to pop all cars which have SPEED >= my speed they will never collide
            while stk and cars[stk[-1]][1] >= cars[i][1]:
                stk.pop()

            while stk:
                collisionTime = (cars[stk[-1]][0] - cars[i][0]) / (cars[i][1] - cars[stk[-1]][1])

                if res[stk[-1]] == -1 or collisionTime <= res[stk[-1]]:
                    res[i] = (collisionTime)
                    break
                
                stk.pop()

            stk.append(i)

        return res