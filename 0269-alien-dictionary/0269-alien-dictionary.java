class Solution {
    // DFS Helper (unchanged logic, just cleaner parameters)
    boolean dfs(Character node, Map<Character, List<Character>> g, Stack<Character> s, Set<Character> vis, Set<Character> path) {
        vis.add(node);
        path.add(node);
        
        for (Character nei : g.get(node)) { // g.get(node) is safe now because we initialize everything
            if (path.contains(nei)) return true; // Cycle detected
            if (!vis.contains(nei)) {
                if (dfs(nei, g, s, vis, path)) return true;
            }
        }

        s.push(node);
        path.remove(node);
        return false;
    }

    public String alienOrder(String[] words) {
        Map<Character, List<Character>> g = new HashMap<>();

        // 1. Initialize the graph with EVERY unique character (Matches Python logic)
        // This handles cases like ["z", "z"] where no edges are ever created.
        for (String word : words) {
            for (char c : word.toCharArray()) {
                g.putIfAbsent(c, new ArrayList<>());
            }
        }

        // 2. Build the edges
        for (int i = 0; i < words.length - 1; i++) {
            String w1 = words[i];
            String w2 = words[i + 1];
            
            // Check for invalid prefix case (e.g., "abc" before "ab")
            if (w1.length() > w2.length() && w1.startsWith(w2)) {
                return "";
            }

            // Find the first difference
            for (int j = 0; j < Math.min(w1.length(), w2.length()); j++) {
                if (w1.charAt(j) != w2.charAt(j)) {
                    g.get(w1.charAt(j)).add(w2.charAt(j));
                    break; // Only the first difference matters
                }
            }
            // Note: We removed the "if (!foundDiff) return """ block. 
            // If words are identical (["z", "z"]), we simply add no edges and continue.
        }

        Stack<Character> s = new Stack<>();
        Set<Character> vis = new HashSet<>();
        Set<Character> path = new HashSet<>();

        // 3. DFS over every character in the map
        for (Character c : g.keySet()) {
            if (!vis.contains(c)) {
                if (dfs(c, g, s, vis, path)) {
                    return ""; // Cycle detected
                }
            }
        }

        StringBuilder sb = new StringBuilder();
        while (!s.isEmpty()) {
            sb.append(s.pop());
        }
        return sb.toString();
    }
}