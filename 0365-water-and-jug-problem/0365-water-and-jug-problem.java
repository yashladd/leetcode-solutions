class Solution {
    public boolean canMeasureWater(int x, int y, int target) {
        // FIX: Physically impossible if target > total capacity
        if (target > x + y) return false; 
        
        Set<Integer> visited = new HashSet<>();
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(0);
        
        while (!stack.isEmpty()) {
            int currentTotal = stack.pop();
            
            // Move the validity check BEFORE the success check
            if (visited.contains(currentTotal) || currentTotal < 0 || currentTotal > x + y) {
                continue;
            }
            
            if (currentTotal == target) {
                return true;
            }
            
            visited.add(currentTotal);
            
            // ... rest of your push logic ...
            stack.push(currentTotal + x);
            stack.push(currentTotal + y);
            stack.push(currentTotal - x);
            stack.push(currentTotal - y);
        }
        return false;
    }
}