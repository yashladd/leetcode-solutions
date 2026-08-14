import collections
import heapq

class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        # Edge case: If k is 0, any arrangement is valid, so return the original string
        if k == 0: 
            return s
        
        # 1. Count character frequencies
        freq = collections.Counter(s)
        
        # 2. Build a max heap (using negative frequencies for Python's min-heap)
        max_heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(max_heap)
        
        # 3. Queue to keep track of characters on "cooldown"
        # Stores tuples of: (remaining_negative_count, char, next_available_index)
        wait_queue = collections.deque() 
        res = []
        
        # 4. Process characters
        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)
            
            # Decrement absolute frequency (which means adding 1 to our negative count)
            count += 1 
            
            # If the character still has remaining occurrences, put it in the waiting queue
            if count < 0:
                # The next available index will be the index we just placed it at (len(res) - 1) + k
                wait_queue.append((count, char, len(res) - 1 + k))
            
            # Check if the character at the front of the queue is ready to be reused
            if wait_queue and wait_queue[0][2] == len(res):
                ready_count, ready_char, _ = wait_queue.popleft()
                heapq.heappush(max_heap, (ready_count, ready_char))
        
        # 5. If we placed all characters, return the string. Otherwise, return ""
        return "".join(res) if len(res) == len(s) else ""