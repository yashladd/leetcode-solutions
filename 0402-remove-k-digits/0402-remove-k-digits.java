import java.util.Stack;

class Solution {
    public String removeKdigits(String num, int k) {
        Stack<Character> stack = new Stack<>();
        
        for (char digit : num.toCharArray()) {
            // Greedy removal: pop if current digit is smaller than the top of the stack
            while (!stack.isEmpty() && k > 0 && stack.peek() > digit) {
                stack.pop();
                k--;
            }
            
            // Logic to prevent leading zeros:
            // Only push if the stack is NOT empty OR the current digit is NOT '0'.
            // (This matches the Python line: if st or n is not '0')
            if (stack.isEmpty() && digit == '0') {
                continue;
            }
            stack.push(digit);
        }
        
        // If we still need to remove digits (k > 0), remove them from the top (end)
        while (k > 0 && !stack.isEmpty()) {
            stack.pop();
            k--;
        }
        
        // Build the final string
        // Note: Iterating a Java Stack works from bottom-to-top (first-in to last-in),
        // so this correctly builds the number from left to right.
        StringBuilder sb = new StringBuilder();
        for (char c : stack) {
            sb.append(c);
        }
        
        // Return "0" if the result is empty, otherwise the built string
        return sb.length() == 0 ? "0" : sb.toString();
    }
}