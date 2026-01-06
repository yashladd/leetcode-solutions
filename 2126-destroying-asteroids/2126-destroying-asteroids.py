class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        a = sorted(asteroids)
        m = mass
        for c in a:
            if m < c:
                return False
            m += c
        
        return True
        