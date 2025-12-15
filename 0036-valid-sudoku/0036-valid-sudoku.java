import java.util.*;

class Solution {
    public record Point(int x, int y) {}

    public boolean isValidSudoku(char[][] board) {
        // Fix 1: Use <Character> instead of <String> to match board type
        Map<Integer, Set<Character>> r = new HashMap<>();
        Map<Integer, Set<Character>> c = new HashMap<>();
        
        // Fix 2: 'sq' needs to map a Box Coordinate -> Set of numbers in that box
        Map<Point, Set<Character>> sq = new HashMap<>();

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char num = board[i][j]; // Fix 3: No casting needed for char
                
                if (num != '.') { // Fix 4: Use single quotes for char comparison
                    Point box = new Point(i / 3, j / 3);

                    // Fix 5: Condensed Logic
                    // computeIfAbsent gets (or creates) the Set for this row/col/box.
                    // .add(num) returns 'false' if the number is ALREADY in the set.
                    
                    if (!r.computeIfAbsent(i, v -> new HashSet<>()).add(num)) return false;
                    if (!c.computeIfAbsent(j, v -> new HashSet<>()).add(num)) return false;
                    if (!sq.computeIfAbsent(box, v -> new HashSet<>()).add(num)) return false;
                }
            }
        }

        return true;
    }
}