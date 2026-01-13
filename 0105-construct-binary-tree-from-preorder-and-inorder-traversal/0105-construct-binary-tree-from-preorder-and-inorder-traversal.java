class Solution {
    // 1. Global counter to track position in preorder array
    int pi = 0; 
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        pi = 0; // Important: Reset for every new test case
        Map<Integer, Integer> ino = new HashMap<>();
        for (int i = 0; i < inorder.length; i++) {
            ino.put(inorder[i], i);
        }
        
        return f(preorder, 0, inorder.length - 1, ino);
    }

    private TreeNode f(int[] preorder, int l, int r, Map<Integer, Integer> mp) {
        // Base case: no elements left in this subtree range
        if (l > r) return null;

        // 2. Use the counter to get the current root value
        int val = preorder[pi];
        pi++; // Move to the next value for the next recursive call

        TreeNode root = new TreeNode(val);

        // 3. Split using the inorder map
        int inId = mp.get(val);

        // 4. Recursive calls (Order matters: Left then Right)
        root.left = f(preorder, l, inId - 1, mp);
        root.right = f(preorder, inId + 1, r, mp);

        return root;
    }
}