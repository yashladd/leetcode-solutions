import java.util.Arrays;

class Solution {
    public boolean findRotation(int[][] mat, int[][] target) {
        // We check 4 times because 4 rotations of 90 degrees = 360 degrees (back to start)
        for (int i = 0; i < 4; i++) {
            if (isEqual(mat, target)) {
                return true;
            }
            mat = rotate(mat);
        }
        return false;
    }

    // Helper method to rotate the matrix 90 degrees clockwise
    private int[][] rotate(int[][] mat) {
        int n = mat.length;
        int[][] newMat = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                // The element at [i][j] moves to [j][n-1-i]
                newMat[j][n - 1 - i] = mat[i][j];
            }
        }
        return newMat;
    }

    // Helper method to check if two matrices are identical
    private boolean isEqual(int[][] m1, int[][] m2) {
        int n = m1.length;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (m1[i][j] != m2[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
}