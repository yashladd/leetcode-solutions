/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    void dfs(TreeNode node, Map<Integer, int[]>mp, int depth, int par, int x, int y) {
        if (node != null) {
            if (node.val == x){
                mp.put(x, new int[] {depth, par});
            } else if (node.val == y) {
                mp.put(y, new int[] {depth, par});
            }

            dfs(node.left, mp, depth + 1, node.val, x, y);
            dfs(node.right, mp, depth + 1, node.val, x, y);

        }
    }
    public boolean isCousins(TreeNode root, int x, int y) {
        Map<Integer, int[]> mp = new HashMap<>();
        dfs(root, mp, 0, -1, x, y);
        int [] xVals = mp.get(x);
        int [] yVals = mp.get(y);
        if (xVals[1] == yVals[1]) return false;
        return xVals[0]== yVals[0];
    }
}