import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        # Sort courses by deadline (lastDay)
        courses.sort(key=lambda x: x[1])
        
        max_heap = []
        current_total_time = 0
        
        for duration, last_day in courses:
            # Try adding the current course
            current_total_time += duration
            heapq.heappush(max_heap, -duration) # Negative for max-heap
            
            # If we exceed the deadline, remove the longest course taken so far
            if current_total_time > last_day:
                longest_duration = -heapq.heappop(max_heap)
                current_total_time -= longest_duration
                
        return len(max_heap)