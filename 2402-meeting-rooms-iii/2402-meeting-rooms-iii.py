class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        occupied = []
        count = [0] * n
        # Min Heap of available rooms 
        # No need to heapify as it already a sorted array 
        available = [i for i in range(n)] 
        for s, e in meetings:
            while occupied and occupied[0][0] <= s:
                end, room = heappop(occupied)
                heappush(available, room)
            if len(occupied) == n:
                end, room = heappop(occupied)
                heappush(occupied, ( end + (e-s) , room))
                count[room] += 1
            else:
                # USE AIVAILABLE 
                room = heappop(available)
                heappush(occupied, (e, room))
                count[room] += 1
                
        return count.index(max(count))





            

        