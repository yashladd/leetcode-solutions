class Solution {
    boolean rec(int x, int y) {
        if (x >= 1 && y >= 4) {
            if (!rec(x-1, y-4)) return true;
        }
        return false;
    }
    public String winningPlayer(int x, int y) {
        boolean alicWins = rec(x, y);

        return alicWins ? "Alice" : "Bob";
    }
}