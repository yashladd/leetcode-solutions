class Solution {
    public int minimumOperationsToMakeEqual(int x, int y) {

        Queue<Integer> q = new LinkedList<>();
        Set<Integer> visited = new HashSet<>(); // 1. Add visited set

        q.add(x);
        visited.add(x); // Mark start as visited
        int steps = 0;

        while (!q.isEmpty()) {
            int s = q.size();
            for(int i = 0; i < s; i++) {
                int curr = q.poll();
                
                if (curr == y) return steps;
                
                // Better structure to handle visited checks easily:
                List<Integer> neighbors = new ArrayList<>();
                if (curr % 11 == 0) neighbors.add(curr / 11);
                if (curr % 5 == 0) neighbors.add(curr / 5); // 2. Removed "else"
                neighbors.add(curr - 1);
                neighbors.add(curr + 1);
                
                for (int nextVal : neighbors) {
                    if (!visited.contains(nextVal)) { // 3. Check if visited
                        visited.add(nextVal);
                        q.add(nextVal);
                    }
                }
            }
            steps++;
        }
        return steps;
    }
}