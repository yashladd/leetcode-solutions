class Solution {
    public int minimumOperationsToMakeEqual(int x, int y) {

        Queue<Integer> q = new LinkedList<>();
        q.add(x);
        int steps = 0;
        while (!q.isEmpty()) {
            
            int s = q.size();
            for(int i = 0; i < s; i++) {
                int curr = q.poll();
                if (curr == y) return steps;
                if (curr % 11 == 0) {
                    q.add(curr/11);
                } else if (curr % 5 == 0) {
                    q.add(curr/5);
                }
                q.add(curr-1);
                q.add(curr+1);
            }
            steps ++;

        }

        return steps;

    }
}