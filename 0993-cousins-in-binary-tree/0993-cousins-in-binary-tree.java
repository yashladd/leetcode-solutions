class Solution {
    // Define the record to store node metadata
    private record DataNode(int depth, Integer parent) {}

    private Map<Integer, DataNode> map = new HashMap<>();

    public boolean isCousins(TreeNode root, int x, int y) {
        traverse(root, x, y, null, 0);

        // Ensure both values were found before comparing
        if (!map.containsKey(x) || !map.containsKey(y)) return false;

        DataNode nodeX = map.get(x);
        DataNode nodeY = map.get(y);

        // Cousins: same depth, different parents
        return nodeX.depth() == nodeY.depth() && !Objects.equals(nodeX.parent(), nodeY.parent());
    }

    private void traverse(TreeNode root, int x, int y, Integer parent, int depth) {
        if (root == null || map.size() == 2) return;

        if (root.val == x || root.val == y) {
            map.put(root.val, new DataNode(depth, parent));
        }

        traverse(root.left, x, y, root.val, depth + 1);
        traverse(root.right, x, y, root.val, depth + 1);
    }
}