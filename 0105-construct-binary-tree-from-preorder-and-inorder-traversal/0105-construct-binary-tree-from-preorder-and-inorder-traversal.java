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
    int pi;
    TreeNode f(int l, int r, Stack<Integer> p, int []i, Map<Integer, Integer>mp) {
        if(l > r || p.isEmpty()) return null;
        int val = p.pop();
        TreeNode root = new TreeNode(val);

        int inId = mp.get(val);
        pi++;
        root.left = f(l, inId-1, p, i, mp);
        root.right = f(inId + 1, r, p, i, mp);
        return root;
    }
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        Map<Integer, Integer> ino = new HashMap<>();
        int c = 0;
        for (int i: inorder) {
            ino.put(i, c++);
        }    
        Stack<Integer> preStack = new Stack<>();
        // Iterate backwards so the first element (root) ends up at the top
        for (int i = preorder.length - 1; i >= 0; i--) {
            preStack.push(preorder[i]);
        }
        return f(0, preorder.length-1, preStack, inorder, ino);
    }
}