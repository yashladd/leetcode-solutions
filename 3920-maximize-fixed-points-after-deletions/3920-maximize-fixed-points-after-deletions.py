import bisect

class Solution:
    """
    [9, 5, 0, 3, 1, 2] --> Dry run this example

    This is a brilliant problem that looks like dynamic programming at first glance but beautifully reduces into a classic algorithm pattern if you look at the math behind the array shifts.

Here is the intuition, the mathematical reduction, and the optimal approach to solve it.

### The Intuition

With constraints of $N \le 10^5$, an $O(N^2)$ DP approach will result in a Time Limit Exceeded (TLE) error. This points us toward an $O(N \log N)$ solution, which usually implies sorting + binary search or a Greedy approach.

Let's break down the mechanics of a "deletion":

1. **Shifting Left:** When you delete elements, the remaining elements shift to the left. This means an element's new index can only be less than or equal to its original index $i$.
2. **The "Valid" Condition:** For $nums[i]$ to become a fixed point, it must end up at index $nums[i]$. Since it can only shift left, it's physically impossible for an element to become a fixed point if $nums[i] > i$. We can immediately discard all such elements.
3. **The "Shift" Distance:** If $nums[i] \le i$, the element needs to shift left by exactly $i - nums[i]$ positions. This means exactly $i - nums[i]$ elements must be deleted *before* it. Let's define this required shift distance as $diff = i - nums[i]$.

### The Reduction (The "Aha!" Moment)

Suppose we want to keep a sequence of valid elements and turn them *all* into fixed points. If we pick two original indices $i$ and $j$ (where $i < j$), what conditions must they satisfy to coexist as fixed points in the final array?

1. **Strictly Increasing Values:** Since they both become fixed points, their new indices will be exactly $nums[i]$ and $nums[j]$. Because relative order is preserved when deleting, the one originally on the left must end up on the left: $nums[i] < nums[j]$.
2. **Non-Decreasing Deletions:** The number of elements deleted *before* $j$ must be at least the number of elements deleted *before* $i$. If you deleted 3 elements before $i$, you can't have deleted only 2 elements before $j$ (since $j$ comes after $i$). Therefore: $i - nums[i] \le j - nums[j]$.

This means we need to find the longest sequence of elements where:

* $X = nums[i]$ is **strictly increasing**.
* $Y = i - nums[i]$ is **non-decreasing**.

This is a **2D Longest Increasing Subsequence (LIS)** problem!

### The Algorithm

1. **Filter & Map:** Iterate through the array and extract all valid elements as pairs of $(X, Y) \rightarrow (nums[i], i - nums[i])$.
2. **Sort Cleverly:** We sort the pairs primarily by $X$ ascending.
* *Crucial Edge Case:* If two elements have the same $X$, we can only pick one of them (since $X$ must be strictly increasing). To enforce this, if $X$'s are equal, we sort by $Y$ **descending**. This ensures that when we compute the non-decreasing LIS on $Y$, picking the first one (larger $Y$) prevents us from picking the subsequent ones (smaller $Y$).


3. **1D LIS on Y:** We extract the $Y$ values from the sorted pairs and find the longest non-decreasing subsequence using binary search (`bisect_right`).

### Code Implementation

Here is the Python 3 solution to run in your editor:

```python
import bisect

class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        valid_pairs = []
        
        # Step 1: Filter valid elements and create (X, Y) pairs
        for i, num in enumerate(nums):
            if num <= i:
                # X = num (value/target index), Y = i - num (required shifts)
                valid_pairs.append((num, i - num))
                
        if not valid_pairs:
            return 0
            
        # Step 2: Sort by X ascending, then by Y descending
        valid_pairs.sort(key=lambda pair: (pair[0], -pair[1]))
        
        # Step 3: Find Longest Non-Decreasing Subsequence on Y
        tails = []
        for x, y in valid_pairs:
            # We use bisect_right because we want a non-decreasing subsequence (y1 <= y2)
            idx = bisect.bisect_right(tails, y)
            
            if idx == len(tails):
                tails.append(y)
            else:
                tails[idx] = y
                
        return len(tails)

```

### Dry Run

Let's simulate the edge case `nums = [1, 0, 1, 2]` to verify the logic.

* **Extraction:**
* $i=0, num=1 \rightarrow$ Invalid ($1 > 0$)
* $i=1, num=0 \rightarrow$ Valid: $X=0, Y=(1-0)=1 \rightarrow (0, 1)$
* $i=2, num=1 \rightarrow$ Valid: $X=1, Y=(2-1)=1 \rightarrow (1, 1)$
* $i=3, num=2 \rightarrow$ Valid: $X=2, Y=(3-2)=1 \rightarrow (2, 1)$


* **Pairs:** `[(0, 1), (1, 1), (2, 1)]`
* **Sorted:** `[(0, 1), (1, 1), (2, 1)]`
* **LIS on Y `[1, 1, 1]`:**
* Insert $1$: `tails = [1]`
* Insert $1$: `bisect_right` finds index 1. Appends. `tails = [1, 1]`
* Insert $1$: `bisect_right` finds index 2. Appends. `tails = [1, 1, 1]`


* **Result:** `len(tails) == 3`.

### Complexity Analysis

* **Time Complexity:** Filtering takes $O(N)$. Sorting takes $O(K \log K)$ where $K \le N$. The LIS loop runs $K$ times, and `bisect_right` takes $O(\log K)$, giving $O(K \log K)$. The overall time complexity is **$O(N \log N)$**, strictly bypassing any quadratic pitfalls.
* **Space Complexity:** **$O(N)$** to store the `valid_pairs` and the `tails` array for binary search. Amortized dynamic array resizing handles the append operations in $O(1)$ time.

    The $O(N^2)$ Dynamic Programming approach is exactly how you arrive at the optimized solution. It represents the "brute force" way of building valid subsequences before you realize you can optimize it with binary search.

Here is the breakdown of how the $O(N^2)$ DP works.

### The DP State Definition

Let `dp[i]` represent the **maximum number of fixed points** you can achieve if the sequence of fixed points ends exactly at the original index `i`.

For `nums[i]` to even be considered a candidate for a fixed point, it must satisfy the physical constraint that it can only shift left:

* **Validity Condition:** $nums[i] \le i$

If an element doesn't meet this condition, we just ignore it (`dp[i] = 0`).

### The Transition Logic

If we are looking at a valid element at index `i`, we want to extend a previous valid sequence that ended at some index `j` (where $j < i$).

To append `nums[i]` to the sequence ending at `nums[j]` and have *both* become fixed points, two conditions must be true:

1. **Value Condition (Strictly Increasing):** Because they are fixed points, their final indices will be exactly their values. Since $j$ was originally to the left of $i$, it must stay to the left of $i$ after deletions.
* $nums[j] < nums[i]$


2. **Shift Condition (Non-Decreasing Deletions):** The number of elements deleted before $i$ is exactly $i - nums[i]$. The number of elements deleted before $j$ is $j - nums[j]$. Since $i$ comes after $j$, the total deletions accumulated before $i$ must be at least the deletions accumulated before $j$.
* $j - nums[j] \le i - nums[i]$



If both conditions hold, we can transition:


$$dp[i] = \max(dp[i], dp[j] + 1)$$

### The $O(N^2)$ Code

Here is how that logic translates directly into code:

```python
class Solution:
    def maxFixedPoints(self, nums: list[int]) -> int:
        n = len(nums)
        # dp[i] stores the max fixed points ending at original index i
        dp = [0] * n 
        max_fixed = 0
        
        for i in range(n):
            # Check if nums[i] is a valid candidate
            if nums[i] <= i:
                # Base case: A sequence of length 1 containing just itself
                dp[i] = 1 
                
                # Look back at all previous indices j to see if we can extend them
                for j in range(i):
                    # Check if j was a valid candidate
                    if nums[j] <= j: 
                        # Check the two transition conditions
                        if nums[j] < nums[i] and (j - nums[j]) <= (i - nums[i]):
                            dp[i] = max(dp[i], dp[j] + 1)
                            
                max_fixed = max(max_fixed, dp[i])
                
        return max_fixed

```

### Why this naturally leads to $O(N \log N)$

When you write out this $O(N^2)$ solution, you immediately see the pattern:

* You are trying to find the longest sequence.
* You are checking if one property is strictly increasing ($nums[j] < nums[i]$).
* You are checking if another property is non-decreasing ($(j - nums[j]) \le (i - nums[i])$).

This inner `for j in range(i)` loop is the textbook definition of finding a Longest Increasing Subsequence (LIS). Because evaluating two properties in an $O(N^2)$ loop is too slow for $N = 10^5$, the next logical step is to map those properties into `(X, Y)` pairs, sort them to handle the first condition automatically, and use binary search (`bisect`) to handle the second condition in $O(\log N)$ time.
    """
    def maxFixedPoints(self, nums: list[int]) -> int:
        valid_pairs = []
        
        # Step 1: Filter valid elements and create (X, Y) pairs
        for i, num in enumerate(nums):
            if num <= i:
                # X = num (value/target index), Y = i - num (required shifts)
                valid_pairs.append((num, i - num))
                
        if not valid_pairs:
            return 0
            
        # Step 2: Sort by X ascending, then by Y descending
        valid_pairs.sort(key=lambda pair: (pair[0], -pair[1]))
        
        # Step 3: Find Longest Non-Decreasing Subsequence on Y
        tails = []
        for x, y in valid_pairs:
            # We use bisect_right because we want a non-decreasing subsequence (y1 <= y2)
            idx = bisect.bisect_right(tails, y)
            
            if idx == len(tails):
                tails.append(y)
            else:
                tails[idx] = y
                
        return len(tails)