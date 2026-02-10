class Solution(object):
    def canVisitAllRooms(self, rooms):
        seen = [False] * len(rooms)
        seen[0] = True
        def dfs(room):
            seen[room] = True
            for key in rooms[room]:
                if not seen[key]:
                    dfs(key)
        dfs(0)
        return all(seen)