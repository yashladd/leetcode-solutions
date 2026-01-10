class Solution {
    public int countBattleships(char[][] board) {
        int m = board.length;
        int n = board[0].length;
        int count = 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                // If current cell is empty, move on
                if (board[i][j] == '.') continue;
                
                // Check if this is a part of an existing battleship detected from above
                if (i > 0 && board[i - 1][j] == 'X') continue;
                
                // Check if this is a part of an existing battleship detected from the left
                if (j > 0 && board[i][j - 1] == 'X') continue;
                
                // If we passed the checks, we found the 'head' of a new battleship
                count++;
            }
        }
        
        return count;
    }
}