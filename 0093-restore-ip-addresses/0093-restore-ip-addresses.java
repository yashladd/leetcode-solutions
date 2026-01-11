class Solution {
    void dfs(int i, String s, List<String> res, int n, List<String> cur, int k) {
        if (i == n) {
            if (k == 0 ) {
                res.add(String.join(".", cur));
            }
            return;
        }

        if (i > n) return;

        if (k < 0) return;

        for (int j = i + 1; j < i + 4 && j <= n; j++) {
            String curr = s.substring(i, j);
            System.out.println(curr);
            if ((curr.length() >= 2 && curr.startsWith("0")) || Integer.parseInt(curr) > 255) continue;

            cur.add(curr);
            dfs(j, s, res, n, cur, k-1);
            cur.removeLast();
            
        }


    }
    public List<String> restoreIpAddresses(String s) {

        List<String> res = new ArrayList<>();
        List<String> curr = new ArrayList<>();

        for (int i =0; i < s.length(); i++) {
            if(!Character.isDigit(s.charAt(i))) return res;
        }


        dfs(0, s, res, s.length(), curr, 4);

        return res;

        
    }
}