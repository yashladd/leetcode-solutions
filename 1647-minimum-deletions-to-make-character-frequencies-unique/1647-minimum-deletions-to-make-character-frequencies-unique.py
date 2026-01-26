class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Calculates the minimum number of character deletions to make frequencies unique.

        The algorithm uses a greedy approach by tracking seen frequencies in a set. 
        If a frequency conflict is found, it decrements the count until it finds 
        a unique value or reaches zero.

        Time Complexity: O(n + k^2)
            - O(n): Building the initial frequency map where n is the length of string 's'.
            - O(k^2): The outer loop runs for at most k unique characters (k = 26).
            - The inner 'while' loop also runs at most k times for each character, because
            there are only k possible unique frequency slots to fill above zero. 
            Even if n is very large, the frequency adjustments are strictly limited 
            by the number of distinct characters in the alphabet.
            - Overall, since k is constant (26), this is effectively O(n).

        Space Complexity: O(k)
            - To store the frequency counter and the 'seen' set, both of which 
            contain at most k elements (26).

        Args:
            s (str): The input string.
        Returns:
            int: Total number of deletions required.
        """
        f = Counter(s)
        seen = set()
        dels = 0
        for val in f.values():
            while val > 0 and val in seen:
                val -= 1
                dels += 1
            seen.add(val)
        return dels
        