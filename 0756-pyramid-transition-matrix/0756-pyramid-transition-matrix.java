class Solution {
    // Memoization to cache results of rows we've already tried (prevents Time Limit Exceeded)
    Map<String, Boolean> memo = new HashMap<>();

    public boolean pyramidTransition(String bottom, List<String> allowed) {
        Map<String, List<Character>> allowedMap = new HashMap<>();
        
        for (String s : allowed) {

            String base = s.substring(0, 2); 
            char top = s.charAt(2);
            allowedMap.computeIfAbsent(base, k -> new ArrayList<>()).add(top);
        }

        return solve(bottom, allowedMap);
    }

    // Outer Recursion: Moves up the pyramid levels
    private boolean solve(String currentRow, Map<String, List<Character>> map) {

        if (currentRow.length() == 1) return true;
        
        if (memo.containsKey(currentRow)) return memo.get(currentRow);

        boolean result = buildNextRow(currentRow, 0, new StringBuilder(), map);
        
        // Save result to cache
        memo.put(currentRow, result);
        return result;
    }

    private boolean buildNextRow(String currentRow, int idx, StringBuilder nextRowCandidate, Map<String, List<Character>> map) {

        if (idx == currentRow.length() - 1) {
            return solve(nextRowCandidate.toString(), map);
        }


        String base = currentRow.substring(idx, idx + 2);
        
        if (!map.containsKey(base)) return false;


        for (char top : map.get(base)) {

            nextRowCandidate.append(top);
            
            if (buildNextRow(currentRow, idx + 1, nextRowCandidate, map)) {
                return true;
            }
            
            nextRowCandidate.deleteCharAt(nextRowCandidate.length() - 1);
        }

        return false;
    }
}