class Solution {
    public record Entry(int val, int idx) {};
    public int[] dailyTemperatures(int[] t) {
        Stack<Entry> s = new Stack<>();
        int n = t.length;
        int res[] = new int[n];
        for (int i = n-1; i >= 0; i--) {
            // System.out.println(s);
            
            int curr = t[i];
            while (!s.isEmpty() && s.peek().val <= curr){
                s.pop();
            }

            if (s.isEmpty()) res[i] = 0;
            else{
                res[i] = s.peek().idx - i;
            }

            s.push(new Entry(curr, i));
        }

        return res;
    }
}