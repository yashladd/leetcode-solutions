class Solution {
    public record Pos(int x, int y) {
    }

    void dfs(int i, int j, Set<Pos> visSet, int [][] heights, int prevHeight) { 
        int n = heights.length, m = heights[0].length; 
        if (i < 0 || i >= n || j < 0 || j >= m) {
            return;
        } 
        Pos thisPos = new Pos(i, j);
        if (visSet.contains(thisPos) 
        ||  prevHeight > heights[i][j]) {
            return;
        }

        visSet.add(thisPos);
        dfs(i+1, j, visSet, heights, heights[i][j]);
        dfs(i, j+1, visSet, heights, heights[i][j]);
        dfs(i-1, j, visSet, heights, heights[i][j]);
        dfs(i, j-1, visSet, heights, heights[i][j]);
    }
    

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        List<List<Integer>> res = new ArrayList<>();
        Set<Pos> pacific = new HashSet<>();
        Set<Pos> atlantic = new HashSet<>();
        int n = heights.length, m = heights.length; 
        for (int i = 0; i < n; i++) {
            dfs(i, 0, pacific, heights, Integer.MIN_VALUE);
            dfs(i, m-1, atlantic, heights, Integer.MIN_VALUE);
        }

        for (int j = 0; j < m; j++) {
            dfs(0, j, pacific, heights, Integer.MIN_VALUE);
            dfs(n-1, j, atlantic, heights, Integer.MIN_VALUE);
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                Pos thisPos = new Pos(i,j);
                if (pacific.contains(thisPos) && atlantic.contains(thisPos)) {
                    res.add(List.of(i, j));
                }

            }
        }

        return res;
    }
}