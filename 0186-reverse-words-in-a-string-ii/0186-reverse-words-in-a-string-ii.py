class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Helper function to reverse a portion of the array
        def reverse_portion(left, right):
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
        
        # Step 1: Reverse the entire list
        reverse_portion(0, len(s) - 1)
        
        # Step 2: Reverse each word individually
        start = 0
        for end in range(len(s)):
            # If we hit a space, reverse the word we just passed
            if s[end] == " ":
                reverse_portion(start, end - 1)
                start = end + 1
            # If we hit the end of the string, reverse the last word
            elif end == len(s) - 1:
                reverse_portion(start, end)