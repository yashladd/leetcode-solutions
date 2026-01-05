class Solution {
    public int minimumSemesters(int n, int[][] relations) {
        Map<Integer, List<Integer>> g = new HashMap<>();
        int [] ind = new int [n+1];
        for (int nodes[]: relations) {
            int u = nodes[0];
            int v = nodes[1];
            ind[v]++;
            g.computeIfAbsent(u, _ -> new ArrayList<>()).add(v);
        }

        Queue<Integer> q = new LinkedList<>();
        int topoCnt = 0;
        for (int c = 1; c <= n; c++) {
            if(ind[c] == 0) {
                q.add(c);
                topoCnt++;
            }
        }
        // System.out.println(ind);
        // System.out.println(g);




        if (q.size() == 0) return -1;

        int sems = 0;
        while (!q.isEmpty()){
            int sz = q.size();
            // System.out.println(q);

            for (int x = 0; x < sz; x++) {
                int node = q.poll();
                for (int nei: g.getOrDefault(node, new ArrayList<>())){
                    ind[nei]--;
                    if (ind[nei] == 0) {
                        topoCnt++;
                        q.add(nei);
                    }
                }
            }
            sems++;
        }

        // System.out.println(topoCnt);
        // System.out.println(n);

        if (topoCnt!=n) return -1;
        return sems;
         
    }
}