class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []

        for a in asteroids:
            alive = True
            while alive and stk and a < 0 < stk[-1]:
                if stk[-1] < abs(a):
                    stk.pop()
                else:
                    if stk[-1] == abs(a):
                        stk.pop()
                    alive = False

            if alive:
                stk.append(a)

        return stk

